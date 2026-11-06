"""Shared helpers for the context-governance scripts (standard library only)."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

BEGIN = "<!-- BEGIN GENERATED CONTEXT INDEX -->"
END = "<!-- END GENERATED CONTEXT INDEX -->"
SKIP_DIRS = {".git", ".venv", "node_modules", "build", "dist", "__pycache__", ".hypothesis"}


def repo_root(start: Path | None = None) -> Path:
    here = (start or Path.cwd()).resolve()
    for candidate in [here, *here.parents]:
        if (candidate / ".git").exists():
            return candidate
    return here


def markdown_files(root: Path) -> list[Path]:
    """Tracked and untracked-but-not-ignored Markdown files, falling back to a walk."""
    try:
        out = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "*.md"],
            cwd=root, capture_output=True, text=True, check=True,
        ).stdout.split("\n")
        files = [root / line for line in out if line and not SKIP_DIRS & set(Path(line).parts)]
    except (OSError, subprocess.CalledProcessError):
        files = [p for p in root.rglob("*.md") if not SKIP_DIRS & set(p.relative_to(root).parts)]
    return sorted(p for p in files if p.is_file())


def split_frontmatter(text: str) -> tuple[dict[str, object], str]:
    """Parse a small YAML subset: scalars, inline lists, and block lists."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    block, body = text[4:end], text[end + 4:].lstrip("\n")
    data: dict[str, object] = {}
    key: str | None = None
    for raw in block.split("\n"):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        item = re.match(r"^\s+-\s+(.*)$", raw)
        if item and key is not None:
            lst = data.setdefault(key, [])
            if isinstance(lst, list):
                lst.append(unquote(item.group(1)))
            continue
        pair = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if not pair:
            continue
        key, value = pair.group(1), pair.group(2).strip()
        if value == "":
            data[key] = []
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [unquote(v.strip()) for v in inner.split(",")] if inner else []
        else:
            data[key] = unquote(value)
    return data, body


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value
