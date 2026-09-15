# C02-minimum-network

最小连通网络问题。给定无向带权图，选择若干条边使所有点连通，并使边权和最小；若图不连通，输出 `orz`。

本题用于覆盖 Kruskal 最小生成树、并查集维护连通分量、环检测、连通性判断和“只选最小边不等于 MST”的典型过程错误。来源页面仅用于选题和难度参考；仓库内保存的是自写规格、独立参考解和固定测试。

## 复现

```bash
python3 benchmarks/problems/C02-minimum-network/generator.py
python3 scripts/reproduce_problem.py --problem C02-minimum-network
python3 scripts/run_demo.py --problem C02-minimum-network --fixture fixtures/c02_minimum_network/wrong_process_right_code.json
```

