
# 机器人系统与开源硬件

收录开源机器人与硬件项目，重点介绍项目功能、硬件方案、官方代码和复现所需资料，帮助开发者快速找到适合自己的机器人项目。


## 目录

- [🆕 最新亮点](#new-projects)
  - [01. RIG-Hover](#project-rig-hover)
  - [02. OpenCat / Bittle X](#project-opencat)
  - [03. Open Duck Mini v2](#project-open-duck-mini)
  - [04. ToddlerBot 2.0](#project-toddlerbot)
  - [05. Berkeley Humanoid Lite V1](#project-berkeley-humanoid-lite)


- [🤖 更多机器人项目](#open-source-projects)
  - [🦾 1. 整机与开源硬件](#硬件整机)
    - [人形机器人](#hardware-humanoid)
    - [四足机器人](#hardware-quadruped)
    - [机械臂与桌面机器人](#hardware-arms)
    - [移动机器人](#hardware-mobile)
  - [👁️ 2. 感知与操作算法](#感知操作)
    - [SLAM 与感知](#algo-slam)
    - [抓取与操作](#algo-grasping)
  - [🧠 3. 具身模型与平台工具链](#模型平台)
    - [具身模型](#model-vla)
    - [平台与工具链](#model-platform)
  - [🛠️ 4. 数据、训练与遥操作](#数据训练)
    - [学习与训练框架](#data-rl)
    - [数据采集与遥操作](#data-teleop)
    - [教程与知识库](#data-tutorial)

   

## 🆕 最新亮点

<a id="new-projects"></a>

<a id="project-rig-hover"></a>

<p align="center">
  <img src="datasets-img/rig-hover-01.gif"
       alt="RIG-Hover 双轮自平衡机器人动态演示"
       height="300">
</p>

<h3 align="center"><strong>01. RIG-Hover</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>摘要</strong></td>
      <td>基于 ESP32-S3 的开源双轮自平衡桌面机器人，集成运动控制、动态表情、语音交互与视觉感知。</td>
    </tr>
    <tr>
      <td><strong>特点</strong></td>
      <td>支持自平衡、LCD 动态表情、语音交互、人脸检测及蓝牙手柄控制。</td>
    </tr>
    <tr>
      <td><strong>硬件 <br> 方案</strong></td>
      <td>ESP32-S3、QMI8658C 六轴 IMU、FOC 无刷电机、圆形 LCD、头部舵机、摄像头、I2S 数字麦克风及 3D 打印外壳。</td>
    </tr>
    <tr>
      <td><strong>GitHub  <br> 链接</strong></td>
      <td><a href="https://github.com/LuwuDynamics/rig_omni">LuwuDynamics/rig_omni</a></td>
    </tr>
  </tbody>
</table>

配套资料：[官方文档](https://wiki.xgorobot.com/kb/pet-hover) · [3D 打印模型](https://makerworld.com/en/models/2909205) · [烧录工具](https://tools.luwudynamics.ai)


<a id="project-opencat"></a>


<p align="center">
  <img src="datasets-img/opencat.gif"
       alt="OpenCat / Bittle X 四足机器人"
       height="300">
</p>

<h3 align="center"><strong>02. OpenCat / Bittle X</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>摘要</strong></td>
      <td>基于开源四足机器人框架 OpenCat 的机器狗项目，支持动作编程与运动控制，适合入门机器人软硬件开发。</td>
    </tr>
    <tr>
      <td><strong>特点</strong></td>
      <td>支持行走、跑动、转弯及预设动作；可通过图形化编程、C/C++ 或 Python 修改动作，并可扩展摄像头、树莓派或 Jetson，进一步开发视觉和语音功能。</td>
    </tr>
    <tr>
      <td><strong>硬件 <br> 方案</strong></td>
      <td>Bittle X 机器人套件、ESP32 控制板、关节舵机和 IMU；摄像头、树莓派或 Jetson 可作为扩展方案。具体配置以套件版本为准。</td>
    </tr>
    <tr>
      <td><strong>GitHub <br> 链接</strong></td>
      <td><a href="https://github.com/PetoiCamp/OpenCatEsp32-Quadruped-Robot">OpenCatESP32-Quadruped-Robot</a></td>
    </tr>
  </tbody>
</table>


<a id="project-open-duck-mini"></a>



<table width="100%">
  <tr>
    <td align="center" width="33%">
      <img src="datasets-img/open-duck-mini-v2.png" width="220" alt="RIG-Hover">
    </td>
    <td align="center" width="33%">
      <img src="datasets-img/openduckminiv2-2.png" width="220" alt="OpenCat">
    </td>
    <td align="center" width="33%">
      <img src="datasets-img/openduckminiv2-3.png" width="220" alt="Open Duck Mini v2">
    </td>
  </tr>
</table>

<h3 align="center"><strong>03. Open Duck Mini v2</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>摘要</strong></td>
      <td>面向双足运动与强化学习研究的开源小型机器人，通过仿真训练行走策略，并将策略部署到真实机器人。</td>
    </tr>
    <tr>
      <td><strong>特点</strong></td>
      <td>支持站立、前后移动、左右移动和转向；使用 MuJoCo 相关仿真环境训练行走策略，并通过 ONNX 等部署流程将策略应用于真机，适合学习双足控制和 Sim-to-Real。</td>
    </tr>
    <tr>
      <td><strong>硬件 <br> 方案</strong></td>
      <td>3D 打印结构件、串行总线舵机、Raspberry Pi Zero 2 W、IMU、供电系统及线束。完整 BOM 和具体型号以对应版本的官方仓库为准。</td>
    </tr>
    <tr>
      <td><strong>GitHub <br> 链接</strong></td>
      <td><a href="https://github.com/apirrone/Open_Duck_Mini/tree/v2">Open Duck Mini v2</a></td>
    </tr>
  </tbody>
</table>


<a id="project-toddlerbot"></a>



<p align="center">
  <img src="datasets-img/toddlerbot.png"
       alt="ToddlerBot 2.0 人形机器人"
       height="300">
</p>

<h3 align="center"><strong>04. ToddlerBot 2.0</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>摘要</strong></td>
      <td>面向机器人学习与全身运动操作研究的开源人形机器人平台，提供仿真、遥操作、强化学习及视觉操作相关工具链。</td>
    </tr>
    <tr>
      <td><strong>特点</strong></td>
      <td>支持全向行走、全身动作及双手操作任务；提供 MuJoCo 仿真、强化学习、关键帧动作、全身遥操作和视觉操作策略，适合研究运动控制与操作能力的结合。</td>
    </tr>
    <tr>
      <td><strong>硬件 <br> 方案</strong></td>
      <td>3D 打印结构件、Dynamixel 舵机、Jetson 计算平台、定制电源与通信 PCB、摄像头及相关线束。具体配置按对应版本的官方文档核对。</td>
    </tr>
    <tr>
      <td><strong>GitHub <br> 链接</strong></td>
      <td><a href="https://github.com/hshi74/toddlerbot">ToddlerBot 官方代码与文档</a></td>
    </tr>
  </tbody>
</table>


<a id="project-berkeley-humanoid-lite"></a>



<p align="center">
  <img src="datasets-img/berkeley-humanoid-lite.png"
       alt="Berkeley Humanoid Lite V1 人形机器人"
       height="300">
</p>

<h3 align="center"><strong>05. Berkeley Humanoid Lite V1</strong></h3>

<table width="100%">
  <tbody>
      <td><strong>摘要</strong></td>
      <td>面向人形机器人研究的开源平台，开放机械结构、执行器设计、底层控制及强化学习工具链，适合学习人形机器人系统集成。</td>
    </tr>
    <tr>
      <td><strong>特点</strong></td>
      <td>支持强化学习驱动的行走与遥操作抓取；开放 CAD、低层控制、机器人模型、Isaac Lab 训练及真机部署相关资料。</td>
    </tr>
    <tr>
      <td><strong>硬件 <br> 方案</strong></td>
      <td>无刷电机、模块化 3D 打印摆线减速器、关节电机控制器、CAN 通信总线、IMU 和机载计算平台。V1 的具体执行器及控制器配置以对应版本的 BOM 为准。</td>
    </tr>
    <tr>
      <td><strong>GitHub <br> 链接</strong></td>
      <td><a href="https://github.com/HybridRobotics/Berkeley-Humanoid-Lite">Berkeley Humanoid Lite</a></td>
    </tr>
  </tbody>
</table>


<a id="existing-projects"></a>



## 🤖 更多机器人项目

<a id="open-source-projects"></a>

<a id="hardware"></a>

<a id="humanoid"></a>

### 🦾 1. 整机与开源硬件

涵盖人形、四足、机械臂与移动机器人项目及相关硬件资源。

<a id="hardware-humanoid"></a>
#### 人形机器人

- **[AgiBot X1](https://github.com/AgibotTech/agibot_x1_infer)** — [推理](https://github.com/AgibotTech/agibot_x1_infer) · [训练](https://github.com/AgibotTech/agibot_x1_train) · [硬件](https://github.com/AgibotTech/agibot_x1_hardware)  
  📄 智元机器人 X1 完整开源人形机器人项目，包含推理模块、强化学习训练代码和全套硬件设计资料。

- **[OpenLoong 青龙](https://github.com/loongOpen)**  
  📄 全栈开源人形机器人项目，包含动力学控制（MPC+WBC）、硬件设计、训练平台和技能调度框架。

- **[Fourier N1](https://github.com/FFTAI)**  
  📄 傅利叶智能人形机器人项目，提供硬件设计、BOM、装配指南和 Fourier-GRX SDK 等相关资料。

- **[EngineAI Humanoid](https://github.com/engineai-robotics/engineai_humanoid)**  
  📄 EngineAI 双足机器人 SA01/PM01 的开源运动控制算法，采用端到端神经网络实现拟人步态。

- **[Unitree Qmini](https://github.com/unitreerobotics/Qmini)**  
  📄 宇树科技开源双足平台，提供 BOM、装配指南、RoboTamer4Qmini 控制框架与 URDF 模型。

- **[K-Bot](https://github.com/kscalelabs/kbot)**  
  📄 面向开发者和研究人员的开源全栈人形机器人平台。

<a id="hardware-quadruped"></a>
#### 四足机器人

- **[OpenCat](https://github.com/PetoiCamp/OpenCat)** ⭐ 15k  
  📄 开源四足机器人平台。

- **[小米 CyberDog](https://github.com/MiRoboticsLab/cyberdog_ros2)**  
  📄 小米 CyberDog 四足机器人的开源软件和硬件资料。

- **[宇树科技四足机器人 ROS](https://github.com/unitreerobotics/unitree_ros)**  
  📄 宇树科技四足机器人 Go1/Go2 的 ROS 驱动包。

<a id="hardware-arms"></a>
#### 机械臂与桌面机器人

- **[vlm_arm](https://github.com/TommyZihao/vlm_arm)**  
  📄 机械臂、大模型与多模态技术结合的开源项目（同济子豪兄）。

- **[超迷你机械臂 Dummy-Robot](https://github.com/peng-zhihui/Dummy-Robot)**  
  📄 自制迷你机械臂机器人（稚晖君）。

- **[ElectronBot 迷你桌面机器人](https://github.com/peng-zhihui/ElectronBot)**  
  📄 非常小巧的桌面机器人（稚晖君）。

- **[解魔方机器人](http://www.diy-robots.com/?page_id=46)**  
  📄 基于乐高的解魔方机器人（动力老男孩）。

<a id="hardware-mobile"></a>
#### 移动机器人

- **[MiniRover 火星车](https://github.com/peng-zhihui/MiniRover-Hardware)**  
  📄 自制火星车的开源资料（稚晖君）。

- **[ONE-Robot 独轮机器人](https://github.com/peng-zhihui/ONE-Robot)**  
  📄 基于 IMU 和 STM32 的独轮自平衡机器人（稚晖君）。

---

<a id="perception"></a>

### 👁️ 2. 感知与操作算法

涵盖 SLAM、多传感器融合、视觉感知、抓取算法及相关传感器资源。

<a id="slam"></a>
#### SLAM 与感知

- **[视觉 SLAM 十四讲](https://github.com/gaoxiang12/slambook2)** ⭐ 12k  
  📄 SLAM 领域经典中文教程及配套代码（高翔）。

- **[VINS-Mono](https://github.com/HKUST-Aerial-Robotics/VINS-Mono)** ⭐ 5k  
  📄 鲁棒的单目视觉惯性状态估计器（香港科技大学）。

- **[VINS-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion)**  
  📄 基于优化的多传感器状态估计器，支持单目、双目相机与 IMU 融合。

- **[LIO-SAM](https://github.com/TixiaoShan/LIO-SAM)** ⭐ 3.5k  
  📄 紧耦合激光惯性里程计与建图方案。

- **[FAST_LIO](https://github.com/hku-mars/FAST_LIO)** ⭐ 2.5k  
  📄 计算高效且鲁棒的 LiDAR 惯性里程计（港大 MARS 实验室）。

- **[FAST-LIVO2](https://github.com/hku-mars/FAST-LIVO2)**  
  📄 LiDAR、惯性与视觉紧耦合里程计方案。

- **[R3LIVE](https://github.com/hku-mars/r3live)** ⭐ 2.0k  
  📄 实时 RGB 彩色 LiDAR-惯性-视觉融合定位与建图方案。

- **[宇树科技 4D LiDAR SLAM](https://github.com/unitreerobotics/point_lio_unilidar)**  
  📄 基于 Point-LIO 算法适配宇树 L1 4D LiDAR 的 SLAM 方案。

<a id="grasping"></a>
#### 抓取与操作

- **[AnyGrasp](https://github.com/graspnet/anygrasp_sdk)**  
  📄 通用 6 自由度抓取位姿估计算法，支持机器人抓取检测。

- **[小觅双目相机系列](https://github.com/slightech/MYNT-EYE-S-SDK)**  
  📄 小觅双目相机相关 SDK，提供视觉与 SLAM 开发资源。

---

<a id="models"></a>

### 🧠 3. 具身模型与平台工具链

涵盖 VLA 操作模型、对话智能体、具身智能平台与零代码创作工具。

<a id="model-vla"></a>
#### 具身模型

- **[GR-1（ByteDance Model）](https://github.com/bytedance/GR-1)**  
  📄 字节跳动开源的视觉机器人操作模型，面向语言条件下的多任务机器人操作学习与动作预测。注意与智元 GR-1 人形机器人区分。

<a id="model-platform"></a>
#### 平台与工具链

- **[北京人形机器人创新中心·慧思开物](https://open.x-humanoid-cloud.com/)**  
  📄 面向通用具身智能场景的工具链平台，覆盖技能调用、智能体配置与场景部署。

- **[智元灵创平台 LinkCraft](https://www.agibot.com.cn/filepage/295.html)**  
  📄 智元机器人推出的零代码机器人内容创作平台，支持动作模仿、语音驱动和任务脚本生成。

- **[腾讯 Tairos（钛螺丝）](https://tairos.tencent.com/)**  
  📄 面向机器人场景的具身智能开放平台，提供模型、开发工具和数据服务。

- **[Viam](https://www.viam.com/)**  
  📄 面向机器人构建、部署和管理的软件平台，提供统一 API、模块注册、远程运维和车队管理能力。

- **[京东 JoyInside](https://joyinside.com/)**  
  📄 面向机器人与 AI 玩具等智能硬件的对话智能体平台。

- **[网易灵动·灵掘](https://lingdong.fuxi.163.com/productSummary/wj)**  
  📄 面向矿山挖掘机装车场景的具身智能模型与训练框架。

---

<a id="data"></a>

### 🛠️ 4. 数据、训练与遥操作

涵盖强化学习、模仿学习、数据采集、遥操作系统与机器人开发教程。

<a id="data-rl"></a>
#### 学习与训练框架

- **[Booster Gym](https://github.com/BoosterRobotics)**  
  📄 Booster T1/K1 人形机器人端到端强化学习运动控制框架，包含 RoboCup 自主踢球 Demo。

- **[Humanoid-Gym](https://github.com/roboterax/humanoid-gym)**  
  📄 基于 Isaac Gym 的人形机器人强化学习训练框架，支持零样本迁移至真实机器人。

- **[OpenR1-Multimodal](https://github.com/EvolvingLMMs-Lab/open-r1-multimodal)** ⭐ 1.5k  
  📄 探索 R1 推理范式在多模态模型上的应用，开源多模态强化学习训练样本。

- **[unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym)**  
  📄 宇树科技四足与人形机器人强化学习训练框架，基于 Isaac Gym。

- **[unitree_rl_lab](https://github.com/unitreerobotics/unitree_rl_lab)** · [MuJoCo 版本](https://github.com/unitreerobotics/unitree_rl_mjlab)  
  📄 宇树科技机器人强化学习实现，分别基于 Isaac Lab 和 MuJoCo。

- **[unitree_IL_lerobot](https://github.com/unitreerobotics/unitree_IL_lerobot)**  
  📄 基于 LeRobot 框架的模仿学习工具，用于 G1 双臂灵巧手数据训练与测试。

<a id="data-teleop"></a>
#### 数据采集与遥操作

- **[ALOHA 2](https://aloha-2.github.io/)**  
  📄 面向双臂遥操作与具身数据采集的低成本开源硬件平台，附带教程与 MuJoCo 仿真模型。

- **[DexCap](https://dex-cap.github.io/)**  
  📄 斯坦福开源的灵巧手数据采集系统，通过手部动作捕捉与深度相机采集人类灵巧手操作数据。

- **[Dobb-E](https://dobb-e.com/)**  
  📄 NYU 开源的家庭机器人数据采集与模仿学习方案，包含低成本手持采集硬件、数据集和学习框架。

- **[宇树科技 XR 遥操作](https://github.com/unitreerobotics/xr_teleoperate)**  
  📄 基于 Apple Vision Pro、Quest 等 XR 设备的 H1/G1 人形机器人遥操作系统。

<a id="data-tutorial"></a>
#### 教程与知识库

- **[RoboWiki](https://github.com/yfrobotics/robowiki)**  
  📄 机器人领域的维基百科（云飞机器人实验室）。

- **[宇树科技机器人控制教程](https://github.com/unitreerobotics/unitree_guide)**  
  📄 宇树科技四足机器人控制教程，适合入门学习与参考。


<a id="reasoning-rl"></a>

