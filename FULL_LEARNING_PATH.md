# 投资全链路学习路径（从理论到实战）· 2026 增强版

> 由交易分析团队维护。相比初版，本次增强：新增 AI/LLM 投研章节、扩充开源项目与中文资源、补齐可运行脚本与基金实务模板（见仓库 `scripts/`、`docs/`）。

## 🎯 目标
- 掌握基金业务全流程：从设立、募集、投资、投后管理到清算退出
- 学会赛道选标：依据宏观、行业、竞争格局、商业模式进行筛选
- 实现自动化：用 Python / Quant 框架实现数据抓取、因子筛选、组合构建、风险监控

> 章节采用 “理论 → 实战 → 代码/工具 → 项目练习” 的递进方式，适合自学和团队内部培训。

## 1️⃣ 基础理论

| 章节 | 关键概念 | 推荐资源 |
|------|----------|----------|
| 1.1 金融基础 | 资产类别、风险收益、时间价值、CAPM | 《Investopedia》《金融学（第七版）》 |
| 1.2 私募/公募基金制度 | 基金设立流程、监管要求 | 《私募基金实务》证监会官方文档 |
| 1.3 行业赛道模型 | 波特五力、PESTEL、产业链价值结构 | 《波特竞争战略》《麦肯锡行业洞察》 |
| 1.4 投资决策框架 | 4C/5C、DCF、相对估值、PE/EV、竞争壁垒 | 《公司理财（第11版）》《估值》Aswath Damodaran |
| 1.5 市场微观与有效市场 | 随机游走、行为金融、套利限制 | 《漫步华尔街》《思考，快与慢》 |

### 学习建议
- 每章阅读 30‑45 分钟，随后用 10‑15 分钟把概念写成 **One‑Pager**（Markdown），放入 `reports/`。
- 完成后在笔记工具中创建对应笔记并链接到 `FULL_LEARNING_PATH.md`。

## 2️⃣ 基金设立与运营

| 步骤 | 说明 | 关键输出文件 |
|------|------|---------------|
| 2.1 设立基金公司 | 备案、备案材料、合规审计 | `docs/fund_setup_checklist.md` |
| 2.2 编写基金募集说明书（PPM） | 投资策略、风险揭示、费用结构 | `docs/PPM_template.md` |
| 2.3 合伙协议 & 法律文件 | GP/LP 权责、收益分配、退出机制 | `docs/partnership_agreement_template.md` |
| 2.4 募集 & 投资者关系 | CRM、路演 PPT、投资者问答库 | 练习产出：`presentations/roadshow.pptx`（自建） |
| 2.5 监管报送 & 报告 | 月度/季报、审计报告、税务申报 | 练习产出：`reports/quarterly_report_template.md`（自建） |

**实战练习**
1. 用 **Markdown** 完成一份 **《模拟私募基金募集说明书》**（约 5 页），提交到 `docs/`。
2. 用 **Python** 生成 **募集进度表（Excel）**（`scripts/fund_raise_tracker.py`，已提供）。

## 3️⃣ 赛道与标的筛选（系统化方法）

### 3.1 宏观‑行业‑公司三级框架
1. **宏观**：GDP、消费、政策、利率 → World Bank API、CPI、央行数据（akshare / fredapi）
2. **行业**：行业规模、成长率、进入壁垒 → Wind/同花顺行业报告（或公开协会 PDF）
3. **公司**：财务健康、竞争优势、估值 | 关键指标：ROE、毛利率、自由现金流、负债率、PE、PB、EV/EBITDA

### 3.2 常用筛选工具
| 工具 | 说明 | 链接/仓库 |
|------|------|-----------|
| **AkShare** | 国内 A 股、行业、宏观数据 | `akshare` |
| **yfinance / OpenBB** | 海外行情、财报、研报 | `ranaroussi/yfinance` / `OpenBB-finance/OpenBB` |
| **FinanceToolkit** | 财务+估值一体化 | `JerBouma/FinanceToolkit` |
| **pybroker / Lean** | 多因子与回测框架 | `edtechre/pybroker` / `QuantConnect/Lean` |
| **SQL/BigQuery** | 大数据批量筛选 | pybroker SQL 示例 |

### 3.3 示例筛选流程（Python）
```python
# 见 scripts/sector_screening.py（已提供，可直接运行，无网络时降级为示例数据）
import akshare as ak
import pandas as pd
stock_df = ak.stock_zh_a_spot()
target = stock_df[stock_df['行业'].str.contains('新能源车')]
# 计算 ROE/PE 并筛选 ROE>15% 且 PE<20 的标的
```
> 运行：`python scripts/sector_screening.py`

## 4️⃣ 投资组合构建 & 风险管理

