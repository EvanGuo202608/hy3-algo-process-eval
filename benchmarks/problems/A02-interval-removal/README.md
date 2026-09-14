# A02-interval-removal

MVP 第二题，参考洛谷 P1047 的题型进行重新形式化：一条道路有 `0..L` 共 `L + 1` 个整数位置，若干闭区间内的位置被移除，求剩余位置数量。

本目录不保存洛谷私有测试数据，也不复制第三方题解。仓库保存的是项目自写规格、参考实现和独立构造的测试点。

## 主要考点

- 闭区间端点处理；
- 重叠区间去重；
- 最小规模和整段覆盖；
- “答案正确但过程错误地声称端点不包含”的反例识别。

## 复现命令

```bash
python3 scripts/reproduce_problem.py --problem A02-interval-removal
python3 scripts/run_demo.py --problem A02-interval-removal --fixture fixtures/a02_interval_removal/wrong_process_right_code.json
```

