#!/usr/bin/env python3
"""Generate deterministic B02 tests."""

from pathlib import Path
import random


ROOT = Path(__file__).resolve().parent
SEED = 20260906


def solve(heights, need):
    low, high = 0, max(heights)
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        total = sum(max(0, h - mid) for h in heights)
        if total >= need:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


def write_case(group, name, heights, need):
    directory = ROOT / "tests" / group
    directory.mkdir(parents=True, exist_ok=True)
    lines = [f"{len(heights)} {need}", " ".join(map(str, heights))]
    (directory / f"{name}.in").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (directory / f"{name}.out").write_text(str(solve(heights, need)) + "\n", encoding="utf-8")


def main():
    random.seed(SEED)
    write_case("sample", "sample1", [20, 15, 10, 17], 7)
    write_case("boundary", "need_zero", [1, 2, 3], 0)
    write_case("boundary", "single_tree", [10], 4)
    write_case("boundary", "all_cut_to_zero", [2, 3, 4], 9)
    write_case("adversarial", "exact_boundary", [8, 8, 8], 9)
    write_case("adversarial", "overflow_risk", [1000000000, 1000000000, 1000000000], 2500000000)
    for idx in range(4):
        n = random.randint(3, 18)
        heights = [random.randint(0, 200) for _ in range(n)]
        total = sum(heights)
        need = random.randint(0, total)
        write_case("random", f"seeded_{idx:02d}", heights, need)


if __name__ == "__main__":
    main()
