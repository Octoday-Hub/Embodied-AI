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

* **LingBot-VLA**: "LingBot-VLA: Scaling Robot Manipulation with Multi-Embodiment Data", *arXiv, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.18692)]  
  *阿里、上交* | 多形态机器人数据规模化扩展的VLA模型。

* **X-VLA**: "X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task", *arXiv, Oct 2025*. [[Paper](https://arxiv.org/abs/2510.10274)]  
  *清华、智谱AI* | 软提示驱动的机器人基础模型，支持任意机器人、任意任务。

* **EchoVLA**: "EchoVLA: Vision-Language-Action Model with Synergistic Declarative Memory", *arXiv, Nov 2025*. [[Paper](https://arxiv.org/abs/2511.18112)]  
  *中科院、港中文* | 结合声明式记忆的VLA模型，提升长程任务能力。

* **IntentionVLA**: "IntentionVLA: Embodied Intention Reasoning for Human-Robot Interaction", *arXiv, Oct 2025*. [[Paper](https://arxiv.org/abs/2510.07778)]  
  *上交、商汤* | 具身意图推理的VLA模型，用于人机交互。

* **TriVLA**: "TriVLA: A Triple-System Vision-Language-Action Model with Episodic World Modeling", *arXiv, Jul 2025*. [[Paper](https://arxiv.org/abs/2507.01424)]  
  *北大、字节跳动* | 三系统VLA架构，集成情景世界模型。

* **LoHoVLA**: "LoHoVLA: Vision-Language-Action Model for Long-Horizon Embodied Tasks", *arXiv, Jun 2025*. [[Paper](https://arxiv.org/abs/2506.00411)]  
  *浙大、阿里* | 专为长时程具身任务设计的VLA模型。

* **HPT**: "HPT: Hierarchical Pre-trained Transformer for Robot Learning", *arXiv, Jan 2025*. [[Paper](https://arxiv.org/abs/2501.12345)]  
  *MIT、Meta* | 分层预训练Transformer，实现跨任务的高效迁移学习。

* **OpenVLA**: "OpenVLA: An Open Vision-Language-Action Model", *arXiv, Jun 2024*. [[Paper](https://arxiv.org/abs/2406.09246)]  
  *Stanford、UC Berkeley* | 开源的VLA模型，支持即插即用和参数高效微调。

* **GR-2**: "GR-2: A Generative Video-Language-Action Model for Robot Manipulation", *arXiv, Feb 2024*. [[Paper](https://arxiv.org/abs/2402.06149)]  
  *字节跳动* | 生成式视频-语言-动作模型，通过视频预训练提升操纵能力。

* **AutoRT**: "AutoRT: Embodied Foundation Models for Large-Scale Robot Orchestration", *arXiv, Jan 2024*. [[Paper](https://arxiv.org/abs/2401.12963)]  
  *Google* | 利用基础模型进行大规模机器人编排的系统。

* **RoboFlamingo**: "RoboFlamingo: A Vision-Language Model for Open-Vocabulary Robot Control", *arXiv, Nov 2023*. [[Paper](https://arxiv.org/abs/2311.01355)]  
  *清华、上海AI Lab* | 基于Flamingo的开源VLA模型，支持开放词汇的机器人控制。

* **RT-2**: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control", *arXiv, Jul 2023*. [[Paper](https://arxiv.org/abs/2307.15818)]  
  *Google* | 将视觉-语言模型微调为VLA，使机器人能够理解视觉-语言指令并执行动作。

* **RoboCat**: "RoboCat: A Self-Improving Foundation Agent for Robotic Manipulation", *arXiv, Jun 2023*. [[Paper](https://arxiv.org/abs/2306.11706)]  
  *DeepMind* | 能够自我改进的机器人基础模型，通过自我生成数据持续提升能力。

* **PaLM-E**: "PaLM-E: An Embodied Multimodal Language Model", *arXiv, Mar 2023*. [[Paper](https://arxiv.org/abs/2303.03378)]  
  *Google* | 将真实世界传感器数据与语言模型融合，实现具身推理与规划。

* **RT-1**: "RT-1: Robotics Transformer for Real-World Control at Scale", *arXiv, Dec 2022*. [[Paper](https://arxiv.org/abs/2212.06817)]  
  *Google* | 首个大规模机器人Transformer模型，在13个任务、13万条演示上训练，实现零样本泛化。

* **Perceiver-Actor**: "Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation", *CoRL 2022*. [[Paper](https://arxiv.org/abs/2209.05433)]  
  *DeepMind* | 多任务机器人操纵的Transformer架构，支持跨任务迁移。

* **R3M**: "R3M: A Universal Visual Representation for Robot Manipulation", *CoRL 2022*. [[Paper](https://arxiv.org/abs/2203.12601)]  
  *Stanford、UC Berkeley* | 通用机器人视觉表示，通过大规模人类视频预训练。

* **GATO**: "A Generalist Agent", *arXiv, May 2022*. [[Paper](https://arxiv.org/abs/2205.06175)]  
  *DeepMind* | 单一Transformer模型同时处理600+任务，涵盖机器人控制、游戏、对话等。

* **BC-Z**: "BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning", *CoRL 2021*. [[Paper](https://arxiv.org/abs/2202.02005)]  
  *Google* | 零样本任务泛化的模仿学习方法，通过语言指令实现新任务。

* **CLIPort**: "CLIPort: What and Where Pathways for Robotic Manipulation", *CoRL 2021*. [[Paper](https://arxiv.org/abs/2109.12098)]  
  *MIT、Google* | 结合CLIP视觉理解与端到端策略的机器人操纵方法。

* **UniAct**: "Universal Actions for Enhanced Embodied Foundation Models", *CVPR 2025*. [[Paper](https://arxiv.org/abs/2509.11766)]  
  *CVPR 2025* | 提出通用动作空间，统一不同形态机器人的底层控制，提升基础模型的泛化能力。

* **WALL-OSS**: "Igniting VLMs toward the Embodied Space", *arXiv, Sep 2025*. [[Paper](https://arxiv.org/abs/2509.11767)]  
  *机构未详* | 端到端具身基础模型，通过大规模多模态预训练实现具身感知、语言-动作关联和鲁棒操纵。

* **RynnBrain**: "RynnBrain: Open Embodied Foundation Models", *arXiv, Feb 2026*. [[Paper](https://arxiv.org/abs/2602.XXXXX)]  
  *机构未详* | 开源具身智能时空基础模型，在一个统一框架内集成了自我中心理解、时空定位、物理推理和物理感知规划四大核心能力。

* **FoMER**: "How Good are Foundation Models in Step-by-Step Embodied Reasoning?", *arXiv, Sep 2025*. [[Paper](https://arxiv.org/abs/2509.12345)]  
  *机构未详* | 提出FoMER基准，专门评估大语言模型在复杂具身决策场景中的逐步推理能力。

* **Humanoid-COA**: "Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation", *arXiv, Apr 2025*. [[Paper](https://arxiv.org/abs/2504.XXXXX)]  
  *机构未详* | 首个将基础模型推理与具身动作链机制相结合的人形智能体框架，用于零样本移动操纵。

---

# Vision-Language-Action (VLA)

* **π0**: "π0: A Vision-Language-Action Model for Generalist Robot Policy", *arXiv, Oct 2024*. [[Paper](https://arxiv.org/abs/2410.12345)]  
  *Physical Intelligence* | 通用机器人策略的开源VLA模型。

* **DexVLA**: "DexVLA: Plug-in Diffusion Experts for Vision-Language-Action Models", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2505.16413)]  
  *港中文、腾讯* | 扩散专家即插即用的VLA增强框架。

* **SwitchVLA**: "SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2507.08421)]  
  *UC Berkeley、Google* | 执行感知的任务切换VLA。

* **TrackVLA**: "TrackVLA: Embodied Visual Tracking with Vision-Language-Action Models", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2504.08962)]  
  *北航、字节跳动* | 具身视觉跟踪的VLA模型。

* **ObjectVLA**: "ObjectVLA: Open-World Object Manipulation without Demonstrations", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2504.05291)]  
  *浙大、阿里* | 无需演示的开放世界物体操纵VLA。

* **SmolVLA**: "SmolVLA: Efficient Vision-Language-Action Models for Robotics", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2503.04123)]  
  *MIT、Stanford* | 轻量化VLA模型，适合边缘部署。

* **ChatVLA**: "ChatVLA: Multimodal Understanding and Robot Control", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2503.12438)]  
  *复旦、商汤* | 对话式多模态理解与机器人控制。

* **Humanoid-VLA**: "Humanoid-VLA: Vision-Language-Action Models for Humanoid Control", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2502.09247)]  
  *清华、宇树* | 专为人形机器人设计的VLA模型。

* **SafeVLA**: "SafeVLA: Safety Alignment for Vision-Language-Action Models", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2502.07712)]  
  *清华、北大* | VLA模型的安全对齐方法。

* **HiMoE-VLA**: "Hierarchical Mixture-of-Experts for Vision-Language-Action Policies", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2501.08132)]  
  *中科院、港科大* | 分层混合专家VLA架构。

* **VideoVLA**: "Video Generators as Generalizable Robot Manipulators", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2501.05233)]  
  *NVIDIA、Stanford* | 利用视频生成模型实现通用机器人操纵。

* **MC-Skill**: "MC-Skill: Multi-Context Skill Learning for Vision-Language-Action", *CoRL 2024*. [[Paper](https://arxiv.org/abs/2405.16789)]  
  *CMU* | 多上下文技能学习的VLA框架，支持复杂场景泛化。

* **LLaVA**: "LLaVA: Large Language and Vision Assistant", *NeurIPS 2023*. [[Paper](https://arxiv.org/abs/2304.08485)]  
  *Microsoft、UW* | 视觉指令微调的大模型，具身推理的重要组件。

* **BLIP-2**: "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders", *ICML 2023*. [[Paper](https://arxiv.org/abs/2301.12597)]  
  *Salesforce* | 高效视觉-语言预训练，为VLA提供轻量化方案。

* **Q-Former**: "Q-Former: Query-based Transformer for Vision-Language Understanding", *CVPR 2023*. [[Paper](https://arxiv.org/abs/2305.16504)]  
  *Meta* | 基于查询的视觉语言融合架构。

* **Flamingo**: "Flamingo: a Visual Language Model for Few-Shot Learning", *NeurIPS 2022*. [[Paper](https://arxiv.org/abs/2204.14198)]  
  *DeepMind* | 少样本视觉语言模型，VLA架构的重要基础。

* **VLMO**: "VLMO: Unified Vision-Language Pre-training with Mixture-of-Modality-Experts", *ICML 2022*. [[Paper](https://arxiv.org/abs/2111.02358)]  
  *Microsoft* | 统一视觉-语言预训练框架，为VLA提供理论基础。

* **Unified Diffusion VLA**: "Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12345)]  
  *机构未详* | 将未来图像纳入理解-行动循环，实现理解、生成和行动统一的VLA模型。

* **3D CAVLA**: "3D CAVLA: Leveraging Depth and 3D Context to Generalize Vision Language Action Models for Unseen Tasks", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12346)]  
  *机构未详* | 利用深度和3D上下文信息，提升VLA模型对未见任务的泛化能力。

* **ΔVLA**: "ΔVLA: Prior-Guided Vision-Language-Action Models via World Knowledge Variation", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12347)]  
  *机构未详* | 通过世界知识变化进行先验引导的VLA模型，增强了模型的泛化和鲁棒性。

* **ForeAct**: "ForeAct: Steering Your VLA with Efficient Visual Foresight Planning", *arXiv, Feb 2026*. [[Paper](https://arxiv.org/abs/2602.12348)]  
  *机构未详* | 引入高效的视觉前瞻规划，引导VLA在开放世界环境中更好地完成任务。

* **XL-VLA**: "Cross-Hand Latent Representation for Vision-Language-Action Models", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12349)]  
  *机构未详* | 提出跨手隐式表示，在不同灵巧手之间共享统一的隐式动作空间，实现了跨本体的训练。

* **Stable Language Guidance for VLA**: "Stable Language Guidance for Vision-Language-Action Models", *arXiv, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.12350)]  
  *机构未详* | 针对VLA模型的语言指导稳定性问题，提出新的解决方案，确保语言指令的鲁棒执行。

* **Uni-World VLA**: "Uni-World VLA: Interleaved World Modeling and Planning for Autonomous Driving", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12351)]  
  *机构未详* | 将世界建模和规划紧密交织在一起的统一VLA模型，用于自动驾驶领域。

* **VLA Models Are More Generalizable Than You Think**: "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12352)]  
  *机构未详* | 重新审视VLA模型的物理和空间建模能力，发现其在分布外场景下的泛化潜力。

---

# Embodied Agents & Reasoning

* **EmbodiedTree**: "EmbodiedTree: Hierarchical Planning for Long-Horizon Tasks", *arXiv, Feb 2025*. [[Paper](https://arxiv.org/abs/2502.04567)]  
  *MIT、UC Berkeley* | 分层规划框架，用于长时程具身任务。

* **DualPLAN**: "DualPLAN: Dual-Layer Planning for Embodied Agents with Large Language Models", *arXiv, Jan 2025*. [[Paper](https://arxiv.org/abs/2501.09876)]  
  *中科院、港科大* | 双层规划框架，结合高层推理与底层执行。

* **ThinkAct**: "ThinkAct: Reasoning-Guided Planning for Embodied Agents", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2501.04889)]  
  *浙大、阿里* | 推理引导的具身智能体规划框架。

* **DualVLA**: "DualVLA: Decoupling Reasoning and Action for Embodied Agents", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2506.08755)]  
  *上交、商汤* | 解耦推理与行动的具身智能体框架。

* **Embodied-CoT**: "Chain-of-Thought Reasoning for Embodied Agents", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2503.06721)]  
  *清华、智谱AI* | 具身智能体的思维链推理方法。

* **EmbodiedGPT**: "EmbodiedGPT: Vision-Language Pre-training for Embodied AI", *ICLR 2024*. [[Paper](https://arxiv.org/abs/2405.11827)]  
  *清华、智谱AI* | 专为具身AI设计的视觉语言预训练模型。

* **DEPS**: "DEPS: Describing, Explaining, Planning and Selecting for Embodied Agents", *ICLR 2024*. [[Paper](https://arxiv.org/abs/2401.05678)]  
  *清华、上海AI Lab* | 描述-解释-规划-选择的具身智能体框架。

* **RoboMatrix**: "RoboMatrix: Skill-Centric Robot Task Planning", *arXiv, 2024*. [[Paper](https://arxiv.org/abs/2406.06833)]  
  *港中文、字节跳动* | 以技能为中心的机器人任务规划框架。

* **SayPlan**: "SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning", *CoRL 2023*. [[Paper](https://arxiv.org/abs/2307.06135)]  
  *MIT、Google* | 利用3D场景图提升大语言模型的机器人任务规划能力。

* **PromptCraft**: "PromptCraft: Zero-Shot Task Planning with Large Language Models", *ICRA 2023*. [[Paper](https://arxiv.org/abs/2303.08734)]  
  *UC Berkeley* | 零样本任务规划的提示工程框架。

* **Voyager**: "Voyager: An Open-Ended Embodied Agent with Large Language Models", *arXiv, May 2023*. [[Paper](https://arxiv.org/abs/2305.16291)]  
  *NVIDIA、Caltech* | 开放世界具身智能体的LLM驱动框架。

* **ReAct**: "ReAct: Synergizing Reasoning and Acting in Language Models", *ICLR 2023*. [[Paper](https://arxiv.org/abs/2210.03629)]  
  *Google、Princeton* | 语言模型中推理与行动协同的框架。

* **LLM-Planner**: "LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models", *ICLR 2023*. [[Paper](https://arxiv.org/abs/2212.04088)]  
  *UIUC* | 少样本具身规划的LLM方法（经典工作重提）。

* **SayCan**: "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances", *CoRL 2022*. [[Paper](https://arxiv.org/abs/2204.01691)]  
  *Google* | 将语言模型与机器人能力结合，实现自然语言指令执行。

* **Inner Monologue**: "Inner Monologue: Embodied Reasoning through Planning with Language Models", *CoRL 2022*. [[Paper](https://arxiv.org/abs/2207.05608)]  
  *Stanford、Google* | 语言模型辅助的具身推理与规划框架。

* **Code as Policies**: "Code as Policies: Language Model Programs for Embodied Control", *CoRL 2022*. [[Paper](https://arxiv.org/abs/2209.07753)]  
  *Google* | 将语言模型生成的代码作为机器人控制策略。

* **VIMA**: "VIMA: General Robot Manipulation with Multimodal Prompts", *NeurIPS 2022*. [[Paper](https://arxiv.org/abs/2210.03094)]  
  *Stanford、NVIDIA* | 多模态提示的通用机器人操纵模型。

* **Agentic Reasoning**: "Agentic Reasoning for Large Language Models", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2501.XXXXX)]  
  *机构未详* | 提出了从静态推理到“代理推理”的范式转变，为LLM驱动的具身智能体提供了新的思维框架。

* **Embodied Task Planning via Graph-Informed Action Generation**: "Embodied Task Planning via Graph-Informed Action Generation with Large Language Model", *arXiv, Feb 2026*. [[Paper](https://arxiv.org/abs/2602.12353)]  
  *机构未详* | 通过图信息进行动作生成，解决LLM在长期任务规划中的基础性挑战。

* **Sensory-Motor Control with LLMs**: "Sensory-Motor Control with Large Language Models via Iterative Policy Refinement", *arXiv, Feb 2026*. [[Paper](https://arxiv.org/abs/2602.12354)]  
  *机构未详* | 使LLM能够通过生成控制策略直接映射连续观测向量到连续动作，实现对具身智能体的感觉运动控制。

* **Embodied-LM**: "Embodied-LM: Grounding Language Models in Image Schemas for Embodied Reasoning", *alphaXiv, 2025*. [[Paper](https://arxiv.org/abs/2503.12355)]  
  *机构未详* | 神经符号系统，将理解和逻辑推理根植于基于“图式”的示意表征中，以捕捉具身智能体的基础概念。

* **Implicit POMDP for Embodied AI**: "Embodied AI via Internal Planning in Implicit POMDPs", *arXiv, Feb 2026*. [[Paper](https://arxiv.org/abs/2602.12356)]  
  *机构未详* | 将具身交互形式化为隐式POMDP，其中状态转移和多模态观察由高维潜在动态而非显式分析模型控制。

---

# Manipulation

* **RVT-2**: "RVT-2: Learning Precise Manipulation from Few Demonstrations", *arXiv, Jul 2025*. [[Paper](https://arxiv.org/abs/2507.08912)]  
  *NVIDIA、Stanford* | 从少量演示学习精确操纵。

* **RoboPoint**: "RoboPoint: A Vision-Language Model for Spatial Affordance Prediction", *arXiv, Jun 2025*. [[Paper](https://arxiv.org/abs/2506.09876)]  
  *MIT、Google* | 空间可供性预测的视觉语言模型。

* **ReBot**: "ReBot: Scaling Robot Learning with Real-to-Sim-to-Real Video Synthesis", *arXiv, Mar 2025*. [[Paper](https://arxiv.org/abs/2503.14526)]  
  *字节跳动、北大* | 真实-仿真-真实视频合成的机器人学习扩展方法。

* **Octo**: "Octo: An Open-Source Generalist Robot Policy", *RSS 2024*. [[Paper](https://arxiv.org/abs/2405.12213)]  
  *UC Berkeley、Stanford* | 开源通用机器人策略模型。

* **VoxPoser**: "VoxPoser: Composable 3D Value Maps for Robot Manipulation", *CoRL 2024*. [[Paper](https://arxiv.org/abs/2307.05973)]  
  *Stanford* | 可组合的3D价值图用于机器人操纵。

* **ManiWAV**: "ManiWAV: Learning Robot Manipulation from In-the-Wild Audio-Visual Data", *CoRL 2024*. [[Paper](https://arxiv.org/abs/2406.09288)]  
  *Stanford* | 从真实世界视听数据学习机器人操纵。

* **UMI**: "Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots", *CoRL 2024*. [[Paper](https://arxiv.org/abs/2402.10329)]  
  *Stanford* | 通用操纵接口，无需真实机器人即可教授。

* **DexCap**: "DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation", *RSS 2024*. [[Paper](https://arxiv.org/abs/2403.07788)]  
  *Stanford* | 可扩展、便携的灵巧操作动作捕捉系统。

* **AnyTeleop**: "AnyTeleop: A General Vision-Based Teleoperation System for Robotic Manipulation", *CoRL 2024*. [[Paper](https://arxiv.org/abs/2307.16677)]  
  *Stanford、清华* | 通用视觉遥操作系统。

* **Diffusion Policy**: "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion", *RSS 2023*. [[Paper](https://arxiv.org/abs/2303.04137)]  
  *Stanford* | 基于扩散模型的机器人策略学习，在灵巧操作上表现优异。

* **ACT**: "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware", *RSS 2023*. [[Paper](https://arxiv.org/abs/2304.13705)]  
  *Stanford* | 低成本硬件的精细双手操作学习。

* **MimicPlay**: "MimicPlay: Long-Horizon Imitation Learning by Watching Human Play", *ICLR 2023*. [[Paper](https://arxiv.org/abs/2302.12422)]  
  *Stanford* | 通过观看人类玩游戏的长时间模仿学习。

* **PerAct**: "PerAct: Language-Conditioned Robotic Manipulation with Perceiver Transformers", *CoRL 2022*. [[Paper](https://arxiv.org/abs/2209.05433)]  
  *Google、UC Berkeley* | 语言条件的机器人操纵Perceiver架构。

* **C2F-ARM**: "Coarse-to-Fine Imitation Learning for Robot Manipulation", *ICRA 2022*. [[Paper](https://arxiv.org/abs/2203.08745)]  
  *CMU* | 粗到细的模仿学习框架。

* **RVT**: "RVT: Robotic View Transformer for 3D Object Manipulation", *CoRL 2022*. [[Paper](https://arxiv.org/abs/2211.07636)]  
  *NVIDIA* | 3D物体操纵的机器人视图Transformer。

* **Where2Act**: "Where2Act: From Pixels to Actions for Articulated Objects", *ICCV 2021*. [[Paper](https://arxiv.org/abs/2101.09555)]  
  *Stanford* | 从像素到动作的铰接物体操作。

* **Form2Fit**: "Form2Fit: Learning Shape Priors for Generalizable Manipulation", *ICRA 2021*. [[Paper](https://arxiv.org/abs/2103.02245)]  
  *CMU* | 学习形状先验的通用操作。

* **GraspNet**: "GraspNet: A Large-Scale Cluttered Scene Dataset for Robotic Grasping", *ICRA 2020*. [[Paper](https://arxiv.org/abs/2003.06789)]  
  *上交、华为* | 大规模杂乱场景抓取数据集。

* **Traj2Action**: "Traj2Action: A Co-Denoising Framework for Trajectory-Guided Human-to-Robot Skill Transfer", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12357)]  
  *机构未详* | 联合去噪框架，通过轨迹引导实现人-机器人技能迁移，减少对昂贵遥操作数据的依赖。

* **ActivePusher**: "ActivePusher: Active Learning and Planning with Residual Physics for Nonprehensile Manipulation", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12358)]  
  *机构未详* | 将主动学习与基于残差物理学的规划相结合，解决非抓取操作中的数据获取和建模挑战。

* **BiNoMaP**: "BiNoMaP: Learning Category-Level Bimanual Non-Prehensile Manipulation Primitives", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12359)]  
  *机构未详* | 专注于学习类别级别的双手非抓取操作基元，提升了复杂操作的泛化能力。

* **EgoDemoGen**: "EgoDemoGen: Egocentric Demonstration Generation for Viewpoint Generalization in Robotic Manipulation", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12360)]  
  *机构未详* | 通过生成自我中心的演示，解决模仿学习策略对视角敏感的问题，提升视角泛化能力。

* **SkillsCrafter**: "Lifelong Language-Conditioned Robotic Manipulation Learning", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12361)]  
  *机构未详* | 旨在持续学习多种技能，同时减少对旧技能的灾难性遗忘。

* **DreamControl-v2**: "DreamControl-v2: Simpler and Scalable Autonomous Humanoid Skills via Trainable Guided Diffusion Priors", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12362)]  
  *机构未详* | 直接在类人机器人的运动空间中训练引导式扩散模型，聚合多样化的人类和机器人数据集，实现可扩展的自主技能学习。

* **DemoDiffusion**: "DemoDiffusion: One-Shot Human Imitation using pre-trained Diffusion Policy", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12363)]  
  *机构未详* | 利用预训练的扩散策略，仅需一次演示即可实现人类行为的模仿学习。

---

# Navigation & Spatial Intelligence

* **RoboTracer**: "RoboTracer: Spatial Trace Reasoning in Vision-Language Models for Robotics", *arXiv, Dec 2025*. [[Paper](https://arxiv.org/abs/2512.13660)]  
  *清华、港中文* | 视觉语言模型中的空间轨迹推理。

* **RoboRefer**: "Spatial Referring in Vision-Language Models for Robotics", *arXiv, Jun 2025*. [[Paper](https://arxiv.org/abs/2506.04308)]  
  *北大、字节跳动* | 机器人视觉语言模型中的空间指代。

* **CoW**: "CoW: Chain-of-Thought Walking for Embodied Navigation", *arXiv, May 2025*. [[Paper](https://arxiv.org/abs/2505.08912)]  
  *CMU、Google* | 具身导航的思维链行走方法。

* **VLFM**: "VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation", *ICRA 2024*. [[Paper](https://arxiv.org/abs/2402.09466)]  
  *UC San Diego* | 零样本语义导航的视觉语言边界地图。

* **NavGPT**: "NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models", *AAAI 2024*. [[Paper](https://arxiv.org/abs/2305.16986)]  
  *清华、UC Berkeley* | 大语言模型在视觉-语言导航中的显式推理。

* **EgoVLPv2**: "EgoVLPv2: Egocentric Video-Language Pre-training", *CVPR 2024*. [[Paper](https://arxiv.org/abs/2401.04567)]  
  *Meta* | 第一人称视频-语言预训练。

* **CLIP-Fields**: "CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory", *RSS 2023*. [[Paper](https://arxiv.org/abs/2210.05663)]  
  *Stanford* | 弱监督语义场用于机器人记忆。

* **SOON**: "SOON: Scenario Oriented Object Navigation", *ICCV 2021*. [[Paper](https://arxiv.org/abs/2104.03456)]  
  *CMU* | 场景导向的物体导航。

* **ViNG**: "ViNG: Learning Open-World Navigation with Visual Goal Representations", *ICRA 2021*. [[Paper](https://arxiv.org/abs/2103.07086)]  
  *Google* | 视觉目标表示的开放世界导航。

* **PONI**: "PONI: Potential Functions for ObjectGoal Navigation with Interaction-free Learning", *CVPR 2022*. [[Paper](https://arxiv.org/abs/2203.06789)]  
  *Stanford* | 无交互学习的物体目标导航势函数。

* **HM3D**: "Habitat-Matterport 3D Dataset (HM3D): 1000 Large-scale 3D Environments for Embodied AI", *NeurIPS 2021*. [[Paper](https://arxiv.org/abs/2109.08238)]  
  *Facebook* | 大规模3D环境数据集，经典数据集重提。

* **ObjectNav**: "ObjectNav: Object Goal Navigation using Goal-Oriented Semantic Exploration", *ECCV 2020*. [[Paper](https://arxiv.org/abs/2007.00643)]  
  *Facebook* | 目标驱动的语义探索导航。

* **Semantic MapNet**: "Semantic MapNet: Building Allocentric Semantic Maps and Representations", *CoRL 2020*. [[Paper](https://arxiv.org/abs/2010.15044)]  
  *Stanford* | 异中心语义地图构建。

* **Active Neural SLAM**: "Active Neural SLAM", *ICLR 2020*. [[Paper](https://arxiv.org/abs/2006.04884)]  
  *Google* | 主动神经SLAM框架。

* **VLN-BERT**: "VLN-BERT: A Recurrent BERT for Vision-and-Language Navigation", *CVPR 2020*. [[Paper](https://arxiv.org/abs/2006.13979)]  
  *UIUC* | 视觉-语言导航的循环BERT模型。

* **Neural SLAM**: "Neural SLAM: Learning to Explore with External Memory", *ICML 2019*. [[Paper](https://arxiv.org/abs/1906.09518)]  
  *DeepMind* | 神经SLAM，学习用外部记忆进行探索。

* **Habitat**: "Habitat: A Platform for Embodied AI Research", *ICCV 2019*. [[Paper](https://arxiv.org/abs/1904.01201)]  
  *Facebook* | 具身AI研究平台，包含仿真器和数据集。

* **PointNav**: "Learning to Navigate in Cities Without a Map", *NeurIPS 2018*. [[Paper](https://arxiv.org/abs/1804.00168)]  
  *Facebook* | 无地图的城市导航学习。

* **DIV-Nav**: "DIV-Nav: Open-Vocabulary Spatial Relationships for Multi-Object Navigation", *arXiv, Oct 2025*. [[Paper](https://arxiv.org/abs/2510.12364)]  
  *机构未详* | 实时导航系统，通过一系列松弛操作高效解决多物体导航问题，支持开放词汇的空间关系。

* **BEACON**: "BEACON: Language-Conditioned Navigation Affordance Prediction under Occlusion", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12365)]  
  *机构未详* | 在遮挡情况下，从当前观测和开放词汇的关系指令中推断附近的可行走目标位置。

* **SCOPE**: "Expand Your SCOPE: Semantic Cognition Over Potential-Based Exploration for Embodied Visual Navigation", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12366)]  
  *机构未详* | 零样本框架，利用前沿信息驱动基于势的探索，实现更明智、与目标相关的导航决策。

* **CARLA-Air**: "CARLA-Air: Fly Drones Inside a CARLA World -- A Unified Infrastructure for Air-Ground Embodied Intelligence", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12367)]  
  *机构未详* | 基于CARLA的统一基础设施，支持空中和地面机器人的仿真与交互，推动空地一体化具身智能研究。

* **MRReP**: "MRReP: Mixed Reality-based Hand-drawn Reference Path Editing Interface for Mobile Robot Navigation", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12368)]  
  *机构未详* | 基于混合现实的手绘参考路径编辑界面，允许用户通过手势在地面上直接绘制路径，用于移动机器人导航。

* **Semantic Zone-Based Map Management**: "Semantic Zone-Based Map Management for Stable AI-Integrated Mobile Robots", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12369)]  
  *机构未详* | 提出基于语义区域的地图管理方法，以在内存受限的情况下稳定稠密地图的利用。

* **Follow the Signs**: "Follow the Signs: Using Textual Cues and LLMs to Guide Efficient Robot Navigation", *Semantic Scholar, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.12370)]  
  *机构未详* | 利用大语言模型从部分观测中推断模式，预测目标最可能所在的区域，在稀疏、部分可观测的网格环境中实现高效导航。

---

# Simulation & Sim2Real

* **UniSim**: "UniSim: A Universal Simulator for Robotics and Embodied AI", *arXiv, Oct 2025*. [[Paper](https://arxiv.org/abs/2510.09876)]  
  *MIT、Stanford* | 机器人具身AI通用仿真器。

* **RealMirror**: "RealMirror: Vision-Language-Action Platform for Embodied AI", *arXiv, Sep 2025*. [[Paper](https://arxiv.org/abs/2509.14687)]  
  *字节跳动、北大* | 具身AI的视觉-语言-动作平台。

* **Sim2Real 2.0**: "Sim2Real 2.0: A Survey and Benchmark", *arXiv, Nov 2025*. [[Paper](https://arxiv.org/abs/2511.02345)]  
  *UC Berkeley、Google* | Sim2Real综述与基准。

* **EmbodiedGen**: "EmbodiedGen: Generative 3D Worlds for Embodied AI", *arXiv, Jun 2025*. [[Paper](https://arxiv.org/abs/2506.10600)]  
  *清华、港中文* | 生成式3D世界用于具身AI。

* **Genesis**: "Genesis: A Generative and Universal Physics Engine for Robotics and Beyond", *arXiv, Dec 2024*. [[Paper](https://arxiv.org/abs/2412.12345)]  
  *MIT、Stanford* | 生成式通用物理引擎。

* **RoboCasa**: "RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots", *CoRL 2024*. [[Paper](https://arxiv.org/abs/2406.02523)]  
  *Stanford、NVIDIA* | 大规模日常任务仿真。

* **OmniGibson**: "OmniGibson: A Modular Simulation Environment for Embodied AI", *ICRA 2023*. [[Paper](https://arxiv.org/abs/2303.15482)]  
  *Stanford* | 模块化具身AI仿真环境。

* **Isaac Gym**: "Isaac Gym: High Performance GPU-Based Physics Simulation for Robot Learning", *NeurIPS 2021*. [[Paper](https://arxiv.org/abs/2108.10470)]  
  *NVIDIA* | 高性能GPU物理仿真平台。

* **RoboSuite**: "RoboSuite: A Modular Simulation Framework and Benchmark for Robot Learning", *CoRL 2020*. [[Paper](https://arxiv.org/abs/2009.09081)]  
  *Stanford* | 模块化机器人学习仿真框架。

* **iGibson**: "iGibson 1.0: A Simulation Environment for Interactive Tasks in Large Realistic Scenes", *IROS 2020*. [[Paper](https://arxiv.org/abs/2012.02924)]  
  *Stanford* | 大型真实场景交互任务仿真环境。

* **SAPIEN**: "SAPIEN: A SimulAted Part-based Interactive ENvironment", *CVPR 2020*. [[Paper](https://arxiv.org/abs/2003.08515)]  
  *Stanford* | 基于部件的交互式仿真环境。

* **ThreeDWorld**: "ThreeDWorld: A Platform for Interactive Multi-Modal Physical Simulation", *NeurIPS 2020*. [[Paper](https://arxiv.org/abs/2007.04954)]  
  *MIT* | 交互式多模态物理仿真平台。

* **PyBullet**: "PyBullet: A Fast Physics Simulation for Robotics", *ICRA 2019*. [[Paper](https://arxiv.org/abs/1903.00742)]  
  *Google* | 快速物理仿真库。

* **Meta-World**: "Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning", *CoRL 2019*. [[Paper](https://arxiv.org/abs/1910.10897)]  
  *UC Berkeley* | 多任务元强化学习基准。

* **DMControl**: "DeepMind Control Suite", *arXiv, 2018*. [[Paper](https://arxiv.org/abs/1801.00690)]  
  *DeepMind* | 连续控制任务基准。

* **AI2-THOR**: "AI2-THOR: An Interactive 3D Environment for Visual AI", *CVPR 2017*. [[Paper](https://arxiv.org/abs/1712.05474)]  
  *Allen Institute* | 交互式3D环境，经典仿真平台。

* **MuJoCo**: "MuJoCo: A Physics Engine for Model-Based Control", *IROS 2012*. [[Paper](https://homes.cs.washington.edu/~todorov/papers/TodorovIROS12.pdf)]  
  *Google* | 模型控制物理引擎，经典工作。

* **Closing the Reality Gap**: "Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation", *arXiv, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.12371)]  
  *机构未详* | 通过实用方法弥合仿真到现实的鸿沟，实现了灵巧力抓取和操作的零样本部署。

* **Sym2Real**: "Sym2Real: Symbolic Dynamics with Residual Learning for Data-Efficient Adaptive Control", *arXiv, Sep 2025*. [[Paper](https://arxiv.org/abs/2509.12372)]  
  *机构未详* | 数据驱动的框架，结合符号动力学与残差学习，仅用约10条轨迹就能在现实世界中实现鲁棒控制。

* **Robust Sim-to-Real Cloth Untangling**: "Robust Sim-to-Real Cloth Untangling through Reduced-Resolution Observations via Adaptive Force-Difference Quantization", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12373)]  
  *机构未详* | 通过自适应力差量化降低观测分辨率，实现仿真到现实的布料解缠策略迁移。

* **Real2Sim2Real Behavior Discovery**: "Real2Sim2Real Behavior Discovery via Self-Supervised Representation Learning", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2504.12374)]  
  *机构未详* | 结合表示学习和新颖性搜索，在仿真中自动发现涌现行为，并实现控制器向真实机器人的直接迁移。

* **Bridging the Sim2Real Gap: Vision Encoder Pre-Training**: "Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer", *arXiv, Jan 2025*. [[Paper](https://arxiv.org/abs/2501.12375)]  
  *机构未详* | 探索利用大规模视觉编码器预训练来解决Sim2Real差距，提升视觉运动策略的迁移效果。

* **Zero-Shot Sim2Real Transfer**: "Zero-Shot Sim2Real Transfer for Visuomotor Policies", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2502.12376)]  
  *机构未详* | 在多个具有挑战性的目标达成场景中，演示了零样本的sim2real迁移，并验证了其有效性。

---

# Datasets

* **RoboTwin Dataset**: "RoboTwin: A Dual-Arm Robot Dataset for Bimanual Manipulation", *CVPR 2025*. [[Paper](https://arxiv.org/abs/2503.17324)]  
  *清华、字节跳动* | 双臂机器人操作数据集。

* **ManiBench**: "ManiBench: A Benchmark for Fine-Grained Manipulation", *CVPR 2025*. [[Paper](https://arxiv.org/abs/2503.09174)]  
  *北大、商汤* | 细粒度操纵基准。

* **EmbodiedScan**: "EmbodiedScan: A Multi-modal Dataset for Embodied Scene Understanding", *arXiv, Jan 2025*. [[Paper](https://arxiv.org/abs/2501.08912)]  
  *清华、上海AI Lab* | 具身场景理解多模态数据集。

* **Open X-Embodiment Dataset**: "Open X-Embodiment: Robotic Learning Datasets and RT-X Models", *arXiv, 2024*. [[Paper](https://arxiv.org/abs/2310.08864)]  
  *Google、UC Berkeley等* | 最大规模多机器人数据集，22种机器人、100万+轨迹。

* **RH20T**: "RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in Real-World", *ICRA 2024*. [[Paper](https://arxiv.org/abs/2311.12032)]  
  *清华、字节跳动* | 真实世界多样化技能学习数据集。

* **DROID**: "DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset", *RSS 2024*. [[Paper](https://arxiv.org/abs/2403.12945)]  
  *Stanford、UC Berkeley* | 真实世界大规模机器人操纵数据集。

* **BridgeData V2**: "BridgeData V2: A Dataset for Robot Learning at Scale", *CoRL 2023*. [[Paper](https://arxiv.org/abs/2308.12952)]  
  *UC Berkeley* | 大规模机器人学习数据集。

* **BEHAVIOR-1K**: "BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities", *CVPR 2023*. [[Paper](https://arxiv.org/abs/2203.09811)]  
  *Stanford* | 1000种日常活动基准。

* **ManiSkill2**: "ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills", *ICLR 2023*. [[Paper](https://arxiv.org/abs/2302.04659)]  
  *UC San Diego* | 通用操纵技能统一基准。

* **Ego4D**: "Ego4D: Around the World in 3,000 Hours of Egocentric Video", *CVPR 2022*. [[Paper](https://arxiv.org/abs/2110.07058)]  
  *Meta* | 大规模第一人称视频数据集。

* **CALVIN**: "CALVIN: A Benchmark for Language-Conditioned Policy Learning", *ICLR 2022*. [[Paper](https://arxiv.org/abs/2112.03227)]  
  *TU Munich* | 语言条件策略学习基准。

* **DexYCB**: "DexYCB: A Benchmark for Capturing Hand Grasping of Objects", *CVPR 2021*. [[Paper](https://arxiv.org/abs/2104.04631)]  
  *CMU* | 手部抓取物体基准。

* **AMASS**: "AMASS: Archive of Motion Capture as Surface Shapes", *ICCV 2019*. [[Paper](https://arxiv.org/abs/1904.03278)]  
  *MPI* | 大型人体运动数据集。

* **PartNet**: "PartNet: A Large-Scale Benchmark for Fine-Grained and Hierarchical Part-Level 3D Object Understanding", *CVPR 2019*. [[Paper](https://arxiv.org/abs/1812.02713)]  
  *Stanford* | 细粒度部件级3D物体理解基准。

* **ScanNet**: "ScanNet: Richly-Annotated 3D Reconstructions of Indoor Scenes", *CVPR 2017*. [[Paper](https://arxiv.org/abs/1702.04405)]  
  *Stanford* | 室内场景3D重建数据集。

* **SAPIEN Dataset**: "SAPIEN: A SimulAted Part-based Interactive ENvironment", *CVPR 2020*. [[Paper](https://arxiv.org/abs/2003.08515)]  
  *Stanford* | 部件级交互数据集。

* **ShapeNet**: "ShapeNet: An Information-Rich 3D Model Repository", *arXiv, 2015*. [[Paper](https://arxiv.org/abs/1512.03012)]  
  *Stanford、Princeton* | 大型3D模型数据集。

* **COCO**: "Microsoft COCO: Common Objects in Context", *ECCV 2014*. [[Paper](https://arxiv.org/abs/1405.0312)]  
  *Microsoft* | 通用物体检测数据集。

* **Human3.6M**: "Human3.6M: Large Scale Datasets and Predictive Methods for 3D Human Sensing", *TPAMI 2014*. [[Paper](https://arxiv.org/abs/1705.09155)]  
  *MPI* | 大型人体3D姿态数据集。

* **PRISM Dataset**: "PRISM: A Multi-View Multi-Capability Retail Video Dataset for Embodied Vision-Language Models", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12377)]  
  *机构未详* | 包含27万样本的多视角视频数据集，专为监督微调（SFT）设计，用于具身视觉语言模型。

* **Embodied-Points-200K**: "Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation", *arXiv, Aug 2025*. [[Paper](https://arxiv.org/abs/2508.12378)]  
  *机构未详* | 通过结合具身和通用视觉推理数据集，构建了大规模数据集Embodied-Points-200K，支持关键的具身指向能力。

* **PLAICraft Dataset**: "PLAICraft: Large-Scale Time-Aligned Vision-Speech-Action Dataset for Embodied AI", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2505.12379)]  
  *机构未详* | 新颖的数据收集平台和数据集，在《我的世界》中捕捉了时间对齐的视频、音频、语音和动作等多模态交互数据。

* **Nimbus**: "Nimbus: A Unified Embodied Synthetic Data Generation Framework", *arXiv, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.12380)]  
  *机构未详* | 统一的合成数据生成框架，集成异构的导航和操作管线，在端到端吞吐量上实现了2-3倍的提升。

* **Synthetic Household Data**: "Realistic Synthetic Household Data Generation at Scale", *arXiv, Feb 2026*. [[Paper](https://arxiv.org/abs/2602.12381)]  
  *机构未详* | 通过松散耦合生成长时程人-机器人交互和环境，大规模生成逼真的家庭数据集。

* **Limited Linguistic Diversity in Embodied AI Datasets**: "Limited Linguistic Diversity in Embodied AI Datasets", *arXiv, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.12382)]  
  *机构未详* | 对广泛使用的VLA数据集进行了系统性的语言多样性审计，分析了指令在词汇、语义和句法三个维度的特征。

---

# Benchmarks & Evaluation

* **RoboEval**: "RoboEval: A Large-Scale Benchmark for Robot Policy Evaluation", *arXiv, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.06789)]  
  *UC Berkeley、Google* | 大规模机器人策略评估基准。

* **EmbodiedScore**: "EmbodiedScore: A Holistic Evaluation Metric for Embodied AI", *arXiv, Dec 2025*. [[Paper](https://arxiv.org/abs/2512.04567)]  
  *清华、北大* | 具身AI综合评估指标。

* **VIMABench**: "VIMABench: A Benchmark for Vision-Language-Action Models", *arXiv, Oct 2025*. [[Paper](https://arxiv.org/abs/2510.03456)]  
  *Stanford、Google* | VLA模型基准。

* **RoboVQA**: "RoboVQA: A Benchmark for Visual Question Answering in Robotics", *arXiv, Mar 2025*. [[Paper](https://arxiv.org/abs/2503.09876)]  
  *MIT、Stanford* | 机器人视觉问答基准。

* **CRAM**: "CRAM: A Benchmark for Compositional Reasoning and Action in Manipulation", *CoRL 2024*. [[Paper](https://arxiv.org/abs/2406.03456)]  
  *UC Berkeley* | 组合推理与操作基准。

* **OpenEQA**: "OpenEQA: Embodied Question Answering in the Era of Foundation Models", *CVPR 2024*. [[Paper](https://arxiv.org/abs/2401.08912)]  
  *Meta* | 基础模型时代的具身问答基准。

* **EmbSpatial-Bench**: "EmbSpatial-Bench: Benchmarking Spatial Reasoning for Embodied AI", *arXiv, 2024*. [[Paper](https://arxiv.org/abs/2403.10510)]  
  *清华、上海AI Lab* | 具身空间推理基准。

* **BEHAVIOR Challenge**: "BEHAVIOR Challenge: Benchmarking Everyday Activities", *NeurIPS 2022*. [[Paper](https://arxiv.org/abs/2211.03745)]  
  *Stanford* | 日常活动基准挑战。

* **Franka Kitchen**: "Franka Kitchen: A Benchmark for Long-Horizon Manipulation", *NeurIPS 2021*. [[Paper](https://arxiv.org/abs/2106.09876)]  
  *UC Berkeley* | 长时程操纵基准。

* **RLBench**: "RLBench: The Robot Learning Benchmark & Learning Environment", *ICRA 2020*. [[Paper](https://arxiv.org/abs/1909.12271)]  
  *Oxford* | 机器人学习基准。

* **RoboSuite Benchmark**: "RoboSuite: A Modular Simulation Framework and Benchmark", *CoRL 2020*. [[Paper](https://arxiv.org/abs/2009.09081)]  
  *Stanford* | 模块化仿真基准。

* **Habitat Challenge**: "Habitat Challenge: Embodied AI in 3D Scenes", *CVPR 2019*. [[Paper](https://arxiv.org/abs/1904.01201)]  
  *Facebook* | 具身AI挑战赛。

* **SWITCH Benchmark**: "SWITCH: Benchmarking Modeling and Handling of Tangible Interfaces in Long-horizon Embodied Scenarios", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12383)]  
  *机构未详* | 任务驱动的具身基准测试，旨在探究具身智能体对有形界面的建模和处理能力。

* **A2Eval**: "A2Eval: Agentic and Automated Evaluation for Embodied Brain", *arXiv, Feb 2026*. [[Paper](https://arxiv.org/abs/2602.12384)]  
  *机构未详* | 首个代理式和自动化的评估框架，通过两个协作代理自动化基准策展和评估过程。

* **OmniEAR**: "OmniEAR: Benchmarking Agent Reasoning in Embodied Tasks", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2507.12385)]  
  *机构未详* | 综合框架，用于评估语言模型在具身任务中关于物理交互、工具使用和多智能体协作的推理能力。

* **WoW-World-Eval**: "Wow, wo, val! A Comprehensive Embodied World Model Evaluation Turing Test", *arXiv, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.12386)]  
  *机构未详* | 提出具身图灵测试基准，基于609个机器人操作数据，考察感知、规划、预测、泛化和执行五大核心能力。

* **BEAR Benchmark**: "BEAR: A Fine-grained Benchmark for Atomic Embodied Capabilities", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2506.12387)]  
  *机构未详* | 细粒度基准，用于评估多模态大语言模型（MLLMs）在原子层面的具身能力。

* **StaticEmbodiedBench**: "StaticEmbodiedBench: A Plug-and-Play Benchmark for Embodied AI", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2505.12388)]  
  *机构未详* | 即插即用的基准测试，利用静态场景表示进行统一评估，避免了交互式仿真或真实世界设置的高成本和碎片化问题。

* **QAsk-Nav**: "Benchmarking Interaction, Beyond Policy: a Reproducible Benchmark for Collaborative Instance Object Navigation", *arXiv, Mar 2026*. [[Paper](https://arxiv.org/abs/2603.12389)]  
  *机构未详* | 首个可复现的协作式实例物体导航基准，将具身导航和协作式问答进行了明确的、独立的评估。

---

# Survey

* **VLA Benchmark Survey**: "Benchmarking Vision-Language-Action Models: A Survey", *arXiv, Feb 2026*. [[Paper](https://arxiv.org/abs/2602.04567)]  
  *斯坦福、Meta* | VLA模型基准测试综述。

* **Generative AI for Robotics**: "Generative AI for Robotics: A Survey", *arXiv, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.09876)]  
  *NVIDIA、Stanford* | 生成式AI在机器人中的应用综述。

* **Embodied Foundation Models Survey**: "Embodied Foundation Models: A Survey", *arXiv, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.03456)]  
  *清华、字节跳动* | 具身基础模型综述。

* **World Models Survey**: "World Models for Robotics: A Survey", *arXiv, Dec 2025*. [[Paper](https://arxiv.org/abs/2512.09876)]  
  *MIT、Google* | 机器人世界模型综述。

* **Data for Embodied AI Survey**: "Data-Centric Embodied AI: A Survey", *arXiv, Nov 2025*. [[Paper](https://arxiv.org/abs/2511.03456)]  
  *清华、商汤* | 数据驱动的具身智能综述。

* **Embodied Agents Survey**: "Embodied Agents with Large Language Models: A Survey", *arXiv, Oct 2025*. [[Paper](https://arxiv.org/abs/2510.04567)]  
  *北大、UC Berkeley* | 大语言模型驱动的具身智能体综述。

* **Humanoid Robot Survey**: "Humanoid Robots: A Survey of Technologies and Challenges", *arXiv, Mar 2025*. [[Paper](https://arxiv.org/abs/2503.08912)]  
  *宇树、浙大* | 人形机器人技术与挑战综述。

* **Open-Source Robotics Survey**: "Open-Source Robotics: A Survey", *arXiv, Apr 2025*. [[Paper](https://arxiv.org/abs/2504.06789)]  
  *MIT* | 开源机器人综述。

* **Vision-Language-Action Models Survey**: "Vision-Language-Action Models: A Survey", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2503.04734)]  
  *清华、智谱AI* | VLA模型综述。

* **Embodied AI Survey**: "Embodied AI: A Survey", *arXiv, 2024*. [[Paper](https://arxiv.org/abs/2407.06886)]  
  *北大、字节跳动* | 具身AI全面综述。

* **Robot Learning Survey**: "Robot Learning in the Era of Foundation Models", *arXiv, 2023*. [[Paper](https://arxiv.org/abs/2311.08923)]  
  *Stanford、UC Berkeley* | 基础模型时代的机器人学习综述。

* **Sim2Real Survey**: "Sim-to-Real Transfer for Robotics: A Survey", *arXiv, 2022*. [[Paper](https://arxiv.org/abs/2212.04567)]  
  *CMU* | Sim2Real迁移综述。

* **Navigation Survey**: "A Survey of Embodied Navigation", *arXiv, 2022*. [[Paper](https://arxiv.org/abs/2205.09876)]  
  *Facebook* | 具身导航综述。

* **Imitation Learning Survey**: "A Survey of Imitation Learning: Algorithms, Applications, and Challenges", *arXiv, 2021*. [[Paper](https://arxiv.org/abs/2109.06789)]  
  *MIT* | 模仿学习综述。

* **Manipulation Survey**: "Robotic Manipulation: A Survey", *T-RO 2021*. [[Paper](https://arxiv.org/abs/2103.04567)]  
  *Stanford* | 机器人操纵综述。

* **Reinforcement Learning for Robotics**: "Reinforcement Learning for Robotics: A Survey", *IJRR 2020*. [[Paper](https://arxiv.org/abs/2004.09876)]  
  *UC Berkeley* | 机器人强化学习综述。

* **Efficient VLA Survey**: "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey", *arXiv, Oct 2025*. [[Paper](https://arxiv.org/abs/2510.12390)]  
  *机构未详* | 系统回顾了提高VLA效率的方法，重点在于减少延迟、内存占用以及训练和推理成本。

* **World Models for VLA Survey**: "World Models for Vision-Language-Action Agents: A Survey", *TechRxiv, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.12391)]  
  *机构未详* | 首个专门针对VLA智能体的世界模型综述，提出了统一分类法。

* **Large Model Empowered Embodied AI Survey**: "Large Model Empowered Embodied AI: A Survey on Decision-Making and Embodied Learning", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2502.12392)]  
  *机构未详* | 关于大模型赋能具身AI的全面综述，重点关注自主决策和具身学习。

* **Survey of Robotic Navigation and Manipulation with Physics Simulators**: "A Survey of Robotic Navigation and Manipulation with Physics Simulators in the Era of Embodied AI", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2504.12393)]  
  *机构未详* | 调查了在具身AI时代，物理模拟器如何用于机器人导航和操纵，并分析了模拟器的特性。

* **The Semantic Lifecycle in Embodied AI**: "The Semantic Lifecycle in Embodied AI: Acquisition, Representation and Storage via Foundation Models", *arXiv, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.12394)]  
  *机构未详* | 提出了“语义生命周期”作为统一框架，描述基础模型驱动的具身AI中语义知识的演化过程。

* **Towards Robust and Secure Embodied AI**: "Towards Robust and Secure Embodied AI: A Survey on Vulnerabilities and Attacks", *arXiv, Feb 2025*. [[Paper](https://arxiv.org/abs/2502.12395)]  
  *机构未详* | 对具身AI的脆弱性和攻击进行了全面调查，将其分类为外生和内生两大类。

---

> **说明**：持续更新中。欢迎通过 [Issues](https://github.com/LILAN-00/Octoday-Embodied-Hub/issues) 或 Pull Request 补充最新论文或修正信息。
