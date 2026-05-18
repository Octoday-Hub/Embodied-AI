## 🛠️ 工具与平台

> 机器人开发工具集锦，覆盖仿真环境、开发框架、SLAM / 视觉工具等。
>
> 本列表持续更新，如果你发现好工具未被收录，或现有信息需要更新，请直接提交[PR](https://github.com/Octoday-Hub/Embodied-AI/pulls)或在[Issues](https://github.com/Octoday-Hub/Embodied-AI/issues)中反馈。

| 工具名称 | 简介 | 链接 |
|:---|:---|:---|
| **Aerial Gym** | 基于 Isaac Gym 的空中机器人仿真环境，支持无人机强化学习训练。 | [链接](https://github.com/ntnu-arl/aerial_gym_simulator) |
| **AI2-THOR** | 语义交互模拟。由艾伦研究所开发，拥有200+精细房间和2600+可交互物体，支持复杂的物体状态改变（如切片、烹饪）。 | [链接](https://ai2thor.allenai.org/) |
| **AllenAct** | 面向具身智能研究的训练框架，支持 iTHOR、RoboTHOR、Habitat 等多环境和常用 RL / IL 算法。 | [链接](https://allenact.org/) |
| **ALOHA 2** | 面向双臂遥操作与具身数据采集的低成本开源硬件平台，附带教程与 MuJoCo 仿真模型。 | [链接](https://aloha-2.github.io/) |
| **AprilTag** | 机器人领域常用的视觉标记系统，支持标签检测、位姿估计和相机 / 机器人标定。 | [链接](https://github.com/AprilRobotics/apriltag) |
| **Arduino IDE** | 开源电子原型开发工具，适合传感器、执行器和控制板快速联调，支持 C / C++ 编程。 | [链接](https://www.arduino.cc) |
| **北京人形机器人创新中心·慧思开物** | 面向通用具身智能场景的工具链平台，覆盖技能调用、智能体配置到场景部署。 | [链接](https://login.x-humanoid-cloud.com/?responseType=code&clientId=fd6c22fb&redirectUri=https%3A%2F%2Fopen.x-humanoid-cloud.com%2Fhome&stamp=1778429122172&env=cloud) |
| **BEHAVIOR** | 大规模交互仿真基准。基于SAPIEN引擎构建，包含100个日常家居物品和30个复杂任务（如"把湿毛巾挂起来"），提供一套完整的物理交互能力测试环境。 | [链接](https://behavior.stanford.edu/) |
| **CARLA** | 面向自动驾驶与机器人研究的开源仿真器，提供城市道路、交通参与者、传感器和场景脚本能力。 | [链接](https://carla.org) |
| **Cartographer** | Google 开源的经典实时 2D / 3D SLAM 系统，支持多传感器建图、定位和闭环优化。 | [链接](https://google-cartographer-ros.readthedocs.io/) |
| **Clearpath·Husky** | 常见 ROS 科研移动机器人平台，提供标准化接口，适合户外导航与算法验证。 | [链接](https://clearpathrobotics.com) |
| **Clearpath·TurtleBot 4** | 面向教学和研究的 ROS2 入门平台，开箱即用，适合导航与多传感器实验。 | [链接](https://www.turtlebot.com/) |
| **CoppeliaSim (V-REP)** | 支持远程 API、内嵌脚本等多种接口的机器人仿真平台，适用于教学、研究和工业原型验证。 | [链接](https://www.coppeliarobotics.com) |
| **cuRobo** | NVIDIA 开源的 CUDA 加速机器人运动生成库，支持逆运动学、碰撞检测、轨迹优化与高自由度规划。 | [链接](https://github.com/NVlabs/curobo) |
| **Cyclone DDS** | Eclipse 基金会维护的 DDS 实现，以鲁棒性和网络适应性见长，常用于 ROS 2 部署。 | [链接](https://projects.eclipse.org/projects/iot.cyclonedds) |
| **DDS (Data Distribution Service)** | 实时分布式系统的发布-订阅通信标准，也是 ROS 2 中间件体系的基础。 | [链接](https://www.omg.org/omg-dds-portal/index.htm) |
| **DeepMind SI-Tuning** | VLA模型微调框架。Google DeepMind推出的用于微调RT-2、OpenVLA等视觉-语言-动作模型的代码库，专注于提升机器人在特定任务上的泛化能力。 | [链接](https://github.com/google-deepmind/si_tuning) |
| **DexCap** | 灵巧手数据采集。斯坦福开源，通过手部动作捕捉系统和深度相机，低成本、大规模地采集人类灵巧手操作数据，支持精细化的Sim-to-Real迁移。 | [链接](https://dexcap.github.io/) |
| **Diffusion Policy** | 基于扩散模型的机器人策略学习框架，常用于模仿学习与操作控制研究。 | [链接](https://github.com/real-stanford/diffusion_policy) |
| **DISCOVERSE** | 面向 Real2Sim2Real 的高保真机器人仿真框架，结合 3DGS 场景表示、MuJoCo 物理和控制接口。 | [链接](https://air-discoverse.github.io/) |
| **Dobb-E** | 硬件到数据的全栈。NYU开源，包含低成本手持采集硬件"Stick"、数据集和模仿学习框架，核心是让机器人在15分钟示教后学会新家务。 | [链接](https://dobb-e.com/) |
| **DORA** | 面向 AI 机器人应用的数据流中间件，支持低时延、可组合、分布式的数据处理管线。 | [链接](https://github.com/dora-rs/dora) |
| **Drake** | 面向机器人建模、规划与控制的工具包，适用于系统分析、仿真和算法研究。 | [链接](https://github.com/RobotLocomotion/drake) |
| **EmbodiedCity** | 真实开放环境具身智能平台。清华大学发布，基于虚幻引擎5打造真实城市环境，提供在线和离线两种部署方式，支持智能体在开放城市中进行导航与任务规划。 | [链接](https://embodied-city.fiblab.net/) |
| **Fast DDS (原 Fast RTPS)** | eProsima 的 DDS 实现，为 ROS 2 提供高性能、可配置的通信中间件。 | [链接](https://fast-dds.docs.eprosima.com/en/latest/index.html) |
| **Foxglove** | 面向机器人与 Physical AI 的数据可视化和可观测性平台，支持 ROS、MCAP、3D 场景与多模态日志调试。 | [链接](https://foxglove.dev) |
| **Gazebo Sim** | 高保真度开源机器人仿真器，支持多种物理引擎（ODE、Bullet、DART），提供逼真渲染和传感器模型，是 ROS 生态中的主流仿真平台之一。 | [链接](https://gazebosim.org) |
| **Genesis** | 通用机器人仿真引擎。由GenFlow团队推出，专为生成式物理智能设计，集成了刚体、流体、软体等多种物理求解器，旨在解决复杂场景下的仿真难题。 | [链接](https://genesis-embodied-ai.github.io/) |
| **GR-1 (ByteDance Model)** | 字节跳动开源的 GPT 风格视觉机器人操作模型，面向语言条件下的多任务机器人操作学习与动作预测，需与智元机器人的 GR-1 人形机器人整机区分。 | [链接](https://github.com/bytedance/GR-1) |
| **GRUtopia** | 通用具身智能仿真平台。由上海人工智能实验室发布，提供海量高质量可交互场景与数据，支持简单代码定义任务，是解决具身智能数据稀缺问题的核心工具。 | [链接](https://github.com/OpenRobotLab/GRUtopia) |
| **Gymnasium-Robotics** | 基于 Gymnasium API 的机器人仿真环境集合，适合强化学习算法开发、复现和标准化比较。 | [链接](https://robotics.farama.org/) |
| **Habitat-Lab** | 面向具身智能任务的高层开发库，通常与 Habitat Sim 配合使用，支持任务定义、智能体配置、训练与标准化评测。 | [链接](https://github.com/facebookresearch/habitat-lab) |
| **Habitat Sim** | Meta 开源的高性能 3D 仿真器，常与 Habitat-Lab 配合使用，适用于大规模场景导航与交互任务。 | [链接](https://github.com/facebookresearch/habitat-sim) |
| **Habitat 3.0** | 社交具身AI仿真平台。Meta AI推出的最新版本，专注于人与机器人、机器人与机器人之间的交互，支持高精度的社会行为模拟和导航任务。 | [链接](https://aihabitat.org/) |
| **Intern-Robotics** | 书生具身全栈引擎。上海人工智能实验室开源的具身智能全栈框架，涵盖导航、操作、运动大模型等，推动具身大脑的全栈化与量产。 | [链接](https://internrobotics.shlab.org.cn/) |
| **京东 JoyInside** | 面向机器人与 AI 玩具等智能硬件的对话智能体平台。 | [链接](https://joyinside.com/) |
| **Kalibr** | 多传感器标定工具箱，支持相机内参、多相机和相机-IMU 联合标定。 | [链接](https://github.com/ethz-asl/kalibr) |
| **kscale·K-Bot** | 面向开发者和研究人员的开源全栈人形机器人平台。 | [链接](https://docs.kscale.dev/category/k-bot) |
| **LeRobot** | Hugging Face 推出的真实机器人机器学习工具集，提供模型、数据集和训练工具。 | [链接](https://huggingface.co/docs/lerobot/main/en/index) |
| **智元灵创平台 (LinkCraft)** | 智元机器人推出的零代码机器人内容创作平台，支持动作模仿、语音驱动和任务脚本生成。 | [链接](https://www.agibot.com.cn/filepage/295.html) |
| **ManiSkill3** | 下一代操作技能仿真框架。上海AI实验室推出的最新版本，专为训练通用操作策略设计，支持更复杂的铰接物体（如抽屉、门把手）和更高效的并行物理模拟。 | [链接](https://github.com/haosulab/ManiSkill) |
| **Meta-World** | 经典机器人操作 benchmark，包含 50 个操作任务，常用于多任务学习与 meta-RL 评测。 | [链接](https://metaworld.farama.org/) |
| **MimicGen** | 从少量人类示教自动生成大规模机器人数据的数据生成系统，适合扩充 manipulation 训练集。 | [链接](https://github.com/NVlabs/mimicgen) |
| **MORSE Simulator** | 基于 Blender 的学术机器人仿真器，支持移动机器人、人机交互和多中间件接入。 | [链接](https://morse-simulator.github.io/) |
| **MoveIt** | 面向 ROS 的运动规划、操作和运动学框架，常用于机械臂规划、抓取和任务编排。 | [链接](https://moveit.ai) |
| **MQTT** | 轻量级发布-订阅消息协议，常用于机器人边缘设备、网关和云端数据传输。 | [链接](https://mqtt.org/) |
| **MuJoCo** | 高性能物理引擎，专为机器人、生物力学和图形学设计，广泛应用于强化学习和运动控制研究。 | [链接](https://github.com/google-deepmind/mujoco) |
| **Nav2 (Navigation2)** | ROS 2 导航框架，提供定位、规划、控制、恢复行为等完整移动机器人导航能力。 | [链接](https://github.com/ros-navigation/navigation2) |
| **NVIDIA Isaac Gym** | 面向机器人学习的高性能强化学习仿真环境，支持 GPU 加速的大规模并行训练。 | [链接](https://developer.nvidia.com/isaac-gym) |
| **NVIDIA Isaac Lab** | 开源、GPU 加速的模块化机器人学习框架，适合大规模策略训练和仿真到现实迁移。 | [链接](https://developer.nvidia.com/isaac/lab) |
| **NVIDIA Isaac Sim** | 基于 Omniverse 构建的机器人仿真平台，支持物理 AI 训练、合成数据生成和 Sim2Real 工作流。 | [链接](https://developer.nvidia.com/isaac-sim) |
| **NVIDIA RAD-MARS** | 机器人辅助设计与仿真平台。基于Omniverse构建，允许在物理级逼真的环境中设计机器人硬件并测试运动学算法，连接了机械设计与AI训练。 | [链接](https://www.nvidia.com/en-us/omniverse/solutions/robotics/) |
| **Octo** | 开源通用机器人策略，基于多机器人轨迹预训练，支持语言指令、目标图像和小样本微调。 | [链接](https://github.com/octo-models/octo) |
| **OK-Robot** | 系统集成框架。纽约大学（NYU）开源的模块化框架，专为真实家庭环境设计，通过结合VLM实现零样本（Zero-shot）的取放任务。 | [链接](https://ok-robot.github.io/) |
| **OmniGibson** | 基于 Isaac Sim 的具身智能仿真框架，支持交互场景、任务定义、数据采集与并行环境训练。 | [链接](https://behavior.stanford.edu/omnigibson/overview.html) |
| **OMPL** | 开源运动规划库，包含多种经典采样规划算法，常用于路径规划和机械臂规划。 | [链接](https://ompl.kavrakilab.org) |
| **Open3D** | 现代 3D 数据处理库，支持点云、重建、配准、可视化和 3D 机器学习。 | [链接](https://www.open3d.org) |
| **Open-RMF** | 面向多机器人车队与楼宇基础设施协同的开源框架，支持任务调度、资源协调和互操作。 | [链接](https://www.open-rmf.org) |
| **OpenCV** | 经典计算机视觉库，提供图像处理、特征提取、检测跟踪与几何视觉等基础能力。 | [链接](https://opencv.org/) |
| **OpenVLA** | 开源视觉-语言-动作模型，面向通用机器人操作任务，支持微调、训练和评估。 | [链接](https://github.com/openvla/openvla) |
| **OpenXLab** | 具身智能开源开放平台。上海AI实验室推出的综合性平台，提供从数据处理、算法训练到部署的全套工具链，旨在降低具身智能的研发门槛。 | [链接](https://openxlab.org.cn/) |
| **ORB-SLAM3** | 开源视觉 / 视觉惯性 / 多地图 SLAM 系统，支持单目、双目和 RGB-D 相机。 | [链接](https://github.com/UZ-SLAMLab/ORB_SLAM3) |
| **PCL (Point Cloud Library)** | 经典点云处理库，覆盖滤波、分割、配准、重建和可视化等 3D 感知基础能力。 | [链接](https://pointclouds.org/) |
| **PlotJuggler** | 面向机器人时序数据的可视化与分析工具，适合话题调试、日志回放和指标对比。 | [链接](https://github.com/facontidavide/PlotJuggler) |
| **PyBullet** | 基于 Bullet 物理引擎的 Python 接口，轻量易用，适合快速原型开发和强化学习实验。 | [链接](https://github.com/bulletphysics/bullet3) |
| **RobotecAI RAI** | RobotecAI 开源的 agentic robotics framework，基于 ROS 2 工具链，支持自然语言交互、多模态能力集成和机器人任务执行。 | [链接](https://github.com/RobotecAI/rai) |
| **RLBench** | 大规模视觉引导机器人操作 benchmark 与学习环境，覆盖强化学习、模仿学习、多任务和少样本设置。 | [链接](https://github.com/stepjam/RLBench) |
| **RoboGen** | 代码生成式机器人框架。由MIT等机构推出，利用大语言模型自动生成包含感知、规划、控制逻辑的完整Python代码，实现"代码即策略"的自动化生成。 | [链接](https://robogen-ai.github.io/) |
| **RoboCasa** | 面向日常家居操作任务的大规模仿真框架，支持多场景、多对象、示教数据和 benchmark。 | [链接](https://robocasa.ai/) |
| **robomimic** | 面向机器人示教学习的通用框架，提供数据集、离线学习算法和可复现实验基线。 | [链接](https://github.com/ARISE-Initiative/robomimic) |
| **robosuite** | 基于 MuJoCo 的模块化机器人学习仿真框架与基准套件，适合操作任务研究与复现实验。 | [链接](https://github.com/ARISE-Initiative/robosuite) |
| **RobotStudio** | ABB 官方机器人编程、仿真和离线编程软件，适合工业机器人工作站开发。 | [链接](https://www.abb.com/global/en/areas/robotics/products/software/robotstudio-suite) |
| **RoboTwin 2.0** | 面向双臂操作的数据生成与 benchmark 平台，强调强 domain randomization、规模化生成和标准化评测。 | [链接](https://github.com/RoboTwin-Platform/RoboTwin) |
| **ros2_latency_analysis** | 面向 ROS 2 的延迟分析工具，可拆解端到端、通信与计算时延瓶颈。 | [链接](https://github.com/TUM-AVS/ros2_latency_analysis) |
| **ROS / ROS2** | 机器人操作系统，提供丰富工具和库，支持模块化开发与分布式计算，是机器人软件开发的行业标准。 | [链接](https://www.ros.org) |
| **ROSboard** | 将 ROS / ROS 2 话题转换为网页仪表盘的轻量工具，适合远程监控和移动端查看。 | [链接](https://github.com/dheera/rosboard) |
| **RQT Frame Editor** | 用于创建和调整 TF 坐标系的 rqt 插件，便于处理多传感器和多机器人坐标关系。 | [链接](https://github.com/ipa320/rqt_frame_editor_plugin) |
| **rqt_plot** | ROS / ROS 2 常用绘图插件，可实时查看话题数值变化，适合调参与快速排障。 | [链接](https://docs.ros.org/en/rolling/p/rqt_plot/) |
| **RTAB-Map** | 基于图优化与外观闭环检测的视觉 / RGB-D / 激光 SLAM 框架，适合大规模场景建图与定位。 | [链接](https://introlab.github.io/rtabmap/) |
| **RViz / RViz2** | ROS / ROS 2 核心 3D 可视化工具，可实时查看机器人模型、TF、点云、路径和地图。 | [链接](https://docs.ros.org/en/rolling/p/rviz2/) |
| **SAGE** | 具身智能分布式计算框架。由ETH Zurich推出，提供高效的分布式数据流水线和并行计算架构，专门用于加速大规模策略训练和数据处理。 | [链接](https://github.com/eth-easl/sage) |
| **SAPIEN** | 面向部件级交互和操作任务的仿真环境，支持铰接物体建模与操作学习研究。 | [链接](https://github.com/haosulab/SAPIEN) |
| **SimplerEnv** | 面向真实机器人操作策略的仿真评测环境，支持在统一设置下复现和比较 real-to-sim manipulation policy。 | [链接](https://github.com/simpler-env/SimplerEnv) |
| **system_fingerprint** | 采集 ROS / ROS 2 运行环境、节点、话题和 TF 状态的系统快照工具，便于排障与交付验收。 | [链接](https://github.com/MetroRobots/ros_system_fingerprint) |
| **腾讯 Tairos (钛螺丝)** | 面向机器人场景的具身智能开放平台，提供模型、开发工具和数据服务。 | [链接](https://tairos.tencent.com/) |
| **Theseus** | 可微非线性优化库，适合机器人和视觉中的状态估计、几何优化、轨迹优化与端到端可微系统构建。 | [链接](https://github.com/facebookresearch/theseus) |
| **Unity ML-Agents** | Unity 游戏引擎的机器学习代理工具包，支持智能体在 3D 环境中的训练与评估。 | [链接](https://github.com/Unity-Technologies/ml-agents) |
| **Universal Manipulation Interface (UMI)** | 斯坦福开源的通用操作接口，支持多种机器人学习和操作任务。 | [链接](https://github.com/real-stanford/universal_manipulation_interface) |
| **UnrealCV** | 连接 Unreal Engine 与外部视觉 / 机器人程序的开源插件，适合构建仿真环境和合成数据工作流。 | [链接](https://unrealcv.org/) |
| **VEX Robotics Software** | 面向 VEX 机器人平台的软件工具，支持拖放式编程，常用于教育场景。 | [链接](https://www.vexrobotics.com/?srsltid=AfmBOoqB_9zu0-eFHO4wzVB_33rsABV6DRRJ_drQfuk67n-MLcUmVy9M) |
| **Viam** | 面向机器人构建、部署和管理的软件平台，提供统一 API、模块注册、远程运维和车队级管理能力。 | [链接](https://www.viam.com) |
| **VIMA** | 多模态具身任务基准。由UIUC等机构推出，提供复杂的"搭建积木"类任务，专门用于评测机器人模型在处理视觉、语言及空间推理混合指令时的表现。 | [链接](https://vimalabs.github.io/) |
| **网易灵动·灵掘** | 面向矿山挖掘机装车场景的具身智能模型与训练框架。 | [链接](https://lingdong.fuxi.163.com/productSummary/wj) |
| **Webots** | 开源跨平台机器人仿真桌面应用，提供完整的建模、编程与仿真环境。 | [链接](https://cyberbotics.com) |
| **Webviz** | 面向 ROS bag 与实时机器人数据的浏览器可视化平台，适合布局式分析、回放和远程调试。 | [链接](https://webviz.io/) |
| **Zenoh** | 面向机器人与边缘系统的轻量级数据通信协议与中间件，适合分布式场景下的高效 pub/sub 与查询。 | [链接](https://zenoh.io/) |
