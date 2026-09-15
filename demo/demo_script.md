# 2 分钟 demo 脚本

> 当前文件是录屏脚本，不是录屏成品。录制时长建议控制在 100—120 秒。

## 0:00—0:15 开场

画面：打开 GitHub 仓库首页。

讲解：

> 这是我的项目 AlgoTrace-Hy3，面向算法竞赛解法的过程评估与错误定位。普通 OJ 只能判断代码输出是否正确，而这个项目额外检查公开解题过程是否成立。

## 0:15—0:35 展示题集结构

画面：打开 `benchmarks/problems/` 和 `fixtures/`。

讲解：

> 当前验收版包含七道题，覆盖模拟、区间、贪心、二分、动态规划、并查集和简化线段树。每道题都有自写规格、参考解、生成器、checker、固定测试和结构化解答样本。

## 0:35—0:55 运行目录和测试校验

命令：

```bash
python3 scripts/validate_problem_catalog.py
python3 -m unittest discover -s tests -q
```

讲解：

> 这一步验证题目目录、MVP 题单和单元测试。当前共有 24 个无密钥测试，覆盖参考解通过、过程错误定位和错误代码失败。

## 0:55—1:25 展示一个“答案正确但过程错误”的样本

命令：

```bash
python3 scripts/run_demo.py --problem D01-range-add-sum --fixture fixtures/d01_range_add_sum/wrong_process_right_code.json
```

讲解：

> 这个样本的代码是正确的，但解释中说区间加时节点 sum 只需要加 delta。实际上节点存的是区间和，所以必须加 delta 乘以区间长度。项目会输出 final_correct 为 true，但 process_correct 为 false，并定位 first_error_step 为第 1 步。

## 1:25—1:45 展示图论样本

命令：

```bash
python3 scripts/run_demo.py --problem C02-minimum-network --fixture fixtures/c02_minimum_network/wrong_process_right_code.json
```

讲解：

> 这个样本代码使用 Kruskal 和并查集，可以通过测试；但过程声称直接取 n-1 条最小边，这会选到环，不能保证连通。因此评估器会把它判为答案正确但过程不成立。

## 1:45—2:00 收尾

画面：打开 `ACCEPTANCE_CHECKLIST.md` 或 Actions 页面。

讲解：

> 当前版本已经完成七题离线验收链路和 GitHub Actions。真实 Hy3 调用、人工双人复核和正式指标统计仍在后续工作中，仓库中没有虚构这些结果。

