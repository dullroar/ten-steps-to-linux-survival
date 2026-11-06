#!/usr/bin/env python3
"""Validate plan step files, check parallel safety, and print derived status.

Layout: plans/<plan>/spec.md and plans/<plan>/steps/<id>.md (plans/TEMPLATE and plans/archive
are skipped). Each step has front matter: id, status (pending|in_progress|done|blocked),
depends_on, touches, lane, gate, requirements, and (once done) evidence.
Requirements are headings in spec.md such as `### R1. Title`.

Usage: check_plan.py [ROOT]   (exit 1 on any error; conservative overlaps are errors)
"""
from __future__ import annotations

import fnmatch
import re
import sys
from pathlib import Path

from ctx_common import repo_root, split_frontmatter

STATUSES = {"pending", "in_progress", "done", "blocked"}
REQUIRED = ("id", "status", "depends_on", "touches", "lane", "gate", "requirements")


def as_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(v) for v in value if str(v)]
    return [str(value)] if value else []


def overlaps(a: str, b: str) -> bool:
    a, b = a.rstrip("/"), b.rstrip("/")
    if a == b or fnmatch.fnmatch(a, b) or fnmatch.fnmatch(b, a):
        return True
    stem = lambda g: re.split(r"[*?\[]", g)[0].rstrip("/")  # noqa: E731 - literal prefix of a glob
    sa, sb = stem(a), stem(b)
    return bool(sa and sb and (sa == sb or sa.startswith(sb + "/") or sb.startswith(sa + "/")))


def check_plan(plan: Path, root: Path) -> list[str]:
    errors: list[str] = []
    name = plan.relative_to(root).as_posix()
    steps: dict[str, dict] = {}
    for path in sorted((plan / "steps").glob("*.md")):
        meta, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        missing = [k for k in REQUIRED if k not in meta]
        if missing:
            errors.append(f"{name}/steps/{path.name}: missing front matter {', '.join(missing)}")
            continue
        if meta["id"] != path.stem:
            errors.append(f"{name}/steps/{path.name}: id '{meta['id']}' must equal file name")
        if meta["status"] not in STATUSES:
            errors.append(f"{name}/steps/{path.name}: bad status '{meta['status']}'")
        if meta["status"] == "done" and not meta.get("evidence"):
            errors.append(f"{name}/steps/{path.name}: done step needs evidence")
        if not meta["gate"]:
            errors.append(f"{name}/steps/{path.name}: empty gate")
        steps[path.stem] = meta

    spec = plan / "spec.md"
    spec_reqs = set(re.findall(r"^#{2,4}\s+(R\d+)\b", spec.read_text(encoding="utf-8"), re.M)) if spec.exists() else set()
    if not spec.exists():
        errors.append(f"{name}: missing spec.md")

    for sid, meta in steps.items():
        for dep in as_list(meta["depends_on"]):
            if dep not in steps:
                errors.append(f"{name}: {sid} depends on unknown step '{dep}'")
        for req in as_list(meta["requirements"]):
            if req not in spec_reqs:
                errors.append(f"{name}: {sid} cites requirement '{req}' not in spec.md")
    covered = {r for m in steps.values() for r in as_list(m["requirements"])}
    for req in sorted(spec_reqs - covered):
        errors.append(f"{name}: requirement {req} is traced to no step")

    # Cycles (depth-first).
    state: dict[str, int] = {}
    def visit(node: str, trail: list[str]) -> None:
        if state.get(node) == 2:
            return
        if state.get(node) == 1:
            errors.append(f"{name}: dependency cycle {' -> '.join([*trail, node])}")
            return
        state[node] = 1
        for dep in as_list(steps[node]["depends_on"]):
            if dep in steps:
                visit(dep, [*trail, node])
        state[node] = 2
    for sid in steps:
        visit(sid, [])

    def ancestors(sid: str, seen: set[str] | None = None) -> set[str]:
        seen = seen if seen is not None else set()
        for dep in as_list(steps[sid]["depends_on"]):
            if dep in steps and dep not in seen:
                seen.add(dep)
                ancestors(dep, seen)
        return seen

    def derived(sid: str) -> str:
        meta = steps[sid]
        if meta["status"] != "pending":
            return str(meta["status"])
        return "ready" if all(steps.get(d, {}).get("status") == "done" for d in as_list(meta["depends_on"])) else "waiting"

    live = [s for s in steps if derived(s) in {"ready", "in_progress"} and not state.get(s) == 1]
    try:
        for i, a in enumerate(live):
            for b in live[i + 1:]:
                if a in ancestors(b) or b in ancestors(a):
                    continue
                for ta in as_list(steps[a]["touches"]):
                    for tb in as_list(steps[b]["touches"]):
                        if overlaps(ta, tb):
                            errors.append(f"{name}: {a} and {b} may run together but both touch '{ta}' / '{tb}'")
                la, lb = steps[a]["lane"], steps[b]["lane"]
                if la and la == lb and la != "none":
                    errors.append(f"{name}: {a} and {b} share serial lane '{la}'")
    except RecursionError:
        errors.append(f"{name}: dependency graph too deep to analyze")

    print(f"{name}: " + (", ".join(f"{s}={derived(s)}" for s in steps) or "no steps"))
    return errors


def main(argv: list[str]) -> int:
    root = repo_root(Path(argv[0]) if argv else None)
    plans = root / "plans"
    errors: list[str] = []
    if plans.is_dir():
        for plan in sorted(p for p in plans.iterdir() if p.is_dir() and p.name not in {"TEMPLATE", "archive"}):
            errors.extend(check_plan(plan, root))
    for err in errors:
        print(f"ERROR {err}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
