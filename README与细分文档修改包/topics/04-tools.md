# **🛠️ 工具与开源项目**

> 💡 本列表持续更新，如果你发现好工具未被收录，或现有信息需要更新，请直接提交 [PR](https://github.com/Octoday-Hub/Embodied-AI/pulls) 或在 [Issues](https://github.com/Octoday-Hub/Embodied-AI/issues) 中反馈。

<a id="toc"></a>

## **目录**

按资源用途查找。模型、学习训练与 SLAM 已分别整理为细分文档；仿真、机器人硬件及中间件继续在本页维护。

| **资源分类** | **内容** | **入口** |
| :--- | :--- | :--- |
| **模型与策略** | 动作策略、感知推理、系统与论文 | [模型与策略实现](04-models.md) |
| **学习与训练** | 训练框架、机器人训练、采集与评测 | [学习、训练与数据采集](04-learning.md) |
| **SLAM 与感知** | 定位、标定、图像点云与导航 | [SLAM、感知与标定](04-perception.md) |

**工具与项目分类：** [🎮 仿真平台](#simulation-platforms) · [🤖 模型](#models) · [🧰 通用工具与库](#general-tools) · [🏗️ 学习框架](#learning-frameworks) · [🤖 机器人项目](#robot-projects) · [🧠 推理/强化学习](#reasoning-rl) · [🗺️ SLAM 与感知](#slam-perception) · [🔧 中间件与 ROS 工具](#middleware-ros) · [🛒 其他](#other)

<a id="simulation-platforms"></a>

## 🎮 仿真平台

### ManiSkill3

<div align="center">
  <img src="tools-img/maniskill3.jpg" alt="ManiSkill3" style="width:100%">
</div>

<table style="width:100%;display:table;table-layout:fixed" width="100%">
<tbody>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">一句话摘要</td><td style="word-wrap:break-word;width:1200px" width="1200">基于 SAPIEN 的 GPU 并行操作仿真、数据生成与策略评测一体框架，面向可泛化操作技能研究。</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">发布与维护</td><td style="word-wrap:break-word;width:1200px" width="1200">2024 年发布（RSS 2025 发表），仓库活跃维护至 2026 年</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">机构</td><td style="word-wrap:break-word;width:1200px" width="1200">斯坦福大学 Hao Su 实验室主导（haosulab）与开源社区</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">特点</td><td style="word-wrap:break-word;width:1200px" width="1200"><ul><li><strong>最快的 contact-rich GPU 并行仿真</strong>：模拟与渲染同 GPU 运行，30,000+ FPS（4090 上采集 RGBD+分割），比 Isaac/MJX 等快 10–1000×，显存占用低 2–3×</li><li><strong>异构仿真与大规模任务库</strong>：每个并行环境可装载不同场景，12 类任务域、20+ 机器人，场景来自 ReplicaCAD/AI2-THOR 等真实感资源</li><li><strong>数据与评测双向管线</strong>：Real2Sim 支持真实策略 100× 提速的仿真规模化评测，并提供数百万演示帧（运动规划/RL/遥操作来源）</li><li><strong>开箱即用策略基线全家桶</strong>：RL（PPO/SAC/TD-MPC2）、模仿学习（BC/Diffusion Policy）、VLA（Octo/RDT-1B/RT-x）均有调好配置</li></ul></td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">使用场景</td><td style="word-wrap:break-word;width:1200px" width="1200"><ul><li>GPU 大规模合成操作演示数据</li><li>视觉/状态 RL 与模仿学习训练</li><li>真实机器人策略的仿真规模化评测（SIMPLER 式）</li><li>多本体策略与新操作任务的快速基准对比</li></ul></td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">案例</td><td style="word-wrap:break-word;width:1200px" width="1200"><ul><li>作为操作策略统一评测平台，被 VLA/扩散策略等大量研究用于大规模合成演示与基准对比</li></ul></td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">数据与模型</td><td style="word-wrap:break-word;width:1200px" width="1200">ManiSkill3 框架（基于 SAPIEN）；ManiSkill2/3 基准任务与演示数据集</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">官方链接</td><td style="word-wrap:break-word;width:1200px" width="1200"><a href="https://github.com/haosulab/ManiSkill">GitHub haosulab/ManiSkill</a> · <a href="https://maniskill.ai/">官网 maniskill.ai</a> · <a href="https://maniskill.readthedocs.io/">文档</a> · <a href="https://arxiv.org/abs/2410.00425">论文 arXiv 2410.00425</a></td></tr>
</tbody>
</table>

### GR00T-Dreams

<div align="center">
  <img src="tools-img/gr00t-dreams.jpg" alt="GR00T-Dreams" style="width:100%">
</div>

<table style="width:100%;display:table;table-layout:fixed" width="100%">
<tbody>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">一句话摘要</td><td style="word-wrap:break-word;width:1200px" width="1200">用视频世界模型把少量遥操作演示扩成大规模"神经轨迹"的具身数据生成蓝图。</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">发布与维护</td><td style="word-wrap:break-word;width:1200px" width="1200">2025 年发布（DreamGen），开源 Apache-2.0，持续维护</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">机构</td><td style="word-wrap:break-word;width:1200px" width="1200">NVIDIA（GEAR / GR00T 团队）</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">特点</td><td style="word-wrap:break-word;width:1200px" width="1200"><ul><li><strong>世界模型生成未来视频</strong>：先用视频世界模型（Cosmos 系列）按语言指令"想象"机器人执行新任务的视频</li><li><strong>视频转可执行轨迹</strong>：通过逆动力学模型（IDM）或潜在动作模型（LAPA）把生成视频中的运动提取成动作序列，得到 neural trajectories</li><li><strong>跨本体与跨环境扩增</strong>：可从人类第一视角视频与少量遥操作数据出发，覆盖新物体、新环境与新任务，显著降低真实采集成本</li><li><strong>与 GR00T 系列配套</strong>：产出的合成轨迹可直接用于 VLA / 策略训练，作为数据飞轮的一环</li></ul></td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">使用场景</td><td style="word-wrap:break-word;width:1200px" width="1200"><ul><li>用少量遥操作演示扩增大规模训练数据</li><li>新环境 / 新物体 / 新任务的零样本数据合成</li><li>跨本体策略训练与数据飞轮构建</li><li>世界模型驱动的策略预演与评估</li></ul></td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">案例</td><td style="word-wrap:break-word;width:1200px" width="1200"><ul><li>DreamGen 流程在 GR-1 等人形平台上验证：用合成 neural trajectories 训练后，可在未见环境与任务上完成新行为</li></ul></td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">数据与模型</td><td style="word-wrap:break-word;width:1200px" width="1200">GR00T-Dreams blueprint（基于 Cosmos 世界模型权重）；产出 neural trajectories 数据集</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">官方链接</td><td style="word-wrap:break-word;width:1200px" width="1200"><a href="https://github.com/NVIDIA/GR00T-Dreams">GitHub NVIDIA/GR00T-Dreams</a> · <a href="https://arxiv.org/abs/2505.12705">论文 arXiv 2505.12705</a></td></tr>
</tbody>
</table>

### Genesis

<div align="center">
  <img src="tools-img/genesis.jpg" alt="Genesis" style="width:100%">
</div>

<table style="width:100%;display:table;table-layout:fixed" width="100%">
<tbody>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">一句话摘要</td><td style="word-wrap:break-word;width:1200px" width="1200">面向物理 AI 的生成式仿真平台，统一多物理引擎与照片级渲染，号称比实时快数十万倍的仿真速度。</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">发布与维护</td><td style="word-wrap:break-word;width:1200px" width="1200">2024 年 12 月发布学术版，持续活跃维护（GitHub ⭐ 29.8k）；Apache 2.0 开源。</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">机构</td><td style="word-wrap:break-word;width:1200px" width="1200">斯坦福、CMU、MIT、清华、港大等 20 余所高校联合项目（Genesis-Embodied-AI）。</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">特点</td><td style="word-wrap:break-word;width:1200px" width="1200"><ul><li><strong>统一多物理引擎</strong>：刚体、FEM、MPM、SPH、PBD、IPC 等求解器共享同一场景状态</li><li>自研 <strong>Nyx 照片级渲染器</strong> + Luisa 光线追踪 + Pyrender 三条渲染路径</li><li><strong>Quadrants 跨平台编译器</strong>：Python kernel 编译至 CUDA/ROCm/Metal/Vulkan</li><li>内置深度相机、IMU、LiDAR、触觉、接触力等传感器仿真</li></ul></td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">使用场景</td><td style="word-wrap:break-word;width:1200px" width="1200"><ul><li>机器人操作/运动的强化学习与模仿学习大规模并行训练</li><li>可变形物体、流体、布料等多物理耦合的具身任务仿真</li><li>传感器级仿真数据生成（Sim2Real 训练数据管线）</li><li>从笔记本 GPU 到数据中心集群的可扩展训练</li></ul></td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">案例</td><td style="word-wrap:break-word;width:1200px" width="1200"><ul><li>RoboGen 等生成式仿真框架以其作为底层引擎</li><li>社区广泛用于四足/机械臂 RL 训练与多物理耦合演示</li></ul></td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">数据与模型</td><td style="word-wrap:break-word;width:1200px" width="1200">完全开源（Apache 2.0）；支持 URDF/MJCF/USD 等资产格式，内置示例场景库。</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">官方链接</td><td style="word-wrap:break-word;width:1200px" width="1200"><a href="https://github.com/Genesis-Embodied-AI/Genesis">github.com/Genesis-Embodied-AI/Genesis</a></td></tr>
</tbody>
</table>

### XTDrone

<div align="center">
  <img src="tools-img/xtdrone.jpg" alt="XTDrone" style="width:100%">
</div>

<table style="width:100%;display:table;table-layout:fixed" width="100%">
<tbody>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">一句话摘要</td><td style="word-wrap:break-word;width:1200px" width="1200">基于 ROS / PX4 / Gazebo 的开源无人机仿真平台，支持多机型与集群仿真，是无人机算法开发与教学的首选仿真环境。</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">发布与维护</td><td style="word-wrap:break-word;width:1200px" width="1200">开源项目，持续维护更新（GitHub ⭐ 6.5k）。</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">机构</td><td style="word-wrap:break-word;width:1200px" width="1200">robin-shaun 等开源贡献者（国防科技大学背景）。</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">特点</td><td style="word-wrap:break-word;width:1200px" width="1200"><ul><li><strong>多机型支持</strong>：多旋翼、固定翼、复合翼无人机，以及无人车、无人船、机械臂</li><li><strong>全栈仿真</strong>：动力学、传感器（相机 / 激光 / IMU）、控制、状态估计与 3D 场景</li><li><strong>深度集成 PX4 与 ROS</strong>，支持 Offboard 控制、SLAM、路径规划等算法验证</li><li>配套教程完善、社区活跃，教学与科研广泛使用</li></ul></td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">使用场景</td><td style="word-wrap:break-word;width:1200px" width="1200"><ul><li>无人机控制、避障、路径规划算法的开发与仿真验证</li><li>视觉 SLAM、目标跟踪、编队与集群仿真</li><li>PX4 固件开发与软硬件在环验证（SITL / HITL）</li><li>高校无人机课程、毕业设计与竞赛备赛</li></ul></td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">案例</td><td style="word-wrap:break-word;width:1200px" width="1200"><ul><li>大量无人机开发者先在此仿真验证算法、再部署真机</li><li>被高校课程与工作坊用作 PX4 入门仿真环境</li></ul></td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">数据与模型</td><td style="word-wrap:break-word;width:1200px" width="1200">完全开源；基于 PX4、Gazebo 与 ROS 生态，自带示例场景与传感器模型。</td></tr>
<tr><td style="width:110px;min-width:110px;max-width:110px" width="110">官方链接</td><td style="word-wrap:break-word;width:1200px" width="1200"><a href="https://github.com/robin-shaun/XTDrone">github.com/robin-shaun/XTDrone</a></td></tr>
</tbody>
</table>

- **BEHAVIOR-1K** — [`StanfordVL/BEHAVIOR-1K`](https://github.com/StanfordVL/BEHAVIOR-1K) ⭐ 1.5k
  📄 斯坦福大学出品，1,000 种日常生活活动的具身 AI 基准测试与仿真平台

- **Prometheus** — [`amov-lab/Prometheus`](https://github.com/amov-lab/Prometheus) ⭐ 4.5k
  📄 面向自主无人机的开源软件系统，支持目标检测、SLAM 导航、编队控制等

- **Aerial Gym** — [`github.com/ntnu-arl/aerial_gym_simulator`](https://github.com/ntnu-arl/aerial_gym_simulator)
  📄 基于 Isaac Gym 的空中机器人仿真环境，支持无人机强化学习训练。

- **BEHAVIOR** — [`behavior.stanford.edu`](https://behavior.stanford.edu/)
  📄 大规模交互仿真基准。基于SAPIEN引擎构建，包含100个日常家居物品和30个复杂任务（如"把湿毛巾挂起来"），提供一套完整的物理交互能力测试环境。

- **CARLA** — [`carla.org`](https://carla.org)
  📄 面向自动驾驶与机器人研究的开源仿真器，提供城市道路、交通参与者、传感器和场景脚本能力。

- **CoppeliaSim (V-REP)** — [`www.coppeliarobotics.com`](https://www.coppeliarobotics.com)
  📄 支持远程 API、内嵌脚本等多种接口的机器人仿真平台，适用于教学、研究和工业原型验证。

- **DISCOVERSE** — [`air-discoverse.github.io`](https://air-discoverse.github.io/)
  📄 面向 Real2Sim2Real 的高保真仿真框架，结合 3DGS 场景表示、MuJoCo 物理和控制接口。

- **Drake** — [`github.com/RobotLocomotion/drake`](https://github.com/RobotLocomotion/drake)
  📄 面向机器人建模、规划与控制的工具包，适用于系统分析、仿真和算法研究。

- **EmbodiedCity** — [`github.com/tsinghua-fib-lab/EmbodiedCity`](https://github.com/tsinghua-fib-lab/EmbodiedCity)
  📄 真实开放环境具身智能平台。清华大学发布，基于虚幻引擎5打造真实城市环境，提供在线和离线两种部署方式，支持智能体在开放城市中进行导航与任务规划。

- **Gazebo Sim** — [`gazebosim.org`](https://gazebosim.org)
  📄 高保真度开源机器人仿真器，支持多种物理引擎（ODE、Bullet、DART），提供逼真渲染和传感器模型，是 ROS 生态中的主流仿真平台之一。

- **Genesis** — [`genesis-embodied-ai.github.io`](https://genesis-embodied-ai.github.io/)
  📄 通用机器人仿真引擎。专为生成式物理智能设计，集成了刚体、流体、软体等多种物理求解器，旨在解决复杂场景下的仿真难题。

- **GRUtopia** — [`github.com/OpenRobotLab/GRUtopia`](https://github.com/OpenRobotLab/GRUtopia)
  📄 通用具身智能仿真平台。由上海人工智能实验室发布，提供海量高质量可交互场景与数据，支持简单代码定义任务，是解决具身智能数据稀缺问题的核心工具。

- **Gymnasium-Robotics** — [`robotics.farama.org`](https://robotics.farama.org/)
  📄 基于 Gymnasium API 的机器人仿真环境集合，适合强化学习算法开发、复现和标准化比较。

- **Habitat Sim** — [`github.com/facebookresearch/habitat-sim`](https://github.com/facebookresearch/habitat-sim)
  📄 Meta 开源的高性能 3D 仿真器，常与 Habitat-Lab 配合使用，适用于大规模场景导航与交互任务。

- **Habitat 3.0** — [`aihabitat.org`](https://aihabitat.org/)
  📄 社交具身AI仿真平台。Meta AI推出的最新版本，专注于人与机器人、机器人与机器人之间的交互，支持高精度的社会行为模拟和导航任务。

- **ManiSkill3** — [`github.com/haosulab/ManiSkill`](https://github.com/haosulab/ManiSkill)
  📄 下一代操作技能仿真框架。上海AI实验室推出的最新版本，专为训练通用操作策略设计，支持更复杂的铰接物体（如抽屉、门把手）和更高效的并行物理模拟。

- **MORSE Simulator** — [`morse-simulator.github.io`](https://morse-simulator.github.io/)
  📄 基于 Blender 的学术机器人仿真器，支持移动机器人、人机交互和多中间件接入。

- **MuJoCo** — [`github.com/google-deepmind/mujoco`](https://github.com/google-deepmind/mujoco)
  📄 高性能物理引擎，专为机器人、生物力学和图形学设计，广泛应用于强化学习和运动控制研究。

- **NVIDIA Isaac Gym** — [`developer.nvidia.com/isaac-gym`](https://developer.nvidia.com/isaac-gym)
  📄 面向机器人学习的高性能强化学习仿真环境，支持 GPU 加速的大规模并行训练。

- **NVIDIA Isaac Sim** — [`developer.nvidia.com/isaac-sim`](https://developer.nvidia.com/isaac-sim)
  📄 基于 Omniverse 构建的机器人仿真平台，支持物理 AI 训练、合成数据生成和 Sim2Real 工作流。

- **NVIDIA RAD-MARS** — [`developer.nvidia.com/omniverse`](https://developer.nvidia.com/omniverse)
  📄 机器人辅助设计与仿真平台。基于Omniverse构建，允许在物理级逼真的环境中设计机器人硬件并测试运动学算法，连接了机械设计与AI训练。

- **OmniGibson** — [`behavior.stanford.edu/omnigibson/overview.html`](https://behavior.stanford.edu/omnigibson/overview.html)
  📄 基于 Isaac Sim 的具身智能仿真框架，支持交互场景、任务定义、数据采集与并行环境训练。

- **PyBullet** — [`github.com/bulletphysics/bullet3`](https://github.com/bulletphysics/bullet3)
  📄 基于 Bullet 物理引擎的 Python 接口，轻量易用，适合快速原型开发和强化学习实验。

- **RLBench** — [`github.com/stepjam/RLBench`](https://github.com/stepjam/RLBench)
  📄 大规模视觉引导机器人操作 benchmark 与学习环境，覆盖强化学习、模仿学习、多任务和少样本设置。

- **RoboCasa** — [`robocasa.ai`](https://robocasa.ai/)
  📄 面向日常家居操作任务的大规模仿真框架，支持多场景、多对象、示教数据和 benchmark。

- **robosuite** — [`github.com/ARISE-Initiative/robosuite`](https://github.com/ARISE-Initiative/robosuite)
  📄 基于 MuJoCo 的模块化机器人学习仿真框架与基准套件，适合操作任务研究与复现实验。

- **RobotStudio** — [`www.abb.com/global/en/areas/robotics/products/software/robotstudio-suite`](https://www.abb.com/global/en/areas/robotics/products/software/robotstudio-suite)
  📄 ABB 官方机器人编程、仿真和离线编程软件，适合工业机器人工作站开发。

- **SAPIEN** — [`github.com/haosulab/SAPIEN`](https://github.com/haosulab/SAPIEN)
  📄 面向部件级交互和操作任务的仿真环境，支持铰接物体建模与操作学习研究。

- **SimplerEnv** — [`github.com/simpler-env/SimplerEnv`](https://github.com/simpler-env/SimplerEnv)
  📄 面向真实机器人操作策略的仿真评测环境，支持在统一设置下复现和比较 real-to-sim manipulation policy。

- **UnrealCV** — [`unrealcv.org`](https://unrealcv.org/)
  📄 连接 Unreal Engine 与外部视觉 / 机器人程序的开源插件，适合构建仿真环境和合成数据工作流。

- **Webots** — [`cyberbotics.com`](https://cyberbotics.com)
  📄 开源跨平台机器人仿真桌面应用，提供完整的建模、编程与仿真环境。

- **跨维智能 DexVerse** — [`dexforce.com`](https://www.dexforce.com/)
  📄 生成式仿真引擎（WAIC 2026 发布），面向具身智能大规模训练的国产自主基础设施，支持实时多物理场仿真与生成式仿真，可将真实场景快速转化为可训练虚拟环境。
[↑ 回目录](#toc)

<a id="models"></a>

## **🤖 模型**

按动作策略、感知推理、系统与论文分类，查找模型代码及相关入口。

**[查看模型与策略实现](04-models.md)**

[返回目录](#toc)

<a id="general-tools"></a>

## 🧰 通用工具与库

> 涵盖仿真工具、开发框架、中间件、基准和其他通用库

- **AI2-THOR** — [`ai2thor.allenai.org`](https://ai2thor.allenai.org/)
  📄 语义交互模拟器。由艾伦研究所开发，拥有200+精细房间和2600+可交互物体，支持复杂的物体状态改变（如切片、烹饪）。

- **cuRobo** — [`github.com/NVlabs/curobo`](https://github.com/NVlabs/curobo)
  📄 NVIDIA 开源的 CUDA 加速机器人运动生成库，支持逆运动学、碰撞检测、轨迹优化与高自由度规划。

- **DORA** — [`github.com/dora-rs/dora`](https://github.com/dora-rs/dora)
  📄 面向 AI 机器人应用的数据流中间件，支持低时延、可组合、分布式的数据处理管线。

- **Intern-Robotics** — [`internrobotics.shlab.org.cn`](https://internrobotics.shlab.org.cn/)
  📄 书生具身全栈框架。上海人工智能实验室开源的具身智能全栈框架，涵盖导航、操作、运动大模型等，推动具身大脑的全栈化与量产。

- **OpenXLab** — [`openxlab.org.cn`](https://openxlab.org.cn/)
  📄 具身智能开源开放平台。上海AI实验室推出的综合性平台，提供从数据处理、算法训练到部署的全套工具链，旨在降低具身智能的研发门槛。

- **RobotecAI RAI** — [`github.com/RobotecAI/rai`](https://github.com/RobotecAI/rai)
  📄 RobotecAI 开源的 agentic robotics framework，基于 ROS 2 工具链，支持自然语言交互、多模态能力集成和机器人任务执行。

- **RoboGen** — [`robogen-ai.github.io`](https://robogen-ai.github.io/)
  📄 代码生成式机器人框架。由MIT等机构推出，利用大语言模型自动生成包含感知、规划、控制逻辑的完整Python代码，实现"代码即策略"的自动化生成。

- **ROS / ROS2** — [`www.ros.org`](https://www.ros.org)
  📄 机器人操作系统，提供丰富工具和库，支持模块化开发与分布式计算，是机器人软件开发的行业标准。

- **RQT Frame Editor** — [`github.com/ipa320/rqt_frame_editor_plugin`](https://github.com/ipa320/rqt_frame_editor_plugin)
  📄 用于创建和调整 TF 坐标系的 rqt 插件，便于处理多传感器和多机器人坐标关系。

- **Theseus** — [`github.com/facebookresearch/theseus`](https://github.com/facebookresearch/theseus)
  📄 可微非线性优化库，适合机器人和视觉中的状态估计、几何优化、轨迹优化与端到端可微系统构建。

- **VEX Robotics Software** — [`www.vexrobotics.com/?srsltid=AfmBOoqB_9zu0-eFHO4wzVB_33rsABV6DRRJ_drQfuk67n-MLcUmVy9M`](https://www.vexrobotics.com/?srsltid=AfmBOoqB_9zu0-eFHO4wzVB_33rsABV6DRRJ_drQfuk67n-MLcUmVy9M)
  📄 面向 VEX 机器人平台的软件工具，支持拖放式编程，常用于教育场景。

- **具识智能 insightOS Semantic** — [`insightos.cn`](https://www.insightos.cn/)
  📄 具身语义智能体系统（WAIC 2026 发布），以语义为中枢贯通"理解—规划—执行—进化"全链路，支持用自然语言指挥多台异构机器人协同作业。

- **穹彻智能 RoboPocket** — [`noematrix.ai`](https://www.noematrix.ai/)
  📄 无本体数据采集系统（WAIC 2026 发布），大幅降低真实世界数据采集门槛，单日可管理近万条数据，完全摆脱对遥操作数据的依赖。

- **腾讯 TairosAgent 具身智能体框架** — [`tairos.tencent.com`](https://tairos.tencent.com/)
  📄 具身原生智能体框架（WAIC 2026 发布），三层系统（感知反应/认知决策/探索沉淀）全部围绕具身任务原生设计，维护环境/本体/任务三类记忆。

- **腾讯 Apexio 原生具身智能体** — [`tairos.tencent.com`](https://tairos.tencent.com/)
  📄 持续在线具身智能体（WAIC 2026 发布），三层不同频率并行：认知系统按需唤醒、感知行动系统 15Hz 持续运行、执行系统高频反射响应。

<a id="learning-frameworks"></a>
<a id="-学习框架"></a>

## **🏗️ 学习框架**

按训练框架、机器人训练实现、采集工具和评测环境分类。

**[查看机器人学习、训练与数据采集](04-learning.md)**

[返回目录](#toc)

<a id="robot-projects"></a>

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

- **AgileX Cobot Magic** — [`agilexrobotics`](https://github.com/agilexrobotics)
  📄 基于 Mobile ALOHA 架构的开源双臂移动操作平台（松灵机器人），含 PiPER 机械臂、AGV 底盘和深度相机

- **vlm_arm** — [`TommyZihao/vlm_arm`](https://github.com/TommyZihao/vlm_arm)
  📄 机械臂 + 大模型 + 多模态（同济子豪兄）

- **超迷你机械臂 (Dummy-Robot)** — [`peng-zhihui/Dummy-Robot`](https://github.com/peng-zhihui/Dummy-Robot)
  📄 自制迷你机械臂机器人（稚晖君）

- **ElectronBot 迷你桌面机器人** — [`peng-zhihui/ElectronBot`](https://github.com/peng-zhihui/ElectronBot)
  📄 非常小巧的桌面机器人（稚晖君）

- **解魔方机器人** — [`diy-robots.com`](http://www.diy-robots.com/?page_id=46)
  📄 基于乐高的解魔方机器人（动力老男孩）

### 移动机器人

- **MiniRover 火星车** — [`peng-zhihui/MiniRover-Hardware`](https://github.com/peng-zhihui/MiniRover-Hardware)
  📄 自制火星车的开源资料（稚晖君）

- **ONE-Robot 独轮机器人** — [`peng-zhihui/ONE-Robot`](https://github.com/peng-zhihui/ONE-Robot)
  📄 基于 IMU 和 STM32 的独轮自平衡机器人（稚晖君）

### 其他

- **ALOHA 2** — [`aloha-2.github.io`](https://aloha-2.github.io/)
  📄 面向双臂遥操作与具身数据采集的低成本开源硬件平台，附带教程与 MuJoCo 仿真模型。

- **北京人形机器人创新中心·慧思开物** — [`open.x-humanoid-cloud.com`](https://open.x-humanoid-cloud.com/)
  📄 面向通用具身智能场景的工具链平台，覆盖技能调用、智能体配置到场景部署。

- **京东 JoyInside** — [`joyinside.com`](https://joyinside.com/)
  📄 面向机器人与 AI 玩具等智能硬件的对话智能体平台。

- **kscale·K-Bot** — [`github.com/kscalelabs/kbot`](https://github.com/kscalelabs/kbot)
  📄 面向开发者和研究人员的开源全栈人形机器人平台。

- **智元灵创平台 (LinkCraft)** — [`www.agibot.com.cn/filepage/295.html`](https://www.agibot.com.cn/filepage/295.html)
  📄 智元机器人推出的零代码机器人内容创作平台，支持动作模仿、语音驱动和任务脚本生成。

- **腾讯 Tairos (钛螺丝)** — [`tairos.tencent.com`](https://tairos.tencent.com/)
  📄 面向机器人场景的具身智能开放平台，提供模型、开发工具和数据服务。

- **Viam** — [`www.viam.com`](https://www.viam.com)
  📄 面向机器人构建、部署和管理的软件平台，提供统一 API、模块注册、远程运维和车队级管理能力。

- **网易灵动·灵掘** — [`lingdong.fuxi.163.com/productSummary/wj`](https://lingdong.fuxi.163.com/productSummary/wj)
  📄 面向矿山挖掘机装车场景的具身智能模型与训练框架。

- **RoboWiki** — [`yfrobotics/robowiki`](https://github.com/yfrobotics/robowiki)
  📄 机器人领域的维基百科（云飞机器人实验室）

[↑ 回目录](#toc)

<a id="reasoning-rl"></a>

## **🧠 推理 / 强化学习**

强化学习训练实现与通用多模态推理研究在细分文档中分别列出。

**[查看学习、训练与推理资源](04-learning.md)**

[返回目录](#toc)

<a id="slam-perception"></a>
<a id="slam-与感知"></a>
<a id="-slam-与感知"></a>

## **🗺️ SLAM 与感知**

合并原来分散的 SLAM 条目，按定位、标定、图像点云和导航分类。

**[查看SLAM、感知与标定](04-perception.md)**

[返回目录](#toc)

<a id="middleware-ros"></a>

## 🔧 中间件与 ROS 工具

- **AimRT** — [`AimRT/AimRT`](https://github.com/AimRT/AimRT)
  📄 面向现代机器人领域的运行时开发框架，基于 Modern C++，轻量易部署，兼容 ROS2/HTTP/Grpc

- **Cyclone DDS** — [`projects.eclipse.org/projects/iot.cyclonedds`](https://projects.eclipse.org/projects/iot.cyclonedds)
  📄 Eclipse 基金会维护的 DDS 实现，以鲁棒性和网络适应性见长，常用于 ROS 2 部署。

- **DDS (Data Distribution Service)** — [`www.omg.org/omg-dds-portal/index.htm`](https://www.omg.org/omg-dds-portal/index.htm)
  📄 实时分布式系统的发布-订阅通信标准，也是 ROS 2 中间件体系的基础。

- **Fast DDS (原 Fast RTPS)** — [`fast-dds.docs.eprosima.com/en/latest/index.html`](https://fast-dds.docs.eprosima.com/en/latest/index.html)
  📄 eProsima 的 DDS 实现，为 ROS 2 提供高性能、可配置的通信中间件。

- **MQTT** — [`mqtt.org`](https://mqtt.org/)
  📄 轻量级发布-订阅消息协议，常用于机器人边缘设备、网关和云端数据传输。

- **Open-RMF** — [`www.open-rmf.org`](https://www.open-rmf.org)
  📄 面向多机器人车队与楼宇基础设施协同的开源框架，支持任务调度、资源协调和互操作。

- **Zenoh** — [`zenoh.io`](https://zenoh.io/)
  📄 面向机器人与边缘系统的轻量级数据通信协议与中间件，适合分布式场景下的高效 pub/sub 与查询。

- **Foxglove** — [`foxglove.dev`](https://foxglove.dev)
  📄 面向机器人与 Physical AI 的数据可视化和可观测性平台，支持 ROS、MCAP、3D 场景与多模态日志调试。

- **PlotJuggler** — [`github.com/facontidavide/PlotJuggler`](https://github.com/facontidavide/PlotJuggler)
  📄 面向机器人时序数据的可视化与分析工具，适合话题调试、日志回放和指标对比。

- **ros2_latency_analysis** — [`github.com/TUM-AVS/ros2_latency_analysis`](https://github.com/TUM-AVS/ros2_latency_analysis)
  📄 面向 ROS 2 的延迟分析工具，可拆解端到端、通信与计算时延瓶颈。

- **ROSboard** — [`github.com/dheera/rosboard`](https://github.com/dheera/rosboard)
  📄 将 ROS / ROS 2 话题转换为网页仪表盘的轻量工具，适合远程监控和移动端查看。

- **rqt_plot** — [`docs.ros.org/en/rolling/p/rqt_plot`](https://docs.ros.org/en/rolling/p/rqt_plot/)
  📄 ROS / ROS 2 常用绘图插件，可实时查看话题数值变化，适合调参与快速排障。

- **RViz / RViz2** — [`docs.ros.org/en/rolling/p/rviz2`](https://docs.ros.org/en/rolling/p/rviz2/)
  📄 ROS / ROS 2 核心 3D 可视化工具，可实时查看机器人模型、TF、点云、路径和地图。

- **system_fingerprint** — [`github.com/MetroRobots/ros_system_fingerprint`](https://github.com/MetroRobots/ros_system_fingerprint)
  📄 采集 ROS / ROS 2 运行环境、节点、话题和 TF 状态的系统快照工具，便于排障与交付验收。

- **Webviz** — [`webviz.io`](https://webviz.io/)
  📄 面向 ROS bag 与实时机器人数据的浏览器可视化平台，适合布局式分析、回放和远程调试。

- **Arduino IDE** — [`www.arduino.cc`](https://www.arduino.cc)
  📄 开源电子原型开发工具，适合传感器、执行器和控制板快速联调，支持 C / C++ 编程。

- **Clearpath·Husky** — [`clearpathrobotics.com`](https://clearpathrobotics.com)
  📄 常见 ROS 科研移动机器人平台，提供标准化接口，适合户外导航与算法验证。

- **Clearpath·TurtleBot 4** — [`www.turtlebot.com`](https://www.turtlebot.com/)
  📄 面向教学和研究的 ROS2 入门平台，开箱即用，适合导航与多传感器实验。

- **MoveIt** — [`moveit.ai`](https://moveit.ai)
  📄 面向 ROS 的运动规划、操作和运动学框架，常用于机械臂规划、抓取和任务编排。

- **OMPL** — [`ompl.kavrakilab.org`](https://ompl.kavrakilab.org)
  📄 开源运动规划库，包含多种经典采样规划算法，常用于路径规划和机械臂规划。

[↑ 回目录](#toc)

<a id="other"></a>

## 🛒 其他

> 未被以上分类覆盖的工具、平台与项目

[↑ 回目录](#toc)

*原资源列表标注日期：2026年6月22日。本次仅重整模型、学习训练与 SLAM 分类；其余资源说明沿用原文。*
