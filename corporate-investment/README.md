# 企业投资：从资本配置到退出

站在**企业**的角度做投资：资本该投向哪里、一个项目值不值得做、战略投资和产业基金怎么搭、并购怎么定价和整合、出海投资要过哪些关。本模块面向企业管理层、战略与投资部门、财务负责人。

> 法规与报告均为 2026-10-23 核对的现行版本，链接到政府或机构原文。法规会修订，**实际操作前请以官方最新文本和专业顾问意见为准**。本仓库仅供学习，不构成投资或法律建议。

## 学习顺序

| 章节 | 回答的问题 | 配套工具 |
| --- | --- | --- |
| [01 资本配置与项目评估](01-capital-allocation.md) | 钱该投向哪里？一个项目值不值得做？ | [`scripts/capital_budgeting.py`](../scripts/capital_budgeting.py)：NPV、IRR、回收期、情景与敏感性 |
| [02 投资流程、投决会与治理](02-investment-process-governance.md) | 从寻源到退出怎么管？投决会怎么开？ | [投决会报告模板](templates/ic-memo.md)、[尽调清单](templates/due-diligence-checklist.md)、[投后复盘模板](templates/post-investment-review.md) |
| [03 战略投资、CVC 与产业基金](03-cvc-and-industry-funds.md) | 少数股权、企业风险投资和产业基金怎么选、怎么管？ | 设立基金参照 [基金设立清单](../docs/fund_setup_checklist.md)、[合伙协议模板](../docs/partnership_agreement_template.md) |
| [04 并购与投后整合](04-ma-and-integration.md) | 最高能出多少价？怎么避免商誉“爆雷”？整合怎么做？ | [`notebooks/05_ma_valuation.ipynb`](../notebooks/05_ma_valuation.ipynb)、[100 天整合计划](templates/integration-100-day-plan.md) |
| [05 跨境投资与合规](05-cross-border.md) | 出海投资在国内要过哪些手续？东道国会审查什么？ | 国别指南、法规速查（见下表） |

## 企业投资的 10 条原则

1. **价值创造的标准只有一个**：投入资本回报率（ROIC）长期高于资本成本，才是在创造价值；增长本身不等于创造价值。
2. **用 NPV 做决策**，IRR 和回收期只作参考：IRR 在现金流多次变号时可能有多个解，也无法比较规模不同的项目；回收期不考虑资金的时间价值。
3. **折现率要匹配项目风险**，不能所有项目都用公司整体的 WACC。
4. **先算悲观情景**，再看基准情景；用同类项目的历史结果校准预测（参考类预测），抵消天然的乐观偏差。
5. **协同效应要打折、要分期、要扣成本**，最多让渡多少给卖方，要在报价前定好。
6. **投决会对事不对人**：分级授权、利益冲突回避、反对意见必须记录。
7. **尽调覆盖数据与网络安全、合规和人**，不只看财务报表。
8. **投后管理决定一半的结果**：投资时就写好投后的跟踪指标和触发条件。
9. **每笔投资都要事后复盘**：一到三年后对照当初的投决会报告，检验哪些判断对了、哪些错了。
10. **合规前置**：反垄断申报、上市公司重组、境外投资备案、东道国审查，都会影响交易时间表和交易结构。

## 法规与规则速查（中国）

| 事项 | 现行规定 | 原文 |
| --- | --- | --- |
| 并购是否需要反垄断申报 | 《国务院关于经营者集中申报标准的规定》（2024 年修订，国务院令第 773 号）：全部参与方全球营业额合计超过 120 亿元，或境内营业额合计超过 40 亿元，**且**至少两方境内营业额各超过 8 亿元，须事先申报 | [中国政府网](https://www.gov.cn/zhengce/content/202401/content_6928387.htm) |
| 上市公司重大资产重组 | 《上市公司重大资产重组管理办法》（2025 年修正，证监会令第 230 号）：新增分期支付、简易审核程序等 | [证监会](https://www.csrc.gov.cn/csrc/c101953/c7558586/content.shtml) · [国务院公报全文](https://www.gov.cn/gongbao/2025/issue_12166/202507/content_7032496.html) |
| 上市公司信息披露 | 《上市公司信息披露管理办法》（证监会令第 226 号，2025-07-01 施行） | [证监会](https://www.csrc.gov.cn/csrc/c101953/c7547359/content.shtml) |
| 企业合并与商誉 | 《企业会计准则第 20 号——企业合并》《企业会计准则第 8 号——资产减值》：商誉至少每年年末减值测试 | [第 20 号](https://kjs.mof.gov.cn/zt/kjzzss/kuaijizhunzeshishi/200806/t20080618_46228.htm) · [第 8 号](http://www.mof.gov.cn/zhengwuxinxi/zhengcefabu/2006zcfb/200805/t20080519_23147.htm) |
| 私募基金（产业基金、CVC 基金） | 《私募投资基金监督管理条例》（国务院令第 762 号，2023-09-01 施行） | [中国政府网](https://www.gov.cn/zhengce/zhengceku/202307/content_6890739.htm) |
| 境外投资：发改委 | 《企业境外投资管理办法》（发改委令 2017 年第 11 号） | [发改委](https://www.ndrc.gov.cn/xxgk/zcfb/fzggwl/201712/t20171226_960849.html) |
| 境外投资：商务部 | 《境外投资管理办法》（商务部令 2014 年第 3 号） | [商务部](http://www.mofcom.gov.cn/zcfb/blgg/art/2014/art_1d349047003649b7ba2cd5672c1debed.html) |
| 境外投资：外汇 | 《资本项目外汇业务指引（2024 年版）》 | [中国政府网 PDF](https://www.gov.cn/zhengce/zhengceku/202404/P020240413283163235756.pdf) |
| 国有企业（如适用） | 《中央企业投资监督管理办法》（国资委令第 34 号）、《中央企业境外投资监督管理办法》（国资委令第 35 号） | [第 34 号](https://www.gov.cn/zhengce/2022-01/12/content_5718609.htm) · [第 35 号](http://www.sasac.gov.cn/n2588035/n2588320/n2588335/c20164457/content.html) |

境外审查（美国 CFIUS、欧盟外资审查新规）见 [05 跨境投资与合规](05-cross-border.md)。

## 推荐资源

| 资源 | 用途 |
| --- | --- |
| [Damodaran：Corporate Finance 课程](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/corpfin.html) | 企业投资、融资、分红决策的完整公开课（讲义、视频、案例） |
| [Damodaran：当年数据](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html) | 每年初更新的行业 β、资本成本、股权风险溢价、国家风险溢价，估值时的常用参照 |
| [Introduction to Corporate Finance（沃顿，Coursera）](https://www.coursera.org/learn/wharton-finance) | 货币时间价值、折现现金流、项目评估入门 |
| [MIT 15.401 Finance Theory I](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/) | 估值、资本预算、风险与收益 |
| McKinsey《Valuation》（Koller 等著，读最新版） | 企业估值与价值创造的标准教材，ROIC 与增长框架的出处 |
| [Bain：2026 年全球并购报告新闻稿](https://www.bain.com/about/media-center/press-releases/2026/global-ma-poised-to-sustain-momentum-in-2026-after-great-rebound-finds-bain--company/) | 并购市场趋势、整合与协同的最新观察 |
