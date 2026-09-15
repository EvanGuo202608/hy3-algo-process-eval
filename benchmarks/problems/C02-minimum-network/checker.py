#!/usr/bin/env python3
"""Standard exact-output checker for C02."""

from pathlib import Path
import sys


def normalize(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: checker.py EXPECTED ACTUAL", file=sys.stderr)
        return 2
    expected = normalize(Path(sys.argv[1]).read_text(encoding="utf-8"))
    actual = normalize(Path(sys.argv[2]).read_text(encoding="utf-8"))
    return 0 if expected == actual else 1


if __name__ == "__main__":
    raise SystemExit(main())

