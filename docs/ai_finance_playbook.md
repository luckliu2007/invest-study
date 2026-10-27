# AI / LLM 投研实战手册（2026 新风）

把大模型接入投研流程，提升「信息处理 → 决策支持」的效率。

## 1. 四大落地场景

> 模型型号迭代很快（几个月一代），下表只写厂商，使用时选各家当前旗舰或推理模型即可。

| 场景 | 做法 | 工具 |
|------|------|------|
| 财报/公告摘要 | 上传 PDF，让 LLM 抽取关键指标与风险 | Claude / ChatGPT / Gemini / DeepSeek / 通义千问 |
| 研报问答（RAG） | 把研报库建向量索引，问答检索 | LlamaIndex / LangChain + 向量库 |
| 新闻情绪监控 | 实时新闻流 → 情绪打分 → 预警 | FinBERT / LLM 分类 |
| 策略代码生成 | 用自然语言生成、调试回测脚本 | Claude Code / Codex / Cursor / Copilot 等 AI 编程智能体 |

## 2. 推荐组合
- **OpenBB + LLM**：用 OpenBB 开放数据平台（2026-09 发布 5.0）拉数据，LLM 做解读
- **FinBERT**（ProsusAI/finbert）：金融情绪分类基准模型（2022 年后未更新，新项目可直接用 LLM 做情绪分类，用 FinBERT 做对照）
- **AlphaSense / 类似 AI 搜索**：替代关键词检索，语义找资料

## 3. 2025–2026 新趋势：智能体与 MCP

投研 AI 正从“问一句答一句”变成“智能体自己查数据、跑分析、写报告”。值得研究的开源项目（均为研究/教学用途，**不能直接用于实盘**）：

| 项目 | 做什么 | 学习重点 |
|------|--------|----------|
| [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 港大 HKUDS 出品的个人交易智能体工作台（2026 年开源，MIT）：多智能体研究、回测引擎、MCP 接口，覆盖 A 股、港股、美股、加密货币、期权 | 用自然语言驱动“研究→回测→复盘”全流程；⚠️ 官方声明从未发行任何代币，冒充项目方的币一律是骗局 |
| [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 模拟交易公司的多智能体框架：基本面/情绪/技术分析师 + 多空辩论 + 风控 | 多智能体分工与辩论机制 |
| [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | 多个“投资大师风格”智能体协作给出投资观点 | 把投资哲学写成智能体提示词 |
| [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) | 面向金融分析的智能体平台，侧重自动生成股票研究报告 | 用智能体拆解“读财报→估值→写研报” |
| [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) | 开源金融大模型与微调方案 | 金融领域微调、情绪分析基准 |
| [RD-Agent](https://github.com/microsoft/RD-Agent) + [Qlib](https://github.com/microsoft/qlib) | 智能体自动提出因子假设 → 写代码 → 回测 → 迭代 | 自动化因子研发闭环 |

**MCP（Model Context Protocol）**：把行情、财报、自己的研究笔记封装成 MCP 服务器，Claude / ChatGPT 等助手就能直接调用。OpenBB 已把自己定位为“面向分析师、量化和 AI 智能体的开放数据平台”，是现成的数据入口。自建 MCP 服务器请按 [2026-07-28 版规范](https://modelcontextprotocol.io/specification/2026-07-28/changelog)开发。

想先体验现成的投研 MCP 服务器，可以从这两个开始：

| 项目 | 做什么 | 学习重点 |
|------|--------|----------|
| [MaverickMCP](https://github.com/wshobson/maverick-mcp) | 本地运行，基于 yfinance 拉美股数据，核心工具免 API Key；行情、技术指标、选股、持仓与交易日志，可选回测和带引用的公司研究 | 只读分析型 MCP 的工具设计；不下单，适合入门 |
| [Alpaca MCP Server](https://github.com/alpacahq/alpaca-mcp-server) | 美国券商 Alpaca 官方出品，用自然语言查行情、看持仓、下单（股票/ETF/期权/加密） | 交易型 MCP 的权限与风控；默认连免费模拟盘（`ALPACA_PAPER_TRADE=true`），**学习时不要切到实盘** |

## 4. 工程要点
- 数据：用 `akshare`/`yfinance`/`OpenBB` 拉取，存入 parquet/SQL
- RAG：文档切块 → embedding → 向量库（Chroma/FAISS）
- 评估：让 LLM 输出带引用的答案，人工抽检。正式使用前，先用自己准备的 20–50 道带标准答案的题（例如“某公司 2025 年经营现金流是多少”）测一遍。公开评测可以参考 [Vals AI Finance Agent 基准](https://www.vals.ai/benchmarks/finance_agent)：537 道初级分析师任务，2026-06 排名第一的模型准确率为 64.37%，也就是还有三分之一以上答错（更多证据见 [投资证据与研究纪律](../EVIDENCE_2026.md) 第三节）
- 监控：记录每次分析的输入/输出，防止幻觉

## 5. 风险提示
- LLM 会编造数字（幻觉）→ 关键数据必须回查源文件
- 不要直接把 LLM 输出当交易信号，需人工 + 回测验证
- 注意合规：内幕信息、数据安全、客户隐私
- 智能体框架的回测收益普遍存在前视偏差和过拟合，论文/README 里的收益率不要当真；先问一共试了多少个版本，再用 [`scripts/backtest_stats.py`](../scripts/backtest_stats.py) 的折减夏普比率（DSR）打折
- **大模型自带的前视偏差**：通用大模型的训练数据里包含回测期之后才发生的事，用它给历史新闻、财报打分再回测，结果可能偏乐观；它还可能被自己对公司的已有印象干扰（[Glasserman & Lin](https://arxiv.org/abs/2309.17322)）。做法：把公司名匿名化做对照，只把模型训练截止日之后的数据当作样本外，必要时用按时间截断训练的模型（如 [ChronoGPT](https://arxiv.org/abs/2502.21206)）对照
- **A 股自动下单要守程序化交易规则**：用脚本或智能体自动下单前，先读沪深北交易所《程序化交易管理实施细则》（2025-07-07 起实施）。程序化交易实行报告制度，高频交易认定标准和四类异常交易都有明确规定（见 [`TOP_RESOURCES_2026.md`](../TOP_RESOURCES_2026.md) 第十节）
- **让智能体真正下单之前先定授权等级**：默认只给建议（A0）或每笔人工确认（A1）；放开小额自动交易（A2）前，必须有单笔与每日限额、成本上限、一键停用和完整操作记录。用 [智能体授权与管控清单](https://github.com/luckliu2007/ai-ml-data-roadmap/blob/main/templates/agent-governance-checklist.md) 逐项核对，并对照 [OWASP 智能体应用十大风险（2026）](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)

## 6. 入门练习
1. 用 OpenBB 拉一只股票财务，让 LLM 写一段「一句话投资要点」
2. 把 10 份年报 PDF 做 RAG，问「哪家公司毛利率最高」
3. 用 FinBERT 和 LLM 分别对一周财经新闻打情绪分，对比两者差异并画趋势图
4. 本地跑通 TradingAgents 或 ai-hedge-fund，读懂一次完整决策链路里每个智能体的输入输出
5. 用 Vibe-Trading 对一只 A 股做一次“研究 → 回测 → 复盘”，再用本仓库 `scripts/` 的结果交叉验证
6. 让同一个模型给 50 条历史新闻打两次情绪分：一次保留公司名，一次把公司名换成“某公司”，比较两组分数与之后股价表现的关系，体会前视偏差和分心效应
