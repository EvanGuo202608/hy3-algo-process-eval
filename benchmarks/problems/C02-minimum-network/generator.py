#!/usr/bin/env python3
"""Generate deterministic C02 tests."""

from pathlib import Path
import random


ROOT = Path(__file__).resolve().parent
SEED = 20260906


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        self.parent[b] = a
        return True


def solve(n, edges):
    dsu = DSU(n)
    total = 0
    used = 0
    for u, v, w in sorted(edges, key=lambda item: item[2]):
        if dsu.unite(u, v):
            total += w
            used += 1
            if used == n - 1:
                break
    return str(total) if used == n - 1 else "orz"


def write_case(group, name, n, edges):
    directory = ROOT / "tests" / group
    directory.mkdir(parents=True, exist_ok=True)
    lines = [f"{n} {len(edges)}"]
    lines.extend(f"{u} {v} {w}" for u, v, w in edges)
    (directory / f"{name}.in").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (directory / f"{name}.out").write_text(solve(n, edges) + "\n", encoding="utf-8")


def main():
    random.seed(SEED)
    write_case("sample", "sample1", 4, [(1, 2, 1), (2, 3, 2), (3, 4, 3), (1, 4, 10), (1, 3, 4)])
    write_case("boundary", "single_node", 1, [])
    write_case("boundary", "disconnected", 4, [(1, 2, 3), (3, 4, 4)])
    write_case("boundary", "parallel_edges", 3, [(1, 2, 10), (1, 2, 1), (2, 3, 2), (1, 3, 100)])
    write_case("adversarial", "cycle_trap", 4, [(1, 2, 1), (2, 3, 1), (1, 3, 1), (3, 4, 100), (2, 4, 101)])
    write_case("adversarial", "self_loop", 3, [(1, 1, 0), (1, 2, 5), (2, 3, 6), (1, 3, 20)])
    for idx in range(4):
        n = random.randint(4, 8)
        edges = []
        for v in range(2, n + 1):
            u = random.randint(1, v - 1)
            edges.append((u, v, random.randint(1, 20)))
        extra = random.randint(n, n + 4)
        for _ in range(extra):
            u = random.randint(1, n)
            v = random.randint(1, n)
            w = random.randint(0, 30)
            edges.append((u, v, w))
        write_case("random", f"seeded_{idx:02d}", n, edges)


if __name__ == "__main__":
    main()