| 步骤 | 说明 | 参考实现 |
|------|------|----------|
| 4.1 因子模型构建 | 价值、规模、动量、质量因子 | `edtechre/pybroker` 示例 |
| 4.2 资产配置优化 | 均值‑方差、风险平价、黑利特 | `pyportfolioopt` |
| 4.3 组合回测 | Backtrader、Zipline、bt、vectorbt | `scripts/optimize_portfolio.py`（已提供） |
| 4.4 风险监控 | VaR、最大回撤、行业敞口 | quantstats / ffn |
| 4.5 投后报告 | 周报、月报、投资回报分析 | 练习产出：`reports/portfolio_report_template.md`（自建） |

**示例：使用 `pyportfolioopt` 进行最小波动率组合**
```python
# 见 scripts/optimize_portfolio.py（已提供）
from pypfopt import EfficientFrontier, risk_models, expected_returns
mu = expected_returns.mean_historical_return(price_df)
S  = risk_models.sample_cov(price_df)
ef = EfficientFrontier(mu, S); ef.min_volatility()
print(ef.clean_weights())
```
> 运行：`python scripts/optimize_portfolio.py`

## 5️⃣ 投后管理 & 退出机制

| 项目 | 内容 | 推荐工具 |
|------|------|----------|
| 5.1 运营报表 | 投资进度、业绩、现金流 | pandas + openpyxl |
| 5.2 监控 KPI | 市占率、毛利率、用户增长 | PowerBI / Superset |
| 5.3 退出评估 | IPO、并购、二级市场套现 | DCF、相对估值 |
| 5.4 合规审计 | 合规审查、税务优化 | 法务模板、审计清单 |

**已提供脚本**：`scripts/exit_simulation.py` 实现了**并购/退出溢价模拟器**（输入估值、溢价比例、持有年限与期间现金流，输出 IRR、MOIC、年化收益）。运行：`python scripts/exit_simulation.py`。

## 6️⃣ 推荐学习资源（完整列表）

### 6.1 代码仓库（精选，详见 README.md 与 awesome-quant）
- `wilsonfreitas/awesome-quant`（总索引）
- `OpenBB-finance/OpenBB`（开源投研终端）
- `stefan-jansen/machine-learning-for-trading`
- `firmai/financial-machine-learning`
- `edtechre/pybroker`
- `QuantConnect/Lean`
- `pmorissette/bt`
- `ranaroussi/yfinance` / `quantstats`
- `JerBouma/FinanceToolkit`
- `matplotlib/mplfinance`
- `CatsJuice/quantitative-investment-learning`（中文）

### 6.2 经典书籍（扩充）
| 书名 | 作者 | 适用阶段 |
|------|------|----------|
| 《聪明的投资者》 | Benjamin Graham | 价值入门 |
| 《安全边际》 | Seth Klarman | 价值深化 |
| 《投资中最简单的事》 | 邱国鹭 | 价值/A股 |
| 《价值》 | 张磊 | 长期主义 |
| 《手把手教你读财报》 | 唐朝 | 财报实战 |
| 《投资学》 | 滋维·博迪 | 理论 |
| 《公司理财（第11版）》 | Ross | 估值/资本结构 |
| 《估值》 | Aswath Damodaran | 估值 |
| 《Algorithmic Trading》 | Ernest Chan | 实战 |
| 《主动投资组合管理》 | Grinold & Kahn | 量化组合 |
| 《投资最重要的事》 | Howard Marks | 风险周期 |
| 《思考，快与慢》 | Kahneman | 决策心理 |
| 《黑天鹅》《反脆弱》 | Taleb | 尾部风险 |

### 6.3 在线课程
| 平台 | 课程 | 链接 |
|------|------|------|
| Coursera | Investment Management (Geneva) | https://www.coursera.org/learn/investment-management |
| Coursera | Machine Learning for Trading 专项 (NYIF & Google Cloud) | https://www.coursera.org/specializations/machine-learning-trading |
| CFA Institute | Investment Foundations（免费） | https://www.cfainstitute.org/programs/investment-foundations-certificate |
| Class Central | 最佳投资课程榜单 | https://www.classcentral.com/report/best-investment-courses/ |

### 6.4 博客 / 资讯
| 名称 | 方向 | 链接 |
|------|------|------|
| QuantStart | 量化教学 | https://www.quantstart.com |
| Alpha Architect | 因子研究 | https://alphaarchitect.com |
| Flirting with Models | 因子/配置 | https://www.thinknewfound.com |
| 集思录 | 中文固收/套利 | https://www.jisilu.cn |
| Seeking Alpha | 深度分析 | https://seekingalpha.com |
| 机器之心 | AI 前沿 | https://www.jiqizhixin.com |

