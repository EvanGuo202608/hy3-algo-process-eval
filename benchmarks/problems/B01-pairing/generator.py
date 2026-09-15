#!/usr/bin/env python3
"""Generate deterministic B01 tests."""

from itertools import combinations
from pathlib import Path
import random


ROOT = Path(__file__).resolve().parent
SEED = 20260906


def solve(weights, limit):
    weights = sorted(weights)
    left, right = 0, len(weights) - 1
    groups = 0
    while left <= right:
        if left < right and weights[left] + weights[right] <= limit:
            left += 1
        right -= 1
        groups += 1
    return groups


def write_case(group, name, weights, limit):
    directory = ROOT / "tests" / group
    directory.mkdir(parents=True, exist_ok=True)
    lines = [f"{len(weights)} {limit}", " ".join(map(str, weights))]
    (directory / f"{name}.in").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (directory / f"{name}.out").write_text(str(solve(weights, limit)) + "\n", encoding="utf-8")


def main():
    random.seed(SEED)
    write_case("sample", "sample1", [40, 50, 60, 70, 80], 100)
    write_case("boundary", "single", [7], 10)
    write_case("boundary", "all_pair", [1, 1, 1, 1], 2)
    write_case("boundary", "none_pair", [6, 6, 6], 10)
    write_case("adversarial", "lightest_first_trap", [20, 40, 50, 50], 90)
    write_case("adversarial", "duplicates", [40, 40, 40, 60, 60, 60], 100)
    for idx in range(4):
        n = random.randint(2, 16)
        limit = random.randint(30, 120)
        weights = [random.randint(1, limit) for _ in range(n)]
        write_case("random", f"seeded_{idx:02d}", weights, limit)


if __name__ == "__main__":
    main()
