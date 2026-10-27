# 🌟 全网精选投研学习资源（2026 版）

> 由交易分析团队基于公开信息筛选，覆盖「体系 → 量化代码 → 数据 → 大师 → 资讯 → AI 新风」。
> 链接均来自公开可访问来源；排名为大致参考，请以仓库实时状态为准。
> 先读 [投资证据与研究纪律](EVIDENCE_2026.md)：主动与被动基金的长期对比、投资者的“买卖时点损失”、因子复现、回测过拟合和 AI 投研评测，都附原文链接。

## 一、🚀 必收藏的开源项目（GitHub）
| 项目 | 一句话 | 链接 |
|------|--------|------|
| awesome-quant | 量化领域「总索引」，库/数据/书单一网打尽 | https://github.com/wilsonfreitas/awesome-quant |
| OpenBB（Open Data Platform） | 开源金融数据平台：一次接入数据源，同时供 Python、Excel、MCP（AI 智能体）和 REST API 使用；2026-09 发布 5.0 | https://github.com/OpenBB-finance/OpenBB |
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
| skfolio | 基于 scikit-learn 接口的组合优化与风险管理库：可以像机器学习模型一样做交叉验证，内置滚动（Walk Forward）和组合清洗交叉验证（CPCV），适合检验配置方案会不会过拟合（BSD-3） | https://github.com/skfolio/skfolio |
| Riskfolio-Lib | 组合优化库：均值-风险框架下 26 种凸风险度量（CVaR、回撤类等）、风险平价、层次聚类配置（BSD-3） | https://github.com/dcajasn/Riskfolio-Lib |
| vectorbt | 向量化回测：几行代码就能比较成千上万个参数组合。试得越多越要用 DSR 打折（见 `notebooks/06_backtest_overfitting.ipynb`）；这是开源社区版，另有功能更多的 PRO 版 | https://github.com/polakowo/vectorbt |
| NautilusTrader | Rust 内核的事件驱动交易引擎：研究、确定性回测和实盘用同一套架构，Python 写策略（LGPL-3.0） | https://github.com/nautechsystems/nautilus_trader |
| arch | 金融计量：GARCH 类波动率模型，以及检验“挑出来的最好策略是不是运气”的多重比较检验（SPA、StepM、MCS） | https://github.com/bashtage/arch |
| edgartools | 把美国 SEC EDGAR 的 10-K、8-K、XBRL 财报、内部人交易、13F 持仓等文件变成结构化 Python 对象；免费，无需 API Key（需按 SEC 要求填写联系邮箱），附 MCP 服务器（MIT） | https://github.com/dgunning/edgartools |
| AKQuant | AKShare 团队出品的回测/交易框架：Rust 内核 + Python 接口，内置滚动训练(Walk-forward) | https://github.com/akfamily/akquant |
| 看海量化 OSkhQuant | A 股量化回测 Windows 桌面软件（开源版）：免开户、免 QMT，BaoStock/Tushare 数据存本地 DuckDB，Python 写策略一键出回测报告；CC BY-NC 4.0（非商用），商业版另售 | https://github.com/khscience/OSkhQuant |
| TSP 量化工作台 tick-stock-panel | A 股自托管量化工作台（个人开源，MIT）：策略 / 因子 / 回测（含 T+1、费用、滑点）/ 盘中异动监控一体，Docker 单容器、数据存本地 Parquet，附 Open API 与 MCP；数据源插件化（已接 TickFlow、同花顺 fuyao、通达信 TdxQuant 等）；作者声明不做 AI 荐股、仅供学习研究，README 含赞助商与推荐码链接 | https://github.com/shy3130/tick-stock-panel |

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
- Greenblatt Magic Formula（神奇公式）官网：https://www.magicformulainvesting.com/
- ARK 研究：https://ark-invest.com/research/
- Bogle/Vanguard：https://investor.vanguard.com/investor-resources-education 与 https://boglecenter.net/

