# MVP 验收总结

> 项目：AlgoTrace-Hy3  
> 仓库：EvanGuo202608/hy3-algo-process-eval  
> 作者：郭昊杨｜福州三中｜NOIP 省一等奖  
> 日期：2026-09-15  
> 版本：七题离线验收版

## 1. 项目目标

AlgoTrace-Hy3 面向算法竞赛场景，评估结构化解题过程与 C++17 代码。它不仅判断程序是否通过测试，还尝试检查解法思路、复杂度分析、边界处理和公开推理过程是否成立，并定位首个错误步骤。

当前验收版聚焦本地可复现链路：

1. 给定题目规格和固定测试；
2. 编译运行 C++17 代码；
3. 校验结构化解题 JSON；
4. 用规则评估器检查典型过程错误；
5. 聚合输出最终正确性、过程正确性、首错步骤、错误类型、证据和置信度。

## 2. 为什么普通 OJ 不够

普通 OJ 主要判断程序输出是否正确，但无法直接判断解释过程是否成立。例如：

- 程序使用了正确的向上取整公式，但解释说成了向下取整；
- 代码正确处理闭区间端点，但文字过程声称端点不包含；
- Kruskal 代码正确使用 DSU，但过程声称“直接取 n-1 条最小边”；
- 线段树代码正确使用 `delta * len`，但过程说“节点 sum 只加 delta”。

这些样本的最终答案可能正确，但过程不能支撑结论，正是本任务“过程评估与错误定位”的核心价值。

## 3. 当前题集覆盖

| 层级 | 题目 | 算法方向 | 覆盖错误 |
|---|---|---|---|
| A | A01-pack-cost | 模拟、整除边界 | E5、E3 |
| A | A02-interval-removal | 区间端点、重叠 | E1、E5、E6 |
| B | B01-pairing | 排序、双指针贪心 | E2、E3 |
| B | B02-cut-height | 二分答案、单调性 | E3、E4、E5 |
| C | C01-rising-points | 动态规划 | E2、E3、E5、E6 |
| C | C02-minimum-network | Kruskal、并查集 | E2、E3、E5、E6 |
| D | D01-range-add-sum | 简化线段树、lazy propagation | E4、E5、E6 |

说明：D01 原候选来自线段树 2 的方向。考虑验收时间，本版本采用区间加、区间求和的简化 MVP，保留 lazy propagation 的核心错误模式，暂不实现乘法懒标记和仿射组合。

## 4. 数据与样本

每道题包含：

- `metadata.yaml`：来源、难度、算法和复现信息；
- `statement_or_spec.md`：自写规格；
- `reference_solution.cpp`：C++17 参考解；
- `generator.py`：固定种子测试生成器；
- `checker.py`：输出校验器；
- `tests/`：样例、边界、对抗和随机测试；
- `rubric.yaml`：过程评估要点和常见错误；
- `fixtures/`：结构化解答样本。

当前共有：

- 7 道题；
- 每题 3 条结构化轨迹；
- 共 21 条 gold 标签草稿；
- 24 个单元测试。

## 5. 复现结果

最近一次本地运行结果：

| 项目 | 结果 |
|---|---|
| catalog 校验 | 通过 |
| A01 参考解 | AC 5/5 |
| A02 参考解 | AC 6/6 |
| B01 参考解 | AC 6/6 |
| B02 参考解 | AC 6/6 |
| C01 参考解 | AC 10/10 |
| C02 参考解 | AC 10/10 |
| D01 参考解 | AC 10/10 |
| CLI demo | 7 个均可运行 |
| 单元测试 | 24 个全部通过 |
| GitHub Actions | 通过 |

## 6. 当前有效性验证口径

当前版本是离线验收版，验证重点是工程链路与典型错误识别：

- 每题至少包含一个“答案正确但过程错误”的 fixture；
- 每题至少包含一个“代码错误会被测试打掉”的 fixture；
- 每个 demo 都输出 `correct_answer_wrong_process: true`；
- 单元测试检查参考解 AC、过程错误定位、错误代码失败。

尚未声称完成真实 Hy3 输出上的统计指标。正式指标仍需在接入 Hy3 后运行：

- Final Answer Accuracy；
- Process Correct Rate；
- Error Detection Recall；
- Exact Localization Accuracy；
- Relaxed Localization Accuracy；
- False Positive Rate；
- Error Type Macro-F1。

## 7. 局限与下一步

当前局限：

1. 过程评估主要是规则层，尚未接入真实 Hy3 审查层；
2. gold 标签为本人草稿，尚未完成双人复核；
3. D01 是简化版线段树，不是完整区间乘加；
4. 尚未制作正式录屏或 GIF；
5. 尚未完成 D02。

建议验收提交策略：

- 提交当前七题验收版；
- 明确说明 D01 是为了按时验收采用的简化 MVP；
- 把 D02、真实 Hy3 实验和人工复核列为后续扩展；
- 录制 2 分钟 demo 时优先展示 A01、C02、D01 三个代表样本。

