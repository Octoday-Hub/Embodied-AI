# Robot Systems & Open-Source Hardware

A curated collection of open-source robotics and hardware projects. Each
entry highlights the robot’s capabilities, hardware requirements,
official code, and reproduction resources to help developers find
projects suited to their needs.

<a id="toc"></a>

## Contents

- [🆕 Latest Highlights](#new-projects)
  - [01. RIG-Hover](#project-rig-hover)
  - [02. OpenCat / Bittle X](#project-opencat)
  - [03. Open Duck Mini v2](#project-open-duck-mini)
  - [04. ToddlerBot 2.0](#project-toddlerbot)
  - [05. Berkeley Humanoid Lite V1](#project-berkeley-humanoid-lite)
- [🤖 More Robot Projects](#open-source-projects)
  - [🦾 1. Robot Systems & Open-Source Hardware](#hardware)
    - [Humanoid Robots](#hardware-humanoid)
    - [Quadruped Robots](#hardware-quadruped)
    - [Robotic Arms & Desktop Robots](#hardware-arms)
    - [Mobile Robots](#hardware-mobile)
  - [👁️ 2. Perception & Manipulation Algorithms](#perception)
    - [SLAM & Perception](#algo-slam)
    - [Grasping & Manipulation](#algo-grasping)
  - [🧠 3. Embodied Models & Platform Toolchains](#models)
    - [Embodied Models](#model-vla)
    - [Platforms & Toolchains](#model-platform)
  - [🛠️ 4. Data, Training & Teleoperation](#data)
    - [Learning & Training Frameworks](#data-rl)
    - [Data Collection & Teleoperation](#data-teleop)
    - [Tutorials & Knowledge Bases](#data-tutorial)


<a id="new-projects"></a>

## 🆕 Latest Highlights

<p align="center">
  <img src="datasets-img/rig-hover-01.gif"
       alt="RIG-Hover 双轮自平衡机器人动态演示"
       height="300">
</p>

<a id="project-rig-hover"></a>

<h3 align="center">
<strong>01. RIG-Hover</strong>
</h3>
<table width="100%">
<tbody>
<tr>
<td>
<strong>Summary</strong>
</td>
<td>
An open-source, ESP32-S3-based desktop robot with two-wheel
self-balancing, dynamic expressions, voice interaction, and visual
perception.
</td>
</tr>
<tr>
<td>
<strong>Features</strong>
</td>
<td>
Supports self-balancing, animated expressions on an LCD, voice
interaction, face detection, and Bluetooth gamepad control.
</td>
</tr>
<tr>
<td>
<strong>Hardware</strong>
</td>
<td>
ESP32-S3, QMI8658C six-axis IMU, FOC brushless motors, circular LCD,
head servo, camera, I2S digital microphone, and a 3D-printed enclosure.
</td>
</tr>
<tr>
<td>
<strong>GitHub</strong>
</td>
<td>
<a href="https://github.com/LuwuDynamics/rig_omni">LuwuDynamics/rig_omni</a>
</td>
</tr>
</tbody>
</table>

Related resources: [Official
Documentation](https://wiki.xgorobot.com/kb/pet-hover) · [3D-Printable
Model](https://makerworld.com/en/models/2909205) · [Flashing
Tool](https://tools.luwudynamics.ai)


<a id="project-opencat"></a>


<p align="center">
  <img src="datasets-img/opencat.gif"
       alt="OpenCat / Bittle X 四足机器人"
       height="300">
</p>

<h3 align="center"><strong>02. OpenCat / Bittle X</strong></h3>

</h3>
<table width="100%">
<tbody>
<tr>
<td>
<strong>Summary</strong>
</td>
<td>
A quadruped robot based on the open-source OpenCat framework. It
supports motion programming and locomotion control, making it suitable
for getting started with robotics hardware and software.
</td>
</tr>
<tr>
<td>
<strong>Features</strong>
</td>
<td>
Supports walking, running, turning, and predefined actions. Motions can
be modified using visual programming, C/C++, or Python. Cameras,
Raspberry Pi, or Jetson computers can be added for further vision and
voice capabilities.
</td>
</tr>
<tr>
<td>
<strong>Hardware</strong>
</td>
<td>
Bittle X robot kit, ESP32 control board, joint servos, and an IMU. A
camera, Raspberry Pi, or Jetson computer can be added as an extension.
The exact configuration depends on the kit version.
</td>
</tr>
<tr>
<td>
<strong>GitHub</strong>
</td>
<td>
<a href="https://github.com/PetoiCamp/OpenCatEsp32-Quadruped-Robot">OpenCatESP32-Quadruped-Robot</a>
</td>
</tr>
</tbody>
</table>


<a id="project-open-duck-mini"></a>

<table width="100%">
<tr>
<td align="center" width="33%">
<img src="datasets-img/open-duck-mini-v2.png" width="220" alt="Open Duck Mini v2 front view">
</td>
<td align="center" width="33%">
<img src="datasets-img/openduckminiv2-2.png" width="220" alt="Open Duck Mini v2 side view">
</td>
<td align="center" width="33%">
<img src="datasets-img/openduckminiv2-3.png" width="220" alt="Open Duck Mini v2 additional view">
</td>
</tr>
</table>
<h3 align="center">
<strong>03. Open Duck Mini v2</strong>
</h3>
<table width="100%">
<tbody>
<tr>
<td>
<strong>Summary</strong>
</td>
<td>
An open-source small bipedal robot for locomotion and reinforcement
learning research. Walking policies are trained in simulation and then
deployed on the physical robot.
</td>
</tr>
<tr>
<td>
<strong>Features</strong>
</td>
<td>
Supports standing, forward and backward movement, lateral movement, and
turning. Walking policies can be trained in MuJoCo-related simulation
environments and deployed to the real robot through workflows such as
ONNX, making it useful for learning bipedal control and sim-to-real
transfer.
</td>
</tr>
<tr>
<td>
<strong>Hardware</strong>
</td>
<td>
3D-printed structural parts, serial bus servos, Raspberry Pi Zero 2 W,
IMU, power system, and wiring. Check the official repository for the BOM
and exact component models for the relevant version.
</td>
</tr>
<tr>
<td>
<strong>GitHub</strong>
</td>
<td>
<a href="https://github.com/apirrone/Open_Duck_Mini/tree/v2">Open Duck
Mini v2</a>
</td>
</tr>
</tbody>
</table>


<a id="project-toddlerbot"></a>

<p align="center">
<img src="datasets-img/toddlerbot.png"
       alt="ToddlerBot 2.0 humanoid robot"
       height="300">
</p>
<h3 align="center">
<strong>04. ToddlerBot 2.0</strong>
</h3>
<table width="100%">
<tbody>
<tr>
<td>
<strong>Summary</strong>
</td>
<td>
An open-source humanoid robot platform for robot learning, whole-body
locomotion, and manipulation research, with tools for simulation,
teleoperation, reinforcement learning, and vision-based manipulation.
</td>
</tr>
<tr>
<td>
<strong>Features</strong>
</td>
<td>
Supports omnidirectional walking, whole-body motions, and bimanual
manipulation tasks. The toolchain includes MuJoCo simulation,
reinforcement learning, keyframe motions, whole-body teleoperation, and
vision-based manipulation policies.
</td>
</tr>
<tr>
<td>
<strong>Hardware</strong>
</td>
<td>
3D-printed structural parts, Dynamixel servos, a Jetson computing
platform, custom power and communication PCBs, cameras, and wiring.
Check the official documentation for the configuration of the relevant
version.
</td>
</tr>
<tr>
<td>
<strong>GitHub</strong>
</td>
<td>
<a href="https://github.com/hshi74/toddlerbot">ToddlerBot Code and
Documentation</a>
</td>
</tr>
</tbody>
</table>


<a id="project-berkeley-humanoid-lite"></a>

<p align="center">
<img src="datasets-img/berkeley-humanoid-lite.png"
       alt="Berkeley Humanoid Lite V1 humanoid robot"
       height="300">
</p>
<h3 align="center">
<strong>05. Berkeley Humanoid Lite V1</strong>
</h3>
<table width="100%">
<tbody>
<tr>
<td>
<strong>Summary</strong>
</td>
<td>
An open-source humanoid robotics platform providing mechanical designs,
actuator designs, low-level control, and reinforcement learning tools
for studying humanoid system integration.
</td>
</tr>
<tr>
<td>
<strong>Features</strong>
</td>
<td>
Supports reinforcement-learning-based locomotion and teleoperated
grasping. Resources include CAD, low-level control, robot models, Isaac
Lab training, and real-robot deployment.
</td>
</tr>
<tr>
<td>
<strong>Hardware</strong>
</td>
<td>
Brushless motors, modular 3D-printed cycloidal reducers, joint motor
controllers, CAN bus, IMU, and onboard computing. Check the BOM for the
exact V1 actuator and controller configuration.
</td>
</tr>
<tr>
<td>
<strong>GitHub</strong>
</td>
<td>
<a href="https://github.com/HybridRobotics/Berkeley-Humanoid-Lite">Berkeley
Humanoid Lite</a>
</td>
</tr>
</tbody>
</table>


<a id="existing-projects"></a> <a id="open-source-projects"></a>

## 🤖 More Robot Projects

<a id="hardware"></a> <a id="humanoid"></a>
<a id="hardware-humanoid"></a>

### 🦾 1. Robot Systems & Open-Source Hardware

Covers humanoid, quadruped, robotic arm, and mobile robot projects,
along with related hardware resources.

#### Humanoid Robots

- **[AgiBot X1](https://github.com/AgibotTech/agibot_x1_infer)** —
  [Inference](https://github.com/AgibotTech/agibot_x1_infer) ·
  [Training](https://github.com/AgibotTech/agibot_x1_train) ·
  [Hardware](https://github.com/AgibotTech/agibot_x1_hardware)  
  📄 An open-source humanoid robot project featuring inference modules,
  reinforcement learning training code, and comprehensive hardware
  design resources.

- **[OpenLoong Qinglong](https://github.com/loongOpen)**  
  📄 A full-stack open-source humanoid robot project covering dynamics
  control (MPC + WBC), hardware design, training platforms, and skill
  scheduling frameworks.

- **[Fourier N1](https://github.com/FFTAI)**  
  📄 A humanoid robot project by Fourier Intelligence, providing
  hardware designs, BOM, assembly guides, and the Fourier-GRX SDK.

- **[EngineAI
  Humanoid](https://github.com/engineai-robotics/engineai_humanoid)**  
  📄 Open-source locomotion control algorithms for EngineAI’s SA01/PM01
  bipedal robots, using end-to-end neural networks to achieve human-like
  walking.

- **[Unitree Qmini](https://github.com/unitreerobotics/Qmini)**  
  📄 An open-source bipedal robot platform from Unitree Robotics, with
  BOM, assembly guides, the RoboTamer4Qmini control framework, and URDF
  models.

- **[K-Bot](https://github.com/kscalelabs/kbot)**  
  📄 A full-stack open-source humanoid robot platform for developers and
  researchers.

<a id="hardware-quadruped"></a>

#### Quadruped Robots

- **[OpenCat](https://github.com/PetoiCamp/OpenCat)** ⭐ 15k  
  📄 An open-source quadruped robot platform.

- **[Xiaomi
  CyberDog](https://github.com/MiRoboticsLab/cyberdog_ros2)**  
  📄 Open-source software and hardware resources for Xiaomi’s CyberDog
  quadruped robot.

- **[Unitree Quadruped
  ROS](https://github.com/unitreerobotics/unitree_ros)**  
  📄 ROS driver packages for Unitree Go1/Go2 quadruped robots.

<a id="hardware-arms"></a>

#### Robotic Arms & Desktop Robots

- **[vlm_arm](https://github.com/TommyZihao/vlm_arm)**  
  📄 An open-source project combining robotic arms, large language
  models, and multimodal technologies.

- **[Dummy-Robot](https://github.com/peng-zhihui/Dummy-Robot)**  
  📄 A DIY mini robotic arm project by Zhihui Jun.

- **[ElectronBot](https://github.com/peng-zhihui/ElectronBot)**  
  📄 A compact desktop robot project by Zhihui Jun.

- **[Rubik’s Cube Solving
  Robot](http://www.diy-robots.com/?page_id=46)**  
  📄 A LEGO-based Rubik’s Cube solving robot project.

<a id="hardware-mobile"></a>

#### Mobile Robots

- **[MiniRover](https://github.com/peng-zhihui/MiniRover-Hardware)**  
  📄 Open-source resources for a DIY Mars rover by Zhihui Jun.

- **[ONE-Robot](https://github.com/peng-zhihui/ONE-Robot)**  
  📄 A self-balancing unicycle robot based on an IMU and STM32.

------------------------------------------------------------------------

<a id="perception"></a> <a id="slam"></a>

### 👁️ 2. Perception & Manipulation Algorithms

Covers SLAM, sensor fusion, visual perception, grasping algorithms, and
related sensor resources.

<a id="algo-slam"></a>

#### SLAM & Perception

- **[Visual SLAM: A 14-Lecture
  Course](https://github.com/gaoxiang12/slambook2)** ⭐ 12k  
  📄 A classic Chinese-language SLAM tutorial with accompanying code by
  Gao Xiang.

- **[VINS-Mono](https://github.com/HKUST-Aerial-Robotics/VINS-Mono)** ⭐
  5k  
  📄 A robust monocular visual-inertial state estimator developed at the
  Hong Kong University of Science and Technology.

- **[VINS-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion)**  
  📄 An optimization-based multi-sensor state estimator supporting
  monocular and stereo cameras with IMU fusion.

- **[LIO-SAM](https://github.com/TixiaoShan/LIO-SAM)** ⭐ 3.5k  
  📄 A tightly coupled LiDAR-inertial odometry and mapping system.

- **[FAST_LIO](https://github.com/hku-mars/FAST_LIO)** ⭐ 2.5k  
  📄 An efficient and robust LiDAR-inertial odometry framework from the
  HKU MARS Lab.

- **[FAST-LIVO2](https://github.com/hku-mars/FAST-LIVO2)**  
  📄 A tightly coupled LiDAR-inertial-visual odometry system.

- **[R3LIVE](https://github.com/hku-mars/r3live)** ⭐ 2.0k  
  📄 A real-time RGB-colored LiDAR-inertial-visual localization and
  mapping system.

- **[Unitree 4D LiDAR
  SLAM](https://github.com/unitreerobotics/point_lio_unilidar)**  
  📄 A Point-LIO-based SLAM solution adapted for Unitree’s L1 4D LiDAR.

<a id="algo-grasping"></a>

#### Grasping & Manipulation

- **[AnyGrasp](https://github.com/graspnet/anygrasp_sdk)**  
  📄 A general-purpose 6-DoF grasp pose estimation algorithm for robotic
  grasp detection.

- **[MYNT-EYE Stereo Camera
  SDK](https://github.com/slightech/MYNT-EYE-S-SDK)**  
  📄 SDK resources for MYNT-EYE stereo cameras, supporting vision and
  SLAM development.

------------------------------------------------------------------------

<a id="models"></a>

### 🧠 3. Embodied Models & Platform Toolchains

Covers VLA manipulation models, conversational agents, embodied AI
platforms, and no-code robot development tools.

<a id="model-vla"></a>

#### Embodied Models

- **[GR-1 (ByteDance Model)](https://github.com/bytedance/GR-1)**  
  📄 A GPT-style vision-based robot manipulation model from ByteDance
  for language-conditioned, multi-task manipulation learning and action
  prediction. Do not confuse it with AgiBot’s GR-1 humanoid robot.

<a id="model-platform"></a>

#### Platforms & Toolchains

- **[X-Humanoid: Husi Kaiwu](https://open.x-humanoid-cloud.com/)**  
  📄 An embodied AI toolchain platform covering skill invocation, agent
  configuration, and scenario deployment.

- **[Agibot LinkCraft](https://www.agibot.com.cn/filepage/295.html)**  
  📄 A no-code robot content creation platform supporting motion
  imitation, voice-driven interaction, and task script generation.

- **[Tencent Tairos](https://tairos.tencent.com/)**  
  📄 An embodied AI platform providing models, development tools, and
  data services for robotics applications.

- **[Viam](https://www.viam.com/)**  
  📄 A software platform for building, deploying, and managing robots,
  with unified APIs, module registration, remote operations, and fleet
  management.

- **[JD JoyInside](https://joyinside.com/)**  
  📄 A conversational AI agent platform for robots and AI-enabled smart
  devices.

- **[NetEase Lingdong ·
  Lingjue](https://lingdong.fuxi.163.com/productSummary/wj)**  
  📄 An embodied AI model and training framework for excavator loading
  operations in mining scenarios.

------------------------------------------------------------------------

<a id="data"></a>

### 🛠️ 4. Data, Training & Teleoperation

Covers reinforcement learning, imitation learning, data collection,
teleoperation systems, and robotics tutorials.

<a id="data-rl"></a>

#### Learning & Training Frameworks

- **[Booster Gym](https://github.com/BoosterRobotics)**  
  📄 An end-to-end reinforcement learning locomotion framework for
  Booster T1/K1 humanoid robots, including a RoboCup autonomous soccer
  demo.

- **[Humanoid-Gym](https://github.com/roboterax/humanoid-gym)**  
  📄 An Isaac Gym-based reinforcement learning framework for humanoid
  robots, supporting zero-shot transfer to real robots.

- **[OpenR1-Multimodal](https://github.com/EvolvingLMMs-Lab/open-r1-multimodal)**
  ⭐ 1.5k  
  📄 Explores applying the R1 reasoning paradigm to multimodal models
  and provides multimodal reinforcement learning training samples.

- **[unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym)**  
  📄 Unitree’s reinforcement learning framework for quadruped and
  humanoid robots, based on Isaac Gym.

- **[unitree_rl_lab](https://github.com/unitreerobotics/unitree_rl_lab)**
  · [MuJoCo
  Version](https://github.com/unitreerobotics/unitree_rl_mjlab)  
  📄 Unitree robot reinforcement learning implementations based on Isaac
  Lab and MuJoCo.

- **[unitree_IL_lerobot](https://github.com/unitreerobotics/unitree_IL_lerobot)**  
  📄 An imitation learning tool based on LeRobot for training and
  testing Unitree G1 dual-arm and dexterous-hand tasks.

<a id="data-teleop"></a>

#### Data Collection & Teleoperation

- **[ALOHA 2](https://aloha-2.github.io/)**  
  📄 A low-cost open-source hardware platform for bimanual teleoperation
  and embodied data collection, with tutorials and MuJoCo simulation
  models.

- **[DexCap](https://dex-cap.github.io/)**  
  📄 A Stanford-developed dexterous manipulation data collection system
  using hand motion capture and depth cameras to collect human
  manipulation data.

- **[Dobb-E](https://dobb-e.com/)**  
  📄 An NYU-developed home robotics data collection and imitation
  learning solution, including low-cost handheld collection hardware,
  datasets, and a learning framework.

- **[Unitree XR
  Teleoperation](https://github.com/unitreerobotics/xr_teleoperate)**  
  📄 An XR-based teleoperation system for Unitree H1/G1 humanoid robots,
  supporting devices such as Apple Vision Pro and Meta Quest.

<a id="data-tutorial"></a>

#### Tutorials & Knowledge Bases

- **[RoboWiki](https://github.com/yfrobotics/robowiki)**  
  📄 A robotics knowledge base maintained by Yunfei Robotics Lab.

- **[Unitree Robotics Control
  Tutorial](https://github.com/unitreerobotics/unitree_guide)**  
  📄 An open-source tutorial for Unitree quadruped robot control,
  suitable for beginners and reference.

[↑ Back to Contents](#toc)

<!-- Retained for compatibility with existing links. -->

<a id="reasoning-rl"></a>
