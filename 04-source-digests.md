# 04 原始链接消化版

这一页的目的不是重新列链接，而是告诉你：**每个链接最值得提取什么，是否值得深挖，以及它在你的学习体系里扮演什么角色。**

## A. 原仓库里最有价值的两份内部文档

### `ai-infrastructure-fundamentals.md`

适合做“AI Infra 入门骨架”。它已经把计算、存储、网络、训练、推理、特征存储、扩展策略和监控串成了一条线。你可以把它当作概念底稿，而不是最终资料。

### `mlops-tools-guide.md`

适合做“工具入口”。价值不在于记住 59 个工具，而在于快速知道分布式训练、模型服务、MLOps、数据管理、优化工具分别有哪些代表选项。

## B. GitHub 项目与 Awesome Lists

### [AI-Infra-from-Zero-to-Hero](https://github.com/HuaizhengZhang/AI-Infra-from-Zero-to-Hero)

这是最值得深挖的外部 GitHub 资源之一。它的价值不在于“列很多工具”，而在于按 `training / inference / infra / llm training / llm serving / edge / federated learning` 这些真正的系统主题组织材料，还串了论文、代码和会议入口。它适合你在建立基础后，进入“系统研究视角”。

### [awesome-ai-infrastructure](https://github.com/brandonhimpfen/awesome-ai-infrastructure)

这份列表更像“标准 AI Infra 工具地图”。提取重点：

- 分布式训练：Horovod、Ray、PyTorch Distributed、DeepSpeed
- 模型服务：TensorFlow Serving、TorchServe、Triton、ONNX Runtime、KServe
- MLOps：MLflow、Kubeflow、DVC、ZenML、Airflow、Metaflow
- 数据层：Delta Lake、Hudi、Feast、Great Expectations、LakeFS
- IaC：Terraform、Pulumi、Ansible

如果你想把“我到底该认识哪些工具”快速建立起来，这份很适合。

### [awesome-ai-infrastructures](https://github.com/1duo/awesome-ai-infrastructures)

这份的特色不是工具列表，而是“真实生产平台案例”。它会帮你看到 Google TFX、Kubeflow、RAPIDS、Uber Michelangelo、Facebook FBLearner、Apple Alchemist、IBM FfDL、SageMaker 这类系统是怎样被组织起来的。适合从“工具视角”过渡到“平台架构视角”。

### [awesome-opensource-ai](https://github.com/alvinreal/awesome-opensource-ai)

这份资源比 AI Infra 的范围更大，但很适合补全生态认知。它把框架、模型、推理引擎、训练优化、MLOps/LLMOps、评测、安全、自托管平台等都放进了一张全景图。对于你来说，最值得重点看的部分是：

- Core Frameworks
- Inference Engines & Serving
- Training & Fine-tuning Ecosystem
- MLOps / LLMOps & Production
- Evaluation / Safety / Self-hosted Platforms

### [awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)

这份不是基础设施底层，而是“AI 应用怎么落地”的上层样例库。对 AI Infra 的价值在于反向理解需求：当你看到 starter agents、voice agents、MCP agents、memory agents、RAG apps 时，你会更清楚应用层会反过来要求什么样的模型服务、数据层和可观测性。

### [ai-research-writing-prompts](https://github.com/heaven999b/ai-research-writing-prompts)

这是原仓库作者的姊妹仓库，但它更偏 AI 写作与 prompt engineering，不是 AI Infra 主线。可以先忽略，不会影响你建立 AI Infra 框架。

## C. 课程与认证资源

### [Coursera: AI Infrastructure and Operations Fundamentals](https://www.coursera.org/learn/ai-infrastructure-operations-fundamentals)

这是很标准的入门课，适合打基础。它明确分成 AI 简介、AI 基础设施、AI 运维、结课测试几部分，重点覆盖 GPU/CPU、网络、存储、能效、参考架构、云上 AI、监控与编排。优点是结构清晰，适合系统管理员、DevOps、数据中心从业者切入。

### [Udemy: The Complete Guide to AI Infrastructure: Zero to Hero](https://www.udemy.com/course/complete-guide-ai-infrastructure/)

从页面公开内容看，它的价值在于把 `training vs inference`、`hardware / software / ops layers`、`FastAPI / gRPC / HPA / KEDA / Triton / TensorRT` 这些词汇放到一条连贯叙事里。适合你在已有概念基础后，用来补“系统设计 vocabulary”。

### [NVIDIA Training Academy](https://www.nvidia.com/en-us/training/academy/)

这是官方训练入口，不是单门课。它更适合你在确定自己要往 GPU 基础设施、边缘 AI、数据中心、AI factory 这些方向深入后按主题选课。它的价值是“官方硬件生态视角”。

### [Cisco DCAIE](https://www.cisco.com/site/us/en/learn/training-certifications/training/courses/dcaie.html)

Cisco 这门课更偏企业网络和数据中心落地。提取重点：

- AI/ML cluster 架构
- workload placement
- 互操作性
- 合规与治理
- 可持续基础设施
- 用 Jupyter Lab 和 GenAI 自动化网络运维

如果你以后更偏企业基础设施或网络方向，这门资源很有价值。

### [Google Cloud AI Infrastructure Path](https://www.skills.google/paths/2806)

