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
- **OpenBB + LLM**：开源投研终端拉数据，LLM 做解读
- **FinBERT**（ProsusAI/finbert）：金融情绪分类基准模型（2022 年后未更新，新项目可直接用 LLM 做情绪分类，用 FinBERT 做对照）
- **AlphaSense / 类似 AI 搜索**：替代关键词检索，语义找资料

## 3. 2025–2026 新趋势：智能体与 MCP

投研 AI 正从“问一句答一句”变成“智能体自己查数据、跑分析、写报告”。值得研究的开源项目（均为研究/教学用途，**不能直接用于实盘**）：

| 项目 | 做什么 | 学习重点 |
|------|--------|----------|
| [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 模拟交易公司的多智能体框架：基本面/情绪/技术分析师 + 多空辩论 + 风控 | 多智能体分工与辩论机制 |
| [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | 多个“投资大师风格”智能体协作给出投资观点 | 把投资哲学写成智能体提示词 |
| [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) | 开源金融大模型与微调方案 | 金融领域微调、情绪分析基准 |
| [RD-Agent](https://github.com/microsoft/RD-Agent) + [Qlib](https://github.com/microsoft/qlib) | 智能体自动提出因子假设 → 写代码 → 回测 → 迭代 | 自动化因子研发闭环 |

**MCP（Model Context Protocol）**：把行情、财报、自己的研究笔记封装成 MCP 服务器，Claude / ChatGPT 等助手就能直接调用。OpenBB 已把自己定位为“面向分析师、量化和 AI 智能体的开放数据平台”，是现成的数据入口。

## 4. 工程要点
- 数据：用 `akshare`/`yfinance`/`OpenBB` 拉取，存入 parquet/SQL
- RAG：文档切块 → embedding → 向量库（Chroma/FAISS）
- 评估：让 LLM 输出带引用的答案，人工抽检
- 监控：记录每次分析的输入/输出，防止幻觉

## 5. 风险提示
- LLM 会编造数字（幻觉）→ 关键数据必须回查源文件
- 不要直接把 LLM 输出当交易信号，需人工 + 回测验证
- 注意合规：内幕信息、数据安全、客户隐私
- 智能体框架的回测收益普遍存在前视偏差和过拟合，论文/README 里的收益率不要当真

## 6. 入门练习
1. 用 OpenBB 拉一只股票财务，让 LLM 写一段「一句话投资要点」
2. 把 10 份年报 PDF 做 RAG，问「哪家公司毛利率最高」
3. 用 FinBERT 和 LLM 分别对一周财经新闻打情绪分，对比两者差异并画趋势图
4. 本地跑通 TradingAgents 或 ai-hedge-fund，读懂一次完整决策链路里每个智能体的输入输出