### 6.5 播客 & 简报
- 播客：We Study Billionaires、Chat With Traders、Invest Like the Best、Macro Voices、The Rational Reminder
- 简报：Finimize、Morning Brew Markets、Epsilon Theory

### 6.6 全球顶级投资专家与公开资源
| 专家 | 领域 | 关键资源 |
|------|------|----------|
| Warren Buffett | 价值投资 | 股东信 https://www.berkshirehathaway.com/letters/letters.html |
| Charlie Munger | 多元思维 | 《穷查理宝典》在线版 https://www.stripe.press/poor-charlies-almanack |
| Ray Dalio | 宏观 | 《原则》https://www.principles.com/ |
| Howard Marks | 债券/周期 | 备忘录 https://www.oaktreecapital.com/insights/memos |
| Peter Lynch | 成长 | https://www.youtube.com/watch?v=UVD1o8B6Ftc |
| Joel Greenblatt | 价值+质量 | Magic Formula https://www.gurufocus.com/ |
| David Swensen | 资产配置 | Yale Endowment |
| Catherine Wood (ARK) | 创新 | https://ark-invest.com/research/ |
| Jack Bogle | 指数 | https://investor.vanguard.com/investor-resources-education |

### 6.7 🤖 AI / LLM 投研新风（2026 新增）
- 用法与工程要点见 `docs/ai_finance_playbook.md`
- 金融 LLM 评测：https://www.azilen.com/learning/best-llms-for-financial-analysis/
- AI 投研工具：https://www.alpha-sense.com/resources/research-articles/ai-tools-for-financial-research/
- FinBERT 情绪模型：https://github.com/ProsusAI/finbert

## 7️⃣ 项目练习路线（12 周）

| 周次 | 主题 | 任务 |
|------|------|------|
| 1‑2 | 金融基础 & 基金设立 | 读《私募基金实务》1‑3章，写《基金设立检查清单》 |
| 3‑4 | 行业赛道模型 | 用 AkShare 抓新能源车数据，写行业报告 |
| 5‑6 | 标的筛选实战 | 运行 `scripts/sector_screening.py`，筛 5 只 A 股 |
| 7‑8 | 组合构建与回测 | 用 `pyportfolioopt` 生成最小波动组合；回测 1 年 |
| 9‑10| 投后监控 | 用 quantstats 监控最大回撤、行业敞口 |
| 11‑12| 项目汇总 | 统一 Notebook/脚本/报告，PR 提交，CI 自动生成报告 |

## 8️⃣ 自动化 & CI（可选）
```yaml
# .github/workflows/backtest.yml（已提供）
# 每天 01:00 UTC 自动跑筛选+组合优化+募集跟踪，产物作为 artifact
```

## 9️⃣ AI 投研实战（新增章节）
### 9.1 四大场景
| 场景 | 做法 | 工具 |
|------|------|------|
| 财报/公告摘要 | PDF → LLM 抽取指标与风险 | GPT-4.5 / Claude / Gemini |
| 研报问答（RAG） | 研报库 → 向量索引 → 问答 | LlamaIndex / LangChain |
| 新闻情绪监控 | 新闻流 → 情绪分 → 预警 | FinBERT / LLM |
| 策略代码生成 | 自然语言 → 回测脚本 | Copilot / Cursor / Claude |

### 9.2 推荐技术栈
- 数据：`akshare` / `yfinance` / `OpenBB`
- RAG：`LlamaIndex` / `LangChain` + `Chroma` / `FAISS`
- 情绪：`FinBERT`
- 生成：`Copilot` / `Claude`

### 9.3 入门练习
1. OpenBB 拉一只股票财务 → LLM 写「一句话投资要点」
2. 10 份年报做 RAG → 问「哪家公司毛利率最高」
3. FinBERT 对一周新闻打情绪分 → 画趋势图

## 📂 项目结构（更新后）
```
invest-study/
├─ README.md / FULL_LEARNING_PATH.md / TOP_RESOURCES_2026.md / requirements.txt
├─ scripts/   (sector_screening / optimize_portfolio / fund_raise_tracker)
├─ docs/      (fund_setup_checklist / PPM_template / partnership_agreement / ai_finance_playbook)
├─ .github/workflows/backtest.yml
└─ notebooks/ data/ reports/   # 学习产物目录
```

## ✅ 接下来可以做的事
1. 克隆仓库，安装依赖：`pip install -r requirements.txt`
2. 运行 `python scripts/sector_screening.py` 验证筛选流程
3. 阅读 `docs/ai_finance_playbook.md` 了解 AI 投研落地
4. 提交练习 Notebook / 报告，触发 CI 自动回测

⚠️ 本仓库为学习/培训用途，所有内容不构成投资建议。
