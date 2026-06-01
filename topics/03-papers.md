## 📄Table Of Contents
- [Embodied Foundation Models](#embodied-foundation-models)
- [Manipulation & Teleoperation](#manipulation)
- [Locomotion](#locomotion)
- [Navigation & Spatial Intelligence](#navigation-spatial-intelligence)
- [Simulators & Sim2Real](#simulation-sim2real)
- [Datasets](#datasets)
- [Benchmarks & Evaluation](#benchmarks-evaluation)
- [Survey](#survey)
---
<a id="embodied-foundation-models" name="embodied-foundation-models"></a>

## Embodied Foundation Models

- **[arXiv 2026年5月](https://arxiv.org/abs/2605.15153)** Pelican-Unified 1.0: A Unified Embodied Intelligence Model for Understanding, Reasoning, Imagination and Action. 北京人形推出的首个按统一原则训练的具身基础模型，将理解、推理、想象和动作生成集成到单一架构，在WorldArena想象评测上排名第一。


- **[arXiv 2026年5月](https://arxiv.org/abs/2605.14211)** ASH: Agents that Self-Hone via Embodied Learning. 通过从自生成轨迹学习逆动力学模型，从未标注网络视频中提取监督，实现长时程具身学习的自改进智能体框架。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.10332)** EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents. 面向具身智能体的技能自进化框架，通过技能感知反思区分技能内容错误与执行失误，ALFWorld上达93.28%任务成功率。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13403)** RotVLA: Rotational Latent Action for Vision-Language-Action Model. 基于SO(n)旋转潜在动作的VLA框架，提供连续性、组合性和与真实动作动力学对齐的几何结构，仅1.7B参数在LIBERO达98.2%。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13382)** BlockVLA: Accelerating Autoregressive VLA via Block Diffusion Finetuning. 通过块扩散范式将AR骨干适配为高效离散扩散策略，块内并行去噪，在LIBERO和SimplerEnv上实现3.3倍推理加速。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13778)** Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs. 推测推理框架，引入轻量草稿模型和主模型并行验证，将平均任务级延迟降至19.1ms，实现3倍加速，真实传送带分拣验证。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13276)** D-VLA: A High-Concurrency Distributed Asynchronous Reinforcement Learning Framework for Vision-Language-Action Models. 高并发分布式异步RL框架，引入"平面解耦"隔离仿真与优化，四线程异步Swimlane流水线实现全并行，万亿参数规模保持线性加速。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13757)** FrameSkip: Learning from Fewer but More Informative Frames in VLA Training. 数据层帧选择框架，基于动作变化、视觉一致性和任务进度评分帧，仅保留20%帧即达76.15%宏平均成功率，大幅提升VLA训练效率。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13548)** AttenA+: Rectifying Action Inequality in Robotic Foundation Models. 速度驱动动作注意力优先处理运动学关键段，即插即用框架，OpenVLA-OFT提升至98.6%，Franka上验证鲁棒性。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13105)** What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models (PAIR-VLA). 通过不变性项和敏感性目标解决视觉偏移，ManiSkill3上pi_0.5平均提升16.62%，OpenVLA提升9.10%。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13119)** Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models (VLAs-as-Tools). 将长期任务分配给高层VLM和专用VLA工具族，引入工具对齐后训练，LIBERO-Long上pi_0.5提升4.8pp，RoboTwin提升23.1pp。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.00078)** Being-H0.7: A Latent World-Action Model from Egocentric Videos. 提出 Being-H0.7：一种来自第一人称视频的潜在世界-动作模型，在引入世界模型的同时将真实场景部署作为重要考量。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.00416)** Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies. 提出 Learning while Deploying：一个面向通用机器人策略的车队级强化学习框架。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.00321)** Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models. 研究 VLA 模型的可解释性，分析因果理解如何与模型泛化能力相关联。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.30056)** Sample-Efficient Diffusion-based Reinforcement Learning with Critic Guidance. 提出基于扩散模型的样本高效强化学习方法，结合Critic引导提升学习效率，在机器人控制任务中表现优异。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.30260)** How LoRA Remembers? A Parametric Memory Law for LLM Finetuning. 提出参数化记忆法则，量化LoRA在LLM微调中的记忆容量极限，为具身智能模型微调提供理论指导。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.30311)** Archon: A Unified Multimodal Model for Holistic Digital Human Generation. 提出Archon统一多模态模型，整合七种模态实现整体数字人生成，提出"模态内思考"方法逐步增强保真度和可控性。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.29488)** AnyMo: Scaling Any-Modality Conditional Motion Generation with Masked Modeling. 提出AnyMo统一多模态框架，结合残差FSQ运动分词器和可扩展掩码建模Transformer，支持任意模态组合的高质量运动合成。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.30350)** DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation. 提出DynaFLIP动力学感知多模态预训练框架，整合视觉、语言和动力学信息，提升机器人操作中的场景理解和动作执行能力。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.28548)** GEM: Generative Supervision Helps Embodied Intelligence. 提出GEM生成式监督具身视觉语言模型，将深度图生成任务整合到VLM预训练阶段，在模拟和真实环境评估中展现卓越的任务执行能力。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.30248)** GenClaw: Code-Driven Agentic Image Generation. 提出GenClaw代码驱动智能体图像生成范式，代理首先概念化，然后使用代码渲染视觉草图，最后用生成模型补充纹理，实现高度可控的视觉生成。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.28272)** EchoAvatar: Real-time Generative Avatar Animation from Audio Streams. 提出统一流式架构，从增量音频输入合成连续全身运动，支持语音和音乐的无缝泛化，通过工具调用接口实现LLM显式语义控制。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.30263)** minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models. 提出minWM全栈开源框架，将双向视频扩散模型转换为相机可控的少步自回归世界模型，支持实时低延迟推出。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.26933)** Diff-Tracking: Leveraging Text-to-Image Diffusion Models for Unsupervised Visual Object Tracking. 提出Diff-Tracking方法，利用预训练文本到图像扩散模型的丰富语义知识，通过交叉注意力机制实现无监督视觉目标跟踪。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21741)** Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training. 利用动作条件世界模型在闭环想象环境中对通用机器人策略进行失败导向后训练，把人类纠正从真实执行迁移到可复用的模型内修正流程.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.20627)** Occupancy Reward Shaping: Improving Credit Assignment for Offline Goal-Conditioned Reinforcement Learning. 离线目标条件强化学习的奖励塑形方法，从世界模型占据测度中提取时序几何结构，缓解稀疏奖励下的信用分配难题。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.20246)** Cortex 2.0: Grounding World Models in Real-World Industrial Deployment. 面向工业长时程操作的世界模型框架，从反应式控制转向“规划-执行”（plan-and-act），通过生成候选未来状态提升跨任务与跨本体执行稳定性.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.20100)** JoyAI-RA 0.1: A Foundation Model for Robotic Autonomy. 面向开放世界机器人自主性的VLA基础模型，通过多形态数据组织与跨本体训练缓解数据多样性不足和泛化困难.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.19683)** Mask World Model: Predicting What Matters for Robust Robot Policy Learning. 用于机器人策略学习的掩码世界模型，只预测与决策最相关的状态变化，提升世界模型训练效率与策略鲁棒性。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.07799)** Learning Without Losing Identity: Capability Evolution for Embodied Agents. 能力中心演化的具身智能体新范式，引入模块化能力模块实现连续学习，在20次迭代中将任务成功率从32.4%提升至91.3%，零策略漂移.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.07430)** HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents. 专为真实世界具身智能体设计的VLM系列模型，采用MoE架构，覆盖2B/32B两种规模，在22个基准上表现优异.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.27792)** MotuBrain: An Advanced World Action Model for Robot Control. 提出 MotuBrain：一种面向机器人控制的高级世界-动作模型，聚焦长时程任务，并结合异构数据提升任务成功率。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.08168)** ViVa: A Video-Generative Value Model for Robot Reinforcement Learning. 视频生成价值模型，利用预训练视频生成器的时空先验进行价值估计，在真实世界箱体组装任务中取得显著提升.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.24921)** libra-vla: achieving learning equilibrium via asynchronous coarse-to-fine dual-system. 提出 libra-vla：一种面向开放世界场景的异步粗到细双系统架构，用于实现学习平衡并提升鲁棒性。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.24622)** CF-VLA: Efficient Coarse-to-Fine Action Generation for Vision-Language-Action Policies. 面向 VLA 策略的高效粗到细动作生成方法，重点针对多步骤执行场景。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.24447)** Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment. 研究 VLA 模型在不同 XPU 平台上的部署特性，重点关注机器人端部署中的硬件约束、效率与加速问题。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.24182)** $M^2$-VLA: Boosting Vision-Language Models for Generalizable Manipulation via Layer Mixture and Meta-Skills. 通过层混合与元技能机制增强视觉-语言模型在可泛化操作任务中的表现。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.23272)** Modular Sensory Stream for Integrating Physical Feedback in Vision-Language-Action Models. 通过模块化感知流将物理反馈集成到 VLA 模型中，以更好支持触觉交互。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.23121)** Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training. 针对低数据VLA后训练中的“锁定”现象，提出保留视觉接地并结合测试时对比提示引导的方法，缓解模型对训练对象和空间目标的过拟合。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.23073)** RL Token: Bootstrapping Online RL with Vision-Language-Action Models. 提出 RL Token：一种利用 VLA 模型引导在线强化学习启动的方法，通过稀疏空间锚点约束动作生成。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21391)** From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges. 提出ResVLA残差桥接架构，在高层语义理解与低层物理控制之间建立显式过渡，提升生成式VLA的条件对齐与表示效率.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21241)** CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors. 为生成式动作头引入稀疏空间锚点与显式容差走廊，用可解释的物理约束提升VLA策略的动作对齐与成功率。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21232)** ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures. 面向多步骤VLA执行的层次化预测纠错框架，通过前瞻式对齐与规划减轻中间步骤错误带来的级联失误.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.20834)** PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance. 面向轻量部署的小型VLA模型，通过世界知识引导增强参数受限条件下的高层理解、空间感知与操作能力.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.20012)** EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training. 通过mid-training在VLM与VLA之间建立具身过渡阶段，缓解数据分布落差并提升下游动作建模效果.
- **[CVPR 2026年4月](https://arxiv.org/abs/2604.07774)** RoboAgent: Chaining Basic Capabilities for Embodied Task Planning. 面向具身任务规划的VLM能力链框架，将复杂规划分解为基本视觉-语言问题的序列，实现更透明可控的推理过程.
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.00376)** NeuroHex: A Brain-Inspired Hex Coordinate System to Enable Highly Computationally-Efficient World Models for Continuous Online-Adaptive Learning. 提出 NeuroHex：一种受大脑启发的六边形坐标系统与层次化世界建模方法，用于实现面向持续在线自适应学习的高计算效率世界模型。
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.29844)** DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA. 提出 DIAL：一种面向端到端 VLA 的潜在世界建模方法，通过解耦意图与动作来增强真实世界部署能力与泛化性。
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.27670)** ProgressVLA: Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation. 进度引导的扩散策略VLA，通过预训练进度估计器和可微分进度引导实现长程任务中的进度感知.
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.20711)** RoboECC: Multi-Factor-Aware Edge-Cloud Collaborative Deployment for VLA Models. 面向VLA模型的边云协同部署框架，通过模型-硬件协同切分与网络感知调整，在带宽波动下兼顾实时性与推理性能。
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.17573)** HeiSD: Hybrid Speculative Decoding for Embodied Vision-Language-Action Models with Kinematic Awareness. 提出 HeiSD：一种面向具身 VLA 的运动学感知混合推测解码方法，旨在提升推理效率。
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.17192)** Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models. VLA模型内部机制的机械可解释性研究，揭示注意力头在编码指令遵循、物体交互和机器人控制等功能中的分工.
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.01581)** KERV: Kinematic-Rectified Speculative Decoding for Embodied VLA Models. 将机器人运动学引入VLA的推测解码过程，利用运动学预测与阈值校正减少重推理开销，在保持成功率的同时显著加速推理。
- **[arXiv 2026年2月](https://arxiv.org/abs/2602.14979)** RynnBrain: Open Embodied Foundation Models. 开源具身智能时空基础模型，在一个统一框架内集成了自我中心理解、时空定位、物理推理和物理感知规划四大核心能力.
- **[arXiv 2026年2月](https://arxiv.org/abs/2602.04315)** GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning. 知识引导轨迹规划的层次化VLA模型，无需真实机器人数据实现零样本操纵和自动数据生成.
- **[arXiv 2026年2月](https://arxiv.org/abs/2602.11075)** RISE: Self-Improving Robot Policy with Compositional World Model. 组合式世界模型驱动的自改进机器人策略框架，通过在模型内生成经验并迭代优化策略，提升具身任务中的泛化与适应能力。
- **[arXiv 2026年2月](https://arxiv.org/abs/2602.09971)** VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model. 将联合嵌入预测架构（JEPA）集成到VLA模型中，通过潜在空间预测世界动态，提升泛化能力和鲁棒性.
- **[arXiv 2026年1月](https://arxiv.org/abs/2601.12993)** Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization. 以人为中心的跨本体VLA基础模型，构建35,000小时跨30种本体的多模态数据集，实现LIBERO基准98.9%的成功率.
- **[arXiv 2026年1月](https://arxiv.org/abs/2601.18692)** A Pragmatic VLA Foundation Model. 文中模型名为 LingBot-VLA，基于约20,000小时真实世界数据和9种双机械臂配置训练，强调真实部署下的泛化能力与训练效率.
- **[arXiv 2026年1月](https://arxiv.org/abs/2601.04052)** Stable Language Guidance for Vision-Language-Action Models. 提出残差语义引导概率框架，将物理可供性与语义执行解耦，提升VLA模型的语言指导稳定性.
- **[arXiv 2025年11月](https://arxiv.org/abs/2511.18112)** EchoVLA: Vision-Language-Action Model with Synergistic Declarative Memory. 结合声明式记忆的VLA模型，通过外部记忆模块缓解长程任务中的遗忘问题，提升多步骤任务执行能力.
- **[arXiv 2025年11月](https://arxiv.org/abs/2511.17502)** RynnVLA-002: A Unified Vision-Language-Action and World Model. 统一VLA与世界模型的框架，世界模型利用动作和视觉输入预测未来图像状态，学习环境物理以细化动作生成.
- **[arXiv 2025年11月](https://arxiv.org/abs/2511.01718)** Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process. 通过联合离散去噪扩散过程统一理解、生成和行动的VLA模型.
- **[arXiv 2025年10月](https://arxiv.org/abs/2510.10274)** X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task. 软提示驱动的机器人基础模型，通过参数高效微调实现任意机器人、任意任务的泛化.
- **[arXiv 2025年10月](https://arxiv.org/abs/2510.07778)** IntentionVLA: Embodied Intention Reasoning for Human-Robot Interaction. 具身意图推理的VLA模型，通过意图理解增强人机协作的流畅性和安全性.
- **[arXiv 2025年10月](https://arxiv.org/abs/2510.25122)** NanoVLA: Routing Decoupled Vision-Language Understanding for Nano-sized Generalist Robotic Policies. 轻量化VLA架构，通过视觉-语言解耦和动态路由实现高达52倍边缘设备推理加速，参数减少98%.
- **[arXiv 2025年10月](https://arxiv.org/abs/2510.12710)** Reflection-Based Task Adaptation for Self-Improving VLA. 通过失败驱动的反思性RL和成功驱动的质量引导SFT双路径架构，实现VLA模型的快速自主任务自适应.
- **[arXiv 2025年10月](https://arxiv.org/abs/2510.01623)** VLA-R1: Enhancing Reasoning in Vision-Language-Action Models. 通过RLVR和GRPO系统优化推理与执行的推理增强VLA，并发布VLA-CoT-13K思维链监督数据集.
- **[arXiv 2025年9月](https://arxiv.org/abs/2509.12345)** FoMER: How Good are Foundation Models in Step-by-Step Embodied Reasoning. 提出FoMER基准，专门评估大语言模型在复杂具身决策场景中的逐步推理能力.
- **[arXiv 2025年9月](https://arxiv.org/abs/2509.11767)** WALL-OSS: Igniting VLMs toward the Embodied Space. 端到端具身基础模型，通过大规模多模态预训练实现具身感知、语言-动作关联和鲁棒操纵.
- **[NeurIPS 2025年9月](https://arxiv.org/abs/2509.08844)** EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models. 无训练推理加速框架，实现1.93倍加速和28.9%的FLOPs减少.
- **[ICLR 2025年9月](https://arxiv.org/abs/2509.09332)** OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning. 提出任务自适应的3D接地机制和具身感知推理框架，通过门控路由器根据上下文需求显式选择性调节3D融合，实现上下文感知的3D接地和具身约束感知的规划决策.
- **[arXiv 2025年7月](https://arxiv.org/abs/2507.01424)** TriVLA: A Triple-System Vision-Language-Action Model with Episodic World Modeling. 三系统VLA架构（感知-世界模型-行动），通过情景世界模型提升长期任务规划能力.
- **[arXiv 2025年7月](https://arxiv.org/abs/2507.08421)** SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models. 执行感知的任务切换VLA.
- **[arXiv 2025年6月](https://arxiv.org/abs/2506.00411)** LoHoVLA: Vision-Language-Action Model for Long-Horizon Embodied Tasks. 专为长时程具身任务设计的VLA模型，通过分层动作预测缓解复合任务的错误累积问题.
- **[arXiv 2025年6月](https://arxiv.org/abs/2506.04500)** Don't Do That. Guiding Embodied Systems through Large Language Model-based Constraint Generation. 提出STPR约束生成框架，利用LLM将自然语言约束翻译为可执行的Python函数，应用于点云表示和传统搜索算法，确保机器人导航中的约束遵从.
- **[ICML 2025年5月](https://arxiv.org/abs/2505.06412)** DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression. 将自回归推理与扩散策略集成的框架，在102个未见物体上实现63.7%的零样本拾取准确率.
- **[arXiv 2025年5月](https://arxiv.org/abs/2505.03500)** VLAs are Confined yet Capable of Generalizing to Novel Instructions. 研究 VLA 模型如何在保持受约束行为边界的同时，仍能泛化到新指令，并在统一设置下进行评估。
- **[arXiv 2025年3月](https://arxiv.org/abs/2503.12438)** ChatVLA: Multimodal Understanding and Robot Control. 对话式多模态理解与机器人控制.
- **[arXiv 2025年3月](https://arxiv.org/abs/2503.04123)** SmolVLA: Efficient Vision-Language-Action Models for Robotics. 轻量化VLA模型，适合边缘部署.
- **[arXiv 2025年1月](https://arxiv.org/abs/2501.12345)** HPT: Hierarchical Pre-trained Transformer for Robot Learning. 分层预训练Transformer架构，通过层次化表征学习实现跨任务的高效迁移学习.
- **[CVPR 2025年1月](https://arxiv.org/abs/2501.10105)** UniAct: Universal Actions for Enhanced Embodied Foundation Models. 提出通用动作空间，将不同形态机器人的底层控制统一为规范化的动作表征，提升基础模型在不同机器人平台间的泛化能力.
- **[arXiv 2025年1月](https://arxiv.org/abs/2501.08132)** HiMoE-VLA: Hierarchical Mixture-of-Experts for Vision-Language-Action Policies. 分层混合专家VLA架构.
- **[arXiv 2024年10月](https://arxiv.org/abs/2410.24164)** π0: A Vision-Language-Action Flow Model for General Robot Control. 基于预训练VLM的流匹配架构，在多机器人平台多样化数据集上训练，实现零样本任务执行.
- **[arXiv 2024年6月](https://arxiv.org/abs/2406.09246)** OpenVLA: An Open Vision-Language-Action Model. 开源的VLA模型，基于7B参数的Llama 2和DINOv2视觉编码器，支持即插即用和参数高效微调.
- **[arXiv 2024年6月](https://arxiv.org/abs/2406.06833)** RoboMatrix: Skill-Centric Robot Task Planning. 以技能为中心的机器人任务规划框架.
- **[arXiv 2024年5月](https://arxiv.org/abs/2405.12213)** Octo: An Open-Source Generalist Robot Policy. 开源通用机器人策略，在Open X-Embodiment数据集的80万条轨迹上训练，支持语言指令和目标图像双模态条件.
- **[CoRL 2024年5月](https://arxiv.org/abs/2405.16789)** MC-Skill: Multi-Context Skill Learning for Vision-Language-Action. 多上下文技能学习的VLA框架，支持复杂场景泛化.
- **[arXiv 2024年2月](https://arxiv.org/abs/2402.06149)** GR-2: A Generative Video-Language-Action Model for Robot Manipulation. 生成式视频-语言-动作模型，通过大规模视频预训练学习通用视觉表征，再微调到机器人操控任务.
- **[arXiv 2024年1月](https://arxiv.org/abs/2401.12963)** AutoRT: Embodied Foundation Models for Large-Scale Robot Orchestration. 利用基础模型进行大规模机器人编排的系统，结合LLM任务分解和VLM环境理解，在多个机器人上并行收集数据.
- **[arXiv 2023年11月](https://arxiv.org/abs/2311.01355)** RoboFlamingo: A Vision-Language Model for Open-Vocabulary Robot Control. 基于Flamingo的开源VLA模型，通过视觉-语言模型微调实现开放词汇的机器人控制，支持少样本学习.
- **[arXiv 2023年7月](https://arxiv.org/abs/2307.15818)** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. 首个正式提出VLA概念的模型，将视觉-语言模型（PaLI-X/PaLM-E）微调为VLA，使机器人能够从互联网规模的知识中受益.
- **[arXiv 2023年7月](https://arxiv.org/abs/2307.05973)** VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models. 利用LLM和VLM构建3D值图供运动规划器使用，实现零样本机器人操作轨迹合成，无需额外训练.
- **[CoRL 2023年7月](https://arxiv.org/abs/2307.06135)** SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning. 利用3D场景图提升大语言模型的机器人任务规划能力.
- **[arXiv 2023年6月](https://arxiv.org/abs/2306.11706)** RoboCat: A Self-Improving Foundation Agent for Robotic Manipulation. 能够自我改进的机器人基础模型，通过数据聚合和微调在新任务上生成新数据，形成自我提升循环.
- **[arXiv 2023年5月](https://arxiv.org/abs/2305.16291)** Voyager: An Open-Ended Embodied Agent with Large Language Models. 开放世界具身智能体的LLM驱动框架.
- **[arXiv 2023年3月](https://arxiv.org/abs/2303.03378)** PaLM-E: An Embodied Multimodal Language Model. 将真实世界传感器数据（图像、状态估计）与语言模型融合的具身多模态语言模型，实现具身推理与长期规划.
- **[ICRA 2023年3月](https://arxiv.org/abs/2303.08734)** PromptCraft: Zero-Shot Task Planning with Large Language Models. 零样本任务规划的提示工程框架.
- **[arXiv 2022年12月](https://arxiv.org/abs/2212.06817)** RT-1: Robotics Transformer for Real-World Control at Scale. 首个大规模机器人Transformer模型，在13个任务、13万条演示上训练，实现了高成功率和新任务的零样本泛化.
- **[ICLR 2022年12月](https://arxiv.org/abs/2212.04088)** LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models. 少样本具身规划的LLM方法.
- **[ICLR 2022年10月](https://arxiv.org/abs/2210.03629)** ReAct: Synergizing Reasoning and Acting in Language Models. 语言模型中推理与行动协同的框架.
- **[NeurIPS 2022年10月](https://arxiv.org/abs/2210.03094)** VIMA: General Robot Manipulation with Multimodal Prompts. 多模态提示的通用机器人操纵模型.
- **[CoRL 2022年9月](https://arxiv.org/abs/2209.07753)** Code as Policies: Language Model Programs for Embodied Control. 将语言模型生成的代码作为机器人控制策略.
- **[CoRL 2022年7月](https://arxiv.org/abs/2207.05608)** Inner Monologue: Embodied Reasoning through Planning with Language Models. 语言模型辅助的具身推理与规划框架.
- **[arXiv 2022年5月](https://arxiv.org/abs/2205.06175)** GATO: A Generalist Agent. 单一Transformer模型同时处理600+任务，涵盖机器人控制、游戏、对话等，首次展示了通用智能体的可能性.
- **[CoRL 2022年4月](https://arxiv.org/abs/2204.01691)** SayCan: Do As I Can, Not As I Say: Grounding Language in Robotic Affordances. 将语言模型与机器人能力结合，实现自然语言指令执行.
- **[CoRL 2022年3月](https://arxiv.org/abs/2203.12601)** R3M: A Universal Visual Representation for Robot Manipulation. 通用机器人视觉表示，通过Ego4D大规模人类视频预训练，可迁移到多种下游机器人操控任务.

<a id="manipulation" name="manipulation"></a>
## Manipulation & Teleoperation

- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13452)** CUBic: Coordinated Unified Bimanual Perception and Control Framework. 统一双手感知控制框架，学习共享token化表示桥接感知和控制，独立性与协调性从结构中涌现，真实世界Agibot双臂验证。

- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13117)** SECOND-Grasp: Semantic Contact-guided Dexterous Grasping. 统一灵巧抓取框架，基于VLM语义推理生成粗略接触提议，语义几何一致性细化，DexGraspNet上已见/未见类别分别达98.2%/97.7%。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13632)** Guide, Think, Act: Interactive Embodied Reasoning in Vision-Language-Action Models (GTA-VLA). 交互式VLA框架，用户通过视觉线索引导策略，模型生成空间视觉思维链，SimplerEnv WidowX达81.2%成功率，单次视觉交互显著提升OOD性能。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.00475)** MSACT: Multistage Spatial Alignment for Stable Low-Latency Fine Manipulation. 提出 MSACT：一种面向稳定低延迟精细操作的多阶段空间对齐方法，并特别关注双臂协作与扩散式建模。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.00471)** Stereo Multistage Spatial Attention for Real-Time Mobile Manipulation Under Visual Scale Variation and Disturbances. 一种面向实时移动操作的视觉-语言-动作方法，针对尺度变化与干扰场景，围绕层次化空间注意力设计以增强鲁棒性。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.00438)** thinking in text and images: interleaved vision--language reasoning traces for long-horizon robot manipulation. 一种面向长时程机器人操作的 VLA 风格方法，通过交错文本与视觉推理痕迹来提升规划与执行能力。
- **[ICML 2026年5月](https://arxiv.org/abs/2605.29937)** Fisher-Preserving Guidance: Training-Free Manifold Constraints for Safe Diffusion Control. 提出无需训练的Fisher保持引导方法，通过流形约束实现安全的扩散模型控制，适用于机器人运动规划。
- **[ICRA 2026年5月](https://arxiv.org/abs/2605.29298)** MonoDuo: Using One Robot Arm to Learn Bimanual Policies. 提出MonoDuo方法，通过单臂操作数据学习双臂协作策略，降低双臂机器人数据收集成本。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.26478)** Learning from Demonstrations. 研究机器人从示范中学习的方法，探讨模仿学习、行为克隆等技术在机器人操作中的应用，分析样本效率和泛化能力。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.30226)** BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models. 提出BORA方法，结合离线强化学习和在线残差适应，实现真实世界灵巧视觉-语言-动作模型的高效训练。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.29564)** VE2VF: Vision-Enabled to Vision-Free Distillation via Real-world Reinforcement Learning. 提出VE2VF方法，通过真实世界强化学习将视觉依赖策略蒸馏为视觉无关策略，实现鲁棒的接触丰富操作。
- **[ICML 2026年5月](https://arxiv.org/abs/2605.27095)** FA-OPD: Adversarial Dual On-Policy Distillation from Expressive Flow-based Teacher. 提出FA-OPD对抗双重在线策略蒸馏方法，流匹配教师与轻量MLP学生协同训练，在六个机器人基准上超越强基线。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.26848)** starry: spatial-temporal action-centric world modeling for robotic manipulation. 提出 starry：一种面向机器人操作的动作中心时空世界建模方法，重点关注双臂协作与任务成功率提升。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.05320)** ExpressMM: Expressive Mobile Manipulation Behaviors in Human-Robot Interactions. 面向人机交互的富表达移动操作行为框架，把动作执行与社会表达结合起来提升交互自然性与可理解性。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21924)** Long-Horizon Manipulation via Trace-Conditioned VLA Planning. LoHo-Manip框架通过视觉轨迹提示与任务管理VLM，将长时程操作拆解为可恢复的局部执行与滚动式重规划.
- **[ICRA 2026年4月](https://arxiv.org/abs/2604.21914)** VistaBot: View-Robust Robot Manipulation via Spatiotemporal-Aware View Synthesis. 结合前馈几何估计与视频扩散模型，实现无需测试时相机标定的视角鲁棒闭环操作，并提出跨视角泛化评测指标.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.20348)** Bimanual Robot Manipulation via Multi-Agent In-Context Learning. 利用多智能体in-context learning协调双臂高维动作空间，在复杂双手任务中提升协同决策与动作生成能力.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.20347)** A Vision-Language-Action Model for Adaptive Ultrasound-Guided Needle Insertion and Needle Tracking. 将VLA用于自适应超声引导下的穿刺与针体跟踪，把视觉理解、动作决策与医疗机器人控制结合起来。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.19509)** Assessing VLM-Driven Semantic-Affordance Inference for Non-Humanoid Robot Morphologies. 研究VLM在非人形机器人形态上的语义可供性推断能力，揭示在工具使用和非常规操作场景下存在偏保守与高假阴性问题.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.24681)** Learning Human-Intention Priors from Large-Scale Human Demonstrations for Robotic Manipulation. 一种层次化操作方法，从大规模人类示范中学习人类意图先验，以提升机器人操作的鲁棒性。
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.10158)** XL-VLA: Cross-Hand Latent Representation for Vision-Language-Action Models. 跨手隐式表示的VLA框架，在不同灵巧手之间共享统一的隐式动作空间，实现跨本体的灵巧操纵训练.
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.00110)** Learning Physics from Pretrained Video Models: A Multimodal Continuous and Sequential World Interaction Models for Robotic Manipulation. 利用预训练视频模型学习连续与序列物理交互，构建服务机器人操作的多模态世界交互模型。
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.17834)** Generative Control as Optimization: Time Unconditional Flow Matching for Adaptive and Robust Robotic Control. 将流匹配控制从固定步轨迹积分改为自适应优化过程，并利用速度场范数作为无训练的安全与分布外信号，提升控制效率与鲁棒性。
- **[arXiv 2026年1月](https://arxiv.org/abs/2601.21251)** SMP: Abstracting Robot Manipulation Skills via Mixture-of-Experts Diffusion Policies. Skill MoE Policy，学习紧凑正交技能基，使用粘性路由在每一步从小的任务相关专家子集组合动作，变分训练目标支持设计，自适应专家激活实现快速采样.
- **[AAAI 2026年1月](https://arxiv.org/abs/2601.01948)** SDP: Learning Diffusion Policy from Primitive Skills for Robot Manipulation. 技能条件扩散策略SDP，将可解释的技能学习与条件行动规划相结合，抽象出跨任务的八个可复用原始技能，采用VLM提取离散表示，轻量路由网络为每个状态分配期望的原始技能.
- **[ICRA 2025年6月](https://arxiv.org/abs/2506.20668)** DemoDiffusion: One-Shot Human Imitation using pre-trained Diffusion Policy. 利用预训练的通用扩散策略对通过运动学重定向获得的轨迹进行修正，确保其既遵循人体运动又保持在合理机器人动作分布内，实现单次人类演示的机器人操作模仿.
- **[arXiv 2025年5月](https://arxiv.org/abs/2505.16413)** DexVLA: Plug-in Diffusion Experts for Vision-Language-Action Models. 扩散专家即插即用的VLA增强框架.
- **[arXiv 2025年4月](https://arxiv.org/abs/2504.05291)** ObjectVLA: Open-World Object Manipulation without Demonstrations. 无需演示的开放世界物体操纵VLA.
- **[arXiv 2025年1月](https://arxiv.org/abs/2501.05233)** VideoVLA: Video Generators as Generalizable Robot Manipulators. 利用视频生成模型实现通用机器人操纵.
- **[CoRL 2024年6月](https://arxiv.org/abs/2406.09288)** ManiWAV: Learning Robot Manipulation from In-the-Wild Audio-Visual Data. 从真实世界视听数据学习机器人操纵.
- **[RSS 2024年3月](https://arxiv.org/abs/2403.07788)** DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation. 可扩展、便携的灵巧操作动作捕捉系统.
- **[CoRL 2024年2月](https://arxiv.org/abs/2402.10329)** UMI: Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots. 通用操纵接口，无需真实机器人即可教授.
- **[CoRL 2023年7月](https://arxiv.org/abs/2307.16677)** AnyTeleop: A General Vision-Based Teleoperation System for Robotic Manipulation. 通用视觉遥操作系统.
- **[RSS 2023年4月](https://arxiv.org/abs/2304.13705)** ACT: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware. 低成本硬件的精细双手操作学习.
- **[RSS 2023年3月](https://arxiv.org/abs/2303.04137)** Diffusion Policy: Visuomotor Policy Learning via Action Diffusion. 基于扩散模型的机器人策略学习，在灵巧操作上表现优异.
- **[ICLR 2023年2月](https://arxiv.org/abs/2302.12422)** MimicPlay: Long-Horizon Imitation Learning by Watching Human Play. 通过观看人类玩游戏的长时间模仿学习.
- **[CoRL 2022年11月](https://arxiv.org/abs/2211.07636)** RVT: Robotic View Transformer for 3D Object Manipulation. 3D物体操纵的机器人视图Transformer.
- **[CoRL 2022年9月](https://arxiv.org/abs/2209.05451)** Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation. 语言条件的多任务机器人操纵 Transformer，通常也以 PerAct 名称被引用.
- **[ICRA 2022年3月](https://arxiv.org/abs/2203.08745)** C2F-ARM: Coarse-to-Fine Imitation Learning for Robot Manipulation. 粗到细的模仿学习框架.
- **[CoRL 2022年2月](https://arxiv.org/abs/2202.02005)** BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning. 零样本任务泛化的模仿学习方法，通过语言指令条件化，使机器人能在测试时执行训练中未见过的任务.
- **[CoRL 2021年9月](https://arxiv.org/abs/2109.12098)** CLIPort: What and Where Pathways for Robotic Manipulation. 结合CLIP视觉理解与端到端模仿学习的机器人操纵方法，实现开放词汇的物体操纵和泛化.
- **[ICRA 2021年3月](https://arxiv.org/abs/2103.02245)** Form2Fit: Learning Shape Priors for Generalizable Manipulation. 学习形状先验的通用操作.
- **[ICCV 2021年1月](https://arxiv.org/abs/2101.09555)** Where2Act: From Pixels to Actions for Articulated Objects. 从像素到动作的铰接物体操作.
- **[CVPR 2018年12月](https://arxiv.org/abs/1812.02713)** PartNet: A Large-Scale Benchmark for Fine-Grained and Hierarchical Part-Level 3D Object Understanding. 细粒度部件级3D物体理解基准.
<a id="locomotion" name="locomotion"></a>

## Locomotion

- **[arXiv 2026年5月](https://arxiv.org/abs/2605.14417)** Before the Body Moves: Learning Anticipatory Joint Intent for Language-Conditioned Humanoid Control (DAJI). 面向语言条件人形机器人控制的层次化框架，学习预期性联合意图表征，显式编码 upcoming 接触变化与平衡准备，实现稳定的全身动作生成。


- **[arXiv 2026年4月](https://arxiv.org/abs/2604.19734)** UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling. 统一人类到人形机器人的物理语言框架，通过视觉锚定的潜在动作分词器连接跨本体策略学习与世界建模.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.08509)** Visually-grounded Humanoid Agents. 一种面向人形智能体的视觉接地方法，关注具身智能能力。
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.17927)** RoboForge: Physically Optimized Text-guided Whole-Body Locomotion for Humanoids. 物理优化的人形机器人全身运动生成框架，通过PP-Opt模块双向联合优化运动生成和物理执行，实现文本到物理可行运动的端到端转换.
- **[arXiv 2025年4月](https://arxiv.org/abs/2504.09532)** Humanoid-COA: Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation. 首个将基础模型推理与具身动作链机制相结合的人形智能体框架，用于零样本移动操纵.
- **[arXiv 2025年2月](https://arxiv.org/abs/2502.09247)** Humanoid-VLA: Vision-Language-Action Models for Humanoid Control. 专为人形机器人设计的VLA模型.
<a id="navigation-spatial-intelligence" name="navigation-spatial-intelligence"></a>

## Navigation & Spatial Intelligence

- **[arXiv 2026年5月](https://arxiv.org/abs/2605.09387)** NEXUS: Continual Learning of Symbolic Constraints for Safe and Robust Embodied Planning. 面向安全鲁棒具身规划的符号约束持续学习框架。
<a id="simulation-sim2real" name="simulation-sim2real"></a>

- **[arXiv 2026年5月](https://arxiv.org/abs/2605.12624)** MindVLA-U1: VLA Beats VA with Unified Streaming Architecture for Autonomous Driving. 首个统一流式VLA自动驾驶架构，单次前向传播同时生成语言token和流匹配轨迹，在WOD-E2E上首次超越人类驾驶员(RFS 8.20 vs 8.13)。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.12622)** Action Emergence from Streaming Intent. 提出流式意图机制实现端到端自动驾驶中的动作涌现，VLA模型SI通过四步思维链解码意图token，驱动CFG引导流匹配动作头，首次在VLA中实现意图可控性。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.12625)** Driving Intents Amplify Planning-Oriented Reinforcement Learning (DIAL). 通过意图条件CFG扩展采样分布打破模式坍塌，结合多意图GRPO进行偏好RL，在WOD-E2E上RFS达9.14，首次超越人类演示和先前最佳。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.12735)** Toward a Blueprint for Generalizable Robot Autonomy (Unified Autonomy Stack). 开源统一自主栈，融合LiDAR/雷达/视觉/惯性感知，实现因子图定位、语义场景理解和多层安全导航，支持多种空中和地面机器人形态。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.12620)** VeGAS: Verifier-Guided Action Selection For Embodied Agents. 测试时框架，采样候选动作并用生成式验证器识别最可靠选择，LLM驱动的数据合成构建失败案例课程，在Habitat/ALFRED上最高提升36%相对性能。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13775)** RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data. VLM规划器和VGM模拟器耦合为共同进化循环，认知启发双阶段机制：白天探索+夜间巩固，仅500个无标签种子超越全监督基线(50倍数据减少)。
- **[ICRA 2026年5月](https://arxiv.org/abs/2605.29773)** Energy-Aware NECO for Single-Pass Pixel-wise Out-of-Distribution Detection in Semantic Segmentation. 提出能量感知的NECO方法，实现语义分割中的高效像素级分布外检测，提升机器人感知系统的鲁棒性。
- **[CVPR 2026年5月](https://arxiv.org/abs/2605.30342)** GAVIS: Uncertainty-driven 3D Gaussian Splatting Active Mapping via Anisotropic Visibility Field. 提出GAVIS框架，通过各向异性可见场实现3D高斯溅射的不确定性量化和主动建图，支持实时200FPS的不确定性量化。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.27952)** Con-DSO: Learning Short-Horizon Consistency Priors for RGB-D Direct Sparse Odometry. 提出一致性感知的RGB-D直接稀疏里程计框架，通过预测光度和深度几何一致性不确定性，在多个基准上实现20%-80%的轨迹误差降低。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.27178)** Domain Adaptation for Robot Vision. 研究机器人视觉中的域适应问题，提出改进的对抗学习和自监督方法，提升模型在新环境中的泛化能力。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.25832)** Visual-Inertial Odometry. 研究视觉惯性里程计技术，融合相机和IMU数据实现鲁棒的机器人定位，在挑战性环境下保持高精度。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.26949)** DinoComplete: 3D Shape Completion with Distilled Semantic Priors and State Space Models. 提出DinoComplete形状补全框架，利用DINO特征蒸馏的体素对齐语义先验，结合多尺度体素Mamba模块实现高效长程推理。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.24707)** Passage-Aware Structural Mapping for RGB-D Visual SLAM. 一种用于 RGB-D Visual SLAM 的导航与空间建图感知方法。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.22339)** flow4dgs-slam: optical flow-guided 4d gaussian splatting slam. 一种用于导航与建图的感知方法，通过光流引导的 4D Gaussian Splatting 实现更高效且更鲁棒的 SLAM。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21693)** SLAM as a Stochastic Control Problem with Partial Information: Optimal Solutions and Rigorous Approximations. 将主动SLAM重写为部分信息下的随机控制问题，并给出带探索代价的统一建模与严格近似分析.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21640)** Task-specific Subnetwork Discovery in Reinforcement Learning for Autonomous Underwater Navigation. 面向自主水下导航的多任务强化学习可解释框架，通过任务相关子网络发现提升策略适应性与内部决策可读性.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21363)** A Deployable Embodied Vision-Language Navigation System with Hierarchical Cognition and Context-Aware Exploration. 面向真实部署的VLN系统，通过分层认知与上下文感知探索在算力、时延和导航性能之间取得平衡.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.20305)** AdaTracker: Learning Adaptive In-Context Policy for Cross-Embodiment Active Visual Tracking. 面向跨本体主动视觉跟踪的自适应in-context策略学习框架，尝试用统一模型适配不同机器人形态下的物理约束与运动动态.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.22851)** EgoDyn-Bench: Evaluating Ego-Motion Understanding in Vision-Centric Foundation Models for Autonomous Driving. 提出 EgoDyn-Bench：一个用于评估自动驾驶中视觉中心基础模型自我运动理解能力的统一基准。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21453)** Instance-level Visual Active Tracking with Occlusion-Aware Planning. 面向遮挡场景的实例级主动视觉跟踪方法，把目标跟踪与遮挡感知规划结合起来提升持续跟踪稳定性。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.19536)** LiveVLN: Breaking the Stop-and-Go Loop in Vision-Language Navigation. 针对视觉语言导航中的停走式阻塞决策循环，引入更连续的感知-推理-执行机制，提升真实环境中的运动流畅性.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.08232)** HiRO-Nav: Hybrid ReasOning Enables Efficient Embodied Navigation. 首个基于动作熵自适应决定是否在每个步骤进行思考的导航智能体，通过混合监督微调冷启动和在线强化学习，仅在熵高的关键动作上激活显式推理.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.07973)** UrbanNav Benchmark: How Far Are Large Multimodal Models from Human-Level Spatial Action. 首个针对城市场景目标导向导航的具身空间动作基准，包含5037个高质量样本，强调3D垂直行动和丰富城市场景语义信息.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.07957)** WorldMAP: Bootstrapping Vision-Language Navigation Trajectory Prediction with Generative World Models. 教师-学生框架，世界模型驱动的教师从生成视频构建语义空间记忆，通过显式规划产生轨迹伪标签，轻量学生直接训练预测导航轨迹.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21894)** Task-Driven Co-Design of Heterogeneous Multi-Robot Systems. 面向异构多机器人系统的任务驱动协同设计框架，统一考虑机器人设计、编队组成、规划与执行之间的耦合权衡.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21707)** Effects of Swarm Size Variability on Operator Workload. 研究群体机器人规模动态变化对人类操作者负荷与表现的影响，为真实部署中的人群协同与任务分配提供依据.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21138)** Navigating the Clutter: Waypoint-Based Bi-Level Planning for Multi-Robot Systems. 面向拥挤环境多机器人控制的双层规划框架，通过路点表示和可行性反馈联合优化任务规划与运动规划。
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.28032)** CARLA-Air: Fly Drones Inside a CARLA World -- A Unified Infrastructure for Air-Ground Embodied Intelligence. 在CARLA中统一空地机器人仿真，支持无人机与地面智能体的协同训练、感知和评测。
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.16413)** OpenDriveVLA: Towards End-to-end Autonomous Driving with Large Vision Language Action Model. 面向自动驾驶的端到端VLA模型，将视觉-语言-动作统一建模，实现驾驶场景的感知-决策-控制一体化.
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.16947)** EmergeNav: Structured Embodied Inference for Zero-Shot Vision-and-Language Navigation in Continuous Environments. 结构化具身推理的零样本VLN-CE框架，无需训练实现37%的成功率.
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.14669)** RenderMem: Rendering as Spatial Memory Retrieval. 将渲染作为3D世界表示与空间推理之间接口的空间记忆框架，维护3D场景表示，通过从查询隐含的视点渲染场景来生成查询条件化的视觉证据.
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.09163)** SPAN-Nav: Generalized Spatial Awareness for Versatile Vision-Language Navigation. 端到端基础模型，通过占用预测任务从大规模室内外场景中提取空间先验，采用紧凑的单token表示封装粗粒度导航线索，利用CoT机制显式注入空间线索到动作推理.
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.06914)** SysNav: Multi-Level Systematic Cooperation Enables Real-World, Cross-Embodiment Object Navigation. 三层系统级对象导航框架，解耦语义推理、导航规划和运动控制，部署于轮式机器人、Unitree Go2四足和Unitree G1人形三种具身平台，190次真实实验验证.
- **[ICRA 2026年2月](https://arxiv.org/abs/2602.12345)** NavSpace: Spatial Intelligence Navigation Benchmark. 首个空间智能导航评测基准，涵盖六大类超1200条动态空间指令，将评估从静态感知推向持续推理.
- **[arXiv 2025年9月](https://arxiv.org/abs/2509.14000)** JaGuard: Position Error Correction of GNSS Jamming with Deep Temporal Graphs. 将GNSS干扰校正建模为动态图回归问题，利用深度时序图网络融合卫星几何与短时动态，修正固定接收机在干扰条件下的位置漂移。
- **[arXiv 2025年6月](https://arxiv.org/abs/2506.15518)** Real-Time Initialization of Unknown Anchors for UWB-aided Navigation. 面向UWB辅助导航的未知锚点实时初始化方法，在无需先验锚点布局的情况下提升定位可用性。
- **[arXiv 2025年5月](https://arxiv.org/abs/2505.08912)** CoW: Chain-of-Thought Walking for Embodied Navigation. 具身导航的思维链行走方法.
- **[arXiv 2025年4月](https://arxiv.org/abs/2504.08962)** TrackVLA: Embodied Visual Tracking with Vision-Language-Action Models. 具身视觉跟踪的VLA模型.
- **[arXiv 2025年1月](https://arxiv.org/abs/2501.07399)** Efficiently Closing Loops in LiDAR-Based SLAM Using Point Cloud Density Maps. 利用点云密度图高效完成激光SLAM回环检测与验证，在保证精度的同时降低计算开销。
- **[arXiv 2024年7月](https://arxiv.org/abs/2407.00848)** EgoExo++: Integrating On-demand Exocentric Visuals with 2.5D Ground Surface Estimation for Interactive Teleoperation of Underwater ROVs. 用于水下ROV交互遥操作的自我中心与外部视角融合框架，结合2.5D地面估计提升复杂水下环境感知与操控安全性。
- **[ICRA 2024年2月](https://arxiv.org/abs/2402.09466)** VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation. 零样本语义导航的视觉语言边界地图.
- **[CVPR 2024年1月](https://arxiv.org/abs/2401.04567)** EgoVLPv2: Egocentric Video-Language Pre-training. 第一人称视频-语言预训练.
- **[arXiv 2023年8月](https://arxiv.org/abs/2308.00513)** UVIO: An UWB-Aided Visual-Inertial Odometry Framework with Bias-Compensated Anchors Initialization. UWB辅助的视觉惯性里程计框架，通过偏置补偿的锚点初始化提升定位收敛速度与稳定性。
- **[AAAI 2023年5月](https://arxiv.org/abs/2305.16986)** NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models. 大语言模型在视觉-语言导航中的显式推理.
- **[RSS 2022年10月](https://arxiv.org/abs/2210.05663)** CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory. 弱监督语义场用于机器人记忆.
- **[CVPR 2022年3月](https://arxiv.org/abs/2203.06789)** PONI: Potential Functions for ObjectGoal Navigation with Interaction-free Learning. 无交互学习的物体目标导航势函数.
- **[ICCV 2021年4月](https://arxiv.org/abs/2104.03456)** SOON: Scenario Oriented Object Navigation. 场景导向的物体导航.
- **[ICRA 2021年3月](https://arxiv.org/abs/2103.07086)** ViNG: Learning Open-World Navigation with Visual Goal Representations. 视觉目标表示的开放世界导航.
- **[CoRL 2020年10月](https://arxiv.org/abs/2010.15044)** Semantic MapNet: Building Allocentric Semantic Maps and Representations. 异中心语义地图构建.
- **[ECCV 2020年7月](https://arxiv.org/abs/2007.00643)** ObjectNav: Object Goal Navigation using Goal-Oriented Semantic Exploration. 目标驱动的语义探索导航.
- **[CVPR 2020年6月](https://arxiv.org/abs/2006.13979)** VLN-BERT: A Recurrent BERT for Vision-and-Language Navigation. 视觉-语言导航的循环BERT模型.
- **[ICLR 2020年6月](https://arxiv.org/abs/2006.04884)** Active Neural SLAM. 主动神经SLAM框架.
- **[ICML 2019年6月](https://arxiv.org/abs/1906.09518)** Neural SLAM: Learning to Explore with External Memory. 神经SLAM，学习用外部记忆进行探索.
- **[NeurIPS 2018年4月](https://arxiv.org/abs/1804.00168)** PointNav: Learning to Navigate in Cities Without a Map. 无地图的城市导航学习.
- **[CVPR 2017年2月](https://arxiv.org/abs/1702.04405)** ScanNet: Richly-Annotated 3D Reconstructions of Indoor Scenes. 富标注的室内场景 3D 重建数据集.
<a id="simulation-sim2real" name="simulation-sim2real"></a>

## Simulators & Sim2Real
- **[Neutrosophic Sets and Systems 2026年5月](https://arxiv.org/abs/2605.26114)** MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research. 提出MobileGym平台，支持可验证的结果信号和大规模并行在线强化学习，在Sim-to-Real案例中实现95.1%的训练增益保持。

- **[arXiv 2026年5月](https://arxiv.org/abs/2605.13315)** Embodied Neurocomputation: A Framework for Interfacing Biological Neural Cultures with Scaled Task-Driven Validation. 面向生物神经培养与任务驱动验证的具身神经计算框架。


- **[arXiv 2026年5月](https://arxiv.org/abs/2605.14625)** Digital Twin Synchronization Over Mobile Embodied AI Network With Agentic Intelligence. 面向移动具身AI网络的数字孪生同步框架，通过智能体智能实现高保真虚拟表征与低信息年龄。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.12038)** OmniHumanoid: Streaming Cross-Embodiment Video Generation with Paired-Free Adaptation. 流式跨本体视频生成框架，无需配对数据即可适配不同机器人形态，支持连续视频生成。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.12654)** COSMIC: Concurrent Optimization of Structure, Material, and Integrated Control for robotic systems. 梯度共设计框架同时优化拓扑、材料分布和控制策略，嵌入混合拓扑变量到连续设计空间，在可微仿真器中集成神经网络控制器，发现超越分离设计的多样化运动策略。
- **[GECCO 2026年5月](https://arxiv.org/abs/2605.28812)** Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation. 提出基于压力中心的触觉表示方法，保留密集接触信息的同时保持sim-to-real迁移的鲁棒性，实现零样本真实机器人迁移。
- **[ICML 2026年5月](https://arxiv.org/abs/2605.29032)** Theoretical Foundations and Effective Algorithms for Policy-Aware Simulator Learning. 提出策略感知模拟器学习方法，将模拟器学习目标从预测准确性转向策略鲁棒性，通过零和博弈框架解决模拟器利用问题。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.28312)** Sim-to-Real Transfer for Robotic Manipulation. 研究机器人操作中的sim-to-real迁移问题，提出改进的域随机化和适应技术，提升仿真到真实环境的策略迁移效果。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.25459)** GS-Playground: A High-Throughput Photorealistic Simulator for Vision-Informed Robot Learning. 一个面向机器人操作与视觉知情学习的高吞吐量、照片级真实感仿真器。
- **[arXiv 2026年3月](https://arxiv.org/abs/2603.22039)** RAFL: Generalizable Sim-to-Real of Soft Robots with Residual Acceleration Field Learning. 残差加速度场学习框架，用可迁移的单元级校正动力学场增强基础模拟器，基于共享局部特征运行，与全局网格拓扑和离散化无关.
- **[arXiv 2025年11月](https://arxiv.org/abs/2511.02345)** Sim2Real 2.0: A Survey and Benchmark. Sim2Real综述与基准.
- **[arXiv 2025年10月](https://arxiv.org/abs/2510.09876)** UniSim: A Universal Simulator for Robotics and Embodied AI. 机器人具身AI通用仿真器.
- **[OpenReview 2025年10月](https://openreview.net/forum?id=P7tg7VowVX)** RoboSimGS: High-Fidelity Simulated Data Generation for Real-World Zero-Shot Transfer. Real2Sim2Real框架，将多视角真实图像转换为可扩展、高保真、物理交互的仿真环境，采用3DGS捕捉照片级外观、网格基元确保精确物理仿真，MLLM自动化创建物理合理关节资产.
- **[ICRA 2025年9月](https://arxiv.org/abs/2509.14687)** RealMirror: Vision-Language-Action Platform for Embodied AI. 开源端到端仿真基座，提供高视觉保真度和物理交互真实性的仿真平台.
- **[arXiv 2025年9月](https://arxiv.org/abs/2509.24948)** World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training. 利用世界模型构建低成本虚拟环境，为VLA后训练提供连续奖励与动作终止信号，在少样本机器人操作任务中替代高成本真实交互。
- **[arXiv 2025年9月](https://arxiv.org/abs/2509.12372)** Sym2Real: Symbolic Dynamics with Residual Learning for Data-Efficient Adaptive Control. 数据驱动框架，结合符号动力学与残差学习，仅用约10条轨迹就能在现实世界中实现鲁棒控制.
- **[arXiv 2025年6月](https://arxiv.org/abs/2506.10600)** EmbodiedGen: Generative 3D Worlds for Embodied AI. 生成式3D世界用于具身AI.
- **[arXiv 2024年12月](https://arxiv.org/abs/2412.12345)** Genesis: A Generative and Universal Physics Engine for Robotics and Beyond. 生成式通用物理引擎.
- **[CoRL 2024年6月](https://arxiv.org/abs/2406.02523)** RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots. 大规模日常任务仿真.
- **[ICRA 2023年3月](https://arxiv.org/abs/2303.15482)** OmniGibson: A Modular Simulation Environment for Embodied AI. 模块化具身AI仿真环境.
- **[NeurIPS 2021年8月](https://arxiv.org/abs/2108.10470)** Isaac Gym: High Performance GPU-Based Physics Simulation for Robot Learning. 高性能GPU物理仿真平台.
- **[IROS 2020年12月](https://arxiv.org/abs/2012.02924)** iGibson 1.0: A Simulation Environment for Interactive Tasks in Large Realistic Scenes. 大型真实场景交互任务仿真环境.
- **[CoRL 2020年9月](https://arxiv.org/abs/2009.12293)** robosuite: A Modular Simulation Framework and Benchmark for Robot Learning. 面向机器人学习的模块化仿真框架与基准套件.
- **[NeurIPS 2020年7月](https://arxiv.org/abs/2007.04954)** ThreeDWorld: A Platform for Interactive Multi-Modal Physical Simulation. 交互式多模态物理仿真平台.
- **[CVPR 2020年3月](https://arxiv.org/abs/2003.08515)** SAPIEN: A SimulAted Part-based Interactive ENvironment. 基于部件的交互式仿真环境.
- **[CoRL 2019年10月](https://arxiv.org/abs/1910.10897)** Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning. 多任务元强化学习基准.
- **[ICCV 2019年4月](https://arxiv.org/abs/1904.01201)** Habitat: A Platform for Embodied AI Research. 具身AI研究平台，包含仿真器和数据集.
- **[ICRA 2019年3月](https://arxiv.org/abs/1903.00742)** PyBullet: A Fast Physics Simulation for Robotics. 快速物理仿真库.
- **[arXiv 2018年1月](https://arxiv.org/abs/1801.00690)** DMControl: DeepMind Control Suite. 连续控制任务基准.
- **[CVPR 2017年12月](https://arxiv.org/abs/1712.05474)** AI2-THOR: An Interactive 3D Environment for Visual AI. 交互式3D环境，经典仿真平台.
- **[IROS 2012年10月](https://homes.cs.washington.edu/~todorov/papers/TodorovIROS12.pdf)** MuJoCo: A Physics Engine for Model-Based Control. 模型控制物理引擎，经典工作.

<a id="datasets" name="datasets"></a>

## Datasets

- **[arXiv 2026年5月](https://arxiv.org/abs/2605.29462)** CFMME: A Comprehensive Chinese Financial Multimodal Evaluation Dataset. 提出CFMME中文金融多模态评估基准，包含6052个实例覆盖八种金融图像模态，为具身智能金融应用提供评估工具。


- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21017)** Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics. 面向医疗机器人基础模型的大规模具身数据集，缓解医疗场景下数据小规模、单本体和难共享的问题.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.20444)** VTouch++: A Multimodal Dataset with Vision-Based Tactile Enhancement for Bimanual Manipulation. 融合视觉增强触觉信号的多模态双手操作数据集，为接触密集型双臂操控提供更高保真的物理交互监督.
- **[arXiv 2026年2月](https://arxiv.org/abs/2602.01693)** Manip-Cognition-1.6M: GSR: Learning Structured Reasoning for Embodied Manipulation. 大规模数据集，联合监督世界理解、行动规划和目标解释，用于结构化推理学习.
- **[arXiv 2025年10月](https://arxiv.org/abs/2510.11027)** Vlaser-6M: Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning. 高质量具身推理数据集，支持空间推理、具身接地、具身QA和任务规划四个维度的评测.
- **[arXiv 2025年8月](https://arxiv.org/abs/2508.12378)** Embodied-Points-200K: Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation. 通过结合具身和通用视觉推理数据集构建的大规模数据集，支持关键的具身指向能力.
- **[RSS 2024年3月](https://arxiv.org/abs/2403.12945)** DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset. 真实世界大规模机器人操纵数据集.
- **[ICRA 2023年11月](https://arxiv.org/abs/2311.12032)** RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in Real-World. 真实世界多样化技能学习数据集.
- **[arXiv 2023年10月](https://arxiv.org/abs/2310.08864)** Open X-Embodiment Dataset: Robotic Learning Datasets and RT-X Models. 最大规模多机器人数据集，22种机器人、100万+轨迹.
- **[CoRL 2023年8月](https://arxiv.org/abs/2308.12952)** BridgeData V2: A Dataset for Robot Learning at Scale. 大规模机器人学习数据集.
- **[CVPR 2021年10月](https://arxiv.org/abs/2110.07058)** Ego4D: Around the World in 3,000 Hours of Egocentric Video. 大规模第一人称视频数据集.
- **[NeurIPS 2021年9月](https://arxiv.org/abs/2109.08238)** HM3D: Habitat-Matterport 3D Dataset (HM3D): 1000 Large-scale 3D Environments for Embodied AI. 大规模3D环境数据集.
- **[ICRA 2020年3月](https://arxiv.org/abs/2003.06789)** GraspNet: A Large-Scale Cluttered Scene Dataset for Robotic Grasping. 大规模杂乱场景抓取数据集.
- **[ICCV 2019年4月](https://arxiv.org/abs/1904.03278)** AMASS: Archive of Motion Capture as Surface Shapes. 大型人体运动数据集.
- **[TPAMI 2017年5月](https://arxiv.org/abs/1705.09155)** Human3.6M: Large Scale Datasets and Predictive Methods for 3D Human Sensing. 大型人体3D姿态数据集.
<a id="benchmarks-evaluation" name="benchmarks-evaluation"></a>

## Benchmarks & Evaluation

- **[arXiv 2026年5月](https://arxiv.org/abs/2605.12674)** Revealing Interpretable Failure Modes of VLMs (REVELIO). 系统发现VLM可解释失效模式的框架，结合多样性感知束搜索和高斯过程Thompson采样，在自动驾驶和室内机器人中揭示SOTA VLM的未报告漏洞。


- **[arXiv 2026年5月](https://arxiv.org/abs/2605.00397)** MiniVLA-Nav v1: A Multi-Scene Simulation Dataset for Language-Conditioned Robot Navigation. 面向语言条件目标接近导航的多场景仿真数据集，提供RGB、深度、实例分割和专家动作标签，并包含同分布、模板改写与OOD类别等评测划分。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.27932)** When Think-with-Image Meets Safety: What Determines Multimodal Jailbreak Robustness? 研究多模态大模型的安全性，发现显式图像工具交互可将越狱成功率降低约30%，为具身智能安全提供新见解。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.28805)** OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration. 提出OmniVerifier-M1多模态元验证器，利用符号元验证和解耦强化学习实现细粒度错误定位，支持动态区域级自校正。
- **[arXiv 2026年5月](https://arxiv.org/abs/2605.30326)** RoboWits: Unexpected Challenges for Robotic Creative Problem Solving. 提出RoboWits双臂机器人基准测试，系统评估认知推理、创造性工具使用和应对意外条件的鲁棒性，为具身智能创造性问题解决提供新视角。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.24033)** Event-based SLAM Benchmark for High-Speed Maneuvers. 提出面向高速机动场景的事件相机SLAM基准EvSLAM，覆盖多平台、极端光照与复杂运动模式，并设计衡量系统极限能力的统一评测指标。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.23775)** Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms. 系统梳理VLA系统面临的安全威胁、开放挑战、评测方式与缓解机制，重点讨论长时程执行中的风险来源与安全保障路径。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21686)** WorldMark: A Unified Benchmark Suite for Interactive Video World Models. 统一评测交互式视频世界模型的基准套件，用于比较世界模型在预测、交互和可控生成上的能力。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.19133)** baltic: a benchmark and cross-domain strategy for 3d reconstruction across air and underwater domains under varying illumination. 构建跨空气与水下、不同照明条件的三维重建基准，并评估SfM、NeRF与3DGS在跨域场景中的几何精度和感知质量。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.17969)** E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes. 面向3D高斯场景主动感知的评测基准，专门测试视角相关任务中的探索、观察与决策能力。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.25161)** Capability-Oriented Failure Attribution for Vision-and-Language Navigation Agents. 一项面向视觉语言导航智能体的评估研究，从能力导向视角归因失败模式，并重点关注安全约束。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.24086)** AsyncShield: A Plug-and-Play Edge Adapter for Asynchronous Cloud-based VLA Navigation. 面向云端VLA导航的异步控制适配器，通过时空位姿缓冲和运动学映射修正延迟意图，并以约束MDP在目标跟踪与避障安全之间动态权衡。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21568)** A Bayesian Reasoning Framework for Robotic Systems in Autonomous Casualty Triage. 融合多种视觉算法输出与贝叶斯网络推理，在缺失或冲突感知输入下完成自动化伤员分诊与风险判断.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.21192)** How VLAs (Really) Work In Open-World Environments. 系统分析VLA在开放世界环境中的真实工作机制，重点观察其空间感知、任务分解与执行失效模式。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.20472)** Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models. 将时序差分校准引入VLA训练与评估，用于减轻长序列决策中的误差累积和价值偏移。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.20193)** LLM-Guided Safety Agent for Edge Robotics with an ISO-Compliant Perception-Compute-Control Architecture. 面向边缘机器人安全控制的ISO合规架构，将自然语言安全规范转为可执行谓词并部署到低时延闭环控制中.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.20151)** Toward Safe Autonomous Robotic Endovascular Interventions using World Models. 面向血管介入机器人的世界模型安全控制框架，提升在多样化患者解剖条件下的自主导航鲁棒性与长期稳定性.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.19638)** SafetyALFRED: Evaluating Safety-Conscious Planning of Multimodal Large Language Models. 在ALFRED基础上扩展六类厨房危险场景，评估多模态大模型在交互环境中是否会主动规避安全风险.
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.03956)** VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models. 面向具身基础模型的遗忘方法，研究如何安全移除VLA中的特定知识或行为能力，同时尽量保持整体性能。
- **[AAAI 2026年3月](https://ojs.aaai.org/index.php/AAAI/article/view/40880)** IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks. 首个多模态交互安全基准，包含161个挑战性场景和388个独特安全风险，采用新颖的过程导向评估验证风险缓解步骤是否在特定风险步骤前后正确执行.
- **[arXiv 2026年1月](https://arxiv.org/abs/2601.15282)** RBench: Rethinking Video Generation Model for the Embodied World. 面向机器人视频生成的综合基准，涵盖五个任务领域和四种不同具身，评估任务级正确性和视觉保真度，与人类评估Spearman相关系数达0.96.
- **[arXiv 2026年1月](https://arxiv.org/abs/2601.04137)** WoW-World-Eval: Wow, wo, val. A Comprehensive Embodied World Model Evaluation Turing Test. 具身图灵测试基准，基于609个机器人操作数据，考察感知、规划、预测、泛化和执行五大核心能力，22个指标的综合评估协议与人类偏好Pearson相关性>0.93.
- **[arXiv 2026年1月](https://arxiv.org/abs/2601.03136)** Limited Linguistic Diversity in Embodied AI Datasets. 分析具身 AI 数据集中语言多样性受限的问题及其对训练与评测的影响。
- **[arXiv 2025年12月](https://arxiv.org/abs/2512.24125)** ERIQ: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training. 大规模具身推理基准，包含6K+问答对，涵盖四个推理维度，通过解耦推理与执行实现系统评估，揭示具身推理能力与端到端VLA泛化之间的强正相关.
- **[arXiv 2025年11月](https://arxiv.org/abs/2511.20937)** ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric Interaction. 通过自我中心交互世界建模评估具身认知能力的基准，用重排任务考察动作效果推理、具身意识与长程记忆.
- **[arXiv 2025年7月](https://arxiv.org/abs/2507.12385)** OmniEAR: Benchmarking Agent Reasoning in Embodied Tasks. 综合框架，评估语言模型在具身任务中关于物理交互、工具使用和多智能体协作的推理能力.
- **[arXiv 2025年5月](https://arxiv.org/abs/2505.12388)** StaticEmbodiedBench: A Plug-and-Play Benchmark for Embodied AI. 即插即用的基准测试，利用静态场景表示进行统一评估，避免交互式仿真或真实世界设置的高成本和碎片化问题.
- **[arXiv 2025年2月](https://arxiv.org/abs/2502.07712)** SafeVLA: Safety Alignment for Vision-Language-Action Models. VLA模型的安全对齐方法.
- **[CoRL 2024年6月](https://arxiv.org/abs/2406.03456)** CRAM: A Benchmark for Compositional Reasoning and Action in Manipulation. 组合推理与操作基准.
- **[arXiv 2024年3月](https://arxiv.org/abs/2403.10510)** EmbSpatial-Bench: Benchmarking Spatial Reasoning for Embodied AI. 具身空间推理基准.
- **[CVPR 2024年1月](https://arxiv.org/abs/2401.08912)** OpenEQA: Embodied Question Answering in the Era of Foundation Models. 基础模型时代的具身问答基准.
- **[ICLR 2023年2月](https://arxiv.org/abs/2302.04659)** ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills. 通用操纵技能统一基准.
- **[NeurIPS 2022年11月](https://arxiv.org/abs/2211.03745)** BEHAVIOR Challenge: Benchmarking Everyday Activities. 日常活动基准挑战.
- **[CVPR 2022年3月](https://arxiv.org/abs/2203.09811)** BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities. 1000种日常活动基准.
- **[ICLR 2021年12月](https://arxiv.org/abs/2112.03227)** CALVIN: A Benchmark for Language-Conditioned Policy Learning. 语言条件策略学习基准.
- **[NeurIPS 2021年6月](https://arxiv.org/abs/2106.09876)** Franka Kitchen: A Benchmark for Long-Horizon Manipulation. 长时程操纵基准.
- **[CVPR 2021年4月](https://arxiv.org/abs/2104.04631)** DexYCB: A Benchmark for Capturing Hand Grasping of Objects. 手部抓取物体基准.
- **[ICRA 2019年9月](https://arxiv.org/abs/1909.12271)** RLBench: The Robot Learning Benchmark & Learning Environment. 机器人学习基准.
<a id="survey" name="survey"></a>

## Survey

- **[arXiv 2026年5月](https://arxiv.org/abs/2605.12090)** World Action Models: The Next Frontier in Embodied AI. 首个系统综述世界动作模型(WAM)的综述论文，提出将预测状态建模与动作生成统一的分类体系，涵盖级联式和联合式两大范式。


- **[arXiv 2026年5月](https://arxiv.org/abs/2605.27817)** Deep Learning for Robot Vision. 综述深度学习在机器人视觉中的应用，涵盖目标检测、语义分割、深度估计等关键任务，为具身智能感知提供系统参考。
- **[arXiv 2026年4月](https://arxiv.org/abs/2604.23001)** Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines. 一篇关于机器人 VLA 数据集、评测基准与数据引擎的综述，重点关注长时程任务。
- **[arXiv 2026年2月](https://arxiv.org/abs/2602.04567)** Benchmarking Vision-Language-Action Models: A Survey. VLA模型基准测试综述.
- **[Authorea 2026年2月](https://flamechallenge.authorea.com/doi/full/10.22541/au.177023340.02874343/)** Embodied AI Evaluation: A Survey on Evaluation of Embodied AI. 围绕感知-认知-规划-行动完整循环建立系统评估框架，系统总结代表性模拟器、数据集和基准，分析从结果导向到多维度过程质量与物理安全评估的转变.
- **[arXiv 2026年1月](https://arxiv.org/abs/2601.09876)** Generative AI for Robotics: A Survey. 生成式AI在机器人中的应用综述.
- **[arXiv 2026年1月](https://arxiv.org/abs/2601.03456)** Embodied Foundation Models Survey: Embodied Foundation Models: A Survey. 具身基础模型综述.
- **[TechRxiv 2026年1月](https://www.techrxiv.org/doi/full/10.36227/techrxiv.176948355.54623875/v1)** World Models for VLA Agents: Towards Generalist Embodied AI: A Survey on World Models for VLA Agents. 首个专门针对VLA智能体的世界模型综述，提出统一分类法，将现有方法组织为世界规划器、世界行动模型、世界合成器和世界模拟器四个范式.
- **[TechRxiv 2026年1月](https://www.techrxiv.org/doi/full/10.36227/techrxiv.176739762.23746519/v1)** Physical AI: A Comprehensive Review of Physical Artificial Intelligence. 全面分析生成式物理AI系统，引入五类方法的分类法：机器人基础模型RFM、VLA、大行为模型LBM、扩散策略模型DPM和世界基础模型WFM.
- **[arXiv 2025年11月](https://arxiv.org/abs/2511.03456)** Data-Centric Embodied AI: A Survey. 数据驱动的具身智能综述.
- **[arXiv 2025年10月](https://arxiv.org/abs/2510.12390)** Efficient VLA: Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey. 系统回顾提高VLA效率的方法，重点在于减少延迟、内存占用以及训练和推理成本.
- **[arXiv 2025年10月](https://arxiv.org/abs/2510.04567)** Embodied Agents with LLMs: A Survey. 大语言模型驱动的具身智能体综述.
- **[arXiv 2025年4月](https://arxiv.org/abs/2504.06789)** Open-Source Robotics: A Survey. 开源机器人综述.
- **[arXiv 2025年3月](https://arxiv.org/abs/2503.08912)** Humanoid Robots: A Survey of Technologies and Challenges. 人形机器人技术与挑战综述.
- **[arXiv 2025年3月](https://arxiv.org/abs/2503.04734)** Vision-Language-Action Models: A Survey. VLA模型综述.
- **[arXiv 2024年7月](https://arxiv.org/abs/2407.06886)** Embodied AI: A Survey. 具身AI全面综述.
- **[arXiv 2023年11月](https://arxiv.org/abs/2311.08923)** Robot Learning in Era of Foundation Models: Robot Learning in the Era of Foundation Models. 基础模型时代的机器人学习综述.
- **[arXiv 2022年12月](https://arxiv.org/abs/2212.04567)** Sim-to-Real Transfer for Robotics: A Survey. Sim2Real迁移综述.
- **[arXiv 2022年5月](https://arxiv.org/abs/2205.09876)** A Survey of Embodied Navigation. 具身导航综述.
- **[arXiv 2021年9月](https://arxiv.org/abs/2109.06789)** A Survey of Imitation Learning: Algorithms, Applications, and Challenges. 模仿学习综述.
- **[T-RO 2021年3月](https://arxiv.org/abs/2103.04567)** Robotic Manipulation: A Survey. 机器人操纵综述.
- **[IJRR 2020年4月](https://arxiv.org/abs/2004.09876)** Reinforcement Learning for Robotics: A Survey. 机器人强化学习综述.