## 六、📰 博客 / 资讯 / 播客 / 简报
- QuantStart（量化教学；2026-10 起官网返回 502 无法访问，可读网络存档 https://web.archive.org/web/2026/https://www.quantstart.com/ ）：https://www.quantstart.com
- Alpha Architect（因子研究）：https://alphaarchitect.com
- Flirting with Models（Newfound Research）：https://www.thinknewfound.com
- 集思录（中文固收/套利）：https://www.jisilu.cn
- Seeking Alpha：https://seekingalpha.com
- 机器之心（AI前沿）：https://www.jiqizhixin.com
- 播客：We Study Billionaires、Chat With Traders、Invest Like the Best、Macro Voices、The Rational Reminder
- 简报：Finimize、Morning Brew Markets、Epsilon Theory

## 七、🤖 AI / LLM 投研新风（2026）
- 先看评测再选工具（详见 [投资证据与研究纪律](EVIDENCE_2026.md) 第三节）：
  - Vals AI Finance Agent 基准（537 道初级分析师任务，持续更新各家模型的准确率；2026-06 排名第一的模型为 64.37%）：https://www.vals.ai/benchmarks/finance_agent
  - FinanceBench（基于上市公司公开文件的问答评测，论文与数据）：https://arxiv.org/abs/2311.11944
  - 用大模型做历史回测的前视偏差：https://arxiv.org/abs/2309.17322 、按时间截断训练的 ChronoBERT / ChronoGPT：https://arxiv.org/abs/2502.21206
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

## 九、🛡️ 风险管理与衍生品

| 资源 | 说明 | 链接 |
|------|------|------|
| GARP FRM | 金融风险管理师（FRM）官方页面：考试结构、学习大纲、报名与备考资源 | https://www.garp.org/frm |
| CME Group Institute：All About Options | 芝商所免费期权系列课程，配模拟交易账户 | https://www.cmegroup.com/education/courses/curriculum-all-about-options.html |
| Futures Fundamentals | CME、FIA、NFA 等行业机构联合提供的免费期货与衍生品入门教育 | https://www.futuresfundamentals.org/ |
| MIT 18.S096 金融数学专题 | 随机过程、Black-Scholes 推导等量化基础（见第三节课程） | https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/ |
| 本仓库练习 | `notebooks/04_options_pricing.ipynb`：Black-Scholes、希腊字母、看涨-看跌平价、蒙特卡洛定价 | — |

## 十、🏛️ A 股市场制度（官方原文）

制度细节会修订，学习和实操都以交易所和证监会的现行原文为准。

| 文件 / 入口 | 说明 | 链接 |
|------|------|------|
| 《上海证券交易所交易规则（2026年修订）》 | 上证发〔2026〕41 号，2026-07-06 起施行。据上交所公告，主要变化包括：盘后固定价格交易扩展至全部 A 股和 ETF，基金收盘阶段改为收盘集合竞价，主板风险警示股票涨跌幅限制由 5% 调整为 10% | https://www.sse.com.cn/lawandrules/sselawsrules2025/stocks/exchange/c/c_20260424_10816482.shtml |
| 深圳证券交易所业务规则 | 深交所同步修订交易规则（2026-07-06 起施行），据报道引入了做市商制度；规则原文见官网“业务规则”栏目 | https://www.szse.cn/ |
| 北京证券交易所 | 北交所同步修订交易规则，规则原文见官网 | https://www.bse.cn/ |
| 《上市公司信息披露管理办法》（证监会令第 226 号） | 2025-07-01 起施行，原第 182 号令同时废止；强化风险揭示，确立暂缓与豁免披露制度 | https://www.csrc.gov.cn/csrc/c101953/c7547359/content.shtml |
| 国家法律法规数据库 | 检索《证券法》《公司法》等法律的现行有效原文 | https://flk.npc.gov.cn/ |
| 沪深北交易所《程序化交易管理实施细则》 | 2025-07-07 起实施：程序化交易报告制度；单账户每秒申报、撤单合计 300 笔以上或全日 20000 笔以上认定为高频交易；四类异常交易重点监控。用脚本或 AI 智能体自动下单前必读 | https://www.sse.com.cn/aboutus/mediacenter/hotandd/c/c_20250403_10776805.shtml |
| 《公开募集证券投资基金销售费用管理规定》 | 2026-01-01 起施行，费率改革最后一步：调降认申购费和销售服务费，赎回费全部计入基金财产，持有超过一年的份额（货币基金除外）不再收销售服务费 | https://www.csrc.gov.cn/csrc/c100028/c7606047/content.shtml |
| 《公开募集证券投资基金业绩比较基准指引》 | 2026-03-01 起施行：基准与投资风格匹配、一经选定不得随意变更，用来识别“风格漂移” | https://www.csrc.gov.cn/csrc/c100028/c7610827/content.shtml |

