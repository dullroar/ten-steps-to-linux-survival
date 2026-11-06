#!/usr/bin/env python3
"""Check local Markdown links and heading anchors in context files.

Scope: README.md, AGENTS.md, CLAUDE.md, docs/, memory/, references/, plans/, scripts/.
Pass --all to check every Markdown file (authored content may carry older breakage).
Usage: check_links.py [--all] [ROOT]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

from ctx_common import markdown_files, repo_root

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|^\[[^\]]+\]:\s*(\S+)", re.M)
FENCE = re.compile(r"^(```|~~~).*?^\1", re.M | re.S)
INLINE = re.compile(r"`[^`\n]*`")


def slug(heading: str) -> str:
    text = re.sub(r"[`*_]", "", heading.strip().lower())
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    text = FENCE.sub("", path.read_text(encoding="utf-8"))
    seen: dict[str, int] = {}
    result = set()
    headings = re.finditer(r"^#{1,6}\s+(.*?)\s*#*\s*$|^(\S.*?)\n(?:=+|-{2,})\s*$", text, re.M)
    for match in headings:
        title = match.group(1) if match.group(1) is not None else match.group(2)
        explicit = re.search(r"\{[^}]*#([\w-]+)[^}]*\}\s*$", title)
        if explicit:
            result.add(explicit.group(1))
        base = slug(re.sub(r"\s*\{[^}]*\}\s*$", "", title))
        n = seen.get(base, 0)
        seen[base] = n + 1
        result.add(base if n == 0 else f"{base}-{n}")
    return result


SCOPES = ("README.md", "AGENTS.md", "CLAUDE.md", "docs/", "memory/", "references/", "plans/", "scripts/")


def main(argv: list[str]) -> int:
    everything = "--all" in argv
    args = [a for a in argv if not a.startswith("--")]
    root = repo_root(Path(args[0]) if args else None)
    problems = 0
    for path in markdown_files(root):
        if not everything and not path.relative_to(root).as_posix().startswith(SCOPES):
            continue
        text = INLINE.sub("", FENCE.sub("", path.read_text(encoding="utf-8")))
        for match in LINK.finditer(text):
            target = (match.group(1) or match.group(2)).strip("<>")
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue
            file_part, _, frag = target.partition("#")
            dest = path if not file_part else (path.parent / unquote(file_part))
            if not dest.exists():
                print(f"BROKEN {path.relative_to(root)}: {target}")
                problems += 1
            elif frag and dest.suffix == ".md" and slug(unquote(frag)) not in anchors(dest):
                print(f"BAD ANCHOR {path.relative_to(root)}: {target}")
                problems += 1
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
