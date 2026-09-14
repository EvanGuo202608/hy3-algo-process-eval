# Interval Removal

A road contains integer positions from `0` to `L`, inclusive. Initially every position exists. There are `m` removal operations. Each operation gives a closed interval `[left, right]`; every integer position in that interval is removed.

Find how many positions remain after all removals.

## Input

The first line contains two integers `L` and `m`.

The next `m` lines each contain two integers `left` and `right`.

## Output

Print one integer: the number of remaining positions.

## Constraints

- `0 <= L <= 10000`
- `0 <= m <= 1000`
- `0 <= left <= right <= L`

## Correctness Note

Because `L` is small, directly marking every removed integer position is sufficient. Intervals are inclusive, so both endpoints must be removed.

