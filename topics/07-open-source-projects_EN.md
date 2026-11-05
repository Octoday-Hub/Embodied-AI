# Robot Systems & Open-Source Hardware

A curated collection of open-source robotics and hardware projects. Each
entry highlights the robot’s capabilities, hardware requirements,
official code, and reproduction resources to help developers find
projects suited to their needs.

<a id="toc"></a>

## Contents

<a id="new-projects"></a>

**🆕 New This Round (jump straight to the project)**

  - 🦾 [Xiaochujun Dexterous Hand](#project-xiaochujun-dexterous-hand) — servo-and-tendon drive that mimics muscle, a gripping hand you can 3D print
  - 🦾 [RIG-Arm](#project-rig-arm) — open-source arm with teach mode; guide it once by hand and it replays the motion
  - 🦾 [Dummy-Robot](#project-dummy-robot) — Peng Zhihui's build: an industrial arm topology shrunk to desktop scale with direct-drive brushless motors
  - 🦾 [RIG-Hover](#project-rig-hover) — two-wheel self-balancing plus an arm, a desktop demo of balance control
  - 🐕 [XGO-Duck](#project-xgoduck) — a bipedal robot duck on Arduino UNO Q, a new form beyond quadrupeds
  - 🐕 [RIG-Puppy](#project-rig-puppy) — a desk-sized robot dog that runs on just five servos
  - 🐕 [Open Duck Mini v2](#project-open-duck-mini) — a fully reproduced open-source bipedal duck with RL gaits
  - 🐕 [OpenCat / Bittle X](#project-opencat) — the robot dog framework with 30k+ units shipped, used in teaching and research alike
  - 🧍 [PhoneBot](#project-phonebot) — UCLA turns a phone into a humanoid torso, offloading compute and perception to it
  - 🧍 [ToddlerBot 2.0](#project-toddlerbot) — Stanford's low-cost humanoid, fully 3D-printable
  - 🧍 [Berkeley Humanoid Lite V1](#project-berkeley-humanoid-lite) — Berkeley's open humanoid with actuator designs fully published
  - 📚 [Learn Arduino](#project-learn-arduino) — 3D circuit simulation in the browser, learn Arduino without buying a board


**🤖 Robot Projects (sorted alphabetically)**
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


<a id="existing-projects"></a> <a id="open-source-projects"></a>

## 🤖 Robot Projects

<a id="hardware"></a> <a id="humanoid"></a>
<a id="hardware-humanoid"></a>

### 🦾 1. Robot Systems & Open-Source Hardware

Covers humanoid, quadruped, robotic arm, and mobile robot projects,
along with related hardware resources.

#### Humanoid Robots


<a id="project-agibot-x1"></a>

<p align="center">
  <img src="datasets-img/agibot-x1.jpg"
       alt="AgiBot X1"
       height="300">
</p>

<h3 align="center"><strong>01. AgiBot X1</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>智元机器人开源的模块化高自由度人形机器人，以自研 AimRT 中间件为骨架，用强化学习做运动控制，配套提供模型推理、平台驱动、软件仿真三类模块的完整代码。</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>工程化程度较高，推理、驱动、仿真三块拆成独立模块，可以只取其中一块接入自己的系统；中间件用自研 AimRT，支持多语言与多种通信后端，适合作为大型机器人软件架构的学习样本；强化学习控制流程有完整示例，能跑通从仿真训练到实机部署的链路；官方提供开发指南与模块注释，对二次开发比较友好；硬件设计单独放在 agibot_x1_hardware 仓库，软件硬件可以分开跟进。</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>模块化人形本体，具体关节数量与尺寸以官方硬件仓库 agibot_x1_hardware 为准；软件侧依赖自研 AimRT 中间件，支持 x86 与 ARM 平台。</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/AgibotTech/agibot_x1_infer">推理</a> · <a href="https://github.com/AgibotTech/agibot_x1_train">训练</a> · <a href="https://github.com/AgibotTech/agibot_x1_hardware">硬件</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://aimrt.org/">AimRT 官方文档</a>

<a id="project-berkeley-humanoid-lite"></a>

<p align="center">
<img src="datasets-img/berkeley-humanoid-lite.png"
       alt="Berkeley Humanoid Lite V1 humanoid robot"
       height="300">
</p>
<h3 align="center"><strong>02. Berkeley Humanoid Lite V1</strong>
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

<a id="project-engineai-humanoid"></a>

<p align="center">
  <img src="datasets-img/engineai-humanoid.jpg"
       alt="EngineAI Humanoid"
       height="300">
</p>

<h3 align="center"><strong>03. EngineAI Humanoid</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Open-source bipedal locomotion control algorithms from EngineAI (Shenzhen), built on MIT's Cheetah Software leg-control framework, with end-to-end neural-network human-like gaits for the SA01 and PM01 robots.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Grounded in MIT's Cheetah Software, an academically validated leg-control stack, so the learning curve is far gentler than starting from scratch. Code is split into common, config, robot and scripts modules, with robot modelling and closed-chain mapping as standalone directories that are easy to swap or reuse. Uses LCM for logging and debugging, compatible with the MIT toolchain. Mostly C++, making it a solid entry point for biped control. Validated on the SA01 and PM01 robots.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Targets EngineAI SA01 / PM01 bipedal robots. The control stack runs on the robot's onboard compute and relies on LCM as the communication middleware.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/engineai-robotics/engineai_humanoid">engineai_humanoid</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://github.com/mit-biomimetics/Cheetah-Software">MIT Cheetah Software</a>

<a id="project-fourier-n1"></a>

<h3 align="center"><strong>04. Fourier N1</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Fourier Intelligence's open-source humanoid N1 project, publishing hardware design, BOM, assembly guides and the Fourier-GRX SDK — one of the few humanoids opened all the way down to the part level.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Structural design, bill of materials and assembly procedures are all public, so the whole robot can be rebuilt from the documentation. The Fourier-GRX SDK wraps the low-level motion interface, with a separately maintained documentation site covering installation, run modes, APIs and task examples. Hardware and software resources are organised independently: hardware for structural reference, software for control-algorithm validation. Fourier has years of product experience in rehabilitation robots and exoskeletons, so mechanical reliability is well founded.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Fourier N1 humanoid body. Software is accessed through the Fourier-GRX SDK, whose documentation site is built with Jekyll.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/FFTAI/fourier-grx-N1">fourier-grx-N1 文档</a> · <a href="https://github.com/FFTAI/Wiki-GRx-Pipeline">GRx 开发管线</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://fftai.github.io/fourier-grx-N1/">Grex 文档站</a>

<a id="project-k-bot"></a>

<p align="center">
  <img src="datasets-img/k-bot.jpg"
       alt="K-Bot"
       height="300">
</p>

<h3 align="center"><strong>05. K-Bot</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>K-Scale Labs' full-stack open-source humanoid platform, built around the goal of a future where everyone owns a robot — mechanical structure through control software, all open.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Aimed squarely at consumer-level pricing, with the whole machine designed around affordability. The code is organised as submodules and one command updates them all to the latest master. The project is in public alpha and the team explicitly warns of breaking changes — interesting for tracking an early-stage design, not yet for production. Community channels include Discord, a docs site and a bounty programme, and dev kits can be returned for a full refund if unsatisfying, which suggests real confidence in usability.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>K-Scale Labs' in-house humanoid body, sold as a developer kit; control software runs on the onboard compute unit.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/kscalelabs/kbot">K-Bot</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://url.kscale.dev/docs">官方文档</a> · <a href="https://url.kscale.dev/discord">Discord</a>

<a id="project-openloong"></a>

<p align="center">
  <img src="datasets-img/openloong.jpg"
       alt="OpenLoong 青龙"
       height="300">
</p>

<h3 align="center"><strong>06. OpenLoong 青龙</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A full-stack open-source humanoid project incubated by Humanoid Robot (Shanghai) Co., organised in four layers — cloud brain, embodied cerebellum, embodied body and embodied data — spanning OS to hardware.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>One of the few full-stack projects led by a national-team-backed company, with clear layer boundaries so each can be adopted on its own. The cloud-brain layer uses a multi-kernel design, choosing between Linux and LiteOS depending on device resources. The cerebellum layer focuses on dynamics control with mature MPC and WBC stacks. Hardware design, training platform and skill-scheduling framework each live in separate repositories for incremental adoption. A good way to understand the Chinese humanoid technology stack as a whole.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Qinglong humanoid body with hardware opened separately; MPC + WBC dynamics control, plus the OpenLoong-Gymloong training platform.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/loongOpen/OpenLoong">OpenLoong</a> · <a href="https://github.com/loongOpen/OpenLoong-Dyn-Control">动力学控制</a> · <a href="https://github.com/loongOpen/OpenLoong-Hardware">硬件系统</a> · <a href="https://github.com/loongOpen/OpenLoong-Gymloong">训练平台</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://github.com/loongOpen/OpenLoong-Framework">项目框架</a>

<a id="project-phonebot"></a>

<p align="center">
  <img src="datasets-img/phonebot.jpg"
       alt="PhoneBot"
       height="300">
</p>

<h3 align="center"><strong>07. PhoneBot</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A low-cost open humanoid platform from the RoMeLa lab at UCLA that treats an ordinary Android smartphone as the torso-mounted hub for perception, computation and interaction, with a 13-servo lower body for walking and visual following.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Paper-reported: 48.3 cm tall, about 1.8 kg including the phone, 13 actuated joints, roughly 400 USD in hardware cost excluding the phone. The phone supplies the camera, IMU, wireless connectivity and on-board processing, so no separate sensors or computer are needed. Commands travel over Wi-Fi to a small on-board single-board computer that drives the servos. Locomotion policies are trained with reinforcement learning with explicit handling of the servo torque limit.</td>
    </tr>
    <tr>
      <td><strong>Hardware <br> plan</strong></td>
      <td>13 × DYNAMIXEL XL430-W250-T servos, one commodity Android smartphone, a small on-board single-board computer, a USB-to-TTL U2D2 interface, a 3S battery with a DC converter, modular linkage and torso structure. The current version has no arms.</td>
    </tr>
    <tr>
      <td><strong>GitHub <br> link</strong></td>
      <td>No publicly accessible official GitHub repository could be verified. Official project page: <a href="https://phonebot.dev/">phonebot.dev</a></td>
    </tr>
  </tbody>
</table>

Related resources: [Paper arXiv:2610.08737](https://arxiv.org/abs/2610.08737)

<a id="project-toddlerbot"></a>

<p align="center">
<img src="datasets-img/toddlerbot.png"
       alt="ToddlerBot 2.0 humanoid robot"
       height="300">
</p>
<h3 align="center"><strong>08. ToddlerBot 2.0</strong>
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

<a id="project-unitree-qmini"></a>

<p align="center">
  <img src="datasets-img/unitree-qmini.jpg"
       alt="Unitree Qmini"
       height="300">
</p>

<h3 align="center"><strong>09. Unitree Qmini</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Unitree's low-cost open-source bipedal robot, with every structural part 3D-printable and modular assembly that goes together like Lego, aimed at hobbyists, educators and researchers.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Fully open from bill of materials and electrical block diagram to STEP files and assembly SOP — you can start straight from the documentation. Positioned for the lowest possible barrier to entry as an affordable humanoid platform. All structural parts are 3D-printed, so design changes only require model edits and iteration is cheap. Ships with URDF models and the RoboTamer4Qmini control framework so it runs once assembled. A good vehicle for university coursework or robotics competitions.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Fully 3D-printed structure with a low-cost servo setup; complete BOM, electrical diagram and STEP models provided; core software stack is RoboTamer4Qmini.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/unitreerobotics/Qmini">Qmini</a> · <a href="https://github.com/vsislab/RoboTamer4Qmini">控制框架 RoboTamer4Qmini</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://github.com/unitreerobotics/Qmini/blob/main/Qmini_DIY.pdf">DIY 说明 PDF</a>


<a id="hardware-quadruped"></a>

#### Quadruped Robots


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
<h3 align="center"><strong>01. Open Duck Mini v2</strong>
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

<a id="project-opencat"></a>

<p align="center">
  <img src="datasets-img/opencat.jpg"
       alt="OpenCat"
       height="300">
</p>

<h3 align="center"><strong>02. OpenCat</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Petoi 开源的四足机器人框架，最初为 Bittle 机器狗与 Nybble 机器猫设计，把步态协调、舵机控制、IMU 融合这些底层难点封装好，让开发者专注在上层应用。</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>老牌项目，累计出货 3 万多台，覆盖 60 多个国家，有 20 多篇学术论文引用，社区与教学资源都很成熟；本仓库对应 NyBoard 平台（ATmega328P），最多可协调 12 个舵机，支持行走、奔跑、跳跃甚至后空翻；当前世代硬件为 Bittle X 与 Nybble Q，代码在 OpenCatESP32 仓库；配套仿真器可以在网页里先试再买；支持传感器扩展包，适合 K12、高校实验室与创客空间做教学。</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>NyBoard 主控（ATmega328P 定制 Arduino 板），可驱动最多 12 个高性能舵机；当前世代改用 ESP32 / BiBoard；结构件外壳与支架可 3D 打印。</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/PetoiCamp/OpenCat">OpenCat</a> · <a href="https://github.com/PetoiCamp/OpenCatEsp32-Quadruped-Robot">OpenCatESP32</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://www.petoi.com/pages/bittle-x-robot-dog-simulator">Bittle X 仿真器</a>

<a id="project-rig-puppy"></a>

<p align="center">
  <img src="datasets-img/luwudynamics-rig-puppy.jpg"
       alt="RIG-Puppy"
       height="300">
</p>

<h3 align="center"><strong>03. RIG-Puppy</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A puppy-shaped desktop robot from Luwu Dynamics driven by five bus servos, an ESP32-S3 and a round LCD, with voice dialogue backed by cloud LLM agents.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Five-servo robot-dog form with preset sit, stand-up and tail-wag actions, plus head motion that follows device tilt via the IMU. The round LCD plays 20+ expression animations. Voice uses offline wake words with cloud ASR/TTS, wired into the Xiaozhi AI ecosystem with agent personality configuration. BluFi provisioning, OTA updates and MCP tools are supported, with an optional camera.</td>
    </tr>
    <tr>
      <td><strong>Hardware <br> plan</strong></td>
      <td>ESP32-S3 (N16R8), GC9A01 240×240 round LCD, five serial bus servos, QMI8658C six-axis IMU, I2S microphone plus amplifier and speaker, touch module, optional OV2640 camera, Li-ion battery and power management, 3D-printed shell and legs.</td>
    </tr>
    <tr>
      <td><strong>GitHub <br> link</strong></td>
      <td><a href="https://github.com/LuwuDynamics/rig_omni">LuwuDynamics/rig_omni</a></td>
    </tr>
  </tbody>
</table>

Related resources: [Official wiki](https://wiki.xgorobot.com/kb/pet-puppy)

<a id="project-xgoduck"></a>

<p align="center">
  <img src="datasets-img/luwudynamics-xgoduck_hardware.jpg"
       alt="XGO-Duck"
       height="300">
</p>

<h3 align="center"><strong>04. XGO-Duck</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A 3D-printable biped robot duck from Luwu Dynamics, adapted from Pollen Robotics' Microduck, built on an Arduino UNO Q and 15 serial servos with full structure files, expansion board, assembly guide and an RL training pipeline.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Fifteen Feetech 1910 serial servos drive 10 leg joints, 4 neck/head joints and 1 mouth joint. The Arduino UNO Q splits the load: the Linux side runs ONNX policy inference and the web UI while the STM32 side handles 100 Hz servo and IMU loops. A custom expansion board integrates the IMU and servo bus, with PCBA, Gerber and BOM released. Policies are trained with reinforcement learning in simulation and deployed to the real robot.</td>
    </tr>
    <tr>
      <td><strong>Hardware <br> plan</strong></td>
      <td>Arduino UNO Q (2 GB or 4 GB), Luwu UNO Q expansion board (power distribution, servo interfaces, IMU), 15 × Feetech 1910 servos with AMP 3-pin cables, 8.4 V (2S 18650) battery pack with charger, bearings and fasteners, 3D-printed structure. Full BOM per the official repository.</td>
    </tr>
    <tr>
      <td><strong>GitHub <br> link</strong></td>
      <td><a href="https://github.com/LuwuDynamics/xgoduck_hardware">LuwuDynamics/xgoduck_hardware</a> · <a href="https://github.com/LuwuDynamics/xgoduck_runtime_arduino">runtime</a> · <a href="https://github.com/LuwuDynamics/xgoduck_rl">training</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://www.arduino.cc/en/software/">Arduino IDE</a>

<a id="project-unitree-quadruped-ros"></a>

<p align="center">
  <img src="datasets-img/unitree-quadruped-ros.jpg"
       alt="宇树科技四足机器人 ROS"
       height="300">
</p>

<h3 align="center"><strong>05. 宇树科技四足机器人 ROS</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Unitree's official ROS simulation and control packages, providing Gazebo models, joint controllers and real-robot interfaces for the A1, Go1, Go2, B1, B2 and other mainline quadrupeds.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Unusually broad model coverage — A1, A2, AlienGo, B1, B2, Go1, Go2 and newer quadrupeds each have a description package, so one repository serves many robots. Every model is an independent ROS package with its own model files, variant configs and launch files. The Gazebo side supports torque, position and angular-velocity joint control, suitable for validating control algorithms. High-level gait control pairs with unitree_ros_to_real. Actively maintained and kept in sync with the official robot SDK.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Supports Unitree A1 / A2 / AlienGo / B1 / B2 / Go1 / Go2 quadrupeds, mostly 12-DOF configurations; Gazebo for simulation, official Unitree SDK for real robots.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/unitreerobotics/unitree_ros">unitree_ros</a> · <a href="https://github.com/unitreerobotics/unitree_ros_to_real">实机控制包</a></td>
    </tr>
  </tbody>
</table>

<a id="project-cyberdog-ros2"></a>

<p align="center">
  <img src="datasets-img/cyberdog-ros2.jpg"
       alt="小米 CyberDog"
       height="300">
</p>

<h3 align="center"><strong>06. 小米 CyberDog</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>The ROS 2 function-package collection for Xiaomi's CyberDog quadruped, implementing multimodal perception, autonomous decision-making, localisation, navigation and target tracking on ROS 2.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>A big-company open-source quadruped with unusually complete scope — not a single algorithm but a whole robot application stack. Built on ROS 2 Galactic with Cyclone DDS, including a Ubuntu 18.04 adaptation for Jetson platforms managed through mini.repos, which is itself a useful reference for trimming a distro for embedded targets. Features cover multi-device linking, multimodal perception and interaction, autonomous decisions, SLAM navigation and target tracking. Docs sit in each submodule with a wiki as an index. Default user is mi with password 123; connect via the USB Download port and ssh in.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Xiaomi CyberDog body with onboard NVIDIA Jetson compute; Cyclone DDS middleware and ROS 2 Galactic.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/MiRoboticsLab/cyberdog_ros2">cyberdog_ros2</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://github.com/MiRoboticsLab/cyberdog_ros2/wiki">项目 Wiki</a>


<a id="hardware-arms"></a>

#### Robotic Arms & Desktop Robots


<a id="project-dummy-robot"></a>

<p align="center">
  <img src="datasets-img/dummy-robot.jpg"
       alt="Dummy-Robot mini robotic arm"
       height="300">
</p>

<h3 align="center"><strong>01. Dummy-Robot</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A super-compact desktop robotic arm open-sourced by Zhihui Jun (peng-zhihui), driven by stepper motors and reducers, with forward and inverse kinematics, CAN bus control and a wireless teach pendant — industrial-grade arm kinematics squeezed into desktop size.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Computes forward kinematics from joint angles to end-effector pose and inverse kinematics, picking the solution with the smallest joint change from the previous pose out of up to 8 candidates. Trapezoidal acceleration with CAN broadcast sync starts and stops all six joints together. Three command modes: SEQ for low-frequency sequential moves, INT for interruptible real-time control, and TRJ for fixed-period trajectory interpolation. The core firmware moved from LiteOS to FreeRTOS and the kinematics are open source, so swapping DH parameters ports it to a custom arm. Ships with the Peak wireless teach pendant and the DummyStudio host app.</td>
    </tr>
    <tr>
      <td><strong>Hardware <br> plan</strong></td>
      <td>The original uses aluminium CNC structure with 20/42 stepper motors and harmonic reducer modules, built from four core boards: REF core board, REF base board, stepper driver board and the Peak teach pendant. Drivers use integrated closed-loop control over CAN, so each axis needs only two power wires and two CAN wires. The author recommends the upcoming budget version for cost-sensitive builders: 3D-printed structure with self-made cycloidal reducers replacing the harmonic ones, targeting under 2000 CNY for the whole unit.</td>
    </tr>
    <tr>
      <td><strong>GitHub <br> link</strong></td>
      <td><a href="https://github.com/peng-zhihui/Dummy-Robot">peng-zhihui/Dummy-Robot</a></td>
    </tr>
  </tbody>
</table>

Related resources: introduction videos on Bilibili and YouTube (search "稚晖君 robotic arm")

<a id="project-electronbot"></a>

<p align="center">
  <img src="datasets-img/electronbot.jpg"
       alt="ElectronBot 迷你桌面机器人"
       height="300">
</p>

<h3 align="center"><strong>02. ElectronBot 迷你桌面机器人</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Peng Zhihui's open-source mini desktop robot: a two-DOF arm plus a round LCD that together produce expressive faces and motions — a landmark of desktop-scale open hardware.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Small in size but unusually complete, with mechanical structure, circuits, firmware and host software all open. Servo-driven, paired with a circular LCD so motion and expression work together, giving it the feel of a small robot pet. The author is a well-known hardware creator on Bilibili, with thorough companion videos and many community reproductions. Structural parts are 3D-printable and the PCB files can go straight to a fab. A good integrated project for learning mechanical design alongside embedded development.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Two-DOF servo-driven structure with a round LCD display; main control and driver board are integrated with open PCB files; 3D-printed structure.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/peng-zhihui/ElectronBot">ElectronBot</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://www.bilibili.com/video/BV1eR4y1w7uj">Bilibili demo video</a>

<a id="project-rig-arm"></a>

<p align="center">
  <img src="datasets-img/luwudynamics-rig_omni.jpg"
       alt="RIG-Arm"
       height="300">
</p>

<h3 align="center"><strong>03. RIG-Arm</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>The ARM board type of the open-source RIG-Omni ESP32-S3 firmware: a robotic-arm desktop robot combining arm motion, round-screen expressions, voice dialogue and gesture interaction in one body.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>One codebase covers the Puppy, Hover, ARM and TARS forms; boards share voice, networking and sensor drivers while implementing their own motion control. The ARM board provides arm calibration and a teach mode, callable by voice or remote. A round display plays expression animations and wake-word detection runs locally. BluFi provisioning, OTA updates and MCP tools are supported.</td>
    </tr>
    <tr>
      <td><strong>Hardware <br> plan</strong></td>
      <td>ESP32-S3, SCS009 serial bus servos, QMI8658C six-axis IMU, GC9A01 240×240 round LCD, I2S microphone plus amplifier and speaker, touch module and buttons, Li-ion battery and power management, 3D-printed structure. Exact configuration per the official BOM.</td>
    </tr>
    <tr>
      <td><strong>GitHub <br> link</strong></td>
      <td><a href="https://github.com/LuwuDynamics/rig_omni">LuwuDynamics/rig_omni</a></td>
    </tr>
  </tbody>
</table>

Related resources: [Official wiki](https://wiki.xgorobot.com/kb/pet-arm) · [MakerWorld models](https://makerworld.com.cn/zh/@LuwuDynamics)

<a id="project-rig-hover"></a>

<p align="center">
  <img src="datasets-img/rig-hover-01.gif"
       alt="RIG-Hover self-balancing robot demo"
       height="300">
</p>

<h3 align="center"><strong>04. RIG-Hover</strong></h3>
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

<a id="project-vlm-arm"></a>

<p align="center">
  <img src="datasets-img/vlm-arm.jpg"
       alt="vlm_arm"
       height="300">
</p>

<h3 align="center"><strong>05. vlm_arm</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>同济子豪兄开源的多模态机械臂智能体项目，把大语言模型与视觉理解模型接到六轴机械臂上，实现「听得懂人话、看得懂图像、指哪打哪」的人机协作。</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>走的是「大模型当大脑、机械臂当手」的轻量路线，不需要自己训练模型，换 API Key 就能切换不同厂商的大模型；支持 Yi-Large、Claude 3 Opus、文心 4.0 Turbo 等多个 Agent 模型，视觉侧支持 GPT-4v/4o、Yi-Vision、CogVLM2-Grounding、Qwen-VL-Max，方便横向对比各家能力；配套 B 站视频教程与飞书文档，从原理到复现都有讲解；适合作为具身智能入门项目，理解「语言→坐标→动作」这条链路是怎么打通的。</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>大象机器人 MyCobot 280 Pi 六轴机械臂 + 树莓派 4B（Ubuntu 20.04）；配件包括摄像头法兰与吸泵；需要 Python 3.12 环境。</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/TommyZihao/vlm_arm">vlm_arm</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://www.bilibili.com/video/BV1Cn4y1R7V2">Concept walkthrough video</a> · <a href="https://njapov1vnz.feishu.cn/docx/Qosedmc5NoYK7IxVoMBcD47jn9b">Reproduction guide (Feishu)</a>

<a id="project-xiaochujun-dexterous-hand"></a>

<p align="center">
  <img src="datasets-img/xiaochujun-dexterous-hand.jpg"
       alt="Xiaochujun Dexterous Hand"
       height="300">
</p>

<h3 align="center"><strong>06. Xiaochujun Dexterous Hand</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A 3D-printed hand driven by hobby servos and cable tendons that pull the fingers closed, performing open, fist and grasp motions, with a companion phone app.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Commodity servos supply the force while tensioned cables bend 3D-printed fingers, so not every joint needs its own motor. A hands-on example of underactuation in which one servo drives several joints through a tendon. The author publishes video tutorials as 「小楚君CC」 and distributes the files and app through cloud-drive links.</td>
    </tr>
    <tr>
      <td><strong>Hardware <br> plan</strong></td>
      <td>3D-printed palm and finger parts, drive servos, tendons with tubing, a controller board, battery and switch, fasteners and bearings. No complete bill of materials has been published; counts and models follow the author's materials.</td>
    </tr>
    <tr>
      <td><strong>GitHub <br> link</strong></td>
      <td>No official GitHub repository could be verified. Files are distributed by the author: <a href="https://pan.baidu.com/s/1QT5dh-R3a37De9sv_LerFw?pwd=xesd">Baidu Pan (xesd)</a> · <a href="https://pan.baidu.com/s/1nbod7cnuJ4-DOrkbAUGfgA?pwd=12as">App (12as)</a></td>
    </tr>
  </tbody>
</table>

Related resources: search 「小楚君CC」 on major video platforms

<a id="hardware-mobile"></a>
#### Mobile Robots


<a id="project-minirover"></a>

<p align="center">
  <img src="datasets-img/minirover.jpg"
       alt="MiniRover 火星车"
       height="300">
</p>

<h3 align="center"><strong>01. MiniRover 火星车</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Peng Zhihui's open-source mini Mars rover: an ESP32 controller with camera and ToF sensors, remote-controllable over WiFi video streaming and a phone app, with hardware and firmware fully open.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Hardware documentation is thorough: schematics and PCB in Altium Designer format, plus Gerber files in the release directory that can go straight to a fab. The ESP32 firmware includes camera drivers, a JPEG streaming web server, motor drivers and ToF ADC reads — a complete embedded case study. Android sample code demonstrates WiFi communication with the ESP32 and video display. The Docs folder carries datasheets for the relevant ICs. A great first vehicle for getting into mobile robotics.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>ESP32 controller integrating camera driver, JPEG streaming web server, motor driver and ToF ADC reads; open PCB files ready for fabrication.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/peng-zhihui/MiniRover-Hardware">MiniRover-Hardware</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://www.bilibili.com/video/BV1ZA411e7Ff">Bilibili demo video</a>

<a id="project-one-robot"></a>

<p align="center">
  <img src="datasets-img/one-robot.jpg"
       alt="ONE-Robot 独轮机器人"
       height="300">
</p>

<h3 align="center"><strong>02. ONE-Robot 独轮机器人</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A single-wheel self-balancing robot Peng Zhihui built in 2015 on IMU and STM32 — the simplest, most intuitive form for understanding balance control.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>With only one wheel, the balance problem is purer than on two-wheeled designs, making it an excellent vehicle for understanding inverted-pendulum and closed-loop attitude control. The repository includes STM32 firmware source and 3D mechanical models. The control board circuit is lost to time, but the author notes it was simple and can be reconstructed from the firmware pin definitions. An older project with a basic tech stack, well suited to learning self-balancing from first principles.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>STM32 controller with IMU attitude sensor and a single drive wheel; control board circuit unpublished (author notes the design is simple enough to rebuild), 3D models provided.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/peng-zhihui/ONE-Robot">ONE-Robot</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://www.bilibili.com/video/av89252261/">Bilibili demo video</a>


------------------------------------------------------------------------

<a id="perception"></a> <a id="slam"></a>

### 👁️ 2. Perception & Manipulation Algorithms

Covers SLAM, sensor fusion, visual perception, grasping algorithms, and
related sensor resources.

<a id="algo-slam"></a>

#### SLAM & Perception


<a id="project-fast-livo2"></a>

<p align="center">
  <img src="datasets-img/fast-livo2.jpg"
       alt="FAST-LIVO2"
       height="300">
</p>

<h3 align="center"><strong>01. FAST-LIVO2</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A fast direct LiDAR-inertial-visual odometry from HKU's MARS Lab, tightly coupling LiDAR, IMU and camera in a unified ESIKF framework to output high-precision poses and colourised point-cloud maps in real time.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Uses a direct method rather than a feature-based one, skipping feature extraction and matching so it holds up better in texture-poor or repetitive scenes. An error-state iterated Kalman filter handles all three sensor modalities together, coupling more tightly than loosely-coupled alternatives. Balances speed and accuracy, with the paper accepted to T-RO 2024. Official code and datasets are public, and the FAST-LIVO line has become a common baseline in subsequent work.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Requires a LiDAR + IMU + camera rig; ROS-based code depending on PCL, Eigen and Sophus.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/hku-mars/FAST-LIVO2">FAST-LIVO2</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://arxiv.org/abs/2408.14035">项目主页</a>

<a id="project-fast-lio"></a>

<p align="center">
  <img src="datasets-img/fast-lio.jpg"
       alt="FAST_LIO"
       height="300">
</p>

<h3 align="center"><strong>02. FAST_LIO</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>HKU MARS Lab's LiDAR-inertial odometry, using a tightly-coupled iterated Kalman filter on LiDAR and IMU data and its own ikd-Tree data structure to run in real time.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>The core is ikd-Tree, an incrementally-updatable dynamic KD-tree far more efficient than static trees under frequent point insertions and deletions — also released separately for reuse. The tightly-coupled ESIKF framework is stable under fast motion and sparse features. Compute cost is low enough for real-time operation on ordinary onboard hardware. The ecosystem is mature, spawning FAST-LIO-LOCALIZATION for relocalisation, the LI_Init extrinsic initialiser and the FAST-LIVO line.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Requires LiDAR + IMU; ROS-based code that runs in real time on low-power platforms.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/hku-mars/FAST_LIO">FAST_LIO</a> · <a href="https://github.com/hku-mars/ikd-Tree">ikd-Tree</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://github.com/hku-mars/LiDAR_IMU_Init">外参初始化 LI_Init</a>

<a id="project-lio-sam"></a>

<p align="center">
  <img src="datasets-img/lio-sam.jpg"
       alt="LIO-SAM"
       height="300">
</p>

<h3 align="center"><strong>03. LIO-SAM</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A factor-graph LiDAR-inertial odometry that adds LiDAR and IMU observations as factors to a graph optimisation, combining IMU preintegration with loop closure to output smooth trajectories and point-cloud maps.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Takes the optimisation route rather than filtering: the factor-graph framing lets loop closures, GPS factors and extrinsics all be added uniformly, which helps extensibility. IMU preintegration plus LiDAR odometry gives two-rate estimation, balancing real-time behaviour against accuracy. The community is active with many forks adapted to different LiDARs, so a configuration usually exists for common sensors. The authors recommend running the provided dataset before moving to a real robot, and the docs include debugging guidance. One of the most common comparison baselines in LiDAR SLAM.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Requires a 3D LiDAR + 9-axis IMU; ROS-based, with optional GPS for global constraints.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/TixiaoShan/LIO-SAM">LIO-SAM</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://github.com/TixiaoShan/LIO-SAM">作者说明文档</a>

<a id="project-r3live"></a>

<p align="center">
  <img src="datasets-img/r3live.jpg"
       alt="R3LIVE"
       height="300">
</p>

<h3 align="center"><strong>04. R3LIVE</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>HKU MARS Lab's tightly-coupled LiDAR-inertial-visual state estimation and mapping framework, maintaining geometric and textural maps simultaneously so the output point cloud carries RGB colour.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Builds two maps at once — geometry driven by LiDAR and colour driven by the camera — then fuses them into a colourised point cloud that is far more legible than purely geometric maps. The LIO and VIO subsystems are independent yet mutually constraining, improving robustness when one sensor briefly fails. The paper was accepted at ICRA 2022. GPLv2 licensed, free for personal and academic use. Well suited to reconstruction tasks needing coloured maps.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Requires LiDAR + IMU + camera; ROS-based code.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/hku-mars/r3live">R3LIVE</a></td>
    </tr>
  </tbody>
</table>

<a id="project-vins-fusion"></a>

<p align="center">
  <img src="datasets-img/vins-fusion.jpg"
       alt="VINS-Fusion"
       height="300">
</p>

<h3 align="center"><strong>05. VINS-Fusion</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>HKUST's optimisation-based multi-sensor state estimator, supporting monocular, stereo and stereo+IMU combinations to deliver accurate self-localisation for drones, cars and robots.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>An extension of VINS-Mono that widens sensor support from mono+IMU to stereo and stereo+IMU, and can fuse GPS for global consistency. The whole estimator is built on sliding-window optimisation, jointly minimising visual reprojection and IMU preintegration errors for first-tier accuracy and robustness. Published comparisons on KITTI and similar datasets are available. The clean code structure makes it a baseline for a great deal of visual-inertial work, with very high academic citation counts.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Supports monocular or stereo cameras with IMU, optionally plus GPS; ROS-based code.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/HKUST-Aerial-Robotics/VINS-Fusion">VINS-Fusion</a></td>
    </tr>
  </tbody>
</table>

<a id="project-vins-mono"></a>

<p align="center">
  <img src="datasets-img/vins-mono.jpg"
       alt="VINS-Mono"
       height="300">
</p>

<h3 align="center"><strong>06. VINS-Mono</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>HKUST's monocular visual-inertial state estimator, tightly coupling camera and IMU through sliding-window optimisation — one of the most highly cited open-source works in visual-inertial SLAM.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Later versions added map merging, pose-graph reuse, online temporal calibration and rolling-shutter camera support, making it unusually complete for its generation. The tightly-coupled optimisation architecture became the foundation for many subsequent VINS-family works. Full datasets and detailed documentation keep reproduction straightforward. Its extension VINS-Fusion supports more sensor combinations. Widely applied to drone and mobile-robot localisation.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Monocular camera + IMU; ROS-based code depending on Ceres and OpenCV.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/HKUST-Aerial-Robotics/VINS-Mono">VINS-Mono</a></td>
    </tr>
  </tbody>
</table>

<a id="project-unitree-lidar-slam"></a>

<p align="center">
  <img src="datasets-img/unitree-lidar-slam.jpg"
       alt="宇树科技 4D LiDAR SLAM"
       height="300">
</p>

<h3 align="center"><strong>07. 宇树科技 4D LiDAR SLAM</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Unitree's open-source port of the Point-LIO LiDAR-inertial odometry algorithm to its L1 and L2 4D LiDARs — runnable out of the box.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Point-LIO is a point-wise, tightly-coupled LiDAR-inertial odometry that copes well with aggressive motion and sparse geometry. Unitree's official adaptation removes the need for your own extrinsic calibration and parameter tuning: with an L1 or L2 the system runs immediately. Both sensors are 4D units outputting range together with reflectivity and related information. Ideal for users already on Unitree LiDARs who want a localisation pipeline up and running quickly.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Unitree LiDAR L1 or L2 4D LiDAR + IMU; ROS-based code.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/unitreerobotics/point_lio_unilidar">point_lio_unilidar</a></td>
    </tr>
  </tbody>
</table>

<a id="project-slambook2"></a>

<p align="center">
  <img src="datasets-img/slambook2.jpg"
       alt="视觉 SLAM 十四讲"
       height="300">
</p>

<h3 align="center"><strong>08. 视觉 SLAM 十四讲</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>The companion codebase for Gao Xiang's fourteen-chapter visual SLAM book, walking from mathematical foundations to a complete visual odometry and back-end implementation — the most widely used Chinese-language entry point to visual SLAM.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Book and code correspond one-to-one, with a runnable example for every chapter, so typing along turns theory into working code. Coverage is complete: rigid-body motion in 3D, Lie groups and Lie algebras, camera models, feature-based and direct methods, back-end optimisation, loop closure and mapping. Uses Eigen, Sophus, Ceres and g2o, so finishing it also familiarises you with the standard toolchain. Both first and second edition code are kept, with errata updated in this repository. An English edition is in progress, and a Baidu Netdisk mirror helps with access from China.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>No specific hardware — a pure software learning project; depends on Eigen, Sophus, OpenCV, Ceres, g2o and Pangolin.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/gaoxiang12/slambook2">slambook2</a> · <a href="https://github.com/gaoxiang12/slambook">第一版代码</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://book.douban.com/subject/27028215/">豆瓣书评页</a>


<a id="algo-grasping"></a>

#### Grasping & Manipulation


<a id="project-anygrasp"></a>

<h3 align="center"><strong>01. AnyGrasp</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>An open-source general grasp detection and tracking SDK from SJTU and Shanghai AI Lab, producing executable 6-DoF grasp poses for arbitrary objects and poses, with real-time tracking during the grasp.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Not restricted to object categories: it proposes grasps for previously unseen objects, generalising better than early specialised grasp detectors. Supports both detection and tracking, correcting the target continuously as the hand moves. Outputs complete 6-DoF poses that can be sent straight to a manipulator. Ships with the GraspNet dataset and the graspnetAPI toolchain for detection, evaluation and visualisation. Paper and project page are complete, making it a common comparison method in grasping.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Requires an RGB-D camera for depth and colour; the SDK exposes a Python interface and depends on PyTorch with CUDA.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/graspnet/anygrasp_sdk">anygrasp_sdk</a> · <a href="https://github.com/graspnet/graspnetAPI">graspnetAPI</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://graspnet.net/anygrasp.html">项目主页</a> · <a href="https://arxiv.org/abs/2212.08333">arXiv 论文</a>

<a id="project-mynt-eye-s"></a>

<p align="center">
  <img src="datasets-img/mynt-eye-s.jpg"
       alt="小觅双目相机系列"
       height="300">
</p>

<h3 align="center"><strong>02. 小觅双目相机系列</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>The cross-platform SDK for MYNT EYE standard stereo cameras, offering unified interfaces for image capture, stereo synchronisation, depth computation and calibration parameters.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Cross-platform support is well covered, with tested builds on Windows 10, Ubuntu 16.04/14.04 and Jetson TX2. The SDK wraps synchronised stereo capture and depth-map computation, so you don't handle left-right timestamp alignment yourself. Cameras ship factory-calibrated and the SDK reads parameters directly, skipping calibration. Stereo holds up better than structured light at close indoor range, suiting front-end perception for visual SLAM and grasping. Among domestic stereo cameras, one of the better-documented options.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>MYNT EYE standard stereo camera; supports Windows, Ubuntu and Jetson platforms.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/slightech/MYNT-EYE-S-SDK">MYNT-EYE-S-SDK</a></td>
    </tr>
  </tbody>
</table>


------------------------------------------------------------------------

<a id="models"></a>

### 🧠 3. Embodied Models & Platform Toolchains

Covers VLA manipulation models, conversational agents, embodied AI
platforms, and no-code robot development tools.

<a id="model-vla"></a>

#### Embodied Models


<a id="project-gr-1"></a>

<p align="center">
  <img src="datasets-img/gr-1.jpg"
       alt="GR-1（ByteDance Model）"
       height="300">
</p>

<h3 align="center"><strong>01. GR-1（ByteDance Model）</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>ByteDance's open-source multimodal video-pretrained robot manipulation model, learning world dynamics from large-scale video before transferring to manipulation tasks; accepted at ICLR 2024.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>The core idea is applying generative video pretraining to manipulation: video naturally encodes physical common sense about how objects move and hands reach, closer to manipulation than text-only pretraining. A GPT-style unified architecture handles vision and action together, predicting future frames while emitting action sequences. Outperforms contemporary methods on long-horizon benchmarks such as CALVIN. Code and paper are available, making it a reference implementation for the video-pretraining route.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Requires a robot manipulation dataset for fine-tuning; GPU needed for inference, PyTorch-based.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/bytedance/GR-1">GR-1</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://gr1-manipulation.github.io/">项目主页</a> · <a href="https://arxiv.org/abs/2312.13139">arXiv 论文</a>


<a id="model-platform"></a>

#### Platforms & Toolchains


<a id="project-viam"></a>

<p align="center">
  <img src="datasets-img/viam.jpg"
       alt="Viam"
       height="300">
</p>

<h3 align="center"><strong>01. Viam</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>开源的机器人软件平台，把硬件驱动、云端管理、数据采集与机器学习部署整合成一套工具链，支持在浏览器里配置机器人并远程下发指令。</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>定位是机器人的「操作系统层」，硬件驱动、配置、数据、模型都在同一个平台里管理，不用自己拼一堆零散工具；提供云端界面，可以在浏览器里直接配置机器人、看传感器数据、发控制指令；支持多种主流硬件，接入新硬件只需按规范写驱动模块；开源且可自托管，不强制绑定厂商云服务；适合需要快速搭起机器人软件栈、又不想从零造轮子的团队。</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>硬件无关，支持树莓派、Jetson、x86 等常见计算平台，可接入多种传感器与执行器。</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/viamrobotics">Viam Robotics</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://www.viam.com/">官网</a>

<a id="project-joyinside"></a>

<p align="center">
  <img src="datasets-img/joyinside.jpg"
       alt="京东 JoyInside"
       height="300">
</p>

<h3 align="center"><strong>02. 京东 JoyInside</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>京东推出的具身智能开放平台，把京东在对话交互与内容生态上的能力开放给机器人厂商，让硬件具备自然语言对话与智能体能力。</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>依托京东的对话模型与语音能力，接入后机器人可以直接具备多轮对话与意图理解；面向硬件厂商，提供 SDK 与接入流程，不需要自己训练对话模型；背靠京东的内容与服务生态，可以打通商品、服务等场景；属于平台服务型项目，公开资料以官方站点与接入文档为主，开源代码有限。</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>需要联网，硬件侧通过官方 SDK 接入；对主控平台无严格限制。</td>
    </tr>
    <tr>
      <td><strong>Official<br>link</strong></td>
      <td><a href="https://joyinside.com/">JoyInside 官网</a></td>
    </tr>
  </tbody>
</table>

<a id="project-x-humanoid-cloud"></a>

<h3 align="center"><strong>03. 北京人形机器人创新中心·慧思开物</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>北京人形机器人创新中心推出的通用具身智能平台，包含具身大脑与具身小脑两部分，目标是做机器人本体的通用软件底座。</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>把机器人的「思考」与「运动」拆成大脑和小脑两层，大脑负责任务理解与规划，小脑负责实时运动控制；由国家级创新中心主导，背后有天工等实体机器人项目做验证；平台面向多种机器人本体，不是绑定单一机型；目前以平台官网与开放能力介绍为主，开放程度按官方公布的节奏推进。</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>面向多形态机器人本体，具体适配清单以官方公布为准。</td>
    </tr>
    <tr>
      <td><strong>Official<br>link</strong></td>
      <td><a href="https://open.x-humanoid-cloud.com/">慧思开物平台</a></td>
    </tr>
  </tbody>
</table>

<a id="project-linkcraft"></a>

<p align="center">
  <img src="datasets-img/linkcraft.jpg"
       alt="智元灵创平台 LinkCraft"
       height="300">
</p>

<h3 align="center"><strong>04. 智元灵创平台 LinkCraft</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>智元机器人推出的内容创作与动作编排平台，面向智元自家机器人提供动作生成、编排与下发能力，降低机器人表演与交互内容的制作门槛。</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>把机器人动作拆成可编排的片段，用图形化方式拼接，不需要写代码就能做出完整表演；面向内容创作场景，适合展览、活动、科普等需要快速产出机器人动作的场合；与智元的硬件本体绑定，做出来的内容可以直接下发到实机；属于平台服务型项目，公开资料以官方介绍页为主。</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>运行于智元机器人本体，具体机型支持以官方公布为准。</td>
    </tr>
    <tr>
      <td><strong>Official<br>link</strong></td>
      <td><a href="https://www.agibot.com.cn/filepage/295.html">LinkCraft 介绍</a></td>
    </tr>
  </tbody>
</table>

<a id="project-netease-lingjue"></a>

<p align="center">
  <img src="datasets-img/netease-lingjue.jpg"
       alt="网易灵动·灵掘"
       height="300">
</p>

<h3 align="center"><strong>05. 网易灵动·灵掘</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>网易伏羲旗下机器人品牌的挖掘机器人产品，把具身智能能力用在工程机械上，实现挖掘作业的远程操控与自动化。</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>面向的是工程机械这个相对少见的场景，不是通用的桌面或人形机器人；依托网易伏羲在游戏 AI 与强化学习上的积累，把智能决策用到挖掘作业里；提供远程操控与作业管理能力，属于产品化程度较高的具身智能落地案例；公开资料以产品介绍为主，底层算法与代码未完全开放。</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>挖掘机器人整机（工程机械底盘 + 传感器 + 计算单元），具体型号以官方公布为准。</td>
    </tr>
    <tr>
      <td><strong>Official<br>link</strong></td>
      <td><a href="https://lingdong.fuxi.163.com/productSummary/wj">灵掘产品页</a></td>
    </tr>
  </tbody>
</table>

<a id="project-tairos"></a>

<p align="center">
  <img src="datasets-img/tairos.jpg"
       alt="腾讯 Tairos（钛螺丝）"
       height="300">
</p>

<h3 align="center"><strong>06. 腾讯 Tairos（钛螺丝）</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>腾讯推出的具身智能开放平台，为机器人厂商提供感知、规划、控制等基础能力，让硬件团队不必自己从零搭建 AI 能力栈。</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>由腾讯云主导，把大模型、视觉、语音等能力打包成机器人可用的服务；面向机器人厂商提供接入方案，合作机型覆盖多种形态；强调「开箱可用」，厂商接入后可以快速具备智能交互与任务执行能力；属于平台服务型项目，代码未开源，接入方式以官方文档为准。</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>需要联网，硬件侧按官方接入方案改造；对主控平台无严格限制。</td>
    </tr>
    <tr>
      <td><strong>Official<br>link</strong></td>
      <td><a href="https://tairos.tencent.com/">Tairos 官网</a></td>
    </tr>
  </tbody>
</table>


------------------------------------------------------------------------

<a id="data"></a>

### 🛠️ 4. Data, Training & Teleoperation

Covers reinforcement learning, imitation learning, data collection,
teleoperation systems, and robotics tutorials.

<a id="data-rl"></a>

#### Learning & Training Frameworks


<a id="project-booster-gym"></a>

<p align="center">
  <img src="datasets-img/booster-gym.jpg"
       alt="Booster Gym"
       height="300">
</p>

<h3 align="center"><strong>01. Booster Gym</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Booster Robotics' reinforcement learning framework for humanoid locomotion, splitting training, deployment and assets into separate repositories to form a complete sim-to-real pipeline.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Divided into Booster Train, Booster Deploy and Booster Assets, each adoptable independently. Training builds on Isaac Lab with multiple RL tasks for robots such as the K1. The deployment framework makes it easy to run trained policies on real hardware seamlessly. Official real-robot deployment videos show the full chain working end to end. Suited to teams wanting to validate humanoid motion-control policies quickly.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Targets Booster humanoids such as the K1; training needs an NVIDIA GPU and the Isaac Lab simulator.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/BoosterRobotics/booster_gym">Booster Gym</a> · <a href="https://github.com/BoosterRobotics/booster_train">Booster Train</a> · <a href="https://github.com/BoosterRobotics/booster_deploy">Booster Deploy</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://github.com/BoosterRobotics/booster_assets">Booster Assets</a>

<a id="project-humanoid-gym"></a>

<p align="center">
  <img src="datasets-img/humanoid-gym.jpg"
       alt="Humanoid-Gym"
       height="300">
</p>

<h3 align="center"><strong>02. Humanoid-Gym</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A reinforcement learning framework for humanoid robots built around zero-shot sim-to-real transfer, so policies trained in simulation deploy directly to hardware.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>The headline feature is tuning-free sim-to-real: through domain randomisation and symmetry rewards, trained policies work without real-robot fine-tuning. Built on Isaac Gym, training is fast enough to produce a walkable policy in a few hours on a single GPU. Provides the full train / play / export workflow plus evaluation scripts. The paper has clear experimental comparisons and demonstrates transfer across multiple terrains. An important baseline for humanoid locomotion research.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Training needs an NVIDIA GPU with Isaac Gym; deployment targets humanoid bodies, validated on the XBot family.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/roboterax/humanoid-gym">Humanoid-Gym</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://sites.google.com/view/humanoid-gym/">项目主页</a> · <a href="https://arxiv.org/abs/2404.05695">arXiv 论文</a>

<a id="project-open-r1-multimodal"></a>

<p align="center">
  <img src="datasets-img/open-r1-multimodal.jpg"
       alt="OpenR1-Multimodal"
       height="300">
</p>

<h3 align="center"><strong>03. OpenR1-Multimodal</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A multimodal reproduction of the DeepSeek-R1 reinforcement learning paradigm on top of Qwen2-VL, using GRPO to teach vision-language models to reason before answering.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Extends R1's RL approach from pure text to multimodality, showing the paradigm holds for visual tasks too. The full training pipeline is reproduced, with models, datasets and code public on HuggingFace and GitHub. Training data is modest (8k scale) yet the effect is pronounced, indicating high sample efficiency for GRPO. The team stays measured, stating plainly that their insights may not be correct but will be shared honestly. Good practical material for understanding how RL acts on multimodal models.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Multi-GPU needed for training; the Qwen2-VL-2B base model can run inference on consumer-grade cards.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/EvolvingLMMs-Lab/open-r1-multimodal">open-r1-multimodal</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://huggingface.co/lmms-lab/Qwen2-VL-2B-GRPO-8k">HuggingFace 模型</a>

<a id="project-unitree-il-lerobot"></a>

<p align="center">
  <img src="datasets-img/unitree-il-lerobot.jpg"
       alt="unitree_IL_lerobot"
       height="300">
</p>

<h3 align="center"><strong>04. unitree_IL_lerobot</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Unitree's imitation-learning toolchain built on the LeRobot ecosystem, chaining data collection, dataset conversion, policy training and deployment for Unitree robots.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Keeps pace with LeRobot releases and already supports the lerobot dataset v3.0 format. Policies include pi0, pi05 and GR00T among other mainstream VLA models, with no need to implement them yourself. The companion any4lerobot tool converts between dataset format versions. Integrated with Unitree's AVP teleoperation and Isaac Lab simulation repos to close the collect-train-deploy loop. Datasets are hosted on HuggingFace for direct download and reproduction.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Targets Unitree robot bodies; GPU needed for training, with AVP or XR teleoperation hardware for data collection.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/unitreerobotics/unitree_IL_lerobot">unitree_IL_lerobot</a> · <a href="https://github.com/unitreerobotics/avp_teleoperate">AVP 遥操作</a> · <a href="https://github.com/unitreerobotics/unitree_sim_isaaclab">仿真环境</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://huggingface.co/unitreerobotics">宇树数据集（HuggingFace）</a>

<a id="project-unitree-rl-gym"></a>

<p align="center">
  <img src="datasets-img/unitree-rl-gym.jpg"
       alt="unitree_rl_gym"
       height="300">
</p>

<h3 align="center"><strong>05. unitree_rl_gym</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Unitree's reinforcement learning locomotion framework, providing massively parallel training environments on Isaac Gym plus MuJoCo sim-to-sim validation before real-robot deployment.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Breaks the RL control workflow into Train → Play → Sim2Sim → Sim2Real, each with matching commands, so the path is explicit. Isaac Gym enables large-scale parallel environments for efficient training. The MuJoCo sim-to-sim stage adds a validation layer before hardware deployment, reducing crash risk. Supports multiple Unitree models, quadrupeds and humanoids alike, with one reusable workflow. The most direct starting point for learning Unitree RL control.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Training needs an NVIDIA GPU with Isaac Gym; sim-to-sim relies on MuJoCo; deployment targets Unitree robots.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/unitreerobotics/unitree_rl_gym">unitree_rl_gym</a></td>
    </tr>
  </tbody>
</table>

<a id="project-unitree-rl-lab"></a>

<h3 align="center"><strong>06. unitree_rl_lab</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Unitree's next-generation reinforcement learning environment collection built on NVIDIA Isaac Lab, providing standardised training tasks and parallel environments for Unitree robots.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Migrates from Isaac Gym to Isaac Lab, following NVIDIA's recommended technology path. Isaac Lab's abstractions for assets, sensor simulation and domain randomisation are more complete, making new tasks less work than in the Isaac Gym era. Ships a set of ready-to-use Unitree robot tasks, trainable as-is or as a starting point. Apache 2.0 licensed, so commercially friendly. Best for users already on the Isaac Lab ecosystem who need Unitree assets and tasks.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Isaac Sim 5.1 + Isaac Lab 2.3; training needs an NVIDIA RTX-class GPU.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/unitreerobotics/unitree_rl_lab">unitree_rl_lab</a></td>
    </tr>
  </tbody>
</table>


<a id="data-teleop"></a>

#### Data Collection & Teleoperation


<a id="project-aloha2"></a>

<p align="center">
  <img src="datasets-img/aloha2.jpg"
       alt="ALOHA 2"
       height="300">
</p>

<h3 align="center"><strong>01. ALOHA 2</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A low-cost bimanual teleoperation and demonstration platform from Stanford and Google DeepMind, whose leader-follower arm structure lets an operator directly drive the robot and capture high-quality demonstrations.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>The leader-follower design maps the operator's motion straight onto the follower, so captured data carries human dexterity far more naturally than a joystick. Total system cost is in the twenty-thousand-dollar range, among the cheapest bimanual platforms of its kind. ALOHA 2 improves on 1.0 with gravity compensation, grippers and cable routing for noticeably better durability. Ships with imitation-learning algorithms such as ACT, completing the path from demonstration to policy. Widely adopted in academia as a de facto standard bimanual platform.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Leader-follower bimanual structure, roughly 14 DOF total; Dynamixel servos; system cost in the twenty-thousand-dollar range.</td>
    </tr>
    <tr>
      <td><strong>Official<br>link</strong></td>
      <td><a href="https://aloha-2.github.io/">ALOHA 2 项目页</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://arxiv.org/abs/2406.09246">论文（arXiv）</a>

<a id="project-dexbotic-dexcap"></a>

<p align="center">
  <img src="datasets-img/dexbotic-dexcap.jpg"
       alt="DexCap"
       height="300">
</p>

<h3 align="center"><strong>02. DexCap</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Stanford's portable hand motion capture and dexterous manipulation data collection system, using wearable devices to capture finger motion and map human dexterity directly onto dexterous hands.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>The wearable approach frees the operator's range of motion, unlike fixed rigs that only capture data in a specific workspace. It focuses on finger-level dexterity, the hardest part of dexterous manipulation data to obtain. Captured data trains dexterous-hand policies directly, skipping pose reconstruction from video. Hardware cost is far below professional motion capture, making it practical for labs to build. A representative approach in dexterous manipulation data collection.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Wearable hand motion capture plus a dexterous hand end effector; collection and training need an accompanying compute unit.</td>
    </tr>
    <tr>
      <td><strong>Official<br>link</strong></td>
      <td><a href="https://dex-cap.github.io/">DexCap 项目页</a></td>
    </tr>
  </tbody>
</table>

<a id="project-dobb-e"></a>

<p align="center">
  <img src="datasets-img/dobb-e.jpg"
       alt="Dobb-E"
       height="300">
</p>

<h3 align="center"><strong>03. Dobb-E</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A robot learning system that uses an iPhone for both teleoperation and data collection — a simple 3D-printed Reacher tool clamps the phone to the end effector to capture manipulation data and train policies.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>The capture device is just an iPhone, pushing cost to a minimum so any lab with an arm can replicate it. The Reacher gripper is simple to build and 3D-printable. Demonstrates the full cycle of collecting, training and deploying from scratch in a home environment. Emphasis is on working in real, non-laboratory settings, with generalisation as the central concern. A typical representative of the low-cost collection plus fast deployment approach.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Robot arm + iPhone (for pose and visual capture) + 3D-printed Reacher gripper.</td>
    </tr>
    <tr>
      <td><strong>Official<br>link</strong></td>
      <td><a href="https://dobb-e.com/">Dobb-E 项目页</a></td>
    </tr>
  </tbody>
</table>

<a id="project-xr-teleoperate"></a>

<p align="center">
  <img src="datasets-img/xr-teleoperate.jpg"
       alt="宇树科技 XR 遥操作"
       height="300">
</p>

<h3 align="center"><strong>04. 宇树科技 XR 遥操作</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Unitree's open-source XR teleoperation system, driving Unitree humanoids from extended-reality devices such as Apple Vision Pro, mapping the operator's head and hand motion onto the robot in real time.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>XR headset teleoperation gives the operator the robot's viewpoint while hand gestures control arms and grippers directly — far more immersive and intuitive than a controller. Actively updated with support for newer models including the H2 and R1 (A5/A7), plus BrainCo hand controller input. Defaults to a head-yaw-relative arm reference frame so long sessions are less fatiguing. Integrated with unitree_IL_lerobot so captured data flows straight into training. Currently among the more usable open-source humanoid teleoperation options.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Apple Vision Pro or another XR device plus a Unitree humanoid (H2, R1 and others); BrainCo hand controller optional.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/unitreerobotics/xr_teleoperate">xr_teleoperate</a></td>
    </tr>
  </tbody>
</table>


<a id="data-tutorial"></a>

#### Tutorials & Knowledge Bases


[↑ Back to Contents](#toc)

<!-- Retained for compatibility with existing links. -->

<a id="project-learn-arduino"></a>

<p align="center">
  <img src="datasets-img/learn-arduino.jpg"
       alt="Learn Arduino"
       height="300">
</p>

<h3 align="center"><strong>01. Learn Arduino</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>An interactive 3D Arduino course in the browser: drag wires, place components and edit code on a virtual board, then watch simulated LED, servo and sensor feedback.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Rotatable 3D board views with pins and wires laid out by circuit connection so miswiring is visible immediately. Code can be edited and run in place, with a serial monitor. 16 progressive lessons run from blinking an LED, buttons and potentiometers through ultrasonic sensing, servos and stepper motors, ending in an obstacle-avoiding traffic light project. Simulation cannot reproduce loose contacts or under-voltage.</td>
    </tr>
    <tr>
      <td><strong>Hardware <br> plan</strong></td>
      <td>No hardware required — a purely browser-based 3D circuit simulation and course. No download or installation needed.</td>
    </tr>
    <tr>
      <td><strong>GitHub <br> link</strong></td>
      <td>No official GitHub source repository could be verified. Use online: <a href="https://learn-arduino-red.vercel.app/">learn-arduino-red.vercel.app</a></td>
    </tr>
  </tbody>
</table>

Related resources: designed by <a href="https://x.com/DilumSanjaya">Dilum Sanjaya</a> (independent project, not an official Arduino product)

<a id="project-robowiki"></a>

<p align="center">
  <img src="datasets-img/robowiki.jpg"
       alt="RoboWiki"
       height="300">
</p>

<h3 align="center"><strong>02. RoboWiki</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>A Chinese-language robotics wiki initiated by Yunfei Robotics Lab, edited as a public knowledge commons and covering robot design, modelling, simulation, programming, vision, algorithms and industry applications.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>Follows a Wikipedia-style crowdsourcing model that champions knowledge freedom, open to editing by anyone. Content is organised along the full R&D chain, from design and modelling through to algorithms and applications. Initiated by the Bilibili robotics-science channel Yunfei Robotics Lab, with a practical engineering flavour. A useful entry point for Chinese-language robotics material — a good first stop when meeting an unfamiliar concept.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>No hardware requirements — a pure knowledge-base project.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/yfrobotics/robowiki">RoboWiki</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://space.bilibili.com/493264461">Initiator Bilibili channel</a>

<a id="project-unitree-guide"></a>

<h3 align="center"><strong>03. 宇树科技机器人控制教程</strong></h3>

<table width="100%">
  <tbody>
    <tr>
      <td><strong>Summary</strong></td>
      <td>Unitree's open-source robotics control teaching project, accompanying the book Quadruped Robot Control Algorithms and covering modelling, state estimation and motion control through Gazebo simulation.</td>
    </tr>
    <tr>
      <td><strong>Features</strong></td>
      <td>One of the few official open-source projects whose primary goal is teaching; code follows the book's chapters rather than being a scatter of examples. Starts quickly in Gazebo simulation without requiring real hardware. Covers the core of quadruped control: leg kinematics, body state estimation, gait generation and balance control. More detailed documentation is available on Unitree's developer site. Recommended on Ubuntu 18.04 with ROS Melodic. Suited to systematic study rather than a quick demo.</td>
    </tr>
    <tr>
      <td><strong>Hardware<br>plan</strong></td>
      <td>Learnable without hardware via Gazebo simulation; Ubuntu 18.04 + ROS Melodic recommended; deployable on a real Unitree quadruped.</td>
    </tr>
    <tr>
      <td><strong>GitHub<br>link</strong></td>
      <td><a href="https://github.com/unitreerobotics/unitree_guide">unitree_guide</a></td>
    </tr>
  </tbody>
</table>

Related resources: <a href="https://support.unitree.com/home/zh/Algorithm_Practice">宇树开发者文档</a>


<a id="reasoning-rl"></a>
