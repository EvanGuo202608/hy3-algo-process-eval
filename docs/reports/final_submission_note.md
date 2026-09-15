# 最终提交说明

项目名称：AlgoTrace-Hy3  
GitHub 仓库：https://github.com/EvanGuo202608/hy3-algo-process-eval  
作者：郭昊杨，福州三中，信息学竞赛选手，NOIP 省一等奖  
任务方向：犀牛鸟开源·实战任务 2「可验证场景：过程评估与错误定位」—算法竞赛

## 项目一句话说明

AlgoTrace-Hy3 是一个面向算法竞赛的解题过程评估工具。它将结构化解题说明、C++17 代码、参考解和独立测试结合起来，不仅判断程序是否通过测试，还定位公开解题过程中的首个错误步骤，并输出错误类型、证据和置信度。

## 当前可验收成果

当前仓库已经完成七题离线验收版：

1. A01-pack-cost：模拟与整除边界；
2. A02-interval-removal：区间端点与重叠处理；
3. B01-pairing：排序与双指针贪心；
4. B02-cut-height：二分答案与单调性；
5. C01-rising-points：动态规划；
6. C02-minimum-network：Kruskal 与并查集；
7. D01-range-add-sum：简化线段树与 lazy propagation。

每题均包含自写规格、来源元数据、参考解、测试生成器、checker、固定测试、rubric、结构化解答样本和单元测试。

## 验收命令

```bash
python3 scripts/validate_problem_catalog.py
python3 -m unittest discover -s tests -q
```

也可以按 README 运行七题参考解复现和七个 demo。

## 真实性声明

本仓库不虚构尚未完成的结果。当前版本尚未声称完成真实 Hy3 大规模实验、人工双人复核、正式误报率统计或 2 分钟录屏成品。上述内容已在文档中标为后续工作。

## 推荐提交材料

- GitHub 仓库链接；
- `README.md`；
- `ACCEPTANCE_CHECKLIST.md`；
- `docs/reports/mvp_summary.md`；
- `docs/reports/final_submission_note.md`；
- `demo/demo_script.md`；
- GitHub Actions 成功截图或链接。

