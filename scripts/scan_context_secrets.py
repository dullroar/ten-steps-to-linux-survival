#!/usr/bin/env python3
"""Scan context Markdown for credentials, connection strings, personal paths and emails.

Scans AGENTS.md, CLAUDE.md, docs/, memory/, references/, plans/. A scanner supplements review;
it does not justify putting sensitive material in the repository. Add `<!-- scan:ignore -->`
to a line that is a deliberate, reviewed placeholder. Usage: scan_context_secrets.py [ROOT]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from ctx_common import markdown_files, repo_root

SCOPES = ("AGENTS.md", "CLAUDE.md", "docs/", "memory/", "references/", "plans/")
PATTERNS = {
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "token": re.compile(r"\b(ghp_|gho_|github_pat_|sk-[A-Za-z0-9]{16,}|AKIA[0-9A-Z]{16}|xox[bap]-)"),
    "credential in URL": re.compile(r"://[^/\s:@]+:[^/\s@]+@"),
    "connection string": re.compile(r"(?i)\b(password|pwd|accountkey|sharedaccesskey)\s*=\s*[^;\s]{3,}"),
    "personal path": re.compile(r"(/home/[a-z][\w.-]*/|/Users/[A-Za-z][\w.-]*/|[A-Za-z]:\\Users\\[A-Za-z][\w.-]*)"),
    "email": re.compile(r"\b[\w.+-]+@(?!example\.|users\.noreply)[\w-]+\.[\w.-]+\b"),
}


def main(argv: list[str]) -> int:
    root = repo_root(Path(argv[0]) if argv else None)
    findings = 0
    for path in markdown_files(root):
        rel = path.relative_to(root).as_posix()
        if not rel.startswith(SCOPES):
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
            if "scan:ignore" in line:
                continue
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    print(f"{rel}:{number}: possible {label}")
                    findings += 1
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
