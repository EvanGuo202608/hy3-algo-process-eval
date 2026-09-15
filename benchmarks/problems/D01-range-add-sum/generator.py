#!/usr/bin/env python3
"""Generate deterministic D01 simplified segment-tree tests."""

from pathlib import Path
import random


ROOT = Path(__file__).resolve().parent
SEED = 20260906


def solve(values, operations):
    arr = values[:]
    out = []
    for op in operations:
        if op[0] == 1:
            _, l, r, x = op
            for i in range(l - 1, r):
                arr[i] += x
        else:
            _, l, r = op
            out.append(str(sum(arr[l - 1:r])))
    return "\n".join(out)


def write_case(group, name, values, operations):
    directory = ROOT / "tests" / group
    directory.mkdir(parents=True, exist_ok=True)
    lines = [f"{len(values)} {len(operations)}", " ".join(map(str, values))]
    for op in operations:
        lines.append(" ".join(map(str, op)))
    (directory / f"{name}.in").write_text("\n".join(lines) + "\n", encoding="utf-8")
    expected = solve(values, operations)
    (directory / f"{name}.out").write_text((expected + "\n") if expected else "", encoding="utf-8")


def main():
    random.seed(SEED)
    write_case(
        "sample",
        "sample1",
        [1, 2, 3, 4, 5],
        [(2, 1, 5), (1, 2, 4, 10), (2, 1, 3), (2, 4, 5)],
    )
    write_case("boundary", "single", [7], [(2, 1, 1), (1, 1, 1, -3), (2, 1, 1)])
    write_case(
        "boundary",
        "full_cover_then_point",
        [0, 0, 0, 0],
        [(1, 1, 4, 5), (2, 2, 2), (2, 1, 4)],
    )
    write_case(
        "adversarial",
        "pushdown_needed",
        [1, 1, 1, 1, 1, 1, 1, 1],
        [(1, 1, 8, 3), (2, 3, 6), (1, 4, 5, 2), (2, 1, 8), (2, 4, 4)],
    )
    write_case(
        "adversarial",
        "negative_updates",
        [10, -5, 7, 0, 3],
        [(1, 1, 3, -4), (2, 1, 5), (1, 2, 5, 6), (2, 2, 4)],
    )
    write_case(
        "adversarial",
        "int_overflow_sum",
        [1000000000, 1000000000, 1000000000],
        [(2, 1, 3), (1, 1, 3, 1000000000), (2, 1, 3)],
    )
    for idx in range(4):
        n = random.randint(5, 10)
        q = random.randint(8, 14)
        values = [random.randint(-20, 20) for _ in range(n)]
        operations = []
        for _ in range(q):
            l = random.randint(1, n)
            r = random.randint(l, n)
            if random.random() < 0.6:
                operations.append((1, l, r, random.randint(-15, 15)))
            else:
                operations.append((2, l, r))
        if not any(op[0] == 2 for op in operations):
            operations.append((2, 1, n))
        write_case("random", f"seeded_{idx:02d}", values, operations)


if __name__ == "__main__":
    main()

