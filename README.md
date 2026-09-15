# Hy3 Algorithm Process Evaluation

基于 Hy3 的算法竞赛解法过程评估与错误定位项目。

本项目是郭昊杨参与犀牛鸟开源实战任务的个人/活动作品，非腾讯官方发布。

## 一句话说明

普通 Online Judge 主要判断代码能否通过测试；本项目在此基础上继续检查公开的结构化解题过程，定位解题说明中最早出现的错误步骤，并归类错误类型。

## 项目负责人

郭昊杨，福州三中信息学竞赛选手，NOIP 省一等奖。

## 任务方向

本项目选择“犀牛鸟开源 · 实战任务 2：可验证场景——过程评估与错误定位”中的算法竞赛方向。

输入包括算法题目、约束、测试数据、结构化解法说明和 C++17 代码。输出包括：

- 程序是否通过独立测试；
- 解法思路、正确性论证、复杂度和边界处理是否成立；
- 首个错误步骤、错误类型、证据、严重程度和置信度；
- “最终答案正确但过程不能支撑结论”的样本识别。

## 5 分钟离线运行

当前阶段不需要 Hy3 API Key，可以先运行固定 fixture 验证工程闭环。

```bash
git clone https://github.com/EvanGuo202608/hy3-algo-process-eval.git
cd hy3-algo-process-eval
python3 scripts/validate_problem_catalog.py
python3 scripts/reproduce_problem.py --problem A01-pack-cost
python3 scripts/reproduce_problem.py --problem A02-interval-removal
python3 scripts/reproduce_problem.py --problem B01-pairing
python3 scripts/reproduce_problem.py --problem B02-cut-height
python3 scripts/run_demo.py --problem A01-pack-cost
python3 scripts/run_demo.py --problem A02-interval-removal --fixture fixtures/a02_interval_removal/wrong_process_right_code.json
python3 scripts/run_demo.py --problem B01-pairing --fixture fixtures/b01_pairing/wrong_process_right_code.json
python3 scripts/run_demo.py --problem B02-cut-height --fixture fixtures/b02_cut_height/wrong_process_right_code.json
python3 -m unittest discover -s tests -q
```

也可以使用包入口：

```bash
PYTHONPATH=src python3 -m algotrace_hy3 demo --problem A01-pack-cost
```

demo 默认展示 `A01-pack-cost` 中“代码通过测试，但公开推理过程使用了错误的整数除法依据”的样本；也可以切换到 `A02-interval-removal` 展示“端点处理解释错误但代码正确”的样本，切换到 `B01-pairing` 展示“贪心证明错误但代码正确”的样本，或切换到 `B02-cut-height` 展示“二分单调性解释反向但代码正确”的样本。

## 当前进度

- [x] 完成原始任务书核对
- [x] 完成阶段 0 需求追踪与项目规划
- [x] 完成阶段 1：20 题候选矩阵与 8 题 MVP 选题
- [x] 完成阶段 2 最小纵向切片：A01/A02/B01/B02 题目、参考解、测试、fixture、规则评估和 CLI demo
- [ ] 完成全部 8 题 MVP 的参考解、生成器、检查器和标注轨迹
- [ ] 接入真实 Hy3 端点并保存脱敏运行记录
- [ ] 完成定位准确率、误报率、人工抽检和最终报告
- [ ] 完成 2 分钟内 demo 视频或 GIF

## 重要文档

- [项目规划](PROJECT_PLAN.md)
- [需求追踪](docs/planning/requirement_traceability.md)
- [阶段一选题与评测集设计](docs/planning/stage1_problem_selection.md)
- [20 题候选目录](benchmarks/problem_catalog.yaml)
- [标注规范](annotations/annotation_guideline.md)
- [Gold 标签草稿](annotations/gold.jsonl)

## 目录结构

```text
src/algotrace_hy3/                 Python 工程代码
benchmarks/problem_catalog.yaml    阶段一候选题矩阵
benchmarks/problems/A01-pack-cost/ 第一题纵向切片
benchmarks/problems/A02-interval-removal/ 第二题纵向切片
benchmarks/problems/B01-pairing/ 第三题纵向切片
benchmarks/problems/B02-cut-height/ 第四题纵向切片
fixtures/a01_pack_cost/            A01 离线结构化解答样本
fixtures/a02_interval_removal/     A02 离线结构化解答样本
fixtures/b01_pairing/              B01 离线结构化解答样本
fixtures/b02_cut_height/           B02 离线结构化解答样本
annotations/                       标注规范和 gold 标签草稿
scripts/                           复现、校验和 demo 脚本
tests/                             无密钥单元测试
docs/planning/                     阶段规划文档
```

## Hy3 配置

真实 Hy3 调用通过环境变量配置，不在仓库中保存密钥。

```bash
cp .env.example .env
```

然后只在本地 `.env` 或系统环境变量中填写：

```text
HY3_BASE_URL
HY3_API_KEY
HY3_MODEL
HY3_TIMEOUT
HY3_TEMPERATURE
HY3_MAX_RETRIES
```

当前版本的在线 Hy3 调用仍处于待实现状态；离线 fixture 结果不会被写成真实 Hy3 实验结果。

## 安全说明

当前 C++17 runner 只用于仓库内固定 fixture 和自写参考解，不是完整安全沙盒。不要用它执行来源不明的代码。后续阶段会继续加入更严格的超时、内存、文件访问和网络限制说明。

## 真实性声明

本仓库不会虚构 Hy3 调用、人工复核、实验次数、准确率或 demo。尚未完成的功能、指标和演示均明确标为待实现。
