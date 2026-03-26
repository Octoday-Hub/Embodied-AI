## 📄 Embodied AI Papers 具身智能论文精选

A curated list of **recent Embodied AI papers** including robotics foundation models, VLA models, embodied agents, manipulation, and navigation.
持续收录具身智能领域的最新、最具代表性的论文，包含核心内容摘要和原文链接。**欢迎补充**（可通过 Issues 或 PR 提交）。


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

## 📜 经典论文 (2022–2024)

* **RT-1**: "RT-1: Robotics Transformer for Real-World Control at Scale", *arXiv, Dec 2022*. [[Paper](https://arxiv.org/abs/2212.06817)]  
  *Google* | 首个大规模机器人Transformer模型，在13个任务、13万条演示上训练，实现零样本泛化。

* **RT-2**: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control", *arXiv, Jul 2023*. [[Paper](https://arxiv.org/abs/2307.15818)]  
  *Google* | 将视觉-语言模型微调为VLA，使机器人能够理解视觉-语言指令并执行动作。

* **PaLM-E**: "PaLM-E: An Embodied Multimodal Language Model", *arXiv, Mar 2023*. [[Paper](https://arxiv.org/abs/2303.03378)]  
  *Google* | 将真实世界传感器数据与语言模型融合，实现具身推理与规划。

* **GATO**: "A Generalist Agent", *arXiv, May 2022*. [[Paper](https://arxiv.org/abs/2205.06175)]  
  *DeepMind* | 单一Transformer模型同时处理600+任务，涵盖机器人控制、游戏、对话等。

* **RoboCat**: "RoboCat: A Self-Improving Foundation Agent for Robotic Manipulation", *arXiv, Jun 2023*. [[Paper](https://arxiv.org/abs/2306.11706)]  
  *DeepMind* | 能够自我改进的机器人基础模型，通过自我生成数据持续提升能力。

* **BC-Z**: "BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning", *CoRL 2021*. [[Paper](https://arxiv.org/abs/2202.02005)]  
  *Google* | 零样本任务泛化的模仿学习方法，通过语言指令实现新任务。

* **Perceiver-Actor**: "Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation", *CoRL 2022*. [[Paper](https://arxiv.org/abs/2209.05433)]  
  *DeepMind* | 多任务机器人操纵的Transformer架构，支持跨任务迁移。

* **RoboFlamingo**: "RoboFlamingo: A Vision-Language Model for Open-Vocabulary Robot Control", *arXiv, Nov 2023*. [[Paper](https://arxiv.org/abs/2311.01355)]  
  *清华、上海AI Lab* | 基于Flamingo的开源VLA模型，支持开放词汇的机器人控制。

* **CLIPort**: "CLIPort: What and Where Pathways for Robotic Manipulation", *CoRL 2021*. [[Paper](https://arxiv.org/abs/2109.12098)]  
  *MIT、Google* | 结合CLIP视觉理解与端到端策略的机器人操纵方法。

* **R3M**: "R3M: A Universal Visual Representation for Robot Manipulation", *CoRL 2022*. [[Paper](https://arxiv.org/abs/2203.12601)]  
  *Stanford、UC Berkeley* | 通用机器人视觉表示，通过大规模人类视频预训练。
  
# Embodied Foundation Models

* **LingBot-VLA**: "LingBot-VLA: Scaling Robot Manipulation with Multi-Embodiment Data", *arXiv, Jan 2026*. [[Paper](https://arxiv.org/abs/2601.18692)]

* **X-VLA**: "X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task", *arXiv, Oct 2025*. [[Paper](https://arxiv.org/abs/2510.10274)]

* **TriVLA**: "TriVLA: A Triple-System Vision-Language-Action Model with Episodic World Modeling", *arXiv, Jul 2025*. [[Paper](https://arxiv.org/abs/2507.01424)]

* **EchoVLA**: "EchoVLA: Vision-Language-Action Model with Synergistic Declarative Memory", *arXiv, Nov 2025*. [[Paper](https://arxiv.org/abs/2511.18112)]

* **IntentionVLA**: "IntentionVLA: Embodied Intention Reasoning for Human-Robot Interaction", *arXiv, Oct 2025*. [[Paper](https://arxiv.org/abs/2510.07778)]

* **LoHoVLA**: "LoHoVLA: Vision-Language-Action Model for Long-Horizon Embodied Tasks", *arXiv, Jun 2025*. [[Paper](https://arxiv.org/abs/2506.00411)]

* **OpenVLA**: "OpenVLA: An Open Vision-Language-Action Model", *arXiv, Jun 2024*. [[Paper](https://arxiv.org/abs/2406.09246)]

* **GR-2**: "GR-2: A Generative Video-Language-Action Model for Robot Manipulation", *arXiv, Feb 2024*. [[Paper](https://arxiv.org/abs/2402.06149)]

* **AutoRT**: "AutoRT: Embodied Foundation Models for Large-Scale Robot Orchestration", *arXiv, Jan 2024*. [[Paper](https://arxiv.org/abs/2401.12963)]

---

# Vision-Language-Action (VLA)

* **DexVLA**: "DexVLA: Plug-in Diffusion Experts for Vision-Language-Action Models", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2505.16413)]

* **SmolVLA**: "SmolVLA: Efficient Vision-Language-Action Models for Robotics", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2503.04123)]

* **SwitchVLA**: "SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2507.08421)]

* **TrackVLA**: "TrackVLA: Embodied Visual Tracking with Vision-Language-Action Models", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2504.08962)]

* **SafeVLA**: "SafeVLA: Safety Alignment for Vision-Language-Action Models", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2502.07712)]

* **ObjectVLA**: "ObjectVLA: Open-World Object Manipulation without Demonstrations", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2504.05291)]

* **ChatVLA**: "ChatVLA: Multimodal Understanding and Robot Control", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2503.12438)]

* **Humanoid-VLA**: "Humanoid-VLA: Vision-Language-Action Models for Humanoid Control", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2502.09247)]

* **HiMoE-VLA**: "Hierarchical Mixture-of-Experts for Vision-Language-Action Policies", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2501.08132)]

* **VideoVLA**: "Video Generators as Generalizable Robot Manipulators", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2501.05233)]

---

# Embodied Agents & Reasoning

* **DualVLA**: "DualVLA: Decoupling Reasoning and Action for Embodied Agents", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2506.08755)]

* **Embodied-CoT**: "Chain-of-Thought Reasoning for Embodied Agents", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2503.06721)]

* **ThinkAct**: "ThinkAct: Reasoning-Guided Planning for Embodied Agents", *arXiv, 2025*. [[Paper](https://arxiv.org/abs/2501.04889)]

* **EmbodiedGPT**: "EmbodiedGPT: LLM-based Robot Agent", *arXiv, 2024*. [[Paper](https://arxiv.org/abs/2405.11827)]

* **RoboMatrix**: "RoboMatrix: Skill-Centric Robot Task Planning", *arXiv, 2024*. [[Paper](https://arxiv.org/abs/2406.06833)]

---

# Manipulation

* **ReBot**: "ReBot: Scaling Robot Learning with Real-to-Sim-to-Real Video Synthesis", *arXiv, Mar 2025*. [[Paper](https://arxiv.org/abs/2503.14526)]

* **Octo**: "Octo: An Open-Source Generalist Robot Policy", *RSS 2024*. [[Paper](https://arxiv.org/abs/2405.12213)]

* **VoxPoser**: "VoxPoser: Composable 3D Value Maps for Robot Manipulation", *CoRL 2024*. [[Paper](https://arxiv.org/abs/2307.05973)]

---

# Navigation & Spatial Intelligence

* **RoboTracer**: "RoboTracer: Spatial Trace Reasoning in Vision-Language Models for Robotics", *arXiv, Dec 2025*. [[Paper](https://arxiv.org/abs/2512.13660)]

* **RoboRefer**: "Spatial Referring in Vision-Language Models for Robotics", *arXiv, Jun 2025*. [[Paper](https://arxiv.org/abs/2506.04308)]

---

# Simulation & Sim2Real

* **RealMirror**: "RealMirror: Vision-Language-Action Platform for Embodied AI", *arXiv, Sep 2025*. [[Paper](https://arxiv.org/abs/2509.14687)]

* **EmbodiedGen**: "EmbodiedGen: Generative 3D Worlds for Embodied AI", *arXiv, Jun 2025*. [[Paper](https://arxiv.org/abs/2506.10600)]

* **Genesis**: "Genesis: Universal Physics Engine for Robotics and Embodied AI", *arXiv, 2024*. [[Paper](https://arxiv.org/abs/2402.XXXX)]

---

# Datasets

* **Open-X-Embodiment Dataset**, *2024*. [[Paper](https://arxiv.org/abs/2310.08864)]

* **BridgeData V2**, *2024*. [[Paper](https://arxiv.org/abs/2308.12952)]

---

# Benchmarks & Evaluation

* **ManipBench**, *CVPR 2025*. [[Paper](https://arxiv.org/abs/2503.09174)]

* **RoboTwin**, *CVPR 2025*. [[Paper](https://arxiv.org/abs/2503.17324)]

* **EmbSpatial-Bench**, *2024*. [[Paper](https://arxiv.org/abs/2403.10510)]

---

# Survey

* **Vision-Language-Action Models Survey**, *2025*. [[Paper](https://arxiv.org/abs/2503.04734)]

* **Embodied AI Survey**, *2024*. [[Paper](https://arxiv.org/abs/2407.06886)]


> **说明**：本列表持续更新，欢迎通过 [Issues](https://github.com/LILAN-00/Octoday-Robotics/issues) 或 Pull Request 补充最新论文或修正信息。
## 如何添加新内容

- **添加论文**：在“论文”列表末尾新起一行，格式为：
```markdown
- **[论文标题](论文链接)**  
  *作者* | [论文链接] | [代码链接]  
  简介：一句话说明核心贡献