## 十一、🏢 企业投资（企业视角）

| 资源 | 说明 | 链接 |
|------|------|------|
| 本仓库企业投资模块 | 资本配置、投决会、CVC 与产业基金、并购整合、跨境合规，附模板与法规速查 | ./corporate-investment |
| Damodaran Corporate Finance | 企业投资、融资、分红决策的完整公开课 | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/corpfin.html |
| Damodaran 当年数据 | 行业 β、资本成本、股权风险溢价、国家风险溢价 | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html |
| Introduction to Corporate Finance（沃顿） | 折现现金流与项目评估入门 | https://www.coursera.org/learn/wharton-finance |
| Bain 2026 全球并购报告 | 并购趋势、整合与协同 | https://www.bain.com/about/media-center/press-releases/2026/global-ma-poised-to-sustain-momentum-in-2026-after-great-rebound-finds-bain--company/ |

## 十二、🔬 投资证据与研究方法

逐条解读见 [投资证据与研究纪律](EVIDENCE_2026.md)。

| 资源 | 说明 | 链接 |
|------|------|------|
| Morningstar Active/Passive Barometer | 半年度报告：主动基金与同类被动基金的成功率（清盘基金算作失败），按期限、费率分档 | https://www.morningstar.com/business/insights/research/active-passive-barometer |
| Morningstar Mind the Gap | 年度报告：投资者实际拿到的回报比基金本身少多少，以及差距来自哪里 | https://www.morningstar.com/business/insights/research/mind-the-gap |
| UBS 全球投资回报年鉴（公开摘要版） | Dimson、Marsh、Staunton 整理的 1900 年以来 35 个市场的股票、债券、短期国债、汇率和因子长期回报（2026 版新增黄金） | https://www.ubs.com/content/dam/assets/wm/static/cio/documents/giry2026-summary-public.pdf |
| 摩根大通长期资本市场假设（LTCMA） | 每年 10 月发布未来 10–15 年各类资产的预期回报与风险，做长期配置规划时的参照 | https://am.jpmorgan.com/us/en/asset-management/institutional/insights/portfolio-insights/ltcma/ |
| JKP 全球因子数据 | Jensen、Kelly、Pedersen 的 153 个因子、93 个国家，免费下载 | https://jkpfactors.com/ |
| Open Source Asset Pricing | 文献中横截面收益预测信号的开源复现代码与数据 | https://www.openassetpricing.com/ |
| AQR 数据集 | AQR 公开并定期更新的因子数据：质量（QMJ）、低贝塔（BAB）、价值与动量等，覆盖美国和 23 个国际股票市场 | https://www.aqr.com/Insights/Datasets |
| 《The Deflated Sharpe Ratio》 | Bailey、López de Prado：给多次试验后挑出的回测打折；本仓库 `scripts/backtest_stats.py` 复现了论文数值 | https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf |
| 《…and the Cross-Section of Expected Returns》 | Harvey、Liu、Zhu：新因子的 t 值应超过 3.0 | https://www.nber.org/papers/w20592 |
| Bogleheads Wiki | 指数化投资与资产配置的社区百科：低成本、分散、长期持有的完整方法 | https://www.bogleheads.org/wiki/Main_Page |

---
⚠️ 本清单为学习用途整理，不构成投资建议。链接可能随时间失效，欢迎 PR 补充。
