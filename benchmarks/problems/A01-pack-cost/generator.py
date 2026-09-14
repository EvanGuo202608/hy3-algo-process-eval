#!/usr/bin/env python3
"""Generate deterministic A01 tests."""

from pathlib import Path
import random


ROOT = Path(__file__).resolve().parent
SEED = 20260906


def solve(n, options):
    return min(((n + count - 1) // count) * price for count, price in options)


def write_case(group, name, n, options):
    directory = ROOT / "tests" / group
    directory.mkdir(parents=True, exist_ok=True)
    data = [str(n), *[f"{count} {price}" for count, price in options]]
    (directory / f"{name}.in").write_text("\n".join(data) + "\n", encoding="utf-8")
    (directory / f"{name}.out").write_text(str(solve(n, options)) + "\n", encoding="utf-8")


def main():
    random.seed(SEED)
    write_case("sample", "sample1", 57, [(2, 2), (50, 30), (30, 27)])
    write_case("boundary", "min_n", 1, [(2, 5), (3, 7), (10, 20)])
    write_case("boundary", "exact_division", 100, [(10, 12), (25, 28), (40, 50)])
    write_case("adversarial", "floor_division", 11, [(10, 9), (6, 6), (20, 20)])
    write_case("adversarial", "unit_price_trap", 10, [(6, 6), (10, 11), (100, 90)])
    for idx in range(5):
        n = random.randint(1, 100000)
        options = [
            (random.randint(1, 100000), random.randint(1, 100000))
            for _ in range(3)
        ]
        write_case("random", f"seeded_{idx:02d}", n, options)


if __name__ == "__main__":
    main()

