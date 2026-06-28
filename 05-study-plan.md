# 05 六周学习计划

这份计划的目标不是“把所有链接都看完”，而是让你在 6 周内形成可复述、可实践、可继续扩展的 AI Infra 基础。

## 第 1 周：建立概念骨架

任务：

1. 读完 `01-learning-map.md`
2. 读完 `02-core-knowledge.md`
3. 回看原仓库里的 `ai-infrastructure-fundamentals.md`

这一周的产出：

- 你能用自己的话解释 AI Infra 是什么
- 你能画出 `数据 -> 训练 -> 服务 -> 监控` 这条链
- 你能区分训练系统和推理系统

## 第 2 周：先把训练跑起来

任务：

1. 跑 `03-code-cookbook.md` 里的单 GPU 训练骨架
2. 读 `mlops-tools-guide.md` 里的 Horovod 和 Ray 部分
3. 在 `sources/AI-Infra-from-Zero-to-Hero` 里看 `training.md`

这一周的产出：

- 你能解释 data parallel 和 communication overhead
- 你能写一个最小训练循环
- 你知道什么时候该从单机切到分布式

## 第 3 周：把模型服务起来

任务：

1. 跑 Cookbook 里的 TF Serving 或 TorchServe
2. 学推理系统的核心指标：吞吐、延迟、并发、错误率
3. 看 `AI-Infra-from-Zero-to-Hero/inference.md` 和 `llm_serving.md`

这一周的产出：

- 你能把模型暴露成 API
- 你能解释 batching、缓存、autoscaling 的价值
- 你开始真正理解“训练完不等于上线”

## 第 4 周：补上 MLOps 与数据链路

任务：

1. 跑 MLflow 最小记录
2. 跑 DVC 最小版本管理
3. 理解特征存储、对象存储、模型 registry 的关系

这一周的产出：

- 你能记录实验与模型版本
- 你知道为什么数据版本和模型版本要同时管理
- 你能描述一个最小的训练流水线

## 第 5 周：进入平台与架构案例

任务：

1. 看 `awesome-ai-infrastructures` 里的 3 到 5 个真实平台案例
2. 看 Google Cloud / Cisco / NVIDIA 相关课程页面，理解企业侧学习重点
3. 看 Splunk、Tailscale、RudderStack 的相关文章

这一周的产出：

- 你能举出几个真实 AI 平台案例
- 你知道企业最在意的不是“论文技巧”，而是可扩展、可治理、可运维
- 你能开始做云上 / 本地 / 混合的基本权衡

## 第 6 周：做一个最小闭环项目

建议项目：

1. 用 PyTorch 训练一个小模型
2. 用 MLflow 记录实验
3. 用 DVC 追踪数据
4. 用 TorchServe 或 TF Serving 部署
5. 写一个简单压测脚本测延迟和吞吐
6. 记录你观察到的瓶颈

这一周的产出：

- 一个真正串起训练、记录、部署、测试的最小系统
- 一份你自己的复盘文档：
  - 最慢的环节是什么
  - 最容易忽略的工程问题是什么
  - 如果规模扩大 10 倍，你最先要改哪一层

## 你每周都应该回答的复盘问题

1. 这周我学到的是“工具”，还是“系统关系”？
2. 我能不能不用原文，自己讲清楚这个主题？
3. 我有没有亲手跑过最小例子？
4. 这个知识点在真实生产里解决什么问题？
5. 如果团队让我做一个最小 AI 平台，我会先搭哪几层？

## 如果你时间更少

那就压缩成这个顺序：

1. 先读 `02-core-knowledge.md`
2. 再做 `03-code-cookbook.md` 里的 4 个最小实验
3. 最后只看 `04-source-digests.md` 里的第一优先级资源

只要你把这三步做扎实，已经会比“收藏很多链接但没消化”强很多。
