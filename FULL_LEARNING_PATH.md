# 投资全链路学习路径（从理论到实战）

## 🎯 目标

- 掌握基金业务全流程：从设立、募集、投资、投后管理到清算退出
- 学会赛道选标：依据宏观、行业、竞争格局、商业模式进行筛选
- 实现自动化：用 Python / Quant 框架实现数据抓取、因子筛选、组合构建、风险监控

> 章节采用 “理论 → 实战 → 代码/工具 → 项目练习” 的递进方式，适合自学和团队内部培训。

## 1️⃣ 基础理论

| 章节 | 关键概念 | 推荐资源 |
|------|----------|----------|
| 1.1 金融基础 | 资产类别、风险收益、时间价值、资本资产定价模型（CAPM） | 《Investopedia》<br>《金融学（第七版）》 |
| 1.2 私募/公募基金制度 | 基金设立流程、监管要求（证监会《私募投资基金监督管理暂行办法》） | 《私募基金实务》<br>证监会官方文档 |
| 1.3 行业赛道模型 | 波特五力、PESTEL、产业链价值结构 | 《波特竞争战略》<br>《麦肯锡行业洞察》 |
| 1.4 投资决策框架 | 4C/5C、DCF、相对估值、PE/EV、成长率、竞争壁垒 | 《公司金融（第11版）》<br>《估值：衡量企业价值的12个模型》 |

### 学习建议
- 每章阅读 30‑45 分钟，随后用 10‑15 分钟把概念写成 **One‑Pager**（Markdown），放入 `reports/`。
- 完成后在 **Obsidian** 中创建对应笔记并链接到 `FULL_LEARNING_PATH.md`。

## 2️⃣ 基金设立与运营

| 步骤 | 说明 | 关键输出文件 |
|------|------|---------------|
| 2.1 设立基金公司 | 备案、备案材料、合规审计 | `docs/fund_setup_checklist.md` |
| 2.2 编写基金募集说明书（PPM） | 投资策略、风险揭示、费用结构 | `docs/PPM_template.md` |
| 2.3 合伙协议 & 法律文件 | GP/LP 权责、收益分配、退出机制 | `legal/partnership_agreement_template.md` |
| 2.4 募集 & 投资者关系 | CRM、路演 PPT、投资者问答库 | `presentations/roadshow.pptx` |
| 2.5 监管报送 & 报告 | 月度/季报、审计报告、税务申报 | `reports/quarterly_report_template.md` |

**实战练习**
1. 用 **Markdown** 完成一份 **《模拟私募基金募集说明书》**（约 5 页），提交到 `docs/`。
2. 用 **Python** 生成 **募集进度表（Excel）**（`scripts/fund_raise_tracker.py`），示例已有。

## 3️⃣ 赛道与标的筛选（系统化方法）

### 3.1 宏观‑行业‑公司三级框架
1. **宏观**：GDP、消费、政策、利率 → 使用 **World Bank API、CPI、央行数据**（可通过 `akshare`、`pandas_datareader`）
2. **行业**：行业规模、成长率、进入壁垒 → 抓取 **Wind/同花顺行业报告**（或公开的行业协会 PDF）
3. **公司**：财务健康、竞争优势、估值 | 关键指标：ROE、毛利率、自由现金流、负债率、PE、PB、EV/EBITDA |

### 3.2 常用筛选工具
| 工具 | 说明 | 示例仓库 |
|------|------|----------|
| **AkShare** | 国内 A 股、行业、宏观数据 | `akshare` 官方文档 |
| **yfinance** | 海外上市公司行情、财报 | `stefan-jansen/machine-learning-for-trading` |
| **FactorHub（自建）** | 多因子库（价值、成长、质量） | `edtechre/pybroker`（可改写） |
| **SQL/BigQuery** | 大数据批量筛选 | `edtechre/pybroker` 中的 **SQL 示例** |

### 3.3 示例筛选流程（Python）
```python
import akshare as ak
import pandas as pd

# 1️⃣ 拉取所有 A 股上市公司基本信息
stock_df = ak.stock_zh_a_spot()
stock_df = stock_df.rename(columns={'symbol': 'ticker'})

# 2️⃣ 过滤行业（如 “新能源车”）
target_ind = stock_df[stock_df['industry'].str.contains('新能源车')]

# 3️⃣ 拉取最近一季财报
def get_fundamentals(ticker):
    df = ak.stock_financial_report_by_category(symbol=ticker, category="profit")
    return df

funds = [get_fundamentals(t) for t in target_ind['ticker'].tolist()[:50]]
funds_df = pd.concat(funds)

# 4️⃣ 计算关键因子
funds_df['ROE'] = funds_df['netprofit'] / funds_df['equity']
funds_df['PE']  = funds_df['close'] / (funds_df['netprofit'] / funds_df['shares'])

# 5️⃣ 条件筛选：ROE>15% 且 PE<20
candidates = funds_df[(funds_df['ROE']>0.15) & (funds_df['PE']<20)]

print(candidates[['ticker','ROE','PE']].head())
```
> 将上面代码保存为 `scripts/sector_screening.py`，并在 `README.md` 中写明使用方法。

