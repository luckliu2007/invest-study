# 贡献指南

欢迎补充资源、修正错误、改进脚本和练习 Notebook。参与前请先读 [行为准则](CODE_OF_CONDUCT.md)。

> 本仓库只用于学习和培训，所有内容不构成投资建议。

## 参与方式

| 你想做什么 | 怎么做 |
| --- | --- |
| 推荐一个资源 | 填 [推荐资源表单](https://github.com/luckliu2007/invest-study/issues/new?template=resource-suggestion.yml) |
| 报告失效链接 | 填 [失效链接表单](https://github.com/luckliu2007/invest-study/issues/new?template=broken-link.yml) |
| 指出法规条文或数字有误 | 填 [内容勘误表单](https://github.com/luckliu2007/invest-study/issues/new?template=content-error.yml)，附官方原文链接 |
| 脚本或 Notebook 报错 | 填 [报错表单](https://github.com/luckliu2007/invest-study/issues/new?template=script-bug.yml) |
| 直接修改 | Fork 后新建分支，改完发 Pull Request，按 PR 模板自查 |

## 收录标准

- 与投资研究、量化、AI 投研、风险与衍生品、A 股制度或企业投资直接相关，放进 [TOP_RESOURCES_2026.md](TOP_RESOURCES_2026.md) 最合适的一节。
- 自己打开核实过：有实质内容和文档，不是空壳或纯营销。
- 不收录荐股、带单、加密代币推广、付费社群引流或刷星的项目；README 里有付费推广的，条目里要写明。
- 法规一律以证监会、交易所等官方原文为准；研究和报告数字只用原文，并标注发布日期。
- 同类已有更好的，就不再加。

## 代码和 Notebook

- 脚本放在 `scripts/`，并在 `tests/` 补单元测试；提交前本地运行 `python -m pytest -q`。
- Notebook 要能离线运行（没有网络时回退到示例数据），不需要任何 API Key。
- 不提交数据文件、运行产物（`reports/` 已忽略）和任何凭据。

## 维护方式

链接由 Link Check 定期检查，脚本由 CI 每周跑一次；每天的[内容雷达](https://github.com/luckliu2007/content-radar)检查已收录项目的健康状况并发现候选，候选经人工核实后才会收录。
