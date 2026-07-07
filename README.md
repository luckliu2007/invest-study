# invest-study 📈

> 投资研究 / 量化 / 基金实务的**系统性自学与团队培训仓库**。
> 由交易分析团队基于公开资料持续维护，融合基本面、技术面、量化与 AI 投研新风。

## 🧭 快速导航
- 📍 **完整学习路径**：[`FULL_LEARNING_PATH.md`](./FULL_LEARNING_PATH.md)（8 章，理论→实战→代码→项目）
- 🌟 **全网精选资源(2026)**：[`TOP_RESOURCES_2026.md`](./TOP_RESOURCES_2026.md)（课程/书/数据/大师/AI）
- 🤖 **AI 投研手册**：[`docs/ai_finance_playbook.md`](./docs/ai_finance_playbook.md)
- 📋 **基金实务模板**：[`docs/`](./docs)（设立清单 / PPM / 合伙协议）
- 🛠️ **可运行脚本**：[`scripts/`](./scripts)（筛选 / 组合优化 / 募集跟踪）
- 🔧 **自动化 CI**：[`.github/workflows/backtest.yml`](./.github/workflows/backtest.yml)

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
| 10 | financetoolkit | 财务+估值工具 | https://github.com/joshyattridge/financetoolkit |
| 11 | mplfinance | K线图表 | https://github.com/matplotlib/mplfinance |
| 12 | 量化投资学习(中文) | 中文因子/回测笔记 | https://github.com/CatsJuice/quantitative-investment-learning |

> 更多课程/书单/数据/大师资源见 [`TOP_RESOURCES_2026.md`](./TOP_RESOURCES_2026.md)。

## 📂 仓库结构
```
invest-study/
├─ README.md                     # 本文件：导航 + 资源总览
├─ FULL_LEARNING_PATH.md        # 完整学习路径（8 章）
├─ TOP_RESOURCES_2026.md        # 全网精选资源（2026）
├─ requirements.txt             # Python 依赖
├─ scripts/                     # 可运行脚本
│  ├─ sector_screening.py       # 赛道/因子筛选
│  ├─ optimize_portfolio.py     # 组合优化（最小波动/最大夏普）
│  └─ fund_raise_tracker.py     # 募集进度跟踪(xlsx)
├─ docs/                        # 模板与手册
│  ├─ fund_setup_checklist.md
│  ├─ PPM_template.md
│  ├─ partnership_agreement_template.md
│  ├─ ai_finance_playbook.md
│  └─ enneagram_learning_guide.md   # （个人发展，与投研无关，保留）
├─ .github/workflows/backtest.yml    # 每日回测 CI
├─ notebooks/  data/  reports/  legal/  presentations/  # 学习产物目录
```

## 🚀 快速开始
```bash
pip install -r requirements.txt
python scripts/sector_screening.py      # 跑筛选
python scripts/optimize_portfolio.py    # 跑组合优化
python scripts/fund_raise_tracker.py    # 生成募集跟踪表
```

## 🤝 贡献
欢迎 PR 补充资源、修正链接、提交练习 Notebook。

---
⚠️ 本仓库为学习/培训用途，所有内容不构成投资建议。
