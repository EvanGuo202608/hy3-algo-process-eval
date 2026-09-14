# A01-pack-cost

MVP 第一题，参考洛谷 P1909 的题型进行重新形式化：给定购买数量和三种包装规格，只能选择同一种包装，求至少买够所需数量的最小花费。

本目录不保存洛谷私有测试数据，也不复制第三方题解。仓库保存的是项目自写规格、参考实现和独立构造的测试点。

## 主要考点

- 整数向上取整；
- 三种方案枚举；
- 最小规模和不能整除的边界；
- “答案正确但过程使用向下取整”的反例识别。

## 复现命令

```bash
python3 scripts/reproduce_problem.py --problem A01-pack-cost
python3 scripts/run_demo.py --problem A01-pack-cost
```

