#!/usr/bin/env python3
"""Run every context-governance check. Usage: check_context.py [ROOT]"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKS = [
    ["build_context_indexes.py", "--check"],
    ["check_plan.py"],
    ["check_links.py"],
    ["scan_context_secrets.py"],
]


def main(argv: list[str]) -> int:
    failed = []
    for script, *flags in CHECKS:
        code = subprocess.run([sys.executable, str(HERE / script), *flags, *argv]).returncode
        print(f"{'ok  ' if code == 0 else 'FAIL'} {script}")
        if code:
            failed.append(script)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
