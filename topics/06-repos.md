# 具身智能（Embodied AI）开源仓库与项目汇总

> 整理时间：2026-06-08 · 聚焦机器人相关开源库

---

<a name="toc"></a>

## 目录

**仓库项目分类：** [📚 资源列表](#resource-lists) · [🎮 仿真平台](#simulation-platforms) · [🤖 模型](#models) · [🏗️ 学习框架](#learning-frameworks) · [🤖 机器人项目](#robot-projects) · [📖 教程](#tutorials) · [🧠 推理/强化学习](#reasoning-rl)

**平台与社区分类：** [🏭 厂商开发者社区](#vendor-communities) · [🛒 产品/模型/数据平台](#product-platforms)

---

# 仓库项目

<a name="resource-lists"></a>

## 📚 资源列表

- **Embodied-AI-Guide** — [`TianxingChen/Embodied-AI-Guide`](https://github.com/TianxingChen/Embodied-AI-Guide) ⭐ 14.2k  
  📄 偏「百科全书」定位的具身智能中文知识库与资料索引（Lumina 具身智能社区）

- **Awesome-LLM-Robotics** — [`GT-RIPL/Awesome-LLM-Robotics`](https://github.com/GT-RIPL/Awesome-LLM-Robotics) ⭐ 4.4k  
  📄 使用 LLM / 多模态模型进行机器人学与强化学习的论文精选列表

- **Awesome-World-Models** — [`knightnemo/Awesome-World-Models`](https://github.com/knightnemo/Awesome-World-Models) ⭐ 3.0k  
  📄 世界模型（World Models）论文精选列表，一站式资源汇总

- **Awesome-World-Models (leofan90)** — [`leofan90/Awesome-World-Models`](https://github.com/leofan90/Awesome-World-Models) ⭐ 1.8k  
  📄 涵盖世界模型、具身 AI 和自动驾驶的论文列表

- **Embodied_AI_Paper_List** — [`HCPLab-SYSU/Embodied_AI_Paper_List`](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) ⭐ 2.1k  
  📄 中山大学 HCPLab 出品，具身 AI 综述论文列表与资源仓库

- **Awesome-Embodied-Robotics-and-Agent** — [`zchoi/Awesome-Embodied-Robotics-and-Agent`](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent) ⭐ 1.8k  
  📄 具身 AI / 机器人与大语言模型交叉研究的精选论文列表

- **Awesome-Embodied-AI** — [`haoranD/Awesome-Embodied-AI`](https://github.com/haoranD/Awesome-Embodied-AI) ⭐ 525  
  📄 具身 AI 研究与产业资源精选论文列表

- **Awesome-Robotics-Foundation-Models** — [`robotics-survey/Awesome-Robotics-Foundation-Models`](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models)  
  📄 机器人基础模型研究论文和项目汇总，包括 RT-1、RT-2、OpenVLA 等

- **Awesome-3DCV-Papers-Daily** — [`qxiaofan/awesome-3dcv-papers-daily`](https://github.com/qxiaofan/awesome-3dcv-papers-daily)  
  📄 计算机视觉、VSLAM、点云、结构光、机械臂抓取、三维重建、深度学习、自动驾驶等前沿论文与文章

[↑ 回目录](#toc)

---

<a name="simulation-platforms"></a>

## 🎮 仿真平台

- **BEHAVIOR-1K** — [`StanfordVL/BEHAVIOR-1K`](https://github.com/StanfordVL/BEHAVIOR-1K) ⭐ 1.5k  
  📄 斯坦福大学出品，1,000 种日常生活活动的具身 AI 基准测试与仿真平台

- **XTDrone** — [`robin-shaun/XTDrone`](https://github.com/robin-shaun/XTDrone) ⭐ 6.5k  
  📄 基于 PX4、ROS 和 Gazebo 的无人机仿真平台，支持集群仿真

- **Prometheus** — [`amov-lab/Prometheus`](https://github.com/amov-lab/Prometheus) ⭐ 4.5k  
  📄 面向自主无人机的开源软件系统，支持目标检测、SLAM 导航、编队控制等

[↑ 回目录](#toc)

---

<a name="models"></a>

## 🤖 模型

- **VLA-Adapter** — [`OpenHelix-Team/VLA-Adapter`](https://github.com/OpenHelix-Team/VLA-Adapter) ⭐ 2.2k  
  📄 面向小规模 VLA 模型的有效训练范式 —— VLA 适配器

- **LLaVA-OneVision** — [`EvolvingLMMs-Lab/LLaVA-OneVision`](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision) ⭐ 754  
  📄 完全开源的大型多模态模型，低成本实现 SOTA 性能

- **Otter** — [`EvolvingLMMs-Lab/Otter`](https://github.com/EvolvingLMMs-Lab/Otter) ⭐ 3.3k  
  📄 基于 OpenFlamingo 的多模态模型，在 MIMIC-IT 数据集上训练，提升指令跟随能力

- **XR-1** — [`Open-X-Humanoid/XR-1`](https://github.com/Open-X-Humanoid/XR-1)  
  📄 中国首个国标级 VLA 大模型（北京人形机器人创新中心），支持跨机器人平台操作，包含 RoboMIND 2.0 数据集和 ArtVIP 资产

- **DexVLA** — [`juruobenruo/DexVLA`](https://github.com/juruobenruo/DexVLA)  
  📄 基于 Qwen2-VL 的视觉-语言-动作模型，支持单臂、双臂和灵巧手等多种机器人形态的通用控制

- **ManiFoundation** — [`NUS-LinS-Lab/ManiFM`](https://github.com/NUS-LinS-Lab/ManiFM)  
  📄 通用机器人操作基础模型（新加坡国立大学/清华大学），通过接触合成实现对刚性、铰接和可变形物体的操作

- **RoboBrain 2.5** — [`FlagOpen/RoboBrain2.5`](https://github.com/FlagOpen/RoboBrain2.5)  
  📄 新一代具身 AI 基础模型（智源研究院/北京大学），支持精确 3D 空间推理、深度感知坐标预测和时序建模

- **WholebodyVLA** — [`OpenDriveLab/WholebodyVLA`](https://github.com/OpenDriveLab/WholebodyVLA) ⭐  
  📄 ICLR 2026，面向人形机器人全身移动操作控制的统一潜空间 VLA 模型（上海AI实验室）

- **X-VLA** — [`2toinf/X-VLA`](https://github.com/2toinf/X-VLA)  
  📄 ICLR 2026，软提示 Transformer 跨形态 VLA 模型，AgiBot World 挑战赛（IROS 2025）冠军

- **RoboticsDiffusionTransformer (RDT-1B)** — [`thu-ml/RoboticsDiffusionTransformer`](https://github.com/thu-ml/RoboticsDiffusionTransformer)  
  📄 双臂机器人操控基础模型（清华大学），采用扩散 Transformer 架构，在多种双臂操控任务上取得 SOTA 效果

- **AgiBot-World** — [`OpenDriveLab/AgiBot-World`](https://github.com/OpenDriveLab/AgiBot-World)  
  📄 IROS 2025 最佳论文候选，面向可扩展和智能具身系统的大规模操控平台（上海AI实验室）

- **Dexterity-BEV** — 详见 [Dexterity-BEV](https://arxiv.org/abs/2606.02274)  
  📄 对齐 3D 世界与动作实现可泛化机器人策略学习

[↑ 回目录](#toc)

---

<a name="learning-frameworks"></a>

## 🏗️ 学习框架

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

---

<a name="robot-projects"></a>

## 🤖 机器人项目

### 人形机器人

- **AgiBot X1** — [`推理`](https://github.com/AgibotTech/agibot_x1_infer) · [`训练`](https://github.com/AgibotTech/agibot_x1_train) · [`硬件`](https://github.com/AgibotTech/agibot_x1_hardware)  
  📄 智元机器人 X1 完整开源人形机器人项目，包含推理模块、强化学习训练代码和全套硬件设计资料

- **OpenLoong 青龙** — [`loongOpen`](https://github.com/loongOpen)  
  📄 全栈开源人形机器人项目（上海人形机器人创新中心/开放原子基金会），包含动力学控制(MPC+WBC)、硬件设计、训练平台和大规模技能调度框架

- **Fourier N1** — [`FFTAI`](https://github.com/FFTAI)  
  📄 全球首个全开源人形机器人（傅利叶智能），公开全套硬件设计、BOM、装配指南和 Fourier-GRX SDK，1.3m/38kg/3.5m/s

- **EngineAI Humanoid** — [`engineai-robotics/engineai_humanoid`](https://github.com/engineai-robotics/engineai_humanoid)  
  📄 EngineAI（松延动力）双足机器人 SA01/PM01 的开源运动控制算法，采用端到端神经网络实现拟人步态

- **Booster Gym** — [`BoosterRobotics`](https://github.com/BoosterRobotics)  
  📄 Booster T1/K1 人形机器人端到端强化学习运动控制框架（加速进化），含 RoboCup 自主踢球 Demo

- **Humanoid-Gym** — [`roboterax/humanoid-gym`](https://github.com/roboterax/humanoid-gym)  
  📄 基于 Isaac Gym 的人形机器人强化学习训练框架，支持零样本迁移至真实机器人

- **Unitree Qmini** — [`unitreerobotics/Qmini`](https://github.com/unitreerobotics/Qmini)  
  📄 宇树科技开源双足平台，提供全套 BOM/装配指南、RoboTamer4Qmini 控制框架与 URDF 模型

### 四足机器人

- **OpenCat** — [`PetoiCamp/OpenCat`](https://github.com/PetoiCamp/OpenCat) ⭐ 15k  
  📄 开源四足机器人平台

- **小米 CyberDog** — [`MiRoboticsLab/cyberdog_ros2`](https://github.com/MiRoboticsLab/cyberdog_ros2)  
  📄 小米 CyberDog 四足机器人的开源软件和硬件资料

- **宇树科技四足机器人 ROS** — [`unitreerobotics/unitree_ros`](https://github.com/unitreerobotics/unitree_ros)  
  📄 宇树科技四足机器人 Go1/Go2 的 ROS 驱动包

### 机械臂与桌面机器人

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

### 移动机器人

- **MiniRover 火星车** — [`peng-zhihui/MiniRover-Hardware`](https://github.com/peng-zhihui/MiniRover-Hardware)  
  📄 自制火星车的开源资料（稚晖君）

- **ONE-Robot 独轮机器人** — [`peng-zhihui/ONE-Robot`](https://github.com/peng-zhihui/ONE-Robot)  
  📄 基于 IMU 和 STM32 的独轮自平衡机器人（稚晖君）

### 无人机

- **浙江大学 FAST-Drone-250** — [`ZJU-FAST-Lab/Fast-Drone-250`](https://github.com/ZJU-FAST-Lab/Fast-Drone-250)  
  📄 250mm 自主无人机的硬件和软件设计（浙江大学 FAST 实验室）

- **EGO-Planner** — [`ZJU-FAST-Lab/ego-planner`](https://github.com/ZJU-FAST-Lab/ego-planner)  
  📄 高效的无人机梯度引导在线局部规划器（浙江大学 FAST 实验室）

- **FIESTA** — [`HKUST-Aerial-Robotics/FIESTA`](https://github.com/HKUST-Aerial-Robotics/FIESTA)  
  📄 空中机器人在线运动规划的快速增量欧几里得距离场（香港科技大学）

- **大疆 Tello Python SDK** — [`dji-sdk/Tello-Python`](https://github.com/dji-sdk/Tello-Python)  
  📄 大疆 Tello 系列无人机的 Python SDK，支持编程控制和图像处理

### SLAM 与感知

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

### 抓取与操作

- **AnyGrasp** — [`graspnet/anygrasp_sdk`](https://github.com/graspnet/anygrasp_sdk)  
  📄 高效通用的 6 自由度抓取位姿估计算法（上海AI实验室），支持任意物体的机器人抓取检测

- **小觅双目相机系列** — [`slightech/MYNT-EYE-S-SDK`](https://github.com/slightech/MYNT-EYE-S-SDK)  
  📄 小觅双目相机系列（MYNTAI），提供完整的 SLAM 和视觉算法解决方案

### 自动驾驶

- **Apollo** — [`ApolloAuto/apollo`](https://github.com/ApolloAuto/apollo) ⭐ 25k  
  📄 百度 Apollo 开源自动驾驶平台，国内最大的自动驾驶开源生态系统

- **UniAD** — [`OpenDriveLab/UniAD`](https://github.com/OpenDriveLab/UniAD)  
  📄 CVPR 2023 最佳论文，面向规划的统一自动驾驶框架，整合感知、预测和规划

- **BEVFormer** — [`fundamentalvision/BEVFormer`](https://github.com/fundamentalvision/BEVFormer)  
  📄 ECCV 2022，基于纯相机的 BEV 感知框架，用于 3D 目标检测和语义地图分割

### 其他

- **宇树科技 XR 遥操作** — [`unitreerobotics/xr_teleoperate`](https://github.com/unitreerobotics/xr_teleoperate)  
  📄 基于 XR 设备（Apple Vision Pro/Quest 等）的 H1/G1 人形机器人遥操作系统

- **RoboWiki** — [`yfrobotics/robowiki`](https://github.com/yfrobotics/robowiki)  
  📄 机器人领域的维基百科（云飞机器人实验室）

[↑ 回目录](#toc)

---

<a name="tutorials"></a>

## 📖 教程

- **every-embodied** — [`datawhalechina/every-embodied`](https://github.com/datawhalechina/every-embodied) ⭐ 2.2k  
  📄 仅需 Python 基础，从 0 构建 VLA/OpenVLA/SmolVLA/Pi0 的具身智能学习路径

- **宇树科技机器人控制教程** — [`unitreerobotics/unitree_guide`](https://github.com/unitreerobotics/unitree_guide)  
  📄 宇树科技四足机器人控制的开源教程项目，适合入门学习与参考

[↑ 回目录](#toc)

---

<a name="reasoning-rl"></a>

## 🧠 推理 / 强化学习

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

# 平台与社区

<a name="vendor-communities"></a>

## 🏭 厂商开发者社区

- **宇树开发者社区** — [`https://www.unifolm.com/`](https://www.unifolm.com/)  
  📄 宇树科技官方开发者社区，提供机器人开发文档与技术支持

- **宇树科技机器人 SDK2** — [`C++`](https://github.com/unitreerobotics/unitree_sdk2) · [`Python`](https://github.com/unitreerobotics/unitree_sdk2_python)  
  📄 宇树科技新一代机器人 SDK，基于 CycloneDDS，支持 Go2/B2/H1/G1 等机器人

- **宇树科技 ROS2** — [`unitreerobotics/unitree_ros2`](https://github.com/unitreerobotics/unitree_ros2)  
  📄 宇树科技 Go2/B2 机器人的 ROS2 开发包

- **宇树科技 MuJoCo 仿真** — [`unitreerobotics/unitree_mujoco`](https://github.com/unitreerobotics/unitree_mujoco)  
  📄 基于 MuJoCo 的宇树机器人仿真环境，集成 unitree_sdk2

- **宇树科技 Isaac Lab 仿真** — [`unitreerobotics/unitree_sim_isaaclab`](https://github.com/unitreerobotics/unitree_sim_isaaclab)  
  📄 基于 Isaac Lab 的宇树机器人仿真环境，支持数据采集、回放和模型验证

- **华为昇腾社区** — [`官网`](https://www.mindspore.cn) · [`论坛`](https://discuss.mindspore.cn/)  
  📄 华为昇腾 AI 及 MindSpore 开源框架开发者生态

- **地瓜机器人社区** — [`https://developer.d-robotics.cc/`](https://developer.d-robotics.cc/)  
  📄 地瓜机器人（地平线旗下）官方开发者社区，支持 RDK 系列机器人开发板

- **OpenAI 社区** — [`https://developers.openai.com/community`](https://developers.openai.com/community)  
  📄 OpenAI 官方开发者社区，交流 LLM / API 应用与多模态开发

- **宇树科技 UnifoLM 世界模型** — [`unitreerobotics/unifolm-world-model-action`](https://github.com/unitreerobotics/unifolm-world-model-action)  
  📄 宇树科技开源的世界模型-动作架构(UnifoLM-WMA)，支持跨多种机器人形态的通用学习

- **宇树科技 UnifoLM VLA** — [`unitreerobotics/unifolm-vla`](https://github.com/unitreerobotics/unifolm-vla)  
  📄 面向通用人形机器人操作的视觉-语言-动作大模型(UnifoLM-VLA)

[↑ 回目录](#toc)

---

<a name="product-platforms"></a>

## 🛒 产品 / 模型 / 数据平台

- **Hugging Face** — [`https://huggingface.co/papers/trending`](https://huggingface.co/papers/trending)  
  📄 全球最大的模型与数据集托管平台，每日 trending papers 追踪前沿

- **魔塔社区（ModelScope）** — [`https://modelscope.cn/home`](https://modelscope.cn/home)  
  📄 阿里达摩院出品，国内最大模型开源社区，涵盖 VLA / 具身智能模型

- **GitCode** — [`https://gitcode.com/`](https://gitcode.com/)  
  📄 开源中国旗下的代码托管与 AI 模型平台，国内 GitHub 替代方案

- **Kaggle** — [`https://www.kaggle.com/`](https://www.kaggle.com/)  
  📄 Google 旗下数据科学竞赛平台，提供机器人/AI 数据集与 Notebook

- **GitHub (embodied-ai 主题)** — [`https://github.com/topics/embodied-ai`](https://github.com/topics/embodied-ai)  
  📄 GitHub 具身智能主题页，聚合 552+ 相关仓库

- **Product Hunt** — [`https://www.producthunt.com/`](https://www.producthunt.com/)  
  📄 全球新品发布平台，追踪机器人/AI 产品动态

[↑ 回目录](#toc)

---

## 按类别速查

| 类别 | 项目 |
|:---|:---|
| 📚 **资源列表** | [Embodied-AI-Guide](https://github.com/TianxingChen/Embodied-AI-Guide) · [Awesome-LLM-Robotics](https://github.com/GT-RIPL/Awesome-LLM-Robotics) · [Awesome-World-Models](https://github.com/knightnemo/Awesome-World-Models) · [Awesome-World-Models (leofan90)](https://github.com/leofan90/Awesome-World-Models) · [Embodied_AI_Paper_List](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) · [Awesome-Embodied-Robotics-and-Agent](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent) · [Awesome-Embodied-AI](https://github.com/haoranD/Awesome-Embodied-AI) · [Awesome-Robotics-Foundation-Models](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models) · [Awesome-3DCV-Papers-Daily](https://github.com/qxiaofan/awesome-3dcv-papers-daily) |
| 🎮 **仿真平台** | [BEHAVIOR-1K](https://github.com/StanfordVL/BEHAVIOR-1K) · [XTDrone](https://github.com/robin-shaun/XTDrone) · [Prometheus](https://github.com/amov-lab/Prometheus) |
| 🤖 **模型** | [XR-1](https://github.com/Open-X-Humanoid/XR-1) · [DexVLA](https://github.com/juruobenruo/DexVLA) · [VLA-Adapter](https://github.com/OpenHelix-Team/VLA-Adapter) · [LLaVA-OneVision](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision) · [Otter](https://github.com/EvolvingLMMs-Lab/Otter) · [WholebodyVLA](https://github.com/OpenDriveLab/WholebodyVLA) · [X-VLA](https://github.com/2toinf/X-VLA) · [RDT-1B](https://github.com/thu-ml/RoboticsDiffusionTransformer) · [ManiFoundation](https://github.com/NUS-LinS-Lab/ManiFM) · [RoboBrain 2.5](https://github.com/FlagOpen/RoboBrain2.5) · [AgiBot-World](https://github.com/OpenDriveLab/AgiBot-World) · [Dexterity-BEV](https://arxiv.org/abs/2606.02274) |
| 🏗️ **学习框架** | [RLinf](https://github.com/RLinf/RLinf) · [OpenLoong (Brain)](https://github.com/loongOpen) · [AimRT](https://github.com/AimRT/AimRT) · [Open-TeleVision](https://github.com/OpenTeleVision/TeleVision) · [AgileX Cobot Magic](https://github.com/agilexrobotics) |
| 🤖 **机器人项目** | [AgiBot X1](https://github.com/AgibotTech/agibot_x1_infer) · [OpenLoong](https://github.com/loongOpen) · [Fourier N1](https://github.com/FFTAI) · [EngineAI](https://github.com/engineai-robotics/engineai_humanoid) · [Booster Gym](https://github.com/BoosterRobotics) · [Humanoid-Gym](https://github.com/roboterax/humanoid-gym) · [Unitree Qmini](https://github.com/unitreerobotics/Qmini) · [OpenCat](https://github.com/PetoiCamp/OpenCat) · [CyberDog](https://github.com/MiRoboticsLab/cyberdog_ros2) · [Apollo](https://github.com/ApolloAuto/apollo) · [AnyGrasp](https://github.com/graspnet/anygrasp_sdk) · [VINS-Mono](https://github.com/HKUST-Aerial-Robotics/VINS-Mono) · [FAST_LIO](https://github.com/hku-mars/FAST_LIO) · [EGO-Planner](https://github.com/ZJU-FAST-Lab/ego-planner) · [Dummy-Robot](https://github.com/peng-zhihui/Dummy-Robot) |
| 📖 **教程** | [every-embodied](https://github.com/datawhalechina/every-embodied) · [unitree_guide](https://github.com/unitreerobotics/unitree_guide) |
| 🧠 **推理/RL** | [OpenR1-Multimodal](https://github.com/EvolvingLMMs-Lab/OpenR1-Multimodal) · [unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym) · [unitree_rl_lab](https://github.com/unitreerobotics/unitree_rl_lab) · [unitree_IL_lerobot](https://github.com/unitreerobotics/unitree_IL_lerobot) · [Humanoid-Gym](https://github.com/roboterax/humanoid-gym) |
| 🏭 **厂商开发者社区** | [宇树开发者社区](https://www.unifolm.com/) · [宇树 SDK2](https://github.com/unitreerobotics/unitree_sdk2) · [宇树 ROS2](https://github.com/unitreerobotics/unitree_ros2) · [宇树 MuJoCo](https://github.com/unitreerobotics/unitree_mujoco) · [宇树 Isaac Lab](https://github.com/unitreerobotics/unitree_sim_isaaclab) · [宇树 UnifoLM](https://github.com/unitreerobotics/unifolm-world-model-action) · [华为昇腾](https://www.mindspore.cn) · [地瓜机器人](https://developer.d-robotics.cc/) · [OpenAI 社区](https://developers.openai.com/community) |
| 🛒 **产品/模型/数据平台** | [Hugging Face](https://huggingface.co/papers/trending) · [魔塔社区](https://modelscope.cn/home) · [GitCode](https://gitcode.com/) · [Kaggle](https://www.kaggle.com/) · [GitHub (embodied-ai)](https://github.com/topics/embodied-ai) · [Product Hunt](https://www.producthunt.com/) |
