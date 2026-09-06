# AlgoTrace-Hy3 标注规范

版本：v1.0  
日期：2026-09-07  
作者：郭昊杨（福州三中）

> 本规范属于郭昊杨的个人/活动作品，非腾讯官方发布。标注对象是公开的结构化解题说明与代码，不包含模型隐藏思维链。

## 1 标注单位

一条轨迹由题目 ID、结构化步骤、复杂度声明、边界说明、C++17 代码和最终判定组成。标注者先独立运行参考测试，再阅读步骤。不能因为代码通过就默认过程正确，也不能因为过程总体合理就忽略实现错误。

## 2 必填 gold 字段

```yaml
trace_id: ""
problem_id: ""
source: "human_correct|hy3_output|single_error_injection|multi_error_injection"
final_correct: false
process_correct: false
first_error_step: null
error_types: []
evidence: ""
counterexample_id: null
annotator: "guo_haoyang"
reviewer: null
review_status: "draft|reviewed|disputed|resolved"
```

`final_correct` 只由冻结测试集和检查器决定。`process_correct` 判断公开说明能否支持算法、复杂度和边界结论。`first_error_step` 是最早出现不正确或无法成立的步骤编号，无错误时为 `null`。

## 3 错误分类

- E1：题意、输入输出、约束或目标理解错误。
- E2：建模或核心算法不能保证正确。
- E3：不变量、归纳、交换论证、单调性或充分必要性错误。
- E4：复杂度分析与实现不一致，或无法满足约束。
- E5：边界、初始化、下标、空集、重复值、整数溢出、模运算或精度错误。
- E6：代码偏离正确思路，更新顺序或数据结构操作错误。
- E7：只对样例或弱测试成立，错误实现偶然通过。
- E8：虚构性质、步骤矛盾或证据不足。

可以同时标多个 `error_types`，但 `first_error_step` 只有一个。分类必须附可复核证据，优先给出最小反例或具体代码位置。

## 4 首错定位规则

1. 按 `step_id` 顺序检查 claim、justification 和 dependencies。
2. 如果早期步骤只是表述不够漂亮但仍正确，不标错。
3. 如果某步骤依赖一个未给出但标准且显然的定义，可标 `needs_clarification`，不要强行判错。
4. 若步骤首次提出错误核心算法，后续实现错误均为次生错误；首错仍是算法步骤。
5. 若思路和证明正确，代码第一次偏离思路的位置属于 E6，首错步骤取相应 implementation 步骤。
6. 若代码通过全部冻结测试，但过程中的关键论断存在反例，仍标 `final_correct: true`、`process_correct: false`。

## 5 四象限配额

MVP 每题至少 4 条轨迹：

| 象限 | final_correct | process_correct | 最低数量 |
|---|---:|---:|---:|
| Q1 | true | true | 1 |
| Q2 | true | false | 1 |
| Q3 | false | true 或前段正确 | 1 |
| Q4 | false | false | 1 |

正式版每题建议 6 条，增加一条边界错误和一条复杂度或证据错误。单错误注入应占多数，以保证首错标签清楚。

## 6 审核流程

标注者先填写 draft，运行测试并补充证据。所有错误轨迹和 Q2 轨迹必须人工复核。复核者不同意时将状态改为 `disputed`，保存双方理由，确定最终标签后改为 `resolved`。只有一名标注者时，报告必须明确这一限制。

## 7 禁止事项

- 不把评估器预测复制成 gold。
- 不虚构 Hy3 输出、运行次数、复核者或实验指标。
- 不保存密钥、账号密码或其他个人敏感信息。
- 不复制洛谷私有测试或第三方题解。
- 不要求模型给出不可见的内部思维链。

## 8 质量检查

每条标注至少回答四个问题：代码是否通过冻结测试；公开过程是否能推出算法；复杂度是否与代码一致并满足约束；首错证据能否由另一名选手复现。

