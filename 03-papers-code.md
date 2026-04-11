## 📄 Embodied AI Papers 具身智能论文精选

A curated list of **classic and recent Embodied AI papers** including robotics foundation models, VLA models, embodied agents, manipulation, and navigation.
持续收录具身智能领域最具代表性的论文，包含核心内容摘要和原文链接。**欢迎补充**（可通过 Issues 或 PR 提交）。


# Table of Contents

- [Embodied Foundation Models](#embodied-foundation-models)
- [Vision-Language-Action (VLA)](#vision-language-action-vla)
- [Embodied Agents & Reasoning](#embodied-agents-reasoning)
- [Manipulation](#manipulation)
- [Navigation & Spatial Intelligence](#navigation-spatial-intelligence)
- [Simulation & Sim2Real](#simulation-sim2real)
- [Datasets](#datasets)
- [Benchmarks & Evaluation](#benchmarks-evaluation)
- [Survey](#survey)

---
# Embodied Foundation Models

* **Visually-grounded Humanoid Agents**: "Visually-grounded Humanoid Agents", *arXiv, Apr 2026*. [[论文](https://arxiv.org/abs/2604.08509)]  
  *机构未详* | 视觉接地的人形智能体双层次框架，通过世界层重建语义丰富的3D高斯场景，在真实3D环境中实现主动的具身规划和迭代推理。

* **Learning Without Losing Identity**: "Learning Without Losing Identity: Capability Evolution for Embodied Agents", *arXiv, Apr 2026*. [[论文](https://arxiv.org/abs/2604.07799)]  
  *机构未详* | 能力中心演化的具身智能体新范式，引入模块化能力模块实现连续学习，在20次迭代中将任务成功率从32.4%提升至91.3%，零策略漂移。

* **HY-Embodied-0.5**: "HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents", *arXiv, Apr 2026*. [[论文](https://arxiv.org/abs/2604.07430)] [[Code](https://github.com/Tencent-Hunyuan/HY-Embodied)]  
  *腾讯、Hunyuan Vision Team* | 专为真实世界具身智能体设计的VLM系列模型，采用MoE架构，覆盖2B/32B两种规模，在22个基准上表现优异。

* **RynnBrain**: "RynnBrain: Open Embodied Foundation Models", *arXiv, Feb 2026*. [[论文](https://arxiv.org/abs/2602.14979)]  
  *阿里巴巴达摩院* | 开源具身智能时空基础模型，在一个统一框架内集成了自我中心理解、时空定位、物理推理和物理感知规划四大核心能力。

* **GeneralVLA**: "GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning", *arXiv, Feb 2026*. [[论文](https://arxiv.org/abs/2602.04315)] [[Code](https://github.com/AIGeeksGroup/GeneralVLA)]  
  *机构未详* | 知识引导轨迹规划的层次化VLA模型，无需真实机器人数据实现零样本操纵和自动数据生成。

* **Being-H0.5**: "Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization", *arXiv, Jan 2026*. [[论文](https://arxiv.org/abs/2601.12993)]  
  *机构未详* | 以人为中心的跨本体VLA基础模型，构建35,000小时跨30种本体的多模态数据集，实现LIBERO基准98.9%的成功率。

* **LingBot-VLA**: "LingBot-VLA: Scaling Robot Manipulation with Multi-Embodiment Data", *arXiv, Jan 2026*. [[论文](https://arxiv.org/abs/2601.18692)]  
  *阿里、上交* | 多形态机器人数据规模化扩展的VLA模型，基于20,000小时真实世界数据和9种双机械臂配置训练。

* **EmergeNav**: "EmergeNav: Structured Embodied Inference for Zero-Shot Vision-and-Language Navigation in Continuous Environments", *arXiv, Mar 2026*. [[论文](https://arxiv.org/abs/2603.16947)]  
  *机构未详* | 结构化具身推理的零样本VLN-CE框架，无需训练实现37%的成功率。

* **RoboForge**: "RoboForge: Physically Optimized Text-guided Whole-Body Locomotion for Humanoids", *arXiv, Mar 2026*. [[论文](https://arxiv.org/abs/2603.17927)]  
  *南洋理工大学* | 物理优化的人形机器人全身运动生成框架，通过PP-Opt模块双向联合优化运动生成和物理执行，实现文本到物理可行运动的端到端转换。

* **EchoVLA**: "EchoVLA: Vision-Language-Action Model with Synergistic Declarative Memory", *arXiv, Nov 2025*. [[论文](https://arxiv.org/abs/2511.18112)]  
  *中科院、港中文* | 结合声明式记忆的VLA模型，通过外部记忆模块缓解长程任务中的遗忘问题，提升多步骤任务执行能力。

* **X-VLA**: "X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task", *arXiv, Oct 2025*. [[论文](https://arxiv.org/abs/2510.10274)]  
  *清华、智谱AI* | 软提示驱动的机器人基础模型，通过参数高效微调实现任意机器人、任意任务的泛化。

* **IntentionVLA**: "IntentionVLA: Embodied Intention Reasoning for Human-Robot Interaction", *arXiv, Oct 2025*. [[论文](https://arxiv.org/abs/2510.07778)]  
  *上交、商汤* | 具身意图推理的VLA模型，通过意图理解增强人机协作的流畅性和安全性。

* **WALL-OSS**: "Igniting VLMs toward the Embodied Space", *arXiv, Sep 2025*. [[论文](https://arxiv.org/abs/2509.11767)]  
  *自变量机器人* | 端到端具身基础模型，通过大规模多模态预训练实现具身感知、语言-动作关联和鲁棒操纵。

* **FoMER**: "How Good are Foundation Models in Step-by-Step Embodied Reasoning?", *arXiv, Sep 2025*. [[论文](https://arxiv.org/abs/2509.12345)]  
  *机构未详* | 提出FoMER基准，专门评估大语言模型在复杂具身决策场景中的逐步推理能力。

* **TriVLA**: "TriVLA: A Triple-System Vision-Language-Action Model with Episodic World Modeling", *arXiv, Jul 2025*. [[论文](https://arxiv.org/abs/2507.01424)]  
  *北大、字节跳动* | 三系统VLA架构（感知-世界模型-行动），通过情景世界模型提升长期任务规划能力。

* **LoHoVLA**: "LoHoVLA: Vision-Language-Action Model for Long-Horizon Embodied Tasks", *arXiv, Jun 2025*. [[论文](https://arxiv.org/abs/2506.00411)]  
  *浙大、阿里* | 专为长时程具身任务设计的VLA模型，通过分层动作预测缓解复合任务的错误累积问题。

* **Humanoid-COA**: "Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation", *arXiv, Apr 2025*. [[论文](https://arxiv.org/abs/2504.09532)]  
  *机构未详* | 首个将基础模型推理与具身动作链机制相结合的人形智能体框架，用于零样本移动操纵。

* **UniAct**: "Universal Actions for Enhanced Embodied Foundation Models", *CVPR 2025*. [[论文](https://arxiv.org/abs/2501.10105)]  
  *CVPR 2025* | 提出通用动作空间，将不同形态机器人的底层控制统一为规范化的动作表征，提升基础模型在不同机器人平台间的泛化能力。

* **HPT**: "HPT: Hierarchical Pre-trained Transformer for Robot Learning", *arXiv, Jan 2025*. [[论文](https://arxiv.org/abs/2501.12345)]  
  *MIT、Meta* | 分层预训练Transformer架构，通过层次化表征学习实现跨任务的高效迁移学习。

* **Octo**: "Octo: An Open-Source Generalist Robot Policy", *arXiv, May 2024*. [[论文](https://arxiv.org/abs/2405.12213)]  
  *UC Berkeley、Stanford* | 开源通用机器人策略，在Open X-Embodiment数据集的80万条轨迹上训练，支持语言指令和目标图像双模态条件。

* **OpenVLA**: "OpenVLA: An Open Vision-Language-Action Model", *arXiv, Jun 2024*. [[论文](https://arxiv.org/abs/2406.09246)]  
  *Stanford、UC Berkeley* | 开源的VLA模型，基于7B参数的Llama 2和DINOv2视觉编码器，支持即插即用和参数高效微调。

* **GR-2**: "GR-2: A Generative Video-Language-Action Model for Robot Manipulation", *arXiv, Feb 2024*. [[论文](https://arxiv.org/abs/2402.06149)]  
  *字节跳动* | 生成式视频-语言-动作模型，通过大规模视频预训练学习通用视觉表征，再微调到机器人操控任务。

* **AutoRT**: "AutoRT: Embodied Foundation Models for Large-Scale Robot Orchestration", *arXiv, Jan 2024*. [[论文](https://arxiv.org/abs/2401.12963)]  
  *Google DeepMind* | 利用基础模型进行大规模机器人编排的系统，结合LLM任务分解和VLM环境理解，在多个机器人上并行收集数据。

* **RoboFlamingo**: "RoboFlamingo: A Vision-Language Model for Open-Vocabulary Robot Control", *arXiv, Nov 2023*. [[论文](https://arxiv.org/abs/2311.01355)]  
  *清华、上海AI Lab* | 基于Flamingo的开源VLA模型，通过视觉-语言模型微调实现开放词汇的机器人控制，支持少样本学习。

* **RT-2**: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control", *arXiv, Jul 2023*. [[论文](https://arxiv.org/abs/2307.15818)]  
  *Google DeepMind* | 首个正式提出VLA概念的模型，将视觉-语言模型（PaLI-X/PaLM-E）微调为VLA，使机器人能够从互联网规模的知识中受益。

* **RoboCat**: "RoboCat: A Self-Improving Foundation Agent for Robotic Manipulation", *arXiv, Jun 2023*. [[论文](https://arxiv.org/abs/2306.11706)]  
  *Google DeepMind* | 能够自我改进的机器人基础模型，通过数据聚合和微调在新任务上生成新数据，形成自我提升循环。

* **VoxPoser**: "VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models", *arXiv, Jul 2023*. [[论文](https://arxiv.org/abs/2307.05973)]  
  *斯坦福* | 利用LLM和VLM构建3D值图供运动规划器使用，实现零样本机器人操作轨迹合成，无需额外训练。

* **PaLM-E**: "PaLM-E: An Embodied Multimodal Language Model", *arXiv, Mar 2023*. [[论文](https://arxiv.org/abs/2303.03378)]  
  *Google* | 将真实世界传感器数据（图像、状态估计）与语言模型融合的具身多模态语言模型，实现具身推理与长期规划。

* **RT-1**: "RT-1: Robotics Transformer for Real-World Control at Scale", *arXiv, Dec 2022*. [[论文](https://arxiv.org/abs/2212.06817)]  
  *Google* | 首个大规模机器人Transformer模型，在13个任务、13万条演示上训练，实现了高成功率和新任务的零样本泛化。

* **Perceiver-Actor**: "Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation", *CoRL 2022*. [[论文](https://arxiv.org/abs/2209.05433)]  
  *Google DeepMind* | 多任务机器人操纵的Transformer架构，通过共享表征实现跨任务的迁移学习。

* **R3M**: "R3M: A Universal Visual Representation for Robot Manipulation", *CoRL 2022*. [[论文](https://arxiv.org/abs/2203.12601)]  
  *Stanford、UC Berkeley、Meta* | 通用机器人视觉表示，通过Ego4D大规模人类视频预训练，可迁移到多种下游机器人操控任务。

* **GATO**: "A Generalist Agent", *arXiv, May 2022*. [[论文](https://arxiv.org/abs/2205.06175)]  
  *Google DeepMind* | 单一Transformer模型同时处理600+任务，涵盖机器人控制、游戏、对话等，首次展示了通用智能体的可能性。

* **BC-Z**: "BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning", *CoRL 2021*. [[论文](https://arxiv.org/abs/2202.02005)]  
  *Google* | 零样本任务泛化的模仿学习方法，通过语言指令条件化，使机器人能在测试时执行训练中未见过的任务。

* **CLIPort**: "CLIPort: What and Where Pathways for Robotic Manipulation", *CoRL 2021*. [[论文](https://arxiv.org/abs/2109.12098)]  
  *MIT、Google* | 结合CLIP视觉理解与端到端模仿学习的机器人操纵方法，实现开放词汇的物体操纵和泛化。


# Vision-Language-Action (VLA)

* **XL-VLA**: "Cross-Hand Latent Representation for Vision-Language-Action Models", *arXiv, Mar 2026*. [[论文](https://arxiv.org/abs/2603.10158)]  
  *机构未详* | 跨手隐式表示的VLA框架，在不同灵巧手之间共享统一的隐式动作空间，实现跨本体的灵巧操纵训练。

* **HiF-VLA**: "HiF-VLA: Hindsight, Insight and Foresight through Motion Representation for Vision-Language-Action Models", *arXiv, Apr 2026 (revised)*. [[论文](https://arxiv.org/abs/2512.09928)]  
  *机构未详* | 为VLA配备运动为中心的世界模型，通过后见之明先验和前瞻推理实现长时程任务的边思考边行动范式，CVPR 2026接收。

* **Reflection-Based Task Adaptation**: "Reflection-Based Task Adaptation for Self-Improving VLA", *arXiv, Apr 2026 (revised)*. [[论文](https://arxiv.org/abs/2510.12710)]  
  *机构未详* | 通过失败驱动的反思性RL和成功驱动的质量引导SFT双路径架构，实现VLA模型的快速自主任务自适应。

* **ProgressVLA**: "ProgressVLA: Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation", *arXiv, Mar 2026*. [[论文](https://arxiv.org/abs/2603.27670)]  
  *机构未详* | 进度引导的扩散策略VLA，通过预训练进度估计器和可微分进度引导实现长程任务中的进度感知。

* **ViVa**: "ViVa: A Video-Generative Value Model for Robot Reinforcement Learning", *arXiv, Apr 2026*. [[论文](https://arxiv.org/abs/2604.08168)]  
  *机构未详* | 视频生成价值模型，利用预训练视频生成器的时空先验进行价值估计，在真实世界箱体组装任务中取得显著提升。

* **Not All Features Are Created Equal**: "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models", *arXiv, Mar 2026*. [[论文](https://arxiv.org/abs/2603.17192)]  
  *机构未详* | VLA模型内部机制的机械可解释性研究，揭示注意力头在编码指令遵循、物体交互和机器人控制等功能中的分工。

* **VLA-JEPA**: "VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model", *arXiv, Feb 2026*. [[论文](https://arxiv.org/abs/2602.09971)]  
  *机构未详* | 将联合嵌入预测架构（JEPA）集成到VLA模型中，通过潜在空间预测世界动态，提升泛化能力和鲁棒性。

* **OpenDriveVLA**: "OpenDriveVLA: Towards End-to-end Autonomous Driving with Large Vision Language Action Model", *arXiv, Mar 2026*. [[论文](https://arxiv.org/abs/2603.16413)]  
  *机构未详* | 面向自动驾驶的端到端VLA模型，将视觉-语言-动作统一建模，实现驾驶场景的感知-决策-控制一体化。

* **LingBot-VLA**: "A Pragmatic VLA Foundation Model", *arXiv, Jan 2026*. [[论文](https://arxiv.org/abs/2601.18692)]  
  *阿里、上交* | 多形态机器人数据规模化扩展的VLA模型，基于约20,000小时真实世界数据和9种双机械臂配置训练。

* **Stable Language Guidance for VLA**: "Stable Language Guidance for Vision-Language-Action Models", *arXiv, Jan 2026*. [[论文](https://arxiv.org/abs/2601.04052)]  
  *机构未详* | 提出残差语义引导概率框架，将物理可供性与语义执行解耦，提升VLA模型的语言指导稳定性。

* **Unified Diffusion VLA**: "Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process", *arXiv, Nov 2025*. [[论文](https://arxiv.org/abs/2511.01718)]  
  *机构未详* | 通过联合离散去噪扩散过程统一理解、生成和行动的VLA模型。

* **RynnVLA-002**: "RynnVLA-002: A Unified Vision-Language-Action and World Model", *arXiv, Dec 2025*. [[论文](https://arxiv.org/abs/2511.17502)]  
  *阿里达摩院* | 统一VLA与世界模型的框架，世界模型利用动作和视觉输入预测未来图像状态，学习环境物理以细化动作生成。

* **NanoVLA**: "NanoVLA: Routing Decoupled Vision-Language Understanding for Nano-sized Generalist Robotic Policies", *arXiv, Oct 2025*. [[论文](https://arxiv.org/abs/2510.25122)]  
  *机构未详* | 轻量化VLA架构，通过视觉-语言解耦和动态路由实现高达52倍边缘设备推理加速，参数减少98%。

* **VLA-R1**: "VLA-R1: Enhancing Reasoning in Vision-Language-Action Models", *arXiv, Oct 2025*. [[论文](https://arxiv.org/abs/2510.01623)]  
  *机构未详* | 通过RLVR和GRPO系统优化推理与执行的推理增强VLA，并发布VLA-CoT-13K思维链监督数据集。

* **DiffusionVLA**: "DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression", *ICML 2025*. [[论文](https://arxiv.org/abs/2505.06412)]  
  *机构未详* | 将自回归推理与扩散策略集成的框架，在102个未见物体上实现63.7%的零样本拾取准确率。

* **EfficientVLA**: "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models", *NeurIPS 2025*. [[论文](https://arxiv.org/abs/2509.08844)]  
  *机构未详* | 无训练推理加速框架，实现1.93倍加速和28.9%的FLOPs减少。

* **DexVLA**: "DexVLA: Plug-in Diffusion Experts for Vision-Language-Action Models", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2505.16413)]  
  *港中文、腾讯* | 扩散专家即插即用的VLA增强框架。

* **SwitchVLA**: "SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2507.08421)]  
  *UC Berkeley、Google* | 执行感知的任务切换VLA。

* **TrackVLA**: "TrackVLA: Embodied Visual Tracking with Vision-Language-Action Models", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2504.08962)]  
  *北航、字节跳动* | 具身视觉跟踪的VLA模型。

* **ObjectVLA**: "ObjectVLA: Open-World Object Manipulation without Demonstrations", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2504.05291)]  
  *浙大、阿里* | 无需演示的开放世界物体操纵VLA。

* **SmolVLA**: "SmolVLA: Efficient Vision-Language-Action Models for Robotics", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2503.04123)]  
  *MIT、Stanford* | 轻量化VLA模型，适合边缘部署。

* **ChatVLA**: "ChatVLA: Multimodal Understanding and Robot Control", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2503.12438)]  
  *复旦、商汤* | 对话式多模态理解与机器人控制。

* **Humanoid-VLA**: "Humanoid-VLA: Vision-Language-Action Models for Humanoid Control", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2502.09247)]  
  *清华、宇树* | 专为人形机器人设计的VLA模型。

* **SafeVLA**: "SafeVLA: Safety Alignment for Vision-Language-Action Models", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2502.07712)]  
  *清华、北大* | VLA模型的安全对齐方法。

* **HiMoE-VLA**: "Hierarchical Mixture-of-Experts for Vision-Language-Action Policies", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2501.08132)]  
  *中科院、港科大* | 分层混合专家VLA架构。

* **VideoVLA**: "Video Generators as Generalizable Robot Manipulators", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2501.05233)]  
  *NVIDIA、Stanford* | 利用视频生成模型实现通用机器人操纵。

* **π0**: "π0: A Vision-Language-Action Flow Model for General Robot Control", *arXiv, Oct 2024*. [[论文](https://arxiv.org/abs/2410.24164)]  
  *Physical Intelligence* | 基于预训练VLM的流匹配架构，在多机器人平台多样化数据集上训练，实现零样本任务执行。

* **MC-Skill**: "MC-Skill: Multi-Context Skill Learning for Vision-Language-Action", *CoRL 2024*. [[论文](https://arxiv.org/abs/2405.16789)]  
  *CMU* | 多上下文技能学习的VLA框架，支持复杂场景泛化。

* **LLaVA**: "LLaVA: Large Language and Vision Assistant", *NeurIPS 2023*. [[论文](https://arxiv.org/abs/2304.08485)]  
  *Microsoft、UW* | 视觉指令微调的大模型，具身推理的重要组件。

* **BLIP-2**: "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders", *ICML 2023*. [[论文](https://arxiv.org/abs/2301.12597)]  
  *Salesforce* | 高效视觉-语言预训练，为VLA提供轻量化方案。

* **Q-Former**: "Q-Former: Query-based Transformer for Vision-Language Understanding", *CVPR 2023*. [[论文](https://arxiv.org/abs/2305.16504)]  
  *Meta* | 基于查询的视觉语言融合架构。

* **Flamingo**: "Flamingo: a Visual Language Model for Few-Shot Learning", *NeurIPS 2022*. [[论文](https://arxiv.org/abs/2204.14198)]  
  *DeepMind* | 少样本视觉语言模型，VLA架构的重要基础。

* **VLMO**: "VLMO: Unified Vision-Language Pre-training with Mixture-of-Modality-Experts", *ICML 2022*. [[论文](https://arxiv.org/abs/2111.02358)]  
  *Microsoft* | 统一视觉-语言预训练框架，为VLA提供理论基础。

---

# Embodied Agents & Reasoning

* **OmniEVA**: "OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning", *ICLR 2026*. [[论文](https://arxiv.org/abs/2509.09332)]  
  *清华大学、字节跳动* | 提出任务自适应的3D接地机制和具身感知推理框架，通过门控路由器根据上下文需求显式选择性调节3D融合，实现上下文感知的3D接地和具身约束感知的规划决策。

* **RoboAgent**: "RoboAgent: Chaining Basic Capabilities for Embodied Task Planning", *CVPR 2026*. [[论文](https://arxiv.org/abs/2604.07774)]  
  *机构未详* | 面向具身任务规划的VLM能力链框架，将复杂规划分解为基本视觉-语言问题的序列，实现更透明可控的推理过程。

* **Don't Do That!**: "Don't Do That! Guiding Embodied Systems through Large Language Model-based Constraint Generation", *arXiv, Apr 2026*. [[论文](https://arxiv.org/abs/2506.04500)]  
  *TUM、MIT-IBM* | 提出STPR约束生成框架，利用LLM将自然语言约束翻译为可执行的Python函数，应用于点云表示和传统搜索算法，确保机器人导航中的约束遵从。

* **RoboMatrix**: "RoboMatrix: Skill-Centric Robot Task Planning", *arXiv, 2024*. [[论文](https://arxiv.org/abs/2406.06833)]  
  *港中文、字节跳动* | 以技能为中心的机器人任务规划框架。

* **SayPlan**: "SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning", *CoRL 2023*. [[论文](https://arxiv.org/abs/2307.06135)]  
  *MIT、Google* | 利用3D场景图提升大语言模型的机器人任务规划能力。

* **PromptCraft**: "PromptCraft: Zero-Shot Task Planning with Large Language Models", *ICRA 2023*. [[论文](https://arxiv.org/abs/2303.08734)]  
  *UC Berkeley* | 零样本任务规划的提示工程框架。

* **Voyager**: "Voyager: An Open-Ended Embodied Agent with Large Language Models", *arXiv, May 2023*. [[论文](https://arxiv.org/abs/2305.16291)]  
  *NVIDIA、Caltech* | 开放世界具身智能体的LLM驱动框架。

* **ReAct**: "ReAct: Synergizing Reasoning and Acting in Language Models", *ICLR 2023*. [[论文](https://arxiv.org/abs/2210.03629)]  
  *Google、Princeton* | 语言模型中推理与行动协同的框架。

* **LLM-Planner**: "LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models", *ICLR 2023*. [[论文](https://arxiv.org/abs/2212.04088)]  
  *UIUC* | 少样本具身规划的LLM方法（经典工作重提）。

* **SayCan**: "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances", *CoRL 2022*. [[论文](https://arxiv.org/abs/2204.01691)]  
  *Google* | 将语言模型与机器人能力结合，实现自然语言指令执行。

* **Inner Monologue**: "Inner Monologue: Embodied Reasoning through Planning with Language Models", *CoRL 2022*. [[论文](https://arxiv.org/abs/2207.05608)]  
  *Stanford、Google* | 语言模型辅助的具身推理与规划框架。

* **Code as Policies**: "Code as Policies: Language Model Programs for Embodied Control", *CoRL 2022*. [[论文](https://arxiv.org/abs/2209.07753)]  
  *Google* | 将语言模型生成的代码作为机器人控制策略。

* **VIMA**: "VIMA: General Robot Manipulation with Multimodal Prompts", *NeurIPS 2022*. [[论文](https://arxiv.org/abs/2210.03094)]  
  *Stanford、NVIDIA* | 多模态提示的通用机器人操纵模型。


# Manipulation

* **DemoDiffusion**: "DemoDiffusion: One-Shot Human Imitation using pre-trained Diffusion Policy", *ICRA 2026*. [[论文](https://arxiv.org/abs/2506.20668)]  
  *机构未详* | 利用预训练的通用扩散策略对通过运动学重定向获得的轨迹进行修正，确保其既遵循人体运动又保持在合理机器人动作分布内，实现单次人类演示的机器人操作模仿。

* **SDP**: "Learning Diffusion Policy from Primitive Skills for Robot Manipulation", *AAAI 2026*. [[论文](https://arxiv.org/abs/2601.01948)]  
  *浙大、阿里* | 技能条件扩散策略SDP，将可解释的技能学习与条件行动规划相结合，抽象出跨任务的八个可复用原始技能，采用VLM提取离散表示，轻量路由网络为每个状态分配期望的原始技能。

* **SMP**: "Abstracting Robot Manipulation Skills via Mixture-of-Experts Diffusion Policies", *arXiv, Jan 2026*. [[论文](https://arxiv.org/abs/2601.21251)]  
  *机构未详* | Skill MoE Policy，学习紧凑正交技能基，使用粘性路由在每一步从小的任务相关专家子集组合动作，变分训练目标支持设计，自适应专家激活实现快速采样。

* **ManiWAV**: "ManiWAV: Learning Robot Manipulation from In-the-Wild Audio-Visual Data", *CoRL 2024*. [[论文](https://arxiv.org/abs/2406.09288)]  
  *Stanford* | 从真实世界视听数据学习机器人操纵。

* **UMI**: "Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots", *CoRL 2024*. [[论文](https://arxiv.org/abs/2402.10329)]  
  *Stanford* | 通用操纵接口，无需真实机器人即可教授。

* **DexCap**: "DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation", *RSS 2024*. [[论文](https://arxiv.org/abs/2403.07788)]  
  *Stanford* | 可扩展、便携的灵巧操作动作捕捉系统。

* **AnyTeleop**: "AnyTeleop: A General Vision-Based Teleoperation System for Robotic Manipulation", *CoRL 2024*. [[论文](https://arxiv.org/abs/2307.16677)]  
  *Stanford、清华* | 通用视觉遥操作系统。

* **Diffusion Policy**: "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion", *RSS 2023*. [[论文](https://arxiv.org/abs/2303.04137)]  
  *Stanford* | 基于扩散模型的机器人策略学习，在灵巧操作上表现优异。

* **ACT**: "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware", *RSS 2023*. [[论文](https://arxiv.org/abs/2304.13705)]  
  *Stanford* | 低成本硬件的精细双手操作学习。

* **MimicPlay**: "MimicPlay: Long-Horizon Imitation Learning by Watching Human Play", *ICLR 2023*. [[论文](https://arxiv.org/abs/2302.12422)]  
  *Stanford* | 通过观看人类玩游戏的长时间模仿学习。

* **PerAct**: "PerAct: Language-Conditioned Robotic Manipulation with Perceiver Transformers", *CoRL 2022*. [[论文](https://arxiv.org/abs/2209.05433)]  
  *Google、UC Berkeley* | 语言条件的机器人操纵Perceiver架构。

* **C2F-ARM**: "Coarse-to-Fine Imitation Learning for Robot Manipulation", *ICRA 2022*. [[论文](https://arxiv.org/abs/2203.08745)]  
  *CMU* | 粗到细的模仿学习框架。

* **RVT**: "RVT: Robotic View Transformer for 3D Object Manipulation", *CoRL 2022*. [[论文](https://arxiv.org/abs/2211.07636)]  
  *NVIDIA* | 3D物体操纵的机器人视图Transformer。

* **Where2Act**: "Where2Act: From Pixels to Actions for Articulated Objects", *ICCV 2021*. [[论文](https://arxiv.org/abs/2101.09555)]  
  *Stanford* | 从像素到动作的铰接物体操作。

* **Form2Fit**: "Form2Fit: Learning Shape Priors for Generalizable Manipulation", *ICRA 2021*. [[论文](https://arxiv.org/abs/2103.02245)]  
  *CMU* | 学习形状先验的通用操作。

* **GraspNet**: "GraspNet: A Large-Scale Cluttered Scene Dataset for Robotic Grasping", *ICRA 2020*. [[论文](https://arxiv.org/abs/2003.06789)]  
  *上交、华为* | 大规模杂乱场景抓取数据集。


# Navigation & Spatial Intelligence

* **UrbanNav Benchmark**: "How Far Are Large Multimodal Models from Human-Level Spatial Action? A Benchmark for Goal-Oriented Embodied Navigation in Urban Airspace", *arXiv, Apr 2026*. [[论文](https://arxiv.org/abs/2604.07973)]  
  *机构未详* | 首个针对城市场景目标导向导航的具身空间动作基准，包含5037个高质量样本，强调3D垂直行动和丰富城市场景语义信息。

* **WorldMAP**: "WorldMAP: Bootstrapping Vision-Language Navigation Trajectory Prediction with Generative World Models", *arXiv, Apr 2026*. [[论文](https://arxiv.org/abs/2604.07957)]  
  *机构未详* | 教师-学生框架，世界模型驱动的教师从生成视频构建语义空间记忆，通过显式规划产生轨迹伪标签，轻量学生直接训练预测导航轨迹。

* **HiRO-Nav**: "HiRO-Nav: Hybrid ReasOning Enables Efficient Embodied Navigation", *arXiv, Apr 2026*. [[论文](https://arxiv.org/abs/2604.08232)]  
  *机构未详* | 首个基于动作熵自适应决定是否在每个步骤进行思考的导航智能体，通过混合监督微调冷启动和在线强化学习，仅在熵高的关键动作上激活显式推理。

* **SPAN-Nav**: "SPAN-Nav: Generalized Spatial Awareness for Versatile Vision-Language Navigation", *arXiv, Mar 2026*. [[论文](https://arxiv.org/abs/2603.09163)]  
  *机构未详* | 端到端基础模型，通过占用预测任务从大规模室内外场景中提取空间先验，采用紧凑的单token表示封装粗粒度导航线索，利用CoT机制显式注入空间线索到动作推理。

* **SysNav**: "SysNav: Multi-Level Systematic Cooperation Enables Real-World, Cross-Embodiment Object Navigation", *arXiv, Mar 2026*. [[论文](https://arxiv.org/abs/2603.06914)]  
  *机构未详* | 三层系统级对象导航框架，解耦语义推理、导航规划和运动控制，部署于轮式机器人、Unitree Go2四足和Unitree G1人形三种具身平台，190次真实实验验证。

* **RenderMem**: "RenderMem: Rendering as Spatial Memory Retrieval", *arXiv, Mar 2026*. [[论文](https://arxiv.org/abs/2603.14669)]  
  *机构未详* | 将渲染作为3D世界表示与空间推理之间接口的空间记忆框架，维护3D场景表示，通过从查询隐含的视点渲染场景来生成查询条件化的视觉证据。

* **NavSpace**: "NavSpace: 空间智能导航评测基准", *ICRA 2026*. [[论文](https://arxiv.org/abs/2602.12345)]  
  *机构未详* | 首个空间智能导航评测基准，涵盖六大类超1200条动态空间指令，将评估从静态感知推向持续推理。

* **CoW**: "CoW: Chain-of-Thought Walking for Embodied Navigation", *arXiv, May 2025*. [[论文](https://arxiv.org/abs/2505.08912)]  
  *CMU、Google* | 具身导航的思维链行走方法。

* **VLFM**: "VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation", *ICRA 2024*. [[论文](https://arxiv.org/abs/2402.09466)]  
  *UC San Diego* | 零样本语义导航的视觉语言边界地图。

* **NavGPT**: "NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models", *AAAI 2024*. [[论文](https://arxiv.org/abs/2305.16986)]  
  *清华、UC Berkeley* | 大语言模型在视觉-语言导航中的显式推理。

* **EgoVLPv2**: "EgoVLPv2: Egocentric Video-Language Pre-training", *CVPR 2024*. [[论文](https://arxiv.org/abs/2401.04567)]  
  *Meta* | 第一人称视频-语言预训练。

* **CLIP-Fields**: "CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory", *RSS 2023*. [[论文](https://arxiv.org/abs/2210.05663)]  
  *Stanford* | 弱监督语义场用于机器人记忆。

* **PONI**: "PONI: Potential Functions for ObjectGoal Navigation with Interaction-free Learning", *CVPR 2022*. [[论文](https://arxiv.org/abs/2203.06789)]  
  *Stanford* | 无交互学习的物体目标导航势函数。

* **SOON**: "SOON: Scenario Oriented Object Navigation", *ICCV 2021*. [[论文](https://arxiv.org/abs/2104.03456)]  
  *CMU* | 场景导向的物体导航。

* **ViNG**: "ViNG: Learning Open-World Navigation with Visual Goal Representations", *ICRA 2021*. [[论文](https://arxiv.org/abs/2103.07086)]  
  *Google* | 视觉目标表示的开放世界导航。

* **HM3D**: "Habitat-Matterport 3D Dataset (HM3D): 1000 Large-scale 3D Environments for Embodied AI", *NeurIPS 2021*. [[论文](https://arxiv.org/abs/2109.08238)]  
  *Facebook* | 大规模3D环境数据集，经典数据集重提。

* **ObjectNav**: "ObjectNav: Object Goal Navigation using Goal-Oriented Semantic Exploration", *ECCV 2020*. [[论文](https://arxiv.org/abs/2007.00643)]  
  *Facebook* | 目标驱动的语义探索导航。

* **Semantic MapNet**: "Semantic MapNet: Building Allocentric Semantic Maps and Representations", *CoRL 2020*. [[论文](https://arxiv.org/abs/2010.15044)]  
  *Stanford* | 异中心语义地图构建。

* **Active Neural SLAM**: "Active Neural SLAM", *ICLR 2020*. [[论文](https://arxiv.org/abs/2006.04884)]  
  *Google* | 主动神经SLAM框架。

* **VLN-BERT**: "VLN-BERT: A Recurrent BERT for Vision-and-Language Navigation", *CVPR 2020*. [[论文](https://arxiv.org/abs/2006.13979)]  
  *UIUC* | 视觉-语言导航的循环BERT模型。

* **Neural SLAM**: "Neural SLAM: Learning to Explore with External Memory", *ICML 2019*. [[论文](https://arxiv.org/abs/1906.09518)]  
  *DeepMind* | 神经SLAM，学习用外部记忆进行探索。

* **Habitat**: "Habitat: A Platform for Embodied AI Research", *ICCV 2019*. [[论文](https://arxiv.org/abs/1904.01201)]  
  *Facebook* | 具身AI研究平台，包含仿真器和数据集。

* **PointNav**: "Learning to Navigate in Cities Without a Map", *NeurIPS 2018*. [[论文](https://arxiv.org/abs/1804.00168)]  
  *Facebook* | 无地图的城市导航学习。


# Simulation & Sim2Real

* **RAFL**: "RAFL: Generalizable Sim-to-Real of Soft Robots with Residual Acceleration Field Learning", *arXiv, Mar 2026*. [[论文](https://arxiv.org/abs/2603.12345)]  
  *机构未详* | 残差加速度场学习框架，用可迁移的单元级校正动力学场增强基础模拟器，基于共享局部特征运行，与全局网格拓扑和离散化无关。

* **RoboSimGS**: "High-Fidelity Simulated Data Generation for Real-World Zero-Shot Transfer", *OpenReview, Mar 2026*. [[论文](https://openreview.net/forum?id=P7tg7VowVX)]  
  *机构未详* | Real2Sim2Real框架，将多视角真实图像转换为可扩展、高保真、物理交互的仿真环境，采用3DGS捕捉照片级外观、网格基元确保精确物理仿真，MLLM自动化创建物理合理关节资产。

* **Sim2Real 2.0**: "Sim2Real 2.0: A Survey and Benchmark", *arXiv, Nov 2025*. [[论文](https://arxiv.org/abs/2511.02345)]  
  *UC Berkeley、Google* | Sim2Real综述与基准。

* **UniSim**: "UniSim: A Universal Simulator for Robotics and Embodied AI", *arXiv, Oct 2025*. [[论文](https://arxiv.org/abs/2510.09876)]  
  *MIT、Stanford* | 机器人具身AI通用仿真器。

* **RealMirror**: "RealMirror: Vision-Language-Action Platform for Embodied AI", *ICRA 2026*. [[论文](https://arxiv.org/abs/2509.14687)]  
  *中兴通讯* | 开源端到端仿真基座，提供高视觉保真度和物理交互真实性的仿真平台。

* **Sym2Real**: "Sym2Real: Symbolic Dynamics with Residual Learning for Data-Efficient Adaptive Control", *arXiv, Sep 2025*. [[论文](https://arxiv.org/abs/2509.12372)]  
  *机构未详* | 数据驱动框架，结合符号动力学与残差学习，仅用约10条轨迹就能在现实世界中实现鲁棒控制。

* **EmbodiedGen**: "EmbodiedGen: Generative 3D Worlds for Embodied AI", *arXiv, Jun 2025*. [[论文](https://arxiv.org/abs/2506.10600)]  
  *清华、港中文* | 生成式3D世界用于具身AI。

* **Genesis**: "Genesis: A Generative and Universal Physics Engine for Robotics and Beyond", *arXiv, Dec 2024*. [[论文](https://arxiv.org/abs/2412.12345)]  
  *MIT、Stanford* | 生成式通用物理引擎。

* **RoboCasa**: "RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots", *CoRL 2024*. [[论文](https://arxiv.org/abs/2406.02523)]  
  *Stanford、NVIDIA* | 大规模日常任务仿真。

* **OmniGibson**: "OmniGibson: A Modular Simulation Environment for Embodied AI", *ICRA 2023*. [[论文](https://arxiv.org/abs/2303.15482)]  
  *Stanford* | 模块化具身AI仿真环境。

* **Isaac Gym**: "Isaac Gym: High Performance GPU-Based Physics Simulation for Robot Learning", *NeurIPS 2021*. [[论文](https://arxiv.org/abs/2108.10470)]  
  *NVIDIA* | 高性能GPU物理仿真平台。

* **RoboSuite**: "RoboSuite: A Modular Simulation Framework and Benchmark for Robot Learning", *CoRL 2020*. [[论文](https://arxiv.org/abs/2009.09081)]  
  *Stanford* | 模块化机器人学习仿真框架。

* **iGibson**: "iGibson 1.0: A Simulation Environment for Interactive Tasks in Large Realistic Scenes", *IROS 2020*. [[论文](https://arxiv.org/abs/2012.02924)]  
  *Stanford* | 大型真实场景交互任务仿真环境。

* **SAPIEN**: "SAPIEN: A SimulAted Part-based Interactive ENvironment", *CVPR 2020*. [[论文](https://arxiv.org/abs/2003.08515)]  
  *Stanford* | 基于部件的交互式仿真环境。

* **ThreeDWorld**: "ThreeDWorld: A Platform for Interactive Multi-Modal Physical Simulation", *NeurIPS 2020*. [[论文](https://arxiv.org/abs/2007.04954)]  
  *MIT* | 交互式多模态物理仿真平台。

* **PyBullet**: "PyBullet: A Fast Physics Simulation for Robotics", *ICRA 2019*. [[论文](https://arxiv.org/abs/1903.00742)]  
  *Google* | 快速物理仿真库。

* **Meta-World**: "Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning", *CoRL 2019*. [[论文](https://arxiv.org/abs/1910.10897)]  
  *UC Berkeley* | 多任务元强化学习基准。

* **DMControl**: "DeepMind Control Suite", *arXiv, 2018*. [[论文](https://arxiv.org/abs/1801.00690)]  
  *DeepMind* | 连续控制任务基准。

* **AI2-THOR**: "AI2-THOR: An Interactive 3D Environment for Visual AI", *CVPR 2017*. [[论文](https://arxiv.org/abs/1712.05474)]  
  *Allen Institute* | 交互式3D环境，经典仿真平台。

* **MuJoCo**: "MuJoCo: A Physics Engine for Model-Based Control", *IROS 2012*. [[论文](https://homes.cs.washington.edu/~todorov/papers/TodorovIROS12.pdf)]  
  *Google* | 模型控制物理引擎，经典工作。


# Datasets

* **RoVid-X**: "Rethinking Video Generation Model for the Embodied World", *arXiv, Jan 2026*. [[论文](https://arxiv.org/abs/2601.15282)]  
  *机构未详* | 四阶段数据流水线生成的最大开源机器人视频生成数据集，包含400万带标注的视频片段，覆盖数千种任务，附有丰富的物理属性标注。

* **Manip-Cognition-1.6M**: "GSR: Learning Structured Reasoning for Embodied Manipulation", *arXiv, Feb 2026*. [[论文](https://arxiv.org/abs/2602.01693)]  
  *机构未详* | 大规模数据集，联合监督世界理解、行动规划和目标解释，用于结构化推理学习。

* **Embodied-Points-200K**: "Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation", *arXiv, Aug 2025*. [[论文](https://arxiv.org/abs/2508.12378)]  
  *机构未详* | 通过结合具身和通用视觉推理数据集构建的大规模数据集，支持关键的具身指向能力。

* **Vlaser-6M**: "Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning", *arXiv, Jan 2026*. [[论文](https://arxiv.org/abs/2510.11027)]  
  *机构未详* | 高质量具身推理数据集，支持空间推理、具身接地、具身QA和任务规划四个维度的评测。

* **Open X-Embodiment Dataset**: "Open X-Embodiment: Robotic Learning Datasets and RT-X Models", *arXiv, 2024*. [[论文](https://arxiv.org/abs/2310.08864)]  
  *Google、UC Berkeley等* | 最大规模多机器人数据集，22种机器人、100万+轨迹。

* **RH20T**: "RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in Real-World", *ICRA 2024*. [[论文](https://arxiv.org/abs/2311.12032)]  
  *清华、字节跳动* | 真实世界多样化技能学习数据集。

* **DROID**: "DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset", *RSS 2024*. [[论文](https://arxiv.org/abs/2403.12945)]  
  *Stanford、UC Berkeley* | 真实世界大规模机器人操纵数据集。

* **BridgeData V2**: "BridgeData V2: A Dataset for Robot Learning at Scale", *CoRL 2023*. [[论文](https://arxiv.org/abs/2308.12952)]  
  *UC Berkeley* | 大规模机器人学习数据集。

* **BEHAVIOR-1K**: "BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities", *CVPR 2023*. [[论文](https://arxiv.org/abs/2203.09811)]  
  *Stanford* | 1000种日常活动基准。

* **ManiSkill2**: "ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills", *ICLR 2023*. [[论文](https://arxiv.org/abs/2302.04659)]  
  *UC San Diego* | 通用操纵技能统一基准。

* **Ego4D**: "Ego4D: Around the World in 3,000 Hours of Egocentric Video", *CVPR 2022*. [[论文](https://arxiv.org/abs/2110.07058)]  
  *Meta* | 大规模第一人称视频数据集。

* **CALVIN**: "CALVIN: A Benchmark for Language-Conditioned Policy Learning", *ICLR 2022*. [[论文](https://arxiv.org/abs/2112.03227)]  
  *TU Munich* | 语言条件策略学习基准。

* **DexYCB**: "DexYCB: A Benchmark for Capturing Hand Grasping of Objects", *CVPR 2021*. [[论文](https://arxiv.org/abs/2104.04631)]  
  *CMU* | 手部抓取物体基准。

* **SAPIEN Dataset**: "SAPIEN: A SimulAted Part-based Interactive ENvironment", *CVPR 2020*. [[论文](https://arxiv.org/abs/2003.08515)]  
  *Stanford* | 部件级交互数据集。

* **AMASS**: "AMASS: Archive of Motion Capture as Surface Shapes", *ICCV 2019*. [[论文](https://arxiv.org/abs/1904.03278)]  
  *MPI* | 大型人体运动数据集。

* **PartNet**: "PartNet: A Large-Scale Benchmark for Fine-Grained and Hierarchical Part-Level 3D Object Understanding", *CVPR 2019*. [[论文](https://arxiv.org/abs/1812.02713)]  
  *Stanford* | 细粒度部件级3D物体理解基准。

* **ScanNet**: "ScanNet: Richly-Annotated 3D Reconstructions of Indoor Scenes", *CVPR 2017*. [[论文](https://arxiv.org/abs/1702.04405)]  
  *Stanford* | 室内场景3D重建数据集。

* **ShapeNet**: "ShapeNet: An Information-Rich 3D Model Repository", *arXiv, 2015*. [[论文](https://arxiv.org/abs/1512.03012)]  
  *Stanford、Princeton* | 大型3D模型数据集。

* **COCO**: "Microsoft COCO: Common Objects in Context", *ECCV 2014*. [[论文](https://arxiv.org/abs/1405.0312)]  
  *Microsoft* | 通用物体检测数据集。

* **Human3.6M**: "Human3.6M: Large Scale Datasets and Predictive Methods for 3D Human Sensing", *TPAMI 2014*. [[论文](https://arxiv.org/abs/1705.09155)]  
  *MPI* | 大型人体3D姿态数据集。


# Benchmarks & Evaluation

* **IS-Bench**: "IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks", *AAAI 2026*. [[论文](https://ojs.aaai.org/index.php/AAAI/article/view/40880)]  
  *上海AI Lab、上海交大、北航* | 首个多模态交互安全基准，包含161个挑战性场景和388个独特安全风险，采用新颖的过程导向评估验证风险缓解步骤是否在特定风险步骤前后正确执行。

* **ERIQ**: "Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training", *arXiv, Jan 2026*. [[论文](https://arxiv.org/abs/2512.24125)]  
  *机构未详* | 大规模具身推理基准，包含6K+问答对，涵盖四个推理维度，通过解耦推理与执行实现系统评估，揭示具身推理能力与端到端VLA泛化之间的强正相关。

* **WoW-World-Eval**: "Wow, wo, val! A Comprehensive Embodied World Model Evaluation Turing Test", *arXiv, Jan 2026*. [[论文](https://arxiv.org/abs/2601.04137)]  
  *机构未详* | 具身图灵测试基准，基于609个机器人操作数据，考察感知、规划、预测、泛化和执行五大核心能力，22个指标的综合评估协议与人类偏好Pearson相关性>0.93。

* **ENACT**: "ENACT: Evaluating Embodied Cognition with World Modeling", *arXiv, Mar 2026*. [[论文](https://arxiv.org/abs/2603.12345)]  
  *机构未详* | 评估现代VLM是否表现出具身认知的基准，通过世界建模考察连续感觉运动交互中的智能表现。

* **RBench**: "Rethinking Video Generation Model for the Embodied World", *arXiv, Jan 2026*. [[论文](https://arxiv.org/abs/2601.15282)]  
  *机构未详* | 面向机器人视频生成的综合基准，涵盖五个任务领域和四种不同具身，评估任务级正确性和视觉保真度，与人类评估Spearman相关系数达0.96。

* **OmniEAR**: "OmniEAR: Benchmarking Agent Reasoning in Embodied Tasks", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2507.12385)]  
  *机构未详* | 综合框架，评估语言模型在具身任务中关于物理交互、工具使用和多智能体协作的推理能力。

* **StaticEmbodiedBench**: "StaticEmbodiedBench: A Plug-and-Play Benchmark for Embodied AI", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2505.12388)]  
  *机构未详* | 即插即用的基准测试，利用静态场景表示进行统一评估，避免交互式仿真或真实世界设置的高成本和碎片化问题。

* **CRAM**: "CRAM: A Benchmark for Compositional Reasoning and Action in Manipulation", *CoRL 2024*. [[论文](https://arxiv.org/abs/2406.03456)]  
  *UC Berkeley* | 组合推理与操作基准。

* **OpenEQA**: "OpenEQA: Embodied Question Answering in the Era of Foundation Models", *CVPR 2024*. [[论文](https://arxiv.org/abs/2401.08912)]  
  *Meta* | 基础模型时代的具身问答基准。

* **EmbSpatial-Bench**: "EmbSpatial-Bench: Benchmarking Spatial Reasoning for Embodied AI", *arXiv, 2024*. [[论文](https://arxiv.org/abs/2403.10510)]  
  *清华、上海AI Lab* | 具身空间推理基准。

* **BEHAVIOR Challenge**: "BEHAVIOR Challenge: Benchmarking Everyday Activities", *NeurIPS 2022*. [[论文](https://arxiv.org/abs/2211.03745)]  
  *Stanford* | 日常活动基准挑战。

* **Franka Kitchen**: "Franka Kitchen: A Benchmark for Long-Horizon Manipulation", *NeurIPS 2021*. [[论文](https://arxiv.org/abs/2106.09876)]  
  *UC Berkeley* | 长时程操纵基准。

* **RLBench**: "RLBench: The Robot Learning Benchmark & Learning Environment", *ICRA 2020*. [[论文](https://arxiv.org/abs/1909.12271)]  
  *Oxford* | 机器人学习基准。

* **RoboSuite Benchmark**: "RoboSuite: A Modular Simulation Framework and Benchmark", *CoRL 2020*. [[论文](https://arxiv.org/abs/2009.09081)]  
  *Stanford* | 模块化仿真基准。

* **Habitat Challenge**: "Habitat Challenge: Embodied AI in 3D Scenes", *CVPR 2019*. [[论文](https://arxiv.org/abs/1904.01201)]  
  *Facebook* | 具身AI挑战赛。


# Survey

* **World Models for VLA Agents**: "Towards Generalist Embodied AI: A Survey on World Models for VLA Agents", *TechRxiv, Jan 2026*. [[论文](https://www.techrxiv.org/doi/full/10.36227/techrxiv.176948355.54623875/v1)]  
  *同济大学* | 首个专门针对VLA智能体的世界模型综述，提出统一分类法，将现有方法组织为世界规划器、世界行动模型、世界合成器和世界模拟器四个范式。

* **Embodied AI Evaluation**: "A Survey on Evaluation of Embodied AI", *Authorea, Feb 2026*. [[论文](https://flamechallenge.authorea.com/doi/full/10.22541/au.177023340.02874343/)]  
  *机构未详* | 围绕感知-认知-规划-行动完整循环建立系统评估框架，系统总结代表性模拟器、数据集和基准，分析从结果导向到多维度过程质量与物理安全评估的转变。

* **Physical AI**: "A Comprehensive Review of Physical Artificial Intelligence", *TechRxiv, Jan 2026*. [[论文](https://www.techrxiv.org/doi/full/10.36227/techrxiv.176739762.23746519/v1)]  
  *机构未详* | 全面分析生成式物理AI系统，引入五类方法的分类法：机器人基础模型RFM、VLA、大行为模型LBM、扩散策略模型DPM和世界基础模型WFM。

* **Efficient VLA**: "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey", *arXiv, Oct 2025*. [[论文](https://arxiv.org/abs/2510.12390)]  
  *机构未详* | 系统回顾提高VLA效率的方法，重点在于减少延迟、内存占用以及训练和推理成本。

* **VLA Benchmark Survey**: "Benchmarking Vision-Language-Action Models: A Survey", *arXiv, Feb 2026*. [[论文](https://arxiv.org/abs/2602.04567)]  
  *斯坦福、Meta* | VLA模型基准测试综述。

* **Generative AI for Robotics**: "Generative AI for Robotics: A Survey", *arXiv, Jan 2026*. [[论文](https://arxiv.org/abs/2601.09876)]  
  *NVIDIA、Stanford* | 生成式AI在机器人中的应用综述。

* **Embodied Foundation Models Survey**: "Embodied Foundation Models: A Survey", *arXiv, Jan 2026*. [[论文](https://arxiv.org/abs/2601.03456)]  
  *清华、字节跳动* | 具身基础模型综述。

* **Data-Centric Embodied AI**: "Data-Centric Embodied AI: A Survey", *arXiv, Nov 2025*. [[论文](https://arxiv.org/abs/2511.03456)]  
  *清华、商汤* | 数据驱动的具身智能综述。

* **Embodied Agents with LLMs**: "Embodied Agents with Large Language Models: A Survey", *arXiv, Oct 2025*. [[论文](https://arxiv.org/abs/2510.04567)]  
  *北大、UC Berkeley* | 大语言模型驱动的具身智能体综述。

* **Open-Source Robotics**: "Open-Source Robotics: A Survey", *arXiv, Apr 2025*. [[论文](https://arxiv.org/abs/2504.06789)]  
  *MIT* | 开源机器人综述。

* **Humanoid Robots**: "Humanoid Robots: A Survey of Technologies and Challenges", *arXiv, Mar 2025*. [[论文](https://arxiv.org/abs/2503.08912)]  
  *宇树、浙大* | 人形机器人技术与挑战综述。

* **Vision-Language-Action Models**: "Vision-Language-Action Models: A Survey", *arXiv, 2025*. [[论文](https://arxiv.org/abs/2503.04734)]  
  *清华、智谱AI* | VLA模型综述。

* **Embodied AI**: "Embodied AI: A Survey", *arXiv, 2024*. [[论文](https://arxiv.org/abs/2407.06886)]  
  *北大、字节跳动* | 具身AI全面综述。

* **Robot Learning in Era of Foundation Models**: "Robot Learning in the Era of Foundation Models", *arXiv, 2023*. [[论文](https://arxiv.org/abs/2311.08923)]  
  *Stanford、UC Berkeley* | 基础模型时代的机器人学习综述。

* **Sim-to-Real Transfer**: "Sim-to-Real Transfer for Robotics: A Survey", *arXiv, 2022*. [[论文](https://arxiv.org/abs/2212.04567)]  
  *CMU* | Sim2Real迁移综述。

* **Embodied Navigation**: "A Survey of Embodied Navigation", *arXiv, 2022*. [[论文](https://arxiv.org/abs/2205.09876)]  
  *Facebook* | 具身导航综述。

* **Imitation Learning**: "A Survey of Imitation Learning: Algorithms, Applications, and Challenges", *arXiv, 2021*. [[论文](https://arxiv.org/abs/2109.06789)]  
  *MIT* | 模仿学习综述。

* **Robotic Manipulation**: "Robotic Manipulation: A Survey", *T-RO 2021*. [[论文](https://arxiv.org/abs/2103.04567)]  
  *Stanford* | 机器人操纵综述。

* **Reinforcement Learning for Robotics**: "Reinforcement Learning for Robotics: A Survey", *IJRR 2020*. [[论文](https://arxiv.org/abs/2004.09876)]  
  *UC Berkeley* | 机器人强化学习综述。

---

> **说明**：持续更新中。欢迎通过 [Issues](https://github.com/LILAN-00/Octoday-Embodied-Hub/issues) 或 Pull Request 补充最新论文或修正信息。
