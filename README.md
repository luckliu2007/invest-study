# invest-study 📈

[![CI](https://github.com/luckliu2007/invest-study/actions/workflows/backtest.yml/badge.svg)](https://github.com/luckliu2007/invest-study/actions/workflows/backtest.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-pytest-green.svg)](./tests)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

> 投资研究 / 量化 / 基金实务的**系统性自学与团队培训仓库**。
> 由交易分析团队基于公开资料持续维护，融合基本面、技术面、量化与 AI 投研新风。

## 🧭 快速导航
- 📍 **完整学习路径**：[`FULL_LEARNING_PATH.md`](./FULL_LEARNING_PATH.md)（8 章，理论→实战→代码→项目）
- 🌟 **全网精选资源(2026)**：[`TOP_RESOURCES_2026.md`](./TOP_RESOURCES_2026.md)（课程/书/数据/大师/AI）
- 🤖 **AI 投研手册**：[`docs/ai_finance_playbook.md`](./docs/ai_finance_playbook.md)
- 📋 **基金实务模板**：[`docs/`](./docs)（设立清单 / PPM / 合伙协议）
- 🛠️ **可运行脚本**：[`scripts/`](./scripts)（筛选 / 组合优化 / 募集跟踪 / 退出模拟）
- ✅ **单元测试**：[`tests/`](./tests)（`pytest`，覆盖脚本核心逻辑与降级路径）
- 🔧 **自动化 CI**：[`.github/workflows/backtest.yml`](./.github/workflows/backtest.yml)（test + smoke 两段式）

## 🗂️ 资源总览（GitHub 开源项目）
| # | 项目 | 简介 | 链接 |
|---|------|------|------|
| 1 | awesome-quant | 量化总索引（库/数据/书单） | https://github.com/wilsonfreitas/awesome-quant |
| 2 | OpenBB Terminal | 开源投研终端 | https://github.com/OpenBB-finance/OpenBB |
| 3 | Machine Learning for Trading | 算法交易 ML 代码 | https://github.com/stefan-jansen/machine-learning-for-trading |
| 4 | financial-machine-learning | 金融 ML 案例集 | https://github.com/firmai/financial-machine-learning |
| 5 | pybroker | ML 算法交易框架 | https://github.com/edtechre/pybroker |
| 6 | QuantConnect/Lean | 机构级回测引擎 | https://github.com/QuantConnect/Lean |
| 7 | bt | 组合回测框架 | https://github.com/pmorissette/bt |
| 8 | yfinance | 行情/财报抓取 | https://github.com/ranaroussi/yfinance |
| 9 | quantstats | 绩效/风险分析 | https://github.com/ranaroussi/quantstats |
| 10 | FinanceToolkit | 财务+估值工具 | https://github.com/JerBouma/FinanceToolkit |
| 11 | mplfinance | K线图表 | https://github.com/matplotlib/mplfinance |
| 12 | 量化投资学习(中文) | 中文因子/回测笔记 | https://github.com/CatsJuice/quantitative-investment-learning |

> 更多课程/书单/数据/大师资源见 [`TOP_RESOURCES_2026.md`](./TOP_RESOURCES_2026.md)。

## 📂 仓库结构
```
invest-study/
├─ README.md                     # 本文件：导航 + 资源总览
├─ FULL_LEARNING_PATH.md        # 完整学习路径（8 章）
├─ TOP_RESOURCES_2026.md        # 全网精选资源（2026）
├─ requirements.txt             # 完整学习环境依赖
├─ requirements-ci.txt          # CI 冒烟测试最小依赖
├─ scripts/                     # 可运行脚本（结果输出到 reports/）
│  ├─ sector_screening.py       # 赛道/因子筛选
│  ├─ optimize_portfolio.py     # 组合优化（最小波动/最大夏普）
│  ├─ fund_raise_tracker.py     # 募集进度跟踪(xlsx)
│  └─ exit_simulation.py        # 退出/并购溢价 IRR 模拟
├─ tests/                       # pytest 单元测试（覆盖降级路径）
├─ docs/                        # 模板与手册
│  ├─ fund_setup_checklist.md
│  ├─ PPM_template.md
│  ├─ partnership_agreement_template.md
│  ├─ ai_finance_playbook.md
│  └─ enneagram_learning_guide.md   # （个人发展，与投研无关，保留）
├─ .github/workflows/backtest.yml    # 每日回测 CI（产物存 artifact）
├─ notebooks/  data/  reports/       # 学习产物目录
```

## 🚀 快速开始
```bash
pip install -r requirements.txt         # 完整环境（或只装 requirements-ci.txt 快速体验）
python scripts/sector_screening.py      # 跑筛选 → reports/sector_screening.csv
python scripts/optimize_portfolio.py    # 跑组合优化 → reports/portfolio_weights.csv
python scripts/fund_raise_tracker.py    # 生成募集跟踪表 → reports/fund_raise_tracker.xlsx
python scripts/exit_simulation.py       # 退出溢价 IRR 模拟 → reports/exit_simulation.csv
```

> 所有脚本在无网络 / 缺少可选依赖时会自动降级为内置示例数据，保证流程可跑通。

## ✅ 运行测试

```bash
pip install -r requirements-test.txt    # 轻量测试依赖
pytest                                   # 运行全部单元测试
```

## 🤝 贡献
欢迎 PR 补充资源、修正链接、提交练习 Notebook。

---
⚠️ 本仓库为学习/培训用途，所有内容不构成投资建议。
