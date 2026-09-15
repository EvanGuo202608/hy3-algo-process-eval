# Cut Height

There are `n` trees. Tree `i` has height `h_i`. If the saw height is `x`, tree `i` contributes `max(0, h_i - x)` units of wood.

Find the maximum integer saw height `x` such that the total collected wood is at least `need`.

## Input

The first line contains two integers `n` and `need`.

The second line contains `n` non-negative integers `h_i`.

## Output

Print one integer: the maximum feasible saw height.

## Constraints

- `1 <= n <= 200000`
- `0 <= h_i <= 1000000000`
- `0 <= need <= sum(h_i)`

## Correctness Note

As `x` increases, collected wood never increases. Therefore feasibility is monotonic and binary search can find the maximum feasible height.

