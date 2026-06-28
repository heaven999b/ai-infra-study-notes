# AI Infra 学习资料（个人整理版）

这套资料不是“链接导航站”，而是把 [`ai-infra-learning`](https://github.com/heaven999b/ai-infra-learning) 里的核心知识、实践代码、外部资源价值点重新整理成一条更适合自己学习和复习的路径。

## 最近新增

- `06-微信资料整理入口.md`：两篇重要微信学习资料的识别状态、来源信息和后续整理入口。
- `07-两篇微信资料学习提要.md`：两篇微信资料的主题拆解、可学内容、以及和本机可运行项目的对应关系。
- `upstream-learning-sources/`：筛过一轮的上游学习资料快照，保留文档、源码和关键图示，去掉 Git 历史、演示视频和大体积附件。

## 先读这个

- `AI-Infra-直读学习手册.md`：单文件、连续阅读版，不需要先点很多链接。
- `Awesome-Lists-精读版.md`：把几个 awesome lists 真正消化成可直接阅读的工具图谱和项目地图。

## 你现在有什么

- `AI-Infra-直读学习手册.md`：把概念、系统、代码、案例揉成一份可直接阅读的主手册。
- `Awesome-Lists-精读版.md`：把 `awesome-ai-infrastructure`、`awesome-ai-infrastructures`、`awesome-opensource-ai`、`awesome-ai-apps` 重写成可学习内容。
- `01-learning-map.md`：先看全局，知道 AI Infra 到底学什么。
- `02-core-knowledge.md`：把核心概念压成一份可反复复习的知识底稿。
- `03-code-cookbook.md`：只保留最值得自己动手敲的代码和命令。
- `04-source-digests.md`：把原仓库里的外链都变成“这个链接值得学什么”。
- `05-study-plan.md`：给你一个能执行的 6 周学习方案。
- `06-微信资料整理入口.md`：记录这次微信资料识别、抓取尝试和后续处理规则。
- `07-两篇微信资料学习提要.md`：把两篇微信文章压成可执行学习建议。
- `upstream-learning-sources/`：适合继续深挖的上游原始资料快照。
- `source-link-index.json`：原仓库 Markdown 链接索引，方便你后续继续扩展。

## 推荐阅读顺序

1. 先读 `AI-Infra-直读学习手册.md`
2. 再读 `Awesome-Lists-精读版.md`
3. 然后用 `03-code-cookbook.md` 边学边动手
4. 需要扩展阅读时查 `04-source-digests.md`
5. 最后按 `05-study-plan.md` 去排自己的节奏

## 这套资料的整理原则

- 不再按“原始链接顺序”学习，而是按“概念 -> 系统 -> 代码 -> 生产实践”学习。
- 不把所有资源一视同仁，而是明确区分：
  - 哪些适合建立知识框架
  - 哪些适合看代码和工具
  - 哪些适合了解行业趋势
  - 哪些只适合当补充材料
- 优先保留你以后真的会反复回看的内容：系统设计问题、代码骨架、工具选型、常见权衡。

## 仓库说明

- 这个 GitHub 仓库会优先保存“我真正会回看的学习笔记”。
- 本地 `sources/` 目录包含下载下来的上游参考仓库，体积较大，因此默认不纳入 GitHub 版本库。
- `upstream-learning-sources/` 是从 `sources/` 里整理出来的“可公开、可阅读、体积更合理”的精选版本。

## 一句话理解 AI Infra

AI Infra 不是“买几张 GPU”这么简单，它是把计算、存储、网络、训练框架、数据管道、模型服务、监控治理和成本控制，拼成一个可以稳定支撑训练与推理的系统。
