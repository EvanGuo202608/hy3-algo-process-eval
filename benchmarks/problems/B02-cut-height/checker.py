#!/usr/bin/env python3
"""Strict integer-output checker for B02."""

from pathlib import Path
import sys


def normalize(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: checker.py EXPECTED ACTUAL", file=sys.stderr)
        return 2
    return 0 if normalize(Path(sys.argv[1])) == normalize(Path(sys.argv[2])) else 1


if __name__ == "__main__":
    raise SystemExit(main())

