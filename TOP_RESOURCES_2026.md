# 🌟 全网精选投研学习资源（2026 版）

> 由交易分析团队基于公开信息筛选，覆盖「体系 → 量化代码 → 数据 → 大师 → 资讯 → AI 新风」。
> 链接均来自公开可访问来源；排名为大致参考，请以仓库实时状态为准。

## 一、🚀 必收藏的开源项目（GitHub）
| 项目 | 一句话 | 链接 |
|------|--------|------|
| awesome-quant | 量化领域「总索引」，库/数据/书单一网打尽 | https://github.com/wilsonfreitas/awesome-quant |
| OpenBB Terminal | 开源投研终端，数据+分析一体 | https://github.com/OpenBB-finance/OpenBB |
| Machine Learning for Trading | 《算法交易机器学习》官方代码(Jupyter) | https://github.com/stefan-jansen/machine-learning-for-trading |
| financial-machine-learning | 金融 ML 工具与案例集 | https://github.com/firmai/financial-machine-learning |
| pybroker | 轻量 ML 算法交易框架 | https://github.com/edtechre/pybroker |
| QuantConnect/Lean | 机构级回测/交易引擎 | https://github.com/QuantConnect/Lean |
| bt | 灵活组合回测框架(Python) | https://github.com/pmorissette/bt |
| yfinance | Yahoo 财经行情/财报抓取 | https://github.com/ranaroussi/yfinance |
| quantstats | 组合绩效与风险分析 | https://github.com/ranaroussi/quantstats |
| FinanceToolkit | 财务数据+估值一体化工具 | https://github.com/JerBouma/FinanceToolkit |
| mplfinance | K线/金融图表绘制 | https://github.com/matplotlib/mplfinance |
| Qlib | 微软 AI 量化平台：因子挖掘→模型→回测，支持 A 股 | https://github.com/microsoft/qlib |
| AKQuant | AKShare 团队出品的回测/交易框架：Rust 内核 + Python 接口，内置滚动训练(Walk-forward) | https://github.com/akfamily/akquant |
| 看海量化 OSkhQuant | A 股量化回测 Windows 桌面软件（开源版）：免开户、免 QMT，BaoStock/Tushare 数据存本地 DuckDB，Python 写策略一键出回测报告；CC BY-NC 4.0（非商用），商业版另售 | https://github.com/khscience/OSkhQuant |

## 二、📚 经典书单（入门→进阶）
**价值/基本面**
- 《聪明的投资者》Benjamin Graham
- 《安全边际》Seth Klarman
- 《投资中最简单的事》邱国鹭
- 《价值》张磊
- 《手把手教你读财报》唐朝

**体系/工具**
- 《投资学》滋维·博迪
- 《公司理财》Ross（第11版）
- 《估值》Aswath Damodaran
- 《Algorithmic Trading》Ernest Chan
- 《主动投资组合管理》Grinold & Kahn

**思维/风险**
- 《穷查理宝典》Charlie Munger
- 《原则》《大债务危机》Ray Dalio
- 《投资最重要的事》Howard Marks
- 《随机漫步的傻瓜》《黑天鹅》《反脆弱》Nassim Taleb
- 《思考，快与慢》Daniel Kahneman
- 《漫步华尔街》Burton Malkiel

## 三、🎓 优质课程（多数免费/可旁听）
| 课程 | 平台 | 链接 |
|------|------|------|
| Investment Management | Coursera (Geneva) | https://www.coursera.org/learn/investment-management |
| Machine Learning for Trading 专项 | Coursera (NYIF & Google Cloud) | https://www.coursera.org/specializations/machine-learning-trading |
| Investment Foundations | CFA Institute（免费） | https://www.cfainstitute.org/programs/investment-foundations-certificate |
| Financial Markets（Robert Shiller） | Coursera（耶鲁，可免费旁听） | https://www.coursera.org/learn/financial-markets-global |
| 15.401 Finance Theory I | MIT OpenCourseWare（免费） | https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/ |
| 18.S096 金融数学专题 | MIT OpenCourseWare（免费） | https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/ |
| QuantEcon 讲义 | QuantEcon（免费，Python） | https://quantecon.org/lectures/ |
| 最佳投资课程榜单 | Class Central | https://www.classcentral.com/report/best-investment-courses/ |

