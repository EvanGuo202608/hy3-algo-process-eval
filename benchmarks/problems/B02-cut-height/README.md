# B02-cut-height

MVP 第四题，参考洛谷 P1873 的题型进行重新形式化：给定若干树高和需要获得的木材量，选择切割高度，使得到的木材不少于目标值且切割高度尽可能高。

本目录不保存洛谷私有测试数据，也不复制第三方题解。仓库保存的是项目自写规格、参考实现和独立构造的测试点。

## 主要考点

- 二分答案；
- 单调性证明；
- 边界更新；
- `long long` 累加；
- “代码正确但单调性解释说反”的反例识别。

## 复现命令

```bash
python3 scripts/reproduce_problem.py --problem B02-cut-height
python3 scripts/run_demo.py --problem B02-cut-height --fixture fixtures/b02_cut_height/wrong_process_right_code.json
```

