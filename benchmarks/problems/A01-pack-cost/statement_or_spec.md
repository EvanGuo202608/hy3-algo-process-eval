# Pack Cost

You need to buy at least `n` pencils. The shop provides three package types. Package type `i` contains `count_i` pencils and costs `price_i`.

You may choose exactly one package type and buy any positive integer number of packages of that type. Find the minimum total cost that buys at least `n` pencils.

## Input

The first line contains integer `n`.

The next three lines each contain two positive integers `count_i` and `price_i`.

## Output

Print one integer: the minimum total cost.

## Constraints

- `1 <= n <= 100000`
- `1 <= count_i, price_i <= 100000`
- The answer fits in signed 64-bit integer arithmetic.

## Correctness Note

For one package type, the number of packages needed is `ceil(n / count_i)`. Since there are only three package types, checking all three and taking the minimum is sufficient.

