# C01-rising-points

二维上升点列问题。给定若干平面点，求能选出的最长序列长度，使序列中点的 `x` 坐标和 `y` 坐标都严格递增。

本题用于覆盖动态规划状态定义、转移条件、排序预处理、严格不等号和重复坐标边界。来源页面仅用于选题和难度参考；仓库内保存的是自写规格、独立参考解和固定测试。

## 复现

```bash
python3 benchmarks/problems/C01-rising-points/generator.py
python3 scripts/reproduce_problem.py --problem C01-rising-points
python3 scripts/run_demo.py --problem C01-rising-points --fixture fixtures/c01_rising_points/wrong_process_right_code.json
```