## 4️⃣ 投资组合构建 & 风险管理

| 步骤 | 说明 | 参考实现 |
|------|------|----------|
| 4.1 因子模型构建 | 价值、规模、动量、质量因子 | `edtechre/pybroker` 示例 `factor_model.py` |
| 4.2 资产配置优化 | 均值‑方差、风险平价、黑利特 | `pyportfolioopt`（`pip install pyportfolioopt`） |
| 4.3 组合回测 | 使用 **Backtrader**、**Zipline** | `strategy/sma_cross_vol.py`（改为多资产） |
| 4.4 风险监控 | VaR、最大回撤、行业敞口 | `monitor/watchdog.py` 扩展监控指标 |
| 4.5 投后报告 | 周报、月报、投资回报分析 | `reports/portfolio_report_template.md` |

**示例：使用 `pyportfolioopt` 进行最小波动率组合**
```python
import pandas as pd
from pypfopt import EfficientFrontier, risk_models, expected_returns

price_df = pd.read_csv('data/price_history.csv', parse_dates=['date'], index_col='date')
# 计算年化收益率和协方差矩阵
mu = expected_returns.mean_historical_return(price_df)
S  = risk_models.sample_cov(price_df)

ef = EfficientFrontier(mu, S)
ef.min_volatility()
weights = ef.clean_weights()
print(weights)
```
> 将代码保存为 `scripts/optimize_portfolio.py`，在 `reports/` 中加入运行结果的 Markdown 表格。

## 5️⃣ 投后管理 & 退出机制

| 项目 | 内容 | 推荐工具 |
|------|------|----------|
| 5.1 运营报表 | 投资进度、业绩、现金流 | `pandas` + `openpyxl` |
| 5.2 监控 KPI | 市占率、毛利率、用户增长 | PowerBI / Superset |
| 5.3 退出评估 | IPO、并购、二级市场套现 | DCF、相对估值、交易对手数据 |
| 5.4 合规审计 | 合规审查、税务优化 | 法务模板、审计清单 |

**练手项目**：在 `scripts/exit_simulation.py` 中实现一个 **并购溢价模拟器**（输入目标公司估值、溢价比例，输出 IRR）。

## 6️⃣ 推荐学习资源（完整列表）

### 6.1 代码仓库（已在 `README.md` ）
- `firmai/financial-machine-learning`
- `stefan-jansen/machine-learning-for-trading`
- `edtechre/pybroker`
- `PeterSchuld/EDHEC_Investment-Management-with-Python-and-Machine-Learning-`
- `kristina969/Empirical-Asset-Pricing-via-Machine-Learning...`
- …（其余 5 项同上）

### 6.2 经典书籍
| 书名 | 作者 | 适用阶段 |
|------|------|----------|
| 《私募基金实务》 | 陈晓 | 基础、设立 |
| 《金融市场与机构》 | Frederic Mishkin | 理论 |
| 《公司金融（第11版）》 | Ross, Westerfield & Jaffe | 估值、资本结构 |
| 《估值：衡量企业价值的12个模型》 | Aswath Damodaran | 估值 |
| 《Algorithmic Trading: Winning Strategies & Their Rationale》 | Ernest Chan | 实战 |

### 6.3 在线课程
| 平台 | 课程 | 链接 |
|------|------|------|
| Coursera | “Investment Management” (University of Geneva) | https://www.coursera.org/learn/investment-management |
| Udemy | “Python for Financial Analysis & Algorithmic Trading” | https://www.udemy.com/course/python-for-financial-analysis/ |
| edX | “Machine Learning for Trading” (Georgia Tech) | https://www.edx.org/course/machine-learning-for-trading |
| CFA Institute | “Investment Foundations” (免费) | https://www.cfainstitute.org/en/programs/investment-foundations |

### 6.4 博客 / 资讯
| 名称 | 方向 | 链接 |
|------|------|------|
| **QuantStart** | 量化教学、实战案例 | https://www.quantstart.com |
| **Alpha Architect** | 因子研究、行业报告 | https://alphaarchitect.com |
| **机器之心 – 金融AI** | 中文前沿技术 | https://www.jiqizhixin.com |
| **Seeking Alpha** | 投资者观点、深度分析 | https://seekingalpha.com |
| **东财行业研究** | 行业数据、报告 | https://www.eastmoney.com |

