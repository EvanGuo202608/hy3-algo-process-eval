#!/usr/bin/env python3
"""Generate deterministic C01 tests."""

from pathlib import Path
import random


ROOT = Path(__file__).resolve().parent
SEED = 20260906


def solve(points):
    points = sorted(points)
    n = len(points)
    dp = [1] * n
    ans = 1
    for i in range(n):
        for j in range(i):
            if points[j][0] < points[i][0] and points[j][1] < points[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
        ans = max(ans, dp[i])
    return ans


def write_case(group, name, points):
    directory = ROOT / "tests" / group
    directory.mkdir(parents=True, exist_ok=True)
    lines = [str(len(points))]
    lines.extend(f"{x} {y}" for x, y in points)
    (directory / f"{name}.in").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (directory / f"{name}.out").write_text(str(solve(points)) + "\n", encoding="utf-8")


def main():
    random.seed(SEED)
    write_case("sample", "sample1", [(1, 1), (2, 2), (2, 3), (3, 4), (4, 5)])
    write_case("boundary", "single", [(7, 9)])
    write_case("boundary", "same_x", [(1, 1), (1, 2), (1, 3), (1, 4)])
    write_case("boundary", "same_y", [(1, 5), (2, 5), (3, 5), (4, 5)])
    write_case("adversarial", "duplicate_trap", [(1, 1), (1, 2), (2, 2), (3, 3)])
    write_case("adversarial", "unsorted_input", [(3, 3), (1, 2), (2, 1), (2, 3), (4, 4)])
    for idx in range(4):
        n = random.randint(5, 12)
        points = [(random.randint(0, 8), random.randint(0, 8)) for _ in range(n)]
        write_case("random", f"seeded_{idx:02d}", points)


if __name__ == "__main__":
    main()

