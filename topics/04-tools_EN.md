# 🛠️ Tools & Open-Source Projects

> **Updated: June 15, 2026**
> Curated robotics tools, simulation platforms, open-source projects, and development frameworks
> This module merges the original Tools & Platforms and Open-Source Repositories sections

---

<a name="toc"></a>

## Table of Contents

**Categories:** [🎮 Simulation Platforms](#simulation-platforms) · [🤖 Models](#models) · [🏗️ Learning Frameworks](#learning-frameworks) · [🤖 Robot Projects](#robot-projects) · [🧠 Reasoning / RL](#reasoning-rl) · [📖 Tutorials](#tutorials) · [🔧 Middleware & ROS Tools](#middleware-ros) · [🗺️ SLAM & Perception](#slam-perception)

---

<a name="simulation-platforms"></a>

## 🎮 Simulation Platforms

(Items merged from repos and tools)

- **BEHAVIOR-1K** — [`StanfordVL/BEHAVIOR-1K`](https://github.com/StanfordVL/BEHAVIOR-1K) ⭐ 1.5k  
  📄 斯坦福大学出品，1,000 种日常生活活动的具身 AI 基准测试与仿真平台

- **XTDrone** — [`robin-shaun/XTDrone`](https://github.com/robin-shaun/XTDrone) ⭐ 6.5k  
  📄 基于 PX4、ROS 和 Gazebo 的无人机仿真平台，支持集群仿真

- **Prometheus** — [`amov-lab/Prometheus`](https://github.com/amov-lab/Prometheus) ⭐ 4.5k  
  📄 面向自主无人机的开源软件系统，支持目标检测、SLAM 导航、编队控制等

[↑ 回目录](#toc)


---

- **Aerial Gym** — [`github.com/ntnu-arl/aerial_gym_simulator`](https://github.com/ntnu-arl/aerial_gym_simulator)
  📄 An aerial robot simulation environment built on Isaac Gym, designed for drone reinforcement learning.

- **AllenAct** — [`allenact.org`](https://allenact.org/)
  📄 A training framework for embodied AI research that supports multiple environments such as iTHOR, RoboTHOR, and Habitat, along with common RL and IL algorithms.

- **CARLA** — [`carla.org`](https://carla.org)
  📄 An open-source simulator for autonomous driving and robotics research, with city roads, traffic participants, sensors, and scenario scripting support.

- **CoppeliaSim (V-REP)** — [`www.coppeliarobotics.com`](https://www.coppeliarobotics.com)
  📄 A robotics simulation platform that supports remote APIs, embedded scripting, and multiple interfaces for teaching, research, and industrial prototyping.

- **cuRobo** — [`github.com/NVlabs/curobo`](https://github.com/NVlabs/curobo)
  📄 NVIDIA's open-source CUDA-accelerated motion generation library for robotics, supporting inverse kinematics, collision checking, trajectory optimization, and high-DoF planning.

- **DISCOVERSE** — [`air-discoverse.github.io`](https://air-discoverse.github.io/)
  📄 A high-fidelity Real2Sim2Real simulation framework that combines 3D Gaussian splatting scene representations, MuJoCo physics, and control interfaces.

- **Drake** — [`github.com/RobotLocomotion/drake`](https://github.com/RobotLocomotion/drake)
  📄 A toolkit for robot modeling, planning, and control, widely used for system analysis, simulation, and algorithm research.

- **EmbodiedCity** — [`embodied-city.fiblab.net`](https://embodied-city.fiblab.net/)
  📄 A real-world embodied AI platform for open environments, released by Tsinghua University and built on Unreal Engine 5, supporting both online and offline deployment for navigation and task planning in open urban scenes.

- **Gazebo Sim** — [`gazebosim.org`](https://gazebosim.org)
  📄 A high-fidelity open-source robot simulator that supports multiple physics engines such as ODE, Bullet, and DART, with realistic rendering and sensor models.

- **GRUtopia** — [`github.com/OpenRobotLab/GRUtopia`](https://github.com/OpenRobotLab/GRUtopia)
  📄 A general embodied AI simulation platform from the Shanghai AI Lab that offers massive high-quality interactive scenes and data, with lightweight task definition through code.

- **Gymnasium-Robotics** — [`robotics.farama.org`](https://robotics.farama.org/)
  📄 A collection of robot simulation environments built on the Gymnasium API, suitable for RL development, reproducibility, and standardized comparison.

- **Habitat-Lab** — [`github.com/facebookresearch/habitat-lab`](https://github.com/facebookresearch/habitat-lab)
  📄 A high-level development library for embodied AI tasks, typically paired with Habitat Sim for task definition, agent configuration, training, and standardized evaluation.

- **Habitat Sim** — [`github.com/facebookresearch/habitat-sim`](https://github.com/facebookresearch/habitat-sim)
  📄 Meta's high-performance open-source 3D simulator, widely used with Habitat-Lab for large-scale navigation and interaction tasks.

- **Habitat 3.0** — [`aihabitat.org`](https://aihabitat.org/)
  📄 Meta AI's latest social embodied AI simulation platform, focused on human-robot and robot-robot interaction with high-fidelity social behavior simulation and navigation tasks.

- **Meta-World** — [`metaworld.farama.org`](https://metaworld.farama.org/)
  📄 A classic robot manipulation benchmark with 50 tasks, commonly used in multitask learning and meta-RL evaluation.

- **MORSE Simulator** — [`morse-simulator.github.io`](https://morse-simulator.github.io/)
  📄 A Blender-based academic robot simulator supporting mobile robots, human-robot interaction, and multiple middleware integrations.

- **MuJoCo** — [`github.com/google-deepmind/mujoco`](https://github.com/google-deepmind/mujoco)
  📄 A high-performance physics engine for robotics, biomechanics, and graphics, widely used in reinforcement learning and motion control research.

- **NVIDIA Isaac Gym** — [`developer.nvidia.com/isaac-gym`](https://developer.nvidia.com/isaac-gym)
  📄 A high-performance RL simulation environment for robot learning that supports massively parallel GPU-accelerated training.

- **NVIDIA Isaac Lab** — [`developer.nvidia.com/isaac/lab`](https://developer.nvidia.com/isaac/lab)
  📄 An open-source, GPU-accelerated modular framework for robot learning, suited to large-scale policy training and sim-to-real transfer.

- **NVIDIA Isaac Sim** — [`developer.nvidia.com/isaac-sim`](https://developer.nvidia.com/isaac-sim)
  📄 A robot simulation platform built on Omniverse that supports Physical AI training, synthetic data generation, and Sim2Real workflows.

- **NVIDIA RAD-MARS** — [`www.nvidia.com/en-us/omniverse/solutions/robotics`](https://www.nvidia.com/en-us/omniverse/solutions/robotics/)
  📄 A robot-assisted design and simulation platform built on Omniverse, allowing robot hardware design and kinematics testing in physically realistic environments.

- **OmniGibson** — [`behavior.stanford.edu/omnigibson/overview.html`](https://behavior.stanford.edu/omnigibson/overview.html)
  📄 An embodied AI simulation framework built on Isaac Sim, supporting interactive scenes, task definition, data collection, and parallel environment training.

- **PyBullet** — [`github.com/bulletphysics/bullet3`](https://github.com/bulletphysics/bullet3)
  📄 A lightweight Python interface to the Bullet physics engine, suitable for quick prototyping and reinforcement learning experiments.

- **RLBench** — [`github.com/stepjam/RLBench`](https://github.com/stepjam/RLBench)
  📄 A large-scale vision-guided robot manipulation benchmark and learning environment covering RL, imitation learning, multitask, and few-shot settings.

- **RoboCasa** — [`robocasa.ai`](https://robocasa.ai/)
  📄 A large-scale simulation framework for everyday household manipulation tasks, supporting multiple scenes, objects, demonstrations, and benchmarks.

- **robosuite** — [`github.com/ARISE-Initiative/robosuite`](https://github.com/ARISE-Initiative/robosuite)
  📄 A modular robot learning simulation framework and benchmark suite built on MuJoCo, suitable for manipulation research and reproducible experimentation.

- **RobotStudio** — [`www.abb.com/global/en/areas/robotics/products/software/robotstudio-suite`](https://www.abb.com/global/en/areas/robotics/products/software/robotstudio-suite)
  📄 ABB's official robot programming, simulation, and offline programming suite for industrial robot workstation development.

- **RoboTwin 2.0** — [`github.com/RoboTwin-Platform/RoboTwin`](https://github.com/RoboTwin-Platform/RoboTwin)
  📄 A data generation and benchmark platform for bimanual manipulation, emphasizing strong domain randomization, large-scale generation, and standardized evaluation.

- **SAPIEN** — [`github.com/haosulab/SAPIEN`](https://github.com/haosulab/SAPIEN)
  📄 A simulation environment built for part-level interaction and manipulation tasks, with support for articulated object modeling and manipulation learning.

- **SimplerEnv** — [`github.com/simpler-env/SimplerEnv`](https://github.com/simpler-env/SimplerEnv)
  📄 A simulation evaluation environment for real robot manipulation policies, designed to reproduce and compare real-to-sim manipulation methods under unified settings.

- **Unity ML-Agents** — [`github.com/Unity-Technologies/ml-agents`](https://github.com/Unity-Technologies/ml-agents)
  📄 Unity's machine learning agents toolkit, supporting training and evaluation for agents in 3D environments.

- **UnrealCV** — [`unrealcv.org`](https://unrealcv.org/)
  📄 An open-source plugin that connects Unreal Engine with external vision and robotics programs, useful for simulation environments and synthetic data workflows.

- **VIMA** — [`vimalabs.github.io`](https://vimalabs.github.io/)
  📄 A multimodal embodied task benchmark from UIUC and collaborators, designed to evaluate how robot models handle mixed visual, language, and spatial reasoning instructions.

[↑ Back to TOC](#toc)

---



---


- **AI2-THOR** — [`ai2thor.allenai.org`](https://ai2thor.allenai.org/)
  📄 语义交互模拟器。由艾伦研究所开发，拥有200+精细房间和2600+可交互物体，支持复杂的物体状态改变（如切片、烹饪）。

- **cuRobo** — [`github.com/NVlabs/curobo`](https://github.com/NVlabs/curobo)
  📄 NVIDIA 开源的 CUDA 加速机器人运动生成库，支持逆运动学、碰撞检测、轨迹优化与高自由度规划。

- **DeepMind SI-Tuning** — [`github.com/google-deepmind/si_tuning`](https://github.com/google-deepmind/si_tuning)
  📄 VLA模型微调框架。Google DeepMind推出的用于微调RT-2、OpenVLA等视觉-语言-动作模型的代码库，专注于提升机器人在特定任务上的泛化能力。

- **Diffusion Policy** — [`github.com/real-stanford/diffusion_policy`](https://github.com/real-stanford/diffusion_policy)
  📄 基于扩散模型的机器人策略学习框架，常用于模仿学习与操作控制研究。

- **DORA** — [`github.com/dora-rs/dora`](https://github.com/dora-rs/dora)
  📄 面向 AI 机器人应用的数据流中间件，支持低时延、可组合、分布式的数据处理管线。

- **Intern-Robotics** — [`internrobotics.shlab.org.cn`](https://internrobotics.shlab.org.cn/)
  📄 书生具身全栈框架。上海人工智能实验室开源的具身智能全栈框架，涵盖导航、操作、运动大模型等，推动具身大脑的全栈化与量产。

- **LeRobot** — [`huggingface.co/docs/lerobot/main/en/index`](https://huggingface.co/docs/lerobot/main/en/index)
  📄 Hugging Face 推出的真实机器人机器学习工具集，提供模型、数据集和训练工具。

- **Meta-World** — [`metaworld.farama.org`](https://metaworld.farama.org/)
  📄 经典机器人操作 benchmark，包含 50 个操作任务，常用于多任务学习与 meta-RL 评测。

- **MimicGen** — [`github.com/NVlabs/mimicgen`](https://github.com/NVlabs/mimicgen)
  📄 从少量人类示教自动生成大规模机器人数据的数据生成系统，适合扩充 manipulation 训练集。

- **Octo** — [`github.com/octo-models/octo`](https://github.com/octo-models/octo)
  📄 开源通用机器人策略，基于多机器人轨迹预训练，支持语言指令、目标图像和小样本微调。

- **OK-Robot** — [`ok-robot.github.io`](https://ok-robot.github.io/)
  📄 模块化系统集成框架。纽约大学（NYU）开源，专为真实家庭环境设计，通过结合VLM实现零样本（Zero-shot）的取放任务。

- **OpenVLA** — [`github.com/openvla/openvla`](https://github.com/openvla/openvla)
  📄 开源视觉-语言-动作模型，面向通用机器人操作任务，支持微调、训练和评估。

- **OpenXLab** — [`openxlab.org.cn`](https://openxlab.org.cn/)
  📄 具身智能开源开放平台。上海AI实验室推出的综合性平台，提供从数据处理、算法训练到部署的全套工具链，旨在降低具身智能的研发门槛。

- **RobotecAI RAI** — [`github.com/RobotecAI/rai`](https://github.com/RobotecAI/rai)
  📄 RobotecAI 开源的 agentic robotics framework，基于 ROS 2 工具链，支持自然语言交互、多模态能力集成和机器人任务执行。

- **RoboGen** — [`robogen-ai.github.io`](https://robogen-ai.github.io/)
  📄 代码生成式机器人框架。由MIT等机构推出，利用大语言模型自动生成包含感知、规划、控制逻辑的完整Python代码，实现"代码即策略"的自动化生成。

- **robomimic** — [`github.com/ARISE-Initiative/robomimic`](https://github.com/ARISE-Initiative/robomimic)
  📄 面向机器人示教学习的通用框架，提供数据集、离线学习算法和可复现实验基线。

- **RoboTwin 2.0** — [`github.com/RoboTwin-Platform/RoboTwin`](https://github.com/RoboTwin-Platform/RoboTwin)
  📄 面向双臂操作的数据生成与 benchmark 平台，强调强 domain randomization、规模化生成和标准化评测。

- **ROS / ROS2** — [`www.ros.org`](https://www.ros.org)
  📄 机器人操作系统，提供丰富工具和库，支持模块化开发与分布式计算，是机器人软件开发的行业标准。

- **RQT Frame Editor** — [`github.com/ipa320/rqt_frame_editor_plugin`](https://github.com/ipa320/rqt_frame_editor_plugin)
  📄 用于创建和调整 TF 坐标系的 rqt 插件，便于处理多传感器和多机器人坐标关系。

- **SAGE** — [`github.com/eth-easl/sage`](https://github.com/eth-easl/sage)
  📄 具身智能分布式计算框架。由ETH Zurich推出，提供高效的分布式数据流水线和并行计算架构，专门用于加速大规模策略训练和数据处理。

- **Theseus** — [`github.com/facebookresearch/theseus`](https://github.com/facebookresearch/theseus)
  📄 可微非线性优化库，适合机器人和视觉中的状态估计、几何优化、轨迹优化与端到端可微系统构建。

- **Universal Manipulation Interface (UMI)** — [`github.com/real-stanford/universal_manipulation_interface`](https://github.com/real-stanford/universal_manipulation_interface)
  📄 斯坦福开源的通用操作接口，支持多种机器人学习和操作任务。

- **VEX Robotics Software** — [`www.vexrobotics.com/?srsltid=AfmBOoqB_9zu0-eFHO4wzVB_33rsABV6DRRJ_drQfuk67n-MLcUmVy9M`](https://www.vexrobotics.com/?srsltid=AfmBOoqB_9zu0-eFHO4wzVB_33rsABV6DRRJ_drQfuk67n-MLcUmVy9M)
  📄 面向 VEX 机器人平台的软件工具，支持拖放式编程，常用于教育场景。

- **VIMA** — [`vimalabs.github.io`](https://vimalabs.github.io/)
  📄 多模态具身任务基准。由UIUC等机构推出，提供复杂的"搭建积木"类任务，专门用于评测机器人模型在处理视觉、语言及空间推理混合指令时的表现。

<a name="learning-frameworks"></a>

## 🏗️ Learning Frameworks

(Items merged from repos and tools)

- **RLinf** — [`RLinf/RLinf`](https://github.com/RLinf/RLinf) ⭐ 3.7k  
  📄 面向具身和智能体 AI 的强化学习基础设施

- **OpenLoong (Brain)** — [`loongOpen`](https://github.com/loongOpen)  
  📄 青龙人形机器人全栈技能调度框架（上海人形机器人创新中心/开放原子基金会），包含动力学控制(MPC+WBC)、训练平台(Gymloong/MiniGym)

- **AimRT** — [`AimRT/AimRT`](https://github.com/AimRT/AimRT)  
  📄 面向现代机器人领域的运行时开发框架，基于 Modern C++，轻量易部署，兼容 ROS2/HTTP/Grpc

- **Open-TeleVision** — [`OpenTeleVision/TeleVision`](https://github.com/OpenTeleVision/TeleVision)  
  📄 基于 VR 头显的沉浸式机器人遥操作系统，操作者通过第一视角实时控制机器人双臂完成灵巧操作

- **AgileX Cobot Magic** — [`agilexrobotics`](https://github.com/agilexrobotics)  
  📄 基于 Mobile ALOHA 架构的开源双臂移动操作平台（松灵机器人），含 PiPER 机械臂、AGV 底盘和深度相机

[↑ 回目录](#toc)


- **DeepMind SI-Tuning** — [`github.com/google-deepmind/si_tuning`](https://github.com/google-deepmind/si_tuning)
  📄 A VLA fine-tuning framework from Google DeepMind for models such as RT-2 and OpenVLA, focused on improving generalization on task-specific robotic workloads.

- **Diffusion Policy** — [`github.com/real-stanford/diffusion_policy`](https://github.com/real-stanford/diffusion_policy)
  📄 A robot policy learning framework based on diffusion models, commonly used in imitation learning and manipulation control research.

- **DORA** — [`github.com/dora-rs/dora`](https://github.com/dora-rs/dora)
  📄 A dataflow middleware for AI robotics applications that supports low-latency, composable, and distributed data-processing pipelines.

- **Intern-Robotics (ShuSheng)** — [`internrobotics.shlab.org.cn`](https://internrobotics.shlab.org.cn/)
  📄 An open-source full-stack embodied robotics framework from the Shanghai AI Lab, covering navigation, manipulation, and motion foundation models to support embodied AI development at scale.

- **LeRobot** — [`huggingface.co/docs/lerobot/main/en/index`](https://huggingface.co/docs/lerobot/main/en/index)
  📄 Hugging Face's real-world robot machine learning toolkit, providing models, datasets, and training utilities.

- **MimicGen** — [`github.com/NVlabs/mimicgen`](https://github.com/NVlabs/mimicgen)
  📄 A data generation system that scales a small number of human demonstrations into large robot datasets, useful for expanding manipulation training corpora.

- **Octo** — [`github.com/octo-models/octo`](https://github.com/octo-models/octo)
  📄 An open-source general robot policy pretrained on multi-robot trajectories, supporting language instructions, goal images, and few-shot fine-tuning.

- **OK-Robot** — [`ok-robot.github.io`](https://ok-robot.github.io/)
  📄 A modular framework from NYU for real home environments that combines VLMs to perform zero-shot pick-and-place tasks.

- **OpenVLA** — [`github.com/openvla/openvla`](https://github.com/openvla/openvla)
  📄 An open-source vision-language-action model for general robot manipulation, supporting fine-tuning, training, and evaluation.

- **OpenXLab** — [`openxlab.org.cn`](https://openxlab.org.cn/)
  📄 A comprehensive open platform from the Shanghai AI Lab for embodied AI, offering a full toolchain from data processing and algorithm training to deployment.

- **RobotecAI RAI** — [`github.com/RobotecAI/rai`](https://github.com/RobotecAI/rai)
  📄 RobotecAI's open-source agentic robotics framework built on the ROS 2 toolchain, supporting natural-language interaction, multimodal capability integration, and robot task execution.

- **RoboGen** — [`robogen-ai.github.io`](https://robogen-ai.github.io/)
  📄 A code-generative robotics framework from MIT and collaborators that uses large language models to automatically generate full Python policies with perception, planning, and control logic.

- **robomimic** — [`github.com/ARISE-Initiative/robomimic`](https://github.com/ARISE-Initiative/robomimic)
  📄 A general framework for learning from robot demonstrations, with datasets, offline learning algorithms, and reproducible baselines.

- **ROS / ROS2** — [`www.ros.org`](https://www.ros.org)
  📄 The Robot Operating System, with a rich ecosystem of tools and libraries for modular and distributed robot software development.

- **SAGE** — [`github.com/eth-easl/sage`](https://github.com/eth-easl/sage)
  📄 A distributed embodied AI computing framework from ETH Zurich that provides efficient data pipelines and parallel computing for large-scale policy training and data processing.

- **Theseus** — [`github.com/facebookresearch/theseus`](https://github.com/facebookresearch/theseus)
  📄 A differentiable nonlinear optimization library for robotics and vision, suitable for state estimation, geometric optimization, trajectory optimization, and end-to-end differentiable systems.

- **Universal Manipulation Interface (UMI)** — [`github.com/real-stanford/universal_manipulation_interface`](https://github.com/real-stanford/universal_manipulation_interface)
  📄 A general manipulation interface open-sourced by Stanford, supporting a range of robot learning and manipulation tasks.

- **VEX Robotics Software** — [`www.vexrobotics.com/?srsltid=AfmBOoqB_9zu0-eFHO4wzVB_33rsABV6DRRJ_drQfuk67n-MLcUmVy9M`](https://www.vexrobotics.com/?srsltid=AfmBOoqB_9zu0-eFHO4wzVB_33rsABV6DRRJ_drQfuk67n-MLcUmVy9M)
  📄 Software tools for the VEX robotics platform, with drag-and-drop programming support commonly used in educational settings.

[↑ Back to TOC](#toc)

---

<a name="robot-projects"></a>

## 🤖 Robot Projects

### Humanoid Robots

- **AgiBot X1** — [`推理`](https://github.com/AgibotTech/agibot_x1_infer) · [`训练`](https://github.com/AgibotTech/agibot_x1_train) · [`硬件`](https://github.com/AgibotTech/agibot_x1_hardware)  
  📄 智元机器人 X1 完整开源Humanoid Robots项目，包含推理模块、强化学习训练代码和全套硬件设计资料

- **OpenLoong 青龙** — [`loongOpen`](https://github.com/loongOpen)  
  📄 全栈开源Humanoid Robots项目（上海Humanoid Robots创新中心/开放原子基金会），包含动力学控制(MPC+WBC)、硬件设计、训练平台和大规模技能调度框架

- **Fourier N1** — [`FFTAI`](https://github.com/FFTAI)  
  📄 全球首个全开源Humanoid Robots（傅利叶智能），公开全套硬件设计、BOM、装配指南和 Fourier-GRX SDK，1.3m/38kg/3.5m/s

- **EngineAI Humanoid** — [`engineai-robotics/engineai_humanoid`](https://github.com/engineai-robotics/engineai_humanoid)  
  📄 EngineAI（松延动力）双足机器人 SA01/PM01 的开源运动控制算法，采用端到端神经网络实现拟人步态

- **Booster Gym** — [`BoosterRobotics`](https://github.com/BoosterRobotics)  
  📄 Booster T1/K1 Humanoid Robots端到端强化学习运动控制框架（加速进化），含 RoboCup 自主踢球 Demo

- **Humanoid-Gym** — [`roboterax/humanoid-gym`](https://github.com/roboterax/humanoid-gym)  
  📄 基于 Isaac Gym 的Humanoid Robots强化学习训练框架，支持零样本迁移至真实机器人

- **Unitree Qmini** — [`unitreerobotics/Qmini`](https://github.com/unitreerobotics/Qmini)  
  📄 宇树科技开源双足平台，提供全套 BOM/装配指南、RoboTamer4Qmini 控制框架与 URDF 模型

### Quadruped Robots

- **OpenCat** — [`PetoiCamp/OpenCat`](https://github.com/PetoiCamp/OpenCat) ⭐ 15k  
  📄 开源Quadruped Robots平台

- **小米 CyberDog** — [`MiRoboticsLab/cyberdog_ros2`](https://github.com/MiRoboticsLab/cyberdog_ros2)  
  📄 小米 CyberDog Quadruped Robots的开源软件和硬件资料

- **宇树科技Quadruped Robots ROS** — [`unitreerobotics/unitree_ros`](https://github.com/unitreerobotics/unitree_ros)  
  📄 宇树科技Quadruped Robots Go1/Go2 的 ROS 驱动包

### Arms & Desktop Robots

- **vlm_arm** — [`TommyZihao/vlm_arm`](https://github.com/TommyZihao/vlm_arm)  
  📄 机械臂 + 大模型 + 多模态（同济子豪兄）

- **超迷你机械臂 (Dummy-Robot)** — [`peng-zhihui/Dummy-Robot`](https://github.com/peng-zhihui/Dummy-Robot)  
  📄 自制迷你机械臂机器人（稚晖君）

- **X-Bot 智能机械臂** — [`peng-zhihui/X-Bot`](https://github.com/peng-zhihui/X-Bot)  
  📄 基于 CoreXY 结构的写字机械臂（稚晖君）

- **ElectronBot 迷你桌面机器人** — [`peng-zhihui/ElectronBot`](https://github.com/peng-zhihui/ElectronBot)  
  📄 非常小巧的桌面机器人（稚晖君）

- **解魔方机器人** — [`diy-robots.com`](http://www.diy-robots.com/?page_id=46)  
  📄 基于乐高的解魔方机器人（动力老男孩）

### Mobile Robots

- **MiniRover 火星车** — [`peng-zhihui/MiniRover-Hardware`](https://github.com/peng-zhihui/MiniRover-Hardware)  
  📄 自制火星车的开源资料（稚晖君）

- **ONE-Robot 独轮机器人** — [`peng-zhihui/ONE-Robot`](https://github.com/peng-zhihui/ONE-Robot)  
  📄 基于 IMU 和 STM32 的独轮自平衡机器人（稚晖君）


- **视觉SLAM十四讲** — [`gaoxiang12/slambook2`](https://github.com/gaoxiang12/slambook2) ⭐ 12k  
  📄 SLAM 领域经典中文教程及配套代码（高翔）

- **VINS-Mono** — [`HKUST-Aerial-Robotics/VINS-Mono`](https://github.com/HKUST-Aerial-Robotics/VINS-Mono) ⭐ 5k  
  📄 鲁棒通用的单目视觉惯性状态估计器（香港科技大学）

- **VINS-Fusion** — [`HKUST-Aerial-Robotics/VINS-Fusion`](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion)  
  📄 基于优化的多传感器状态估计器，支持单/双目相机+IMU 融合

- **LIO-SAM** — [`TixiaoShan/LIO-SAM`](https://github.com/TixiaoShan/LIO-SAM) ⭐ 3.5k  
  📄 紧耦合激光惯性里程计（平滑和建图），被广泛引用的 LiDAR SLAM 方案

- **FAST_LIO** — [`hku-mars/FAST_LIO`](https://github.com/hku-mars/FAST_LIO) ⭐ 2.5k  
  📄 计算高效且鲁棒的 LiDAR 惯性里程计（港大 MARS 实验室）

- **FAST-LIVO2** — [`hku-mars/FAST-LIVO2`](https://github.com/hku-mars/FAST-LIVO2)  
  📄 快速、直接的 LiDAR-惯性-视觉里程计，多传感器紧耦合方案

- **R3LIVE** — [`hku-mars/r3live`](https://github.com/hku-mars/r3live) ⭐ 2.0k  
  📄 鲁棒、实时的 RGB 彩色 LiDAR-惯性-视觉紧耦合状态估计与建图

- **宇树科技 4D LiDAR SLAM** — [`unitreerobotics/point_lio_unilidar`](https://github.com/unitreerobotics/point_lio_unilidar)  
  📄 基于 Point-LIO 算法适配宇树 L1 4D LiDAR 的 SLAM 方案

### Grasping & Manipulation

- **AnyGrasp** — [`graspnet/anygrasp_sdk`](https://github.com/graspnet/anygrasp_sdk)  
  📄 高效通用的 6 自由度抓取位姿估计算法（上海AI实验室），支持任意物体的机器人抓取检测

- **小觅双目相机系列** — [`slightech/MYNT-EYE-S-SDK`](https://github.com/slightech/MYNT-EYE-S-SDK)  
  📄 小觅双目相机系列（MYNTAI），提供完整的 SLAM 和视觉算法解决方案

### Others


- **ALOHA 2** — [`aloha-2.github.io`](https://aloha-2.github.io/)
  📄 面向双臂遥操作与具身数据采集的低成本开源硬件平台，附带教程与 MuJoCo 仿真模型。

- **北京Humanoid Robots创新中心·慧思开物** — [`login.x-humanoid-cloud.com/?responseType=code&clientId=fd6c22fb&redirectUri=https%3A%2F%2Fopen.x-humanoid-cloud.com%2Fhome&stamp=1778429122172&env=cloud`](https://login.x-humanoid-cloud.com/?responseType=code&clientId=fd6c22fb&redirectUri=https%3A%2F%2Fopen.x-humanoid-cloud.com%2Fhome&stamp=1778429122172&env=cloud)
  📄 面向通用具身智能场景的工具链平台，覆盖技能调用、智能体配置到场景部署。

- **DexCap** — [`dexcap.github.io`](https://dexcap.github.io/)
  📄 灵巧手数据采集系统。斯坦福开源，通过手部动作捕捉系统和深度相机，低成本、大规模地采集人类灵巧手操作数据，支持精细化的Sim-to-Real迁移。

- **Dobb-E** — [`dobb-e.com`](https://dobb-e.com/)
  📄 硬件到数据的全栈方案。NYU开源，包含低成本手持采集硬件"Stick"、数据集和模仿学习框架，核心是让机器人在15分钟示教后学会新家务。

- **GR-1 (ByteDance Model)** — [`github.com/bytedance/GR-1`](https://github.com/bytedance/GR-1)
  📄 字节跳动开源的 GPT 风格视觉机器人操作模型，面向语言条件下的多任务机器人操作学习与动作预测，需与智元机器人的 GR-1 Humanoid Robots整机区分。

- **京东 JoyInside** — [`joyinside.com`](https://joyinside.com/)
  📄 面向机器人与 AI 玩具等智能硬件的对话智能体平台。

- **kscale·K-Bot** — [`docs.kscale.dev/category/k-bot`](https://docs.kscale.dev/category/k-bot)
  📄 面向开发者和研究人员的开源全栈Humanoid Robots平台。

- **智元灵创平台 (LinkCraft)** — [`www.agibot.com.cn/filepage/295.html`](https://www.agibot.com.cn/filepage/295.html)
  📄 智元机器人推出的零代码机器人内容创作平台，支持动作模仿、语音驱动和任务脚本生成。

- **腾讯 Tairos (钛螺丝)** — [`tairos.tencent.com`](https://tairos.tencent.com/)
  📄 面向机器人场景的具身智能开放平台，提供模型、开发工具和数据服务。

- **Viam** — [`www.viam.com`](https://www.viam.com)
  📄 面向机器人构建、部署和管理的软件平台，提供统一 API、模块注册、远程运维和车队级管理能力。

- **网易灵动·灵掘** — [`lingdong.fuxi.163.com/productSummary/wj`](https://lingdong.fuxi.163.com/productSummary/wj)
  📄 面向矿山挖掘机装车场景的具身智能模型与训练框架。
- **网易灵动·灵掘** — [`lingdong.fuxi.163.com/productSummary/wj`](https://lingdong.fuxi.163.com/productSummary/wj)
  📄 面向矿山挖掘机装车场景的具身智能模型与训练框架。

- **Viam** — [`www.viam.com`](https://www.viam.com)
  📄 面向机器人构建、部署和管理的软件平台，提供统一 API、模块注册、远程运维和车队级管理能力。

- **腾讯 Tairos (钛螺丝)** — [`tairos.tencent.com`](https://tairos.tencent.com/)
  📄 面向机器人场景的具身智能开放平台，提供模型、开发工具和数据服务。

- **智元灵创平台 (LinkCraft)** — [`www.agibot.com.cn/filepage/295.html`](https://www.agibot.com.cn/filepage/295.html)
  📄 智元机器人推出的零代码机器人内容创作平台，支持动作模仿、语音驱动和任务脚本生成。

- **kscale·K-Bot** — [`docs.kscale.dev/category/k-bot`](https://docs.kscale.dev/category/k-bot)
  📄 面向开发者和研究人员的开源全栈Humanoid Robots平台。

- **京东 JoyInside** — [`joyinside.com`](https://joyinside.com/)
  📄 面向机器人与 AI 玩具等智能硬件的对话智能体平台。

- **GR-1 (ByteDance Model)** — [`github.com/bytedance/GR-1`](https://github.com/bytedance/GR-1)
  📄 字节跳动开源的 GPT 风格视觉机器人操作模型，面向语言条件下的多任务机器人操作学习与动作预测，需与智元机器人的 GR-1 Humanoid Robots整机区分。

- **Dobb-E** — [`dobb-e.com`](https://dobb-e.com/)
  📄 硬件到数据的全栈方案。NYU开源，包含低成本手持采集硬件"Stick"、数据集和模仿学习框架，核心是让机器人在15分钟示教后学会新家务。

- **DexCap** — [`dexcap.github.io`](https://dexcap.github.io/)
  📄 灵巧手数据采集系统。斯坦福开源，通过手部动作捕捉系统和深度相机，低成本、大规模地采集人类灵巧手操作数据，支持精细化的Sim-to-Real迁移。

- **北京Humanoid Robots创新中心·慧思开物** — [`login.x-humanoid-cloud.com/?responseType=code&clientId=fd6c22fb&redirectUri=https%3A%2F%2Fopen.x-humanoid-cloud.com%2Fhome&stamp=1778429122172&env=cloud`](https://login.x-humanoid-cloud.com/?responseType=code&clientId=fd6c22fb&redirectUri=https%3A%2F%2Fopen.x-humanoid-cloud.com%2Fhome&stamp=1778429122172&env=cloud)
  📄 面向通用具身智能场景的工具链平台，覆盖技能调用、智能体配置到场景部署。

- **ALOHA 2** — [`aloha-2.github.io`](https://aloha-2.github.io/)
  📄 面向双臂遥操作与具身数据采集的低成本开源硬件平台，附带教程与 MuJoCo 仿真模型。

- **宇树科技 XR 遥操作** — [`unitreerobotics/xr_teleoperate`](https://github.com/unitreerobotics/xr_teleoperate)  
  📄 基于 XR 设备（Apple Vision Pro/Quest 等）的 H1/G1 Humanoid Robots遥操作系统

- **RoboWiki** — [`yfrobotics/robowiki`](https://github.com/yfrobotics/robowiki)  
  📄 机器人领域的维基百科（云飞机器人实验室）

[↑ 回目录](#toc)


- **ALOHA 2** — [`aloha-2.github.io`](https://aloha-2.github.io/)
  📄 A low-cost open-source hardware platform for bimanual teleoperation and embodied data collection, bundled with tutorials and MuJoCo simulation models.

- **Beijing Humanoid Robot Innovation Center · Huisi Kaiwu** — [`login.x-humanoid-cloud.com/?responseType=code&clientId=fd6c22fb&redirectUri=https%3A%2F%2Fopen.x-humanoid-cloud.com%2Fhome&stamp=1778429122172&env=cloud`](https://login.x-humanoid-cloud.com/?responseType=code&clientId=fd6c22fb&redirectUri=https%3A%2F%2Fopen.x-humanoid-cloud.com%2Fhome&stamp=1778429122172&env=cloud)
  📄 A toolchain platform for general-purpose embodied AI applications, covering skill invocation, agent configuration, and real-world deployment.

- **DexCap** — [`dexcap.github.io`](https://dexcap.github.io/)
  📄 A dexterous-hand data collection system from Stanford that uses motion capture and depth cameras to collect human hand-manipulation data at scale and low cost, supporting fine-grained sim-to-real transfer.

- **Dobb-E** — [`dobb-e.com`](https://dobb-e.com/)
  📄 A full-stack pipeline from hardware to data released by NYU, including a low-cost handheld data collection device called "Stick," a dataset, and an imitation-learning framework for teaching household tasks from 15 minutes of demonstration.

- **GR-1 (ByteDance Model)** — [`github.com/bytedance/GR-1`](https://github.com/bytedance/GR-1)
  📄 ByteDance's open-source GPT-style vision-based robot manipulation model for language-conditioned multitask learning and action prediction, distinct from Agibot's GR-1 humanoid hardware.

- **JD JoyInside** — [`joyinside.com`](https://joyinside.com/)
  📄 A conversational agent platform for intelligent hardware such as robots and AI toys.

- **kscale·K-Bot** — [`docs.kscale.dev/category/k-bot`](https://docs.kscale.dev/category/k-bot)
  📄 An open-source full-stack humanoid robot platform for developers and researchers.

- **AgiBot LinkCraft Platform** — [`www.agibot.com.cn/filepage/295.html`](https://www.agibot.com.cn/filepage/295.html)
  📄 Agibot's zero-code robot content creation platform, supporting motion imitation, speech-driven generation, and task script creation.

- **Tencent Tairos (Chinese nickname: "Titanium Screw")** — [`tairos.tencent.com`](https://tairos.tencent.com/)
  📄 An open embodied AI platform for robotics scenarios, providing models, development tools, and data services.

- **Viam** — [`www.viam.com`](https://www.viam.com)
  📄 A software platform for building, deploying, and managing robots, with a unified API, module registry, remote operations, and fleet-level management.

- **NetEase Lingdong · Lingjue** — [`lingdong.fuxi.163.com/productSummary/wj`](https://lingdong.fuxi.163.com/productSummary/wj)
  📄 NetEase Lingdong's embodied AI model and training framework for mining excavator loading scenarios.

[↑ Back to TOC](#toc)

---

<a name="tutorials"></a>

## 📖 Tutorials

- **every-embodied** — [`datawhalechina/every-embodied`](https://github.com/datawhalechina/every-embodied) ⭐ 2.2k  
  📄 仅需 Python 基础，从 0 构建 VLA/OpenVLA/SmolVLA/Pi0 的具身智能学习路径

- **Unitree Robot Control Guide** — [`unitreerobotics/unitree_guide`](https://github.com/unitreerobotics/unitree_guide)  
  📄 Open-source tutorial for Unitree quadruped robot control

[↑ 回目录](#toc)


---

<a name="reasoning-rl"></a>

## 🧠 Reasoning / Reinforcement Learning

- **OpenR1-Multimodal** — [`EvolvingLMMs-Lab/OpenR1-Multimodal`](https://github.com/EvolvingLMMs-Lab/OpenR1-Multimodal) ⭐ 1.5k  
  📄 R1 推理范式在多模态模型上的探索，开源 8K 多模态 RL 训练样本

- **unitree_rl_gym** — [`unitreerobotics/unitree_rl_gym`](https://github.com/unitreerobotics/unitree_rl_gym)  
  📄 宇树科技四足/人形机器人强化学习训练框架，基于 Isaac Gym

- **unitree_rl_lab** — [`IsaacLab`](https://github.com/unitreerobotics/unitree_rl_lab) · [`MuJoCo`](https://github.com/unitreerobotics/unitree_rl_mjlab)  
  📄 宇树科技机器人强化学习实现，分别基于 Isaac Lab 和 MuJoCo

- **unitree_IL_lerobot** — [`unitreerobotics/unitree_IL_lerobot`](https://github.com/unitreerobotics/unitree_IL_lerobot)  
  📄 基于 LeRobot 框架的模仿学习工具，用于 G1 双臂灵巧手数据的训练与测试

[↑ 回目录](#toc)


---


<a name="slam-perception"></a>

## 🗺️ SLAM & Perception

- **AprilTag** — [`github.com/AprilRobotics/apriltag`](https://github.com/AprilRobotics/apriltag)
  📄 A widely used visual fiducial system for robotics, supporting tag detection, pose estimation, and camera / robot calibration.

- **Cartographer** — [`google-cartographer-ros.readthedocs.io`](https://google-cartographer-ros.readthedocs.io/)
  📄 Google's classic real-time 2D / 3D SLAM system, supporting multi-sensor mapping, localization, and loop-closure optimization.

- **Kalibr** — [`github.com/ethz-asl/kalibr`](https://github.com/ethz-asl/kalibr)
  📄 A multi-sensor calibration toolbox supporting camera intrinsics, multi-camera setups, and camera-IMU joint calibration.

- **Nav2 (Navigation2)** — [`github.com/ros-navigation/navigation2`](https://github.com/ros-navigation/navigation2)
  📄 A ROS 2 navigation framework that provides a full mobile-robot navigation stack, including localization, planning, control, and recovery behaviors.

- **Open3D** — [`www.open3d.org`](https://www.open3d.org)
  📄 A modern 3D data processing library for point clouds, reconstruction, registration, visualization, and 3D machine learning.

- **OpenCV** — [`opencv.org`](https://opencv.org/)
  📄 A classic computer vision library providing image processing, feature extraction, detection, tracking, and geometric vision fundamentals.

- **ORB-SLAM3** — [`github.com/UZ-SLAMLab/ORB_SLAM3`](https://github.com/UZ-SLAMLab/ORB_SLAM3)
  📄 An open-source visual / visual-inertial / multi-map SLAM system supporting monocular, stereo, and RGB-D cameras.

- **PCL (Point Cloud Library)** — [`pointclouds.org`](https://pointclouds.org/)
  📄 A classic point cloud processing library covering filtering, segmentation, registration, reconstruction, visualization, and other core 3D perception functions.

- **RTAB-Map** — [`introlab.github.io/rtabmap`](https://introlab.github.io/rtabmap/)
  📄 A visual / RGB-D / LiDAR SLAM framework based on graph optimization and appearance-based loop closure, suitable for large-scale mapping and localization.

- **RViz / RViz2** — [`docs.ros.org/en/rolling/p/rviz2`](https://docs.ros.org/en/rolling/p/rviz2/)
  📄 The core 3D visualization tool in ROS / ROS 2 for real-time inspection of robot models, TF, point clouds, paths, and maps.

[↑ Back to TOC](#toc)

---

<a name="middleware-ros"></a>

## 🔧 Middleware & ROS Tools

- **Cyclone DDS** — [`projects.eclipse.org/projects/iot.cyclonedds`](https://projects.eclipse.org/projects/iot.cyclonedds)
  📄 An Eclipse Foundation DDS implementation known for robustness and network adaptability, widely used in ROS 2 deployment.

- **DDS (Data Distribution Service)** — [`www.omg.org/omg-dds-portal/index.htm`](https://www.omg.org/omg-dds-portal/index.htm)
  📄 The publish-subscribe communication standard for real-time distributed systems and the middleware foundation behind ROS 2.

- **Fast DDS (formerly Fast RTPS)** — [`fast-dds.docs.eprosima.com/en/latest/index.html`](https://fast-dds.docs.eprosima.com/en/latest/index.html)
  📄 eProsima's DDS implementation, providing high-performance and configurable communication middleware for ROS 2.

- **MQTT** — [`mqtt.org`](https://mqtt.org/)
  📄 A lightweight publish-subscribe messaging protocol commonly used for robot edge devices, gateways, and cloud data transport.

- **Open-RMF** — [`www.open-rmf.org`](https://www.open-rmf.org)
  📄 An open-source framework for coordinating multi-robot fleets and building infrastructure, supporting task scheduling, resource coordination, and interoperability.

- **Zenoh** — [`zenoh.io`](https://zenoh.io/)
  📄 A lightweight data communication protocol and middleware for robots and edge systems, well suited for efficient pub/sub and query workflows in distributed settings.

- **Foxglove** — [`foxglove.dev`](https://foxglove.dev)
  📄 A data-visualization and observability platform for robotics and Physical AI, supporting ROS, MCAP, 3D scenes, and multimodal log debugging.

- **PlotJuggler** — [`github.com/facontidavide/PlotJuggler`](https://github.com/facontidavide/PlotJuggler)
  📄 A visualization and analysis tool for robot time-series data, ideal for topic debugging, log replay, and metric comparison.

- **ros2_latency_analysis** — [`github.com/TUM-AVS/ros2_latency_analysis`](https://github.com/TUM-AVS/ros2_latency_analysis)
  📄 A latency analysis tool for ROS 2 that helps break down end-to-end, communication, and computation bottlenecks.

- **ROSboard** — [`github.com/dheera/rosboard`](https://github.com/dheera/rosboard)
  📄 A lightweight tool that turns ROS / ROS 2 topics into web dashboards for remote monitoring and mobile viewing.

- **RQT Frame Editor** — [`github.com/ipa320/rqt_frame_editor_plugin`](https://github.com/ipa320/rqt_frame_editor_plugin)
  📄 An rqt plugin for creating and adjusting TF frames, useful for managing multi-sensor and multi-robot coordinate relationships.

- **rqt_plot** — [`docs.ros.org/en/rolling/p/rqt_plot`](https://docs.ros.org/en/rolling/p/rqt_plot/)
  📄 A common ROS / ROS 2 plotting plugin for viewing topic values in real time during tuning and debugging.

- **system_fingerprint** — [`github.com/MetroRobots/ros_system_fingerprint`](https://github.com/MetroRobots/ros_system_fingerprint)
  📄 A system snapshot tool for ROS / ROS 2 runtime environments, nodes, topics, and TF state, useful for debugging and delivery validation.

- **Webviz** — [`webviz.io`](https://webviz.io/)
  📄 A browser-based visualization platform for ROS bag files and live robot data, useful for layout-based analysis, replay, and remote debugging.

- **AI2-THOR** — [`ai2thor.allenai.org`](https://ai2thor.allenai.org/)
  📄 A semantic interactive simulator from the Allen Institute, featuring 200+ detailed rooms and 2600+ interactive objects, with support for complex state changes such as slicing and cooking.

- **Arduino IDE** — [`www.arduino.cc`](https://www.arduino.cc)
  📄 An open-source electronics prototyping environment suited for quick sensor, actuator, and control-board integration, with support for C / C++ programming.

- **BEHAVIOR** — [`behavior.stanford.edu`](https://behavior.stanford.edu/)
  📄 A large-scale interactive simulation benchmark built on the SAPIEN engine, with 100 household objects and 30 complex tasks such as "hang up a wet towel," providing a full testbed for physical interaction capabilities.

- **Clearpath·Husky** — [`clearpathrobotics.com`](https://clearpathrobotics.com)
  📄 A common ROS research mobile robot platform with standardized interfaces, well suited to outdoor navigation and algorithm validation.

- **Clearpath·TurtleBot 4** — [`www.turtlebot.com`](https://www.turtlebot.com/)
  📄 A plug-and-play ROS 2 starter platform for teaching and research, ideal for navigation and multi-sensor experiments.

- **Genesis** — [`genesis-embodied-ai.github.io`](https://genesis-embodied-ai.github.io/)
  📄 A general-purpose simulation engine for robot learning, designed for generative physical intelligence and integrating rigid-body, fluid, and soft-body solvers for complex scenarios.

- **ManiSkill3** — [`github.com/haosulab/ManiSkill`](https://github.com/haosulab/ManiSkill)
  📄 The next-generation manipulation simulation framework from the Shanghai AI Lab, designed for training general manipulation policies with more complex articulated objects and more efficient parallel simulation.

- **MoveIt** — [`moveit.ai`](https://moveit.ai)
  📄 A motion planning, manipulation, and kinematics framework for ROS, widely used for arm planning, grasping, and task orchestration.

- **OMPL** — [`ompl.kavrakilab.org`](https://ompl.kavrakilab.org)
  📄 An open-source motion planning library that includes many classic sampling-based planners for path planning and arm planning.

- **Webots** — [`cyberbotics.com`](https://cyberbotics.com)
  📄 An open-source cross-platform desktop robot simulation application with a complete environment for modeling, programming, and simulation.

[↑ Back to TOC](#toc)

---

*Data updated: June 15, 2026*