这条学习路径更偏 Google Cloud 实战，面向中高级学习者，强调 `AI Hypercomputer、GPU、TPU、Compute、GKE、storage、networking、orchestration`。适合你准备云上 AI 基础设施时用来补“Google 体系”的方法论。

### [Udemy: AI-Powered IT Operations and Infrastructure](https://www.udemy.com/course/ai-powered-it-operations-and-infrastructure/)

这门更偏 AIOps，而不是狭义 AI Infra。重点是实时监控、故障预测、自动化响应、历史日志建模、时间序列预测。适合作为“AI 用在 IT 运维里的一个应用面”。

### [Udemy: SoAI-Certified Professional: AI Infrastructure (NCP-AII)](https://www.udemy.com/course/ncp-aii-nvidia-certified-professional-ai-infrastructure/)

这门课相对更贴近现代 AI Infra 关键词，公开内容里已经出现了 `MIG、vGPU、Kubernetes scheduling、Nsight、DLProf、TensorRT、DCGM、GDPR、HIPAA、RBAC、DOCA`。如果你以后要补 GPU 多租户、性能分析、企业合规，这门比泛入门课更贴近工程面。

## D. 博客与综合指南

### [RudderStack: AI Infrastructure 101](https://www.rudderstack.com/blog/ai-infrastructure/)

这篇适合拿来建立“完整栈”的概念框架。它强调 AI Infra 不只是硬件，还包括数据流、编排、治理和合规。你可以提炼的重点是：**数据流和治理应该从第一天就进入设计。**

### [Splunk: AI Infrastructure Explained](https://www.splunk.com/en_us/blog/learn/ai-infrastructure.html)

这篇最值得提取的是“观测视角”。它把 AI Infra 分成 compute、storage、network、framework、orchestration、data pipeline、deployment、observability，并特别强调生产环境里的可观测性、模型漂移、系统指标和安全。适合在你学完基础之后，补“上线后怎么办”。

### [Nexla: AI Infrastructure Tutorial & Best Practices](https://nexla.com/ai-infrastructure/)

这篇不是简单讲 AI Infra 定义，而是把它放进一条更贴近 LLM 时代的链路里，后续还延伸到 LLM、vector embedding、vector DB、RAG、hallucination、security、LLMOps。对你来说，重点不是品牌，而是这条知识扩展路径本身。

### [Tailscale: 7 Strategies for Efficient AI Deployments](https://tailscale.com/learn/ai-infra-ai-deployment)

这篇最值得学的是“部署策略”而不是概念定义。它把需求评估、云/本地/混合选择、硬件与软件选型、数据存储、扩展性、安全和治理都放进了实际部署决策里。适合你在开始做架构取舍时参考。

### [F5: AI Infrastructure Learning Resources](https://www.f5.com/learn/ai/infrastructure)

F5 这页更像专题入口，不是一篇完整教程。它比较适合你补这些角度：

- AI application architecture
- delivery and security
- inference patterns
- edge AI
- Kubernetes 上的 AI/ML workload 扩展

换句话说，它更像“生产网络与交付视角”的阅读入口。

## E. 行业报告

### [Google Cloud 2025 State of AI Infrastructure Report](https://cloud.google.com/resources/content/state-of-ai-infrastructure)

公开页面最有价值的结论有 4 个：

1. 生成式 AI 基本已经从试验走向广泛采用
2. 数据质量和安全仍然是最大阻碍
3. 成本既是阻碍，也是做好基础设施后的收益点
4. 随着 IoT 和移动端用例增长，分布式工作流和安全要求进一步提高

这类报告的价值不在技术细节，而在帮助你理解企业为什么在意这些基础设施问题。

### [Flexential 2025 State of AI Infrastructure Report](https://www.flexential.com/resources/report/2025-state-ai-infrastructure)

这份报告给出的管理层和组织侧信号很强：

- 90% 的受访者在部署生成式 AI
- 81% 认为 C-suite 正在主导 AI 决策
- 44% 认为 IT 基础设施约束是扩张 AI 的首要障碍
- 86% 担心 AI 基础设施相关人才不足
- 61% 明确报告了专用计算基础设施管理能力缺口

它提醒你一件事：企业落地 AI Infra，难点常常不是“有没有工具”，而是“有没有能力把工具组织起来”。

## F. 我建议你怎么使用这些来源

### 第一优先级：先吃透

- 原仓库两份内部文档
- AI-Infra-from-Zero-to-Hero
- awesome-ai-infrastructure
- Coursera NVIDIA 入门课
- Splunk / RudderStack / Tailscale 三篇文章

### 第二优先级：进到系统设计与平台视角

- awesome-ai-infrastructures
- Google Cloud AI Infrastructure Path
- Cisco DCAIE
- SoAI / NCP-AII 这类偏工程细节课程

### 第三优先级：当扩展阅读

- awesome-opensource-ai
- awesome-ai-apps
- F5 资源入口
- 各类行业报告

## G. 这批链接最终沉淀成什么知识

如果你把这些资源真正吸收掉，应该沉淀成下面 5 类能力：

1. 你能解释 AI Infra 的完整层次结构。
2. 你能说清训练系统与推理系统的不同目标。
3. 你能给常见工具找到它们所在的层和适用场景。
4. 你能理解真实生产平台为什么要长成现在这样。
5. 你能从成本、安全、治理、人才这些角度看待 AI Infra，而不是只看模型本身。
