# D01-range-add-sum

区间加、区间求和的线段树 lazy propagation 简化题。本题是原 D01「区间乘加求和」方向的验收版简化 MVP：保留线段树、区间更新、懒标记下传和区间查询这些核心过程评估点，暂不实现乘法懒标记与仿射组合。

## 复现

```bash
python3 benchmarks/problems/D01-range-add-sum/generator.py
python3 scripts/reproduce_problem.py --problem D01-range-add-sum
python3 scripts/run_demo.py --problem D01-range-add-sum --fixture fixtures/d01_range_add_sum/wrong_process_right_code.json
```

