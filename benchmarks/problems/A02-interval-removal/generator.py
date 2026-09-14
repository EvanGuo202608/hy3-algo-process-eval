#!/usr/bin/env python3
"""Generate deterministic A02 tests."""

from pathlib import Path
import random


ROOT = Path(__file__).resolve().parent
SEED = 20260906


def solve(L, intervals):
    removed = [False] * (L + 1)
    for left, right in intervals:
        for pos in range(left, right + 1):
            removed[pos] = True
    return sum(1 for value in removed if not value)


def write_case(group, name, L, intervals):
    directory = ROOT / "tests" / group
    directory.mkdir(parents=True, exist_ok=True)
    lines = [f"{L} {len(intervals)}", *[f"{left} {right}" for left, right in intervals]]
    (directory / f"{name}.in").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (directory / f"{name}.out").write_text(str(solve(L, intervals)) + "\n", encoding="utf-8")


def main():
    random.seed(SEED)
    write_case("sample", "sample1", 10, [(2, 4), (6, 8)])
    write_case("boundary", "no_interval", 5, [])
    write_case("boundary", "single_point", 0, [(0, 0)])
    write_case("boundary", "full_cover", 10, [(0, 10)])
    write_case("adversarial", "overlap", 12, [(1, 5), (3, 8), (8, 10)])
    write_case("adversarial", "endpoint_inclusive", 4, [(0, 0), (4, 4)])
    for idx in range(4):
        L = random.randint(1, 80)
        intervals = []
        for _ in range(random.randint(1, 8)):
            left = random.randint(0, L)
            right = random.randint(left, L)
            intervals.append((left, right))
        write_case("random", f"seeded_{idx:02d}", L, intervals)


if __name__ == "__main__":
    main()