### 6.5 播客 & 简报
| 名称 | 内容 | 链接 |
|------|------|------|
| **The Investors Podcast** | 投资理念、案例分析 | https://www.theinvestorspodcast.com |
| **Chat With Traders** | 交易员访谈 | https://chatwithtraders.com |
| **Finimize Daily** | 每日金融要点 | https://www.finimize.com |
| **Morning Brew – Markets** | 市场快讯 | https://morningbrew.com/markets |
| **Epsilon Theory** | 宏观视角、金融历史 | https://www.epsilon-theory.com |

## 7️⃣ 项目练习路线（建议时间表）

| 周次 | 主题 | 任务 |
|------|------|------|
| 1‑2 | 金融基础 & 基金设立 | 完成《私募基金实务》第1‑3章阅读，撰写《基金设立检查清单》 |
| 3‑4 | 行业赛道模型 | 用 `AkShare` 抓取新能源车行业数据，写 **行业报告**（Markdown） |
| 5‑6 | 标的筛选实战 | 编写 `scripts/sector_screening.py`，筛选出 5 只符合 ROE/PE 条件的 A 股 |
| 7‑8 | 组合构建与回测 | 使用 `pyportfolioopt` 生成最小波动组合；回测 1 年，输出报告 |
| 9‑10| 投后监控 | 搭建 `monitor/watchdog.py` 实时监控组合最大回撤、行业敞口 |
| 11‑12| 项目汇总 | 将所有 Notebook、脚本、报告统一放入 `invest-study`，在 `README.md` 添加目录链接，提交 PR 并通过 CI 自动生成 PDF 报告 |

> **每个阶段完成后**，在 `reports/` 中写一篇 **学习总结**（约 800‑1200 字），记录收获、难点、下一步计划。

## 8️⃣ 自动化 & CI（可选）

### 示例 GitHub Action：每日回测并生成 PDF
```yaml
# .github/workflows/backtest.yml
name: Daily Backtest

on:
  schedule:
    - cron: '0 1 * * *'   # 每天 01:00 UTC（北京时间 09:00）

jobs:
  backtest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - name: Install deps
        run: |
          pip install -r requirements.txt
          pip install pandas akshare pyportfolioopt
      - name: Run screening & optimization
        run: |
          python scripts/sector_screening.py > reports/screening_$(date +%F).md
          python scripts/optimize_portfolio.py >> reports/optimization_$(date +%F).md
      - name: Convert reports to PDF
        run: |
          pip install weasyprint
          weasyprint reports/screening_$(date +%F).md reports/screening_$(date +%F).pdf
          weasyprint reports/optimization_$(date +%F).md reports/optimization_$(date +%F).pdf
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: daily-reports
          path: reports/*.pdf
```
> 将上述文件保存为 `.github/workflows/backtest.yml`，提交后即可在 **GitHub Actions** 页面看到每日自动运行的回测报告。

## 📂 项目结构（更新后）
```
invest-study/
│
├─ README.md                     # 资源总览（已更新）
├─ FULL_LEARNING_PATH.md        # 完整学习路线（本文件）
├─ notebooks/                    # Jupyter Notebook（学习实验）
├─ data/                         # 原始行情、财报 CSV
├─ scripts/                      # 数据抓取、筛选、组合优化脚本
│   ├─ sector_screening.py
│   ├─ optimize_portfolio.py
│   └─ fund_raise_tracker.py
├─ reports/                      # 学习报告、回测结果、PDF
├─ docs/                         # 基金设立、PPM、合伙协议模板
├─ legal/                        # 法务模板
├─ presentations/                # 路演 PPT、投资者问答
└─ .github/
    └─ workflows/
        └─ backtest.yml          # 自动化回测 CI
```

---

## ✅ 接下来可以做的事

1. **克隆仓库** 并创建上述目录结构（若已存在，可直接使用）。
2. **挑选第一阶段资源**（如 `anthonyng2/Machine-Learning-For-Finance`），把对应 Notebook 放在 `notebooks/`，完成 **财务报表读取** 实验。
3. **运行筛选脚本** `python scripts/sector_screening.py`，把输出写入 `reports/`。
4. **启动 CI**：向仓库提交一次更改（例如在 `reports/` 新建 `2024-Q1-学习总结.md`），GitHub Actions 会自动生成每日回测报告。

如果需要我 **补充脚本**（比如实现 `optimize_portfolio.py`、投后监控脚本）或 **生成模板文件**（PPM、合伙协议），只需告诉我具体需求，我会立即创建并提交。祝你学习顺畅，基金设立与赛道选标一路顺风 🚀！