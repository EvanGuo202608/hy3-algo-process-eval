# 验收清单

> 项目：AlgoTrace-Hy3 / hy3-algo-process-eval  
> 作者：郭昊杨｜福州三中｜信息学竞赛选手｜NOIP 省一等奖  
> 任务方向：犀牛鸟开源·实战任务 2「可验证场景：过程评估与错误定位」—算法竞赛  
> 当前版本：七题离线验收版，最后更新 2026-09-15  
> 声明：本项目是郭昊杨的个人/活动作品，非腾讯官方发布。

## 1. 当前验收结论

当前仓库已经具备可运行、可复现、可展示的离线验收版本。它不声称已经完成真实 Hy3 大规模实验、人工双人复核或正式 2 分钟录屏；这些仍在待完成项中明确列出。

本版本已经完成：

- 公开 GitHub 仓库；
- README、环境样例、运行说明；
- 7 道算法竞赛题的离线纵向切片；
- 每题独立规格、参考解、生成器、检查器、固定测试；
- 每题 3 条结构化解答轨迹；
- 规则评估器、代码运行器、聚合器和 CLI demo；
- “答案正确但过程错误”的可展示样例；
- GitHub Actions 无密钥 CI；
- 阶段 0/1 正式规划文档；
- 本验收包装文档、MVP 总结和 demo 脚本。

## 2. 官方要求对照

| 要求 | 当前文件或证据 | 状态 |
|---|---|---|
| 公开仓库 | https://github.com/EvanGuo202608/hy3-algo-process-eval | 已完成 |
| README 写清项目介绍、运行方式、环境要求 | `README.md` | 已完成 |
| 不提交 API Key | `.env.example`、`.gitignore`、README 安全说明 | 已完成 |
| 标注个人/活动作品、非腾讯官方 | `README.md`、`PROJECT_PLAN.md`、本文档 | 已完成 |
| 题集分层与来源说明 | `benchmarks/problem_catalog.yaml`、各题 `metadata.yaml` | 已完成 |
| 每题标准答案和自动校验 | 各题 `reference_solution.cpp`、`checker.py`、`tests/` | 已完成 |
| 输出结构化解答过程 | `fixtures/*/*.json`、`src/algotrace_hy3/schemas.py` | 已完成 |
| 过程正确性判定 | `src/algotrace_hy3/evaluator/rules.py` | 已完成，离线规则版 |
| 首个错误步骤定位 | `aggregate_result` 与各题单测 | 已完成，离线规则版 |
| 错误类型归类 | `annotations/annotation_guideline.md`、`annotations/gold.jsonl` | 已完成草稿 |
| 识别答案正确但过程不成立 | 七个 demo fixture、单测 | 已完成 |
| 验证定位准确率与误报率 | `docs/reports/mvp_summary.md` 说明当前离线验证状态 | 部分完成，真实 Hy3 实验待完成 |
| 完整分析报告 | `docs/reports/mvp_summary.md`、导出 Word/PDF | 验收版完成 |
| 2 分钟内 demo | `demo/demo_script.md` | 脚本完成，录屏待完成 |

## 3. 已完成题目

| ID | 方向 | 关键过程错误 |
|---|---|---|
| A01-pack-cost | 模拟 / 整除边界 | 把向上取整错误写成向下取整 |
| A02-interval-removal | 区间端点 / 重叠处理 | 把闭区间错误解释成开区间 |
| B01-pairing | 排序 + 双指针贪心 | 错误贪心证明、先配最轻者 |
| B02-cut-height | 二分答案 / 单调性 | 单调性方向说反、32 位累加风险 |
| C01-rising-points | 动态规划 | 严格递增误写成非严格递增 |
| C02-minimum-network | Kruskal / 并查集 | 直接取最小 n-1 条边、忽略判环 |
| D01-range-add-sum | 简化线段树 / lazy propagation | 区间加漏乘区间长度、忘记下传 lazy |

## 4. 一键验收命令

```bash
python3 scripts/validate_problem_catalog.py

for p in A01-pack-cost A02-interval-removal B01-pairing B02-cut-height C01-rising-points C02-minimum-network D01-range-add-sum; do
  python3 scripts/reproduce_problem.py --problem "$p"
done

python3 scripts/run_demo.py --problem A01-pack-cost
python3 scripts/run_demo.py --problem A02-interval-removal --fixture fixtures/a02_interval_removal/wrong_process_right_code.json
python3 scripts/run_demo.py --problem B01-pairing --fixture fixtures/b01_pairing/wrong_process_right_code.json
python3 scripts/run_demo.py --problem B02-cut-height --fixture fixtures/b02_cut_height/wrong_process_right_code.json
python3 scripts/run_demo.py --problem C01-rising-points --fixture fixtures/c01_rising_points/wrong_process_right_code.json
python3 scripts/run_demo.py --problem C02-minimum-network --fixture fixtures/c02_minimum_network/wrong_process_right_code.json
python3 scripts/run_demo.py --problem D01-range-add-sum --fixture fixtures/d01_range_add_sum/wrong_process_right_code.json

python3 -m unittest discover -s tests -q
```

最近一次本地验收结果：

- 目录校验通过；
- 七题参考解均 AC；
- 七个 demo 均可运行；
- 单元测试 24 个全部通过；
- GitHub Actions 通过。

## 5. 当前边界和未完成项

本仓库坚持不虚构结果。当前版本仍未完成：

- 真实 Hy3 在线端点调用与脱敏日志；
- 大规模真实模型实验；
- 人工双人复核与一致率；
- 正式定位准确率、误报率、Macro-F1 等统计表；
- 2 分钟以内录屏或 GIF 成品；
- 第 8 题 D02 的完整纵向切片。

若验收时间紧，可以提交当前七题验收版，并在说明中明确 D01 是简化 MVP、D02 是后续扩展。

