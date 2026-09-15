# B01-pairing

MVP 第三题，参考洛谷 P1094 的题型进行重新形式化：给定若干物品重量和每组承重上限，每组最多放两个物品，求最少需要多少组。

本目录不保存洛谷私有测试数据，也不复制第三方题解。仓库保存的是项目自写规格、参考实现和独立构造的测试点。

## 主要考点

- 排序；
- 双指针贪心；
- 交换论证；
- 重复值、单元素、刚好能配对和不能配对的边界；
- “答案正确但贪心证明不成立”的反例识别。

## 复现命令

```bash
python3 scripts/reproduce_problem.py --problem B01-pairing
python3 scripts/run_demo.py --problem B01-pairing --fixture fixtures/b01_pairing/wrong_process_right_code.json
```

