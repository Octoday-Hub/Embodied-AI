## 🛠️ 工具与平台 · Tools & Platforms

> 具身智能与机器人开发工具集锦，涵盖仿真环境、开发框架、数据集、硬件平台等。本列表持续更新，**欢迎补充**（可通过 Issues 或 PR 提交）。

### 📌 分类导航
- [🖥️ 仿真平台与物理引擎](#simulation)
- [🧠 具身智能平台与开发框架](#framework)
- [🤖 机器人硬件与开发平台](#hardware)
- [⚙️ 机器人开发工具与SDK](#devtools)
- [🏢 机器人公司开源项目](#opensource)

---

<a id="simulation"></a>
## 🖥️ 仿真平台与物理引擎

| 工具名称 | 简介 | 链接 |
|:---|:---|:---|
| **Gazebo Sim** | 高保真度开源机器人仿真器，支持多种物理引擎（ODE、Bullet、DART），提供逼真渲染和传感器模型，是ROS生态标准仿真平台 | [官网](https://gazebosim.org) |
| **MuJoCo** | 高性能物理引擎，专为机器人、生物力学和图形学设计，被DeepMind收购后开源，广泛应用于强化学习和运动控制研究 | [GitHub](https://github.com/google-deepmind/mujoco) |
| **NVIDIA Isaac Sim** | 基于Omniverse构建的机器人仿真平台，支持物理AI训练、合成数据生成和Sim2Real迁移 | [官网](https://developer.nvidia.com/isaac-sim) |
| **NVIDIA Isaac Gym** | 高性能强化学习仿真环境，专为机器人学习设计，支持GPU加速训练 | [官网](https://developer.nvidia.com/isaac-gym) |
| **Genesis** | 通用物理引擎，专为机器人/具身智能/物理AI设计，支持多种材料物理现象模拟，轻量、快速、Python友好，GitHub 22k+ stars | [GitHub](https://github.com/Genesis-Embodied-AI/Genesis) |
| **Habitat Sim** | Meta开源的高性能3D仿真器，用于具身智能研究，通常与Habitat-Lab配合使用，支持大规模场景导航 | [GitHub](https://github.com/facebookresearch/habitat-sim) |
| **PyBullet** | 基于Bullet物理引擎的Python接口，轻量易用，适合快速原型开发和强化学习 | [GitHub](https://github.com/bulletphysics/bullet3) |
| **SAPIEN** | 模拟部件级交互环境，支持铰接物体操作，由斯坦福大学开发 | [GitHub](https://github.com/haosulab/SAPIEN) |
| **Webots** | 开源多平台机器人仿真桌面应用，提供完整的建模、编程和仿真环境 | [官网](https://cyberbotics.com) |
| **CoppeliaSim (V-REP)** | 先进的机器人仿真平台，支持多种编程接口（远程API、内嵌脚本），适用于教育、研究和工业 | [官网](https://www.coppeliarobotics.com) |
| **Aerial Gym** | 基于Isaac Gym的空中机器人仿真环境，支持无人机强化学习训练 | [GitHub](https://github.com/ntnu-arl/aerial_gym_simulator) |
| **Unity ML-Agents** | Unity游戏引擎的机器学习代理工具包，支持智能体在3D环境中的训练 | [GitHub](https://github.com/Unity-Technologies/ml-agents) |

---

<a id="framework"></a>
## 🧠 具身智能平台与开发框架

| 工具名称 | 简介 | 链接 |
|:---|:---|:---|
| **智元灵创平台 (LinkCraft)** | 智元机器人推出的全球首个零代码机器人内容创作平台，支持动作模仿、语音驱动、群控演绎，用户可通过自然语言描述生成机器人任务脚本 | [官网](https://www.agibot.com.cn/filepage/295.html) |
| **腾讯 Tairos (钛螺丝)** | 具身智能开放平台，首创模块化方式提供大模型、开发工具和数据服务，即插即用赋能机器人行业 | [官网](https://ai.tencent.com) |
| **商汤悟能** | 具身智能平台，以具身世界模型为核心引擎，提供感知、视觉导航及多模态交互能力 | [官网](https://www.sensetime.com) |
| **京东 JoyInside** | 附身智能平台，将角色大模型驱动对话智能体植入机器人、AI玩具等智能硬件 | [官网](https://www.jd.com) |
| **北京人形机器人创新中心·慧思开物** | 全球首个“一脑多能、一脑多机”通用具身智能平台，提供技能调用、智能体配置到场景部署的完整工具链 | [官网](https://www.bjhri.com) |
| **网易灵动·灵掘** | 全球首个专为露天矿山挖掘机装车场景打造的具身智能模型，端到端训练框架“机械智心” | [官网](https://fuxi.netease.com) |
| **ROS / ROS2** | 机器人操作系统，提供丰富的工具和库，支持模块化开发和分布式计算，是机器人软件开发的行业标准 | [官网](https://www.ros.org) |
| **OpenVLA** | 开源通用机器人操作策略模型，支持多机器人即插即用和参数高效微调 | [GitHub](https://github.com/openvla/openvla) |
| **GR-1 (ByteDance)** | 字节跳动开源的大规模视频生成预训练模型，用于视觉机器人操作 | [GitHub](https://github.com/bytedance/GR-1) |
| **Universal Manipulation Interface (UMI)** | 斯坦福开源的通用操作接口，支持多种机器人学习任务 | [GitHub](https://github.com/real-stanford/universal_manipulation_interface) |
| **Diffusion Policy** | 斯坦福开源的扩散策略框架，用于模仿学习和机器人控制 | [GitHub](https://github.com/real-stanford/diffusion_policy) |
| **Drake** | 规划与控制工具包，由丰田研究所开发，用于机器人系统建模与分析 | [GitHub](https://github.com/RobotLocomotion/drake) |
| **OMPL** | 开源运动规划库，包含多种经典运动规划算法 | [官网](https://ompl.kavrakilab.org) |

---

<a id="hardware"></a>
## 🤖 机器人硬件与开发平台

| 工具名称 | 简介 | 链接 |
|:---|:---|:---|
| **猎户星空·豹小秘2** | 服务机器人AI开发平台，采用“实时混核架构”，支持ROS/ROS2开发，内置Orion-14B大模型 | [官网](https://www.orionstar.com) |
| **松灵机器人·Scout系列** | 四轮差速驱动底盘，开放CAN总线协议，原生支持ROS，适用于室外非结构化地形 | [官网](https://www.agilex.ai) |
| **九号机器人·RMP系列** | 模块化移动平台，通过NVIDIA Isaac AMR验证，集成Jetson AGX Orin模块 | [官网](https://www.segwayrobotics.com) |
| **Clearpath·Husky** | ROS科研标准平台，完全开源底层控制，预留标准化电气接口 | [官网](https://clearpathrobotics.com) |
| **Clearpath·TurtleBot 4** | ROS2教学标准教具，集成树莓派和空间AI立体相机，开箱即用 | [官网](https://turtlebot.github.io) |
| **斯坦德·OASIS系列** | 工业AMR平台，覆盖300kg-2000kg载重，支持二次集成 | [官网](https://www.standard-robots.com) |
| **思岚科技·Apollo系列** | 商用导航算法验证平台，支持调整路径规划权重、重定位策略 | [官网](https://www.slamtec.com) |
| **大象机器人·myAGV** | 桌面级全向移动平台，主控兼容树莓派/Jetson Nano，完全开源 | [官网](https://www.elephantrobotics.com) |
| **kscale·K-Bot** | 开源全栈人形机器人平台，面向开发者和研究人员 | [官网](https://kscale.dev) |
| **Unitree (宇树科技)** | 全球领先的四足/人形机器人公司，核心部件自研率超90%，产品包括Go2、H1、G1系列 | [官网](https://www.unitree.com) |
| **Figure AI** | 美国通用人形机器人公司，Figure 02具备端到端学习能力 | [官网](https://www.figure.ai) |
| **1X (Kind Humanoid)** | 挪威公司，NEO家用机器人主打家庭场景 | [官网](https://www.1x.tech) |
| **Sanctuary AI·Phoenix** | 加拿大公司的人形机器人，第八代触觉传感器领先 | [官网](https://sanctuary.ai) |

---

<a id="devtools"></a>
## ⚙️ 机器人开发工具与SDK

| 工具名称 | 简介 | 链接 |
|:---|:---|:---|
| **Arduino IDE** | 开源电子原型平台，适合初学者和非专业人士，支持C/C++编程 | [官网](https://www.arduino.cc) |
| **RobotStudio** | ABB官方机器人编程、仿真和离线编程软件，提高编程效率 | [官网](https://new.abb.com/products/robotics/robotstudio) |
| **Microsoft Robotics Developer Studio** | Windows平台机器人开发工具，包含可视化编程和仿真环境 | [官网](https://www.microsoft.com/en-us/download/details.aspx?id=29081) |
| **VEX Robotics Software** | 专为VEX机器人平台设计，支持拖放式编程，适合教育领域 | [官网](https://www.vexrobotics.com) |
| **TagUI** | RPA命令行接口工具，强调语言的简单自然 | [GitHub](https://github.com/kelaberetiv/TagUI) |
| **ChatTTS** | 生成式语音模型，用于日常对话 | [GitHub](https://github.com/2noise/ChatTTS) |
| **Hallo2** | 长时程、高分辨率音频驱动人像动画生成 | [GitHub](https://github.com/fudan-generative-vision/hallo2) |
| **Real3D-Portrait** | 单图逼真3D说话人像合成 | [GitHub](https://github.com/yerfor/Real3DPortrait) |

---

<a id="opensource"></a>
## 🏢 机器人公司开源项目

| 工具名称 | 简介 | 链接 |
|:---|:---|:---|
| **智元机器人** | 远征系列工业人形机器人、灵犀系列协作机器人，灵创平台零代码内容创作 | [官网](https://www.agibot.com) |
| **银河通用 (Galbot)** | GALBOT G1轮式双臂机器人，采用“双臂+单腿+轮式底盘”设计 | [官网](https://www.galbot.com) |
| **逐际动力 (LimX Dynamics)** | LimXOmni全尺寸人形机器人、TRON多形态基座 | [官网](https://www.limxdynamics.com) |
| **星动纪元 (Robotera)** | 双足人形机器人L7、灵巧手XHAND 1 | [官网](https://www.robotera.com) |
| **波士顿动力 (Boston Dynamics)** | Electric Atlas人形机器人、Spot四足机器人、Stretch仓库机器人 | [官网](https://bostondynamics.com) |
| **特斯拉 (Tesla Optimus)** | Optimus Gen 3人形机器人，FSD自动驾驶AI迁移 | [官网](https://www.tesla.com/optimus) |
| **Agility Robotics·Digit** | 专注物流场景的双足机器人 | [官网](https://agilityrobotics.com) |
| **Apptronik·Apollo** | NASA衍生公司的人形机器人，与Jabil合作大规模生产 | [官网](https://apptronik.com) |

---

> **说明**：本列表持续更新。欢迎通过 [Issues](https://github.com/LILAN-00/Octoday-Embodied-Hub/issues) 或 Pull Request 补充新工具或修正信息。
