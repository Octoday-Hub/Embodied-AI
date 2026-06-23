# 🛠️ Tools & Open-Source Projects

> 💡 This list is continuously updated. If you find a good tool that is not included, or if existing information needs updating, please submit a [PR](https://github.com/Octoday-Hub/Embodied-AI/pulls) or provide feedback in [Issues](https://github.com/Octoday-Hub/Embodied-AI/issues).


<a name=toc></a>

## Table of Contents

**Categories:** [🎮 Simulation Platforms](#simulation-platforms) · [🤖 Models](#models) · [🧰 General Tools & Libraries](#general-tools) · [🏗️ Learning Frameworks](#learning-frameworks) · [🤖 Robot Projects](#robot-projects) · [🧠 Reasoning / RL](#reasoning-rl) · [🗺️ SLAM & Perception](#slam-perception) · [🔧 Middleware & ROS Tools](#middleware-ros) · [🛒 Other](#other)


<a name=simulation-platforms></a>

## 🎮 Simulation Platforms

(Items merged from repos and tools)

- **BEHAVIOR-1K** — [`StanfordVL/BEHAVIOR-1K`](https://github.com/StanfordVL/BEHAVIOR-1K) ⭐ 1.5k 
 📄 Stanford benchmark for embodied AI agents on 1,000 everyday household activities.

- **XTDrone** — [`robin-shaun/XTDrone`](https://github.com/robin-shaun/XTDrone) ⭐ 6.5k 
 📄 A UAV simulation platform based on PX4, ROS, and Gazebo, supporting swarm simulation.

- **Prometheus** — [`amov-lab/Prometheus`](https://github.com/amov-lab/Prometheus) ⭐ 4.5k 
 📄 An open-source system for autonomous UAVs, supporting detection, SLAM, and formation control.

[↑ Back to TOC](#toc)

<a name=models></a>

## 🤖 Models

- **VLA-Adapter** — [`OpenHelix-Team/VLA-Adapter`](https://github.com/OpenHelix-Team/VLA-Adapter) ⭐ 2.2k  
 📄 Efficient training paradigm for small-scale VLA models — VLA Adapter

- **LLaVA-OneVision** — [`EvolvingLMMs-Lab/LLaVA-OneVision`](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision) ⭐ 754  
 📄 Fully open-source large multimodal model achieving SOTA at low cost

- **Otter** — [`EvolvingLMMs-Lab/Otter`](https://github.com/EvolvingLMMs-Lab/Otter) ⭐ 3.3k  
 📄 OpenFlamingo-based multimodal model trained on MIMIC-IT dataset for improved instruction following

- **XR-1** — [`Open-X-Humanoid/XR-1`](https://github.com/Open-X-Humanoid/XR-1)  
 📄 China's first national standard VLA foundation model (Beijing Humanoid Robot Innovation Center), supporting cross-robot platform operation with RoboMIND 2.0 dataset and ArtVIP assets

- **DexVLA** — [`juruobenruo/DexVLA`](https://github.com/juruobenruo/DexVLA)  
 📄 Qwen2-VL based vision-language-action model supporting single-arm, dual-arm, and dexterous hand control

- **ManiFoundation** — [`NUS-LinS-Lab/ManiFM`](https://github.com/NUS-LinS-Lab/ManiFM)  
 📄 General robot manipulation foundation model (NUS/Tsinghua) handling rigid, articulated, and deformable objects via contact synthesis

- **RoboBrain 2.5** — [`FlagOpen/RoboBrain2.5`](https://github.com/FlagOpen/RoboBrain2.5)  
 📄 Next-gen embodied AI foundation model (BAAI/Peking University) supporting precise 3D spatial reasoning, depth-aware coordinate prediction, and temporal modeling

- **WholebodyVLA** — [`OpenDriveLab/WholebodyVLA`](https://github.com/OpenDriveLab/WholebodyVLA) ⭐  
 📄 ICLR 2026, unified latent-space VLA model for humanoid whole-body mobile manipulation (Shanghai AI Lab)

- **X-VLA** — [`2toinf/X-VLA`](https://github.com/2toinf/X-VLA)  
 📄 ICLR 2026, soft-prompt Transformer cross-morphology VLA model, AgiBot World Challenge (IROS 2025) champion

- **RoboticsDiffusionTransformer (RDT-1B)** — [`thu-ml/RoboticsDiffusionTransformer`](https://github.com/thu-ml/RoboticsDiffusionTransformer)  
 📄 Bimanual robot manipulation foundation model (Tsinghua University) using diffusion Transformer architecture, SOTA across multiple bimanual tasks

- **AgiBot-World** — [`OpenDriveLab/AgiBot-World`](https://github.com/OpenDriveLab/AgiBot-World)  
 📄 IROS 2025 Best Paper candidate, large-scale manipulation platform for scalable embodied intelligence (Shanghai AI Lab)

- **Dexterity-BEV** — See [Dexterity-BEV](https://arxiv.org/abs/2606.02274)  
 📄 Aligning 3D world and actions for generalizable robot policy learning

[↑ Back to ToC](#toc)


<a name=general-tools></a>

## 🧰 General Tools & Libraries

> Covering simulation tools, development frameworks, middleware, benchmarks, and general-purpose libraries

- **AI2-THOR** — [`ai2thor.allenai.org`](https://ai2thor.allenai.org/)
 📄 Semantic interactive simulator from the Allen Institute, with 200+ rooms and 2600+ interactive objects.

- **DeepMind SI-Tuning** — [`github.com/google-deepmind/si_tuning`](https://github.com/google-deepmind/si_tuning)
 📄 VLA fine-tuning framework from Google DeepMind for RT-2, OpenVLA and other VLA models.

- **Diffusion Policy** — [`github.com/real-stanford/diffusion_policy`](https://github.com/real-stanford/diffusion_policy)
 📄 Diffusion-model-based robot policy learning framework for imitation learning and manipulation.

- **DORA** — [`github.com/dora-rs/dora`](https://github.com/dora-rs/dora)
 📄 Dataflow middleware for AI robotics with low-latency, composable, distributed pipelines.

- **Intern-Robotics** — [`internrobotics.shlab.org.cn`](https://internrobotics.shlab.org.cn/)
 📄 Open-source full-stack embodied robotics framework from Shanghai AI Lab, covering navigation and manipulation.

- **LeRobot** — [`huggingface.co/docs/lerobot/main/en/index`](https://huggingface.co/docs/lerobot/main/en/index)
 📄 Hugging Face real-world robot ML toolkit with models, datasets, and training utilities.

- **MimicGen** — [`github.com/NVlabs/mimicgen`](https://github.com/NVlabs/mimicgen)
 📄 Data generation system that scales few demos into large robot datasets for manipulation.

- **Octo** — [`github.com/octo-models/octo`](https://github.com/octo-models/octo)
 📄 Open-source general robot policy pretrained on multi-robot trajectories.

- **OK-Robot** — [`ok-robot.github.io`](https://ok-robot.github.io/)
 📄 Modular framework from NYU for zero-shot pick-and-place in real homes using VLMs.

- **OpenVLA** — [`github.com/openvla/openvla`](https://github.com/openvla/openvla)
 📄 Open-source VLA model for general robot manipulation, supporting fine-tuning and evaluation.

- **OpenXLab** — [`openxlab.org.cn`](https://openxlab.org.cn/)
 📄 Open embodied AI platform from Shanghai AI Lab with full toolchain from data to deployment.

- **RobotecAI RAI** — [`github.com/RobotecAI/rai`](https://github.com/RobotecAI/rai)
 📄 Open-source agentic robotics framework on ROS 2, supporting natural language and multimodal execution.

- **RoboGen** — [`robogen-ai.github.io`](https://robogen-ai.github.io/)
 📄 Code-generative robotics framework from MIT that uses LLMs to auto-generate Python robot policies.

- **robomimic** — [`github.com/ARISE-Initiative/robomimic`](https://github.com/ARISE-Initiative/robomimic)
 📄 General framework for robot learning from demonstration with datasets and baselines.

- **ROS / ROS2** — [`www.ros.org`](https://www.ros.org)
 📄 Robot Operating System providing tools for modular, distributed robot software development.

- **RQT Frame Editor** — [`github.com/ipa320/rqt_frame_editor_plugin`](https://github.com/ipa320/rqt_frame_editor_plugin)
 📄 Rqt plugin for creating and adjusting TF frames for multi-sensor coordination.

- **SAGE** — [`github.com/eth-easl/sage`](https://github.com/eth-easl/sage)
 📄 Distributed embodied AI computing framework from ETH Zurich for large-scale policy training.

- **Theseus** — [`github.com/facebookresearch/theseus`](https://github.com/facebookresearch/theseus)
 📄 Differentiable nonlinear optimization library for robotics and vision state estimation.

- **Universal Manipulation Interface (UMI)** — [`github.com/real-stanford/universal_manipulation_interface`](https://github.com/real-stanford/universal_manipulation_interface)
 📄 Stanford general manipulation interface for robot learning and manipulation tasks.

- **VEX Robotics Software** — [`www.vexrobotics.com/?srsltid=AfmBOoqB_9zu0-eFHO4wzVB_33rsABV6DRRJ_drQfuk67n-MLcUmVy9M`](https://www.vexrobotics.com/?srsltid=AfmBOoqB_9zu0-eFHO4wzVB_33rsABV6DRRJ_drQfuk67n-MLcUmVy9M)
 📄 Software tools for VEX robotics platform with drag-and-drop programming for education.

[↑ Back to ToC](#toc)


<a name=learning-frameworks></a>

## 🏗️ Learning Frameworks

(Items merged from repos and tools)

- **RLinf** — [`RLinf/RLinf`](https://github.com/RLinf/RLinf) ⭐ 3.7k 
 📄 Reinforcement learning infrastructure for embodied and agentic AI.

- **OpenLoong (Brain)** — [`loongOpen`](https://github.com/loongOpen) 
 📄 Qinglong humanoid full-stack skill scheduling framework with MPC+WBC control, Gymloong/MiniGym training platforms.

- **AimRT** — [`AimRT/AimRT`](https://github.com/AimRT/AimRT) 
 📄 Modern C++ runtime framework for robotics, lightweight and compatible with ROS2/HTTP/gRPC.

- **Open-TeleVision** — [`OpenTeleVision/TeleVision`](https://github.com/OpenTeleVision/TeleVision) 
 📄 Immersive VR-based robot teleoperation system for real-time bimanual manipulation.

- **AgileX Cobot Magic** — [`agilexrobotics`](https://github.com/agilexrobotics) 
 📄 open-source bimanual mobile manipulation platform based on Mobile ALOHA (AgileX Robotics).

[↑ Back to TOC](#toc)

- **every-embodied** — [`datawhalechina/every-embodied`](https://github.com/datawhalechina/every-embodied) ⭐ 2.2k  
  📄 Build VLA/OpenVLA/SmolVLA/Pi0 from scratch with only Python basics.

[↑ Back to TOC](#toc)


<a name=robot-projects></a>

## 🤖 Robot Projects

### humanoid

- **AgiBot X1** — [`infer`](https://github.com/AgibotTech/agibot_x1_infer) · [`train`](https://github.com/AgibotTech/agibot_x1_train) · [`hardware`](https://github.com/AgibotTech/agibot_x1_hardware) 
 📄 Agibot X1 fully open-sourcehumanoid project with inference, RL training code, and hardware design.

- **OpenLoong Qinglong** — [`loongOpen`](https://github.com/loongOpen) 
 📄 Full-stack open-sourcehumanoid project (Shanghaihumanoid Innovation Center/OpenAtom Foundation) with MPC+WBC control and training platform

- **Fourier N1** — [`FFTAI`](https://github.com/FFTAI) 
 📄 World first fully open-sourcehumanoid (Fourier Intelligence) with full hardware design, BOM, assembly guide, and SDK (1.3m/38kg/3.5m/s).m/s

- **EngineAI Humanoid** — [`engineai-robotics/engineai_humanoid`](https://github.com/engineai-robotics/engineai_humanoid) 
 📄 EngineAI SA01/PM01 bipedal robot open-source motion control with end-to-end neural gait.

- **Booster Gym** — [`BoosterRobotics`](https://github.com/BoosterRobotics) 
 📄 Booster T1/K1 humanoid end-to-end RL motion control framework (Booster Robotics) with RoboCup kicking demo.

- **Humanoid-Gym** — [`roboterax/humanoid-gym`](https://github.com/roboterax/humanoid-gym) 
 📄 Isaac Gym-basedhumanoid RL training framework supporting zero-shot sim-to-real transfer.

- **Unitree Qmini** — [`unitreerobotics/Qmini`](https://github.com/unitreerobotics/Qmini) 
 📄 Unitree open-source bipedal platform with BOM, assembly guide, and URDF models.

### quadruped

- **OpenCat** — [`PetoiCamp/OpenCat`](https://github.com/PetoiCamp/OpenCat) ⭐ 15k 
 📄 open-sourcequadruped platform

- **Xiaomi CyberDog** — [`MiRoboticsLab/cyberdog_ros2`](https://github.com/MiRoboticsLab/cyberdog_ros2) 
 📄 Xiaomi CyberDog open-source quadruped software and hardware.

- **Unitreequadruped ROS** — [`unitreerobotics/unitree_ros`](https://github.com/unitreerobotics/unitree_ros) 
 📄 Unitreequadruped Go1/Go2 ROS driver packages.

### Arms & Desktop Robots

- **vlm_arm** — [`TommyZihao/vlm_arm`](https://github.com/TommyZihao/vlm_arm) 
 📄 Robot arm + LLM + multimodal integration (Tongji Zihao).

- **Dummy-Robot (Mini Robot Arm)** — [`peng-zhihui/Dummy-Robot`](https://github.com/peng-zhihui/Dummy-Robot) 
 📄 DIY mini robot arm (ZhiHuijun).

- **X-Bot Smart Robot Arm** — [`peng-zhihui/X-Bot`](https://github.com/peng-zhihui/X-Bot) 
 📄 CoreXY-based drawing robot arm (ZhiHuijun).

- **ElectronBot Mini Desktop Robot** — [`peng-zhihui/ElectronBot`](https://github.com/peng-zhihui/ElectronBot) 
 📄 Compact desktop robot (ZhiHuijun).

- **Rubik Cube Robot** — [`diy-robots.com`](http://www.diy-robots.com/?page_id=46) 
 📄 LEGO-based Rubik cube-solving robot.

### Mobile Robots

- **MiniRover Mars Rover** — [`peng-zhihui/MiniRover-Hardware`](https://github.com/peng-zhihui/MiniRover-Hardware) 
 📄 DIY Mars rover open-source project (ZhiHuijun).

- **ONE-Robot Unicycle Robot** — [`peng-zhihui/ONE-Robot`](https://github.com/peng-zhihui/ONE-Robot) 
 📄 IMU and STM32-based one-wheel self-balancing robot (ZhiHuijun).


- **Visual SLAM 14 Lectures** — [`gaoxiang12/slambook2`](https://github.com/gaoxiang12/slambook2) ⭐ 12k 
 📄 Classic SLAM Chinese tutorial with companion code (Gao Xiang).

- **VINS-Mono** — [`HKUST-Aerial-Robotics/VINS-Mono`](https://github.com/HKUST-Aerial-Robotics/VINS-Mono) ⭐ 5k 
 📄 Robust monocular visual-inertial state estimator (HKUST).

- **VINS-Fusion** — [`HKUST-Aerial-Robotics/VINS-Fusion`](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion) 
 📄 Optimization-based multi-sensor estimator supporting mono/stereo + IMU fusion.

- **LIO-SAM** — [`TixiaoShan/LIO-SAM`](https://github.com/TixiaoShan/LIO-SAM) ⭐ 3.5k 
 📄 Tightly-coupled LiDAR-inertial odometry, widely cited LiDAR SLAM solution.

- **FAST_LIO** — [`hku-mars/FAST_LIO`](https://github.com/hku-mars/FAST_LIO) ⭐ 2.5k 
 📄 Efficient and robust LiDAR-inertial odometry (HKU MARS Lab).

- **FAST-LIVO2** — [`hku-mars/FAST-LIVO2`](https://github.com/hku-mars/FAST-LIVO2) 
 📄 Fast direct LiDAR-inertial-visual odometry with tight coupling.

- **R3LIVE** — [`hku-mars/r3live`](https://github.com/hku-mars/r3live) ⭐ 2.0k 
 📄 Robust real-time RGB-colored LiDAR-inertial-visual SLAM.

- **Unitree 4D LiDAR SLAM** — [`unitreerobotics/point_lio_unilidar`](https://github.com/unitreerobotics/point_lio_unilidar) 
 📄 Point-LIO based SLAM for Unitree L1 4D LiDAR.

### Grasping & Manipulation

- **AnyGrasp** — [`graspnet/anygrasp_sdk`](https://github.com/graspnet/anygrasp_sdk) 
 📄 Efficient 6-DoF grasp pose estimation (Shanghai AI Lab) for general object grasping.

- **MYNT EYE Stereo Camera** — [`slightech/MYNT-EYE-S-SDK`](https://github.com/slightech/MYNT-EYE-S-SDK) 
 📄 MYNT EYE stereo camera series with complete SLAM and vision solutions.

### Others


- **ALOHA 2** — [`aloha-2.github.io`](https://aloha-2.github.io/)
 📄 Low-cost open-source hardware platform, with tutorials and MuJoCo simulation models.

- **Beijing Humanoid Innovation Center·Huisi Kaiwu** — [`login.x-humanoid-cloud.com/?responseType=code&clientId=fd6c22fb&redirectUri=https%3A%2F%2Fopen.x-humanoid-cloud.com%2Fhome&stamp=1778429122172&env=cloud`](https://login.x-humanoid-cloud.com/?responseType=code&clientId=fd6c22fb&redirectUri=https%3A%2F%2Fopen.x-humanoid-cloud.com%2Fhome&stamp=1778429122172&env=cloud)
 📄 toolchain platform covering skill invocation, agent configuration, and deployment.

- **DexCap** — [`dex-cap.github.io`](https://dex-cap.github.io/)
 📄 Stanford dexterous hand data collection system, using motion capture cameras to collect human dexterous manipulation data at scale for Sim-to-Real transfer.

- **Dobb-E** — [`dobb-e.com`](https://dobb-e.com/)
 📄 NYU full-stack pipeline from hardware to data, with low-cost handheld Stick hardware, dataset, and imitation learning frameworkobots to learn tasks from 15 min demos.

- **GR-1 (ByteDance Model)** — [`github.com/bytedance/GR-1`](https://github.com/bytedance/GR-1)
 📄 ByteDance open-source GPT-style vision robot model for language-conditioned multitask learning.

- **JD JoyInside** — [`joyinside.com`](https://joyinside.com/)
 📄 conversational agent platform

- **kscale·K-Bot** — [`docs.kscale.dev/category/k-bot`](https://docs.kscale.dev/category/k-bot)
 📄 open-sourcefull-stack humanoid platform

- **Agibot LinkCraft Platform** — [`www.agibot.com.cn/filepage/295.html`](https://www.agibot.com.cn/filepage/295.html)
 📄 Agibotzero-code robot content creation platform, supporting motion imitation and speech-driven task generation.

- **Tencent Tairos** — [`tairos.tencent.com`](https://tairos.tencent.com/)
 📄 open embodied AI platform, providing models, tools, and data services.

- **Viam** — [`www.viam.com`](https://www.viam.com)
 📄 software platform, with unified API, module registry, remote operations, and fleet management.

- **NetEase Lingdong Lingjue** — [`lingdong.fuxi.163.com/productSummary/wj`](https://lingdong.fuxi.163.com/productSummary/wj)
  📄 Embodied AI model and training framework for mining excavator loading.

- **Unitree XR Teleoperation** — [`unitreerobotics/xr_teleoperate`](https://github.com/unitreerobotics/xr_teleoperate) 
  📄 XR-based (Apple Vision Pro/Quest) H1/G1 humanoid teleoperation system

- **RoboWiki** — [`yfrobotics/robowiki`](https://github.com/yfrobotics/robowiki) 
  📄 Robotics wiki (Yunfei Robotics Lab).

- **Unitree Robot Control Guide** — [`unitreerobotics/unitree_guide`](https://github.com/unitreerobotics/unitree_guide) 
  📄 Open-source tutorial for Unitree quadruped robot control, suitable for beginners.


<a name=reasoning-rl></a>

## 🧠 Reasoning / Reinforcement Learning

- **OpenR1-Multimodal** — [`EvolvingLMMs-Lab/OpenR1-Multimodal`](https://github.com/EvolvingLMMs-Lab/OpenR1-Multimodal) ⭐ 1.5k 
 📄 R1 reasoning paradigm on multimodal models with 8K open-source multimodal RL samples.

- **unitree_rl_gym** — [`unitreerobotics/unitree_rl_gym`](https://github.com/unitreerobotics/unitree_rl_gym) 
 📄 Unitree quadruped/humanoid RL training framework based on Isaac Gym.

- **unitree_rl_lab** — [`IsaacLab`](https://github.com/unitreerobotics/unitree_rl_lab) · [`MuJoCo`](https://github.com/unitreerobotics/unitree_rl_mjlab) 
 📄 Unitree robot RL implementations based on Isaac Lab and MuJoCo.

- **unitree_IL_lerobot** — [`unitreerobotics/unitree_IL_lerobot`](https://github.com/unitreerobotics/unitree_IL_lerobot) 
 📄 LeRobot-based imitation learning tool for G1 bimanual dexterous hand data.

[↑ Back to TOC](#toc)

<a name=slam-perception></a>

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


<a name=middleware-ros></a>

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
 📄 A large-scale interactive simulation benchmark built on the SAPIEN engine, with 100 household objects and 30 complex tasks such as hang up a wet towel, providing a full testbed for physical interaction capabilities.

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


<a name=other></a>

## 🛒 Other

> Tools, platforms, and projects not covered by the above categories

[↑ Back to TOC](#toc)


*Data updated: June 22, 2026*