## 四、📊 数据来源（免费/低成本）
- **A股**：akshare、baostock、tushare(需token)
- **全球**：yfinance、pandas-datareader、fredapi(宏观)、Alpha Vantage、Nasdaq Data Link(原Quandl)
- **另类**：finagg(聚合多免费API)
- **给 AI 编程助手用**：a-stock-data（A 股全栈数据 Skill 文件，聚合 34 个免费数据源：行情、研报、资金面、公告、宏观利率、期货、可转债等）：https://github.com/simonlin1212/a-stock-data
- **本地 A 股数据湖**：CNEquity（免注册、免 token，把行情/财报/资金面/公告/宏观等 55 个数据集增量采集为本地 Parquet，带质量审计与 PIT 语义，可经 MCP 接给 AI 助手；数据来自东财、新浪、BaoStock 等公开源，覆盖以其数据集目录为准）：https://github.com/rootSunc/CNEquity
- **因子研究**：Kenneth French Data Library（Fama-French 因子与组合收益的权威免费数据，做因子回测的基准）：https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
- **研报/公告**：交易所官网、巨潮资讯（证监会指定信息披露网站）：http://www.cninfo.com.cn/ 、公司 IR 页
- **免费研究专著**：CFA Institute Research Foundation（大量投资研究专著与文献综述可免费下载）：https://rpc.cfainstitute.org/research-foundation

## 五、🧠 大师公开资源
- Buffett 股东信：https://www.berkshirehathaway.com/letters/letters.html
- Munger《穷查理宝典》在线版：https://www.stripe.press/poor-charlies-almanack
- Buffett/Munger 股东大会视频档案：https://buffett.cnbc.com/
- Dalio《原则》：https://www.principles.com/
- Marks 备忘录：https://www.oaktreecapital.com/insights/memos
- Greenblatt Magic Formula：https://www.gurufocus.com/
- ARK 研究：https://ark-invest.com/research/
- Bogle/Vanguard：https://investor.vanguard.com/investor-resources-education 与 https://boglecenter.net/

## 六、📰 博客 / 资讯 / 播客 / 简报
- QuantStart（量化教学）：https://www.quantstart.com
- Alpha Architect（因子研究）：https://alphaarchitect.com
- Flirting with Models（Newfound Research）：https://www.thinknewfound.com
- 集思录（中文固收/套利）：https://www.jisilu.cn
- Seeking Alpha：https://seekingalpha.com
- 机器之心（AI前沿）：https://www.jiqizhixin.com
- 播客：We Study Billionaires、Chat With Traders、Invest Like the Best、Macro Voices、The Rational Reminder
- 简报：Finimize、Morning Brew Markets、Epsilon Theory

## 七、🤖 AI / LLM 投研新风（2026）
- 金融分析 LLM 评测：https://www.azilen.com/learning/best-llms-for-financial-analysis/
- AI 投研工具指南：https://www.alpha-sense.com/resources/research-articles/ai-tools-for-financial-research/
- FinBERT 情绪模型：https://github.com/ProsusAI/finbert （2022 年后未更新，适合作为情绪分类基准）
- Vibe-Trading 个人交易智能体工作台（支持 A 股/港股/美股/加密，含回测与 MCP）：https://github.com/HKUDS/Vibe-Trading
- FinRobot 金融分析/研报生成智能体平台：https://github.com/AI4Finance-Foundation/FinRobot
- TradingAgents 多智能体交易研究框架：https://github.com/TauricResearch/TradingAgents
- TradingAgents-astock（TradingAgents 的 A 股特化 fork：A 股数据源、T+1/涨跌停规则，新增政策/游资/解禁分析师，面向研究与教学）：https://github.com/simonlin1212/TradingAgents-astock
- daily_stock_analysis LLM 自选股每日分析与推送（A股/港股/美股等，GitHub Actions 定时运行，含回测；README 含赞助商推广链接）：https://github.com/ZhuLinsen/daily_stock_analysis
- ai-hedge-fund 多智能体投资分析教学项目：https://github.com/virattt/ai-hedge-fund
- FinGPT 开源金融大模型：https://github.com/AI4Finance-Foundation/FinGPT
- RD-Agent 自动化因子/模型研发（配合 Qlib）：https://github.com/microsoft/RD-Agent
- Alpaca MCP Server（券商 Alpaca 官方 MCP 服务器：让 AI 助手查行情、管持仓、下单，覆盖美股/ETF/期权/加密；默认连模拟盘，改配置才会实盘）：https://github.com/alpacahq/alpaca-mcp-server
- MaverickMCP（本地运行的股票分析 MCP 服务器：基于 yfinance，核心工具免 API Key，含技术指标、选股、持仓记录和可选 Python 回测；不下单，定位教学用途）：https://github.com/wshobson/maverick-mcp
- 用法见 `docs/ai_finance_playbook.md`

## 八、📄 论文与研究
- SSRN：https://www.ssrn.com
- arXiv q-fin：https://arxiv.org/list/q-fin/recent
- NBER：https://www.nber.org

---
⚠️ 本清单为学习用途整理，不构成投资建议。链接可能随时间失效，欢迎 PR 补充。
