# **SLAM、感知与标定**

[返回工具与项目导航](04-tools.md#toc) · [模型与策略](04-models.md) · [学习与训练](04-learning.md)

按输入与用途选择工具：视觉/惯性与激光定位、相机及传感器标定、点云与图像处理、抓取感知。导航系统单列，便于区分定位建图与路径规划。

[定位与建图](#localization-mapping) · [标定与传感器](#calibration-sensors) · [图像与点云](#image-pointcloud) · [抓取感知](#grasp-perception) · [导航与参考](#navigation-reference)

<a id="localization-mapping"></a>

## **定位与建图**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **VINS-Mono** | 视觉惯性里程计 | 单目相机与 IMU 的状态估计 | [仓库](https://github.com/HKUST-Aerial-Robotics/VINS-Mono) |
| **VINS-Fusion** | 视觉惯性状态估计 | 查看多传感器配置及融合实现 | [仓库](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion) |
| **ORB-SLAM3** | 视觉与视觉惯性 SLAM | 查看单目、双目或 RGB-D 配置 | [仓库](https://github.com/UZ-SLAMLab/ORB_SLAM3) |
| **LIO-SAM** | 激光惯性里程计 | 激光雷达与 IMU 融合的定位建图 | [仓库](https://github.com/TixiaoShan/LIO-SAM) |
| **FAST_LIO** | 激光惯性里程计 | 查找激光与惯性融合实现 | [仓库](https://github.com/hku-mars/FAST_LIO) |
| **FAST-LIVO2** | 激光惯性视觉里程计 | 查找激光、惯性与视觉融合实现 | [仓库](https://github.com/hku-mars/FAST-LIVO2) |
| **R3LIVE** | 激光惯性视觉融合 | 查看多传感器状态估计与地图构建 | [仓库](https://github.com/hku-mars/r3live) |
| **宇树科技 4D LiDAR SLAM** | 特定传感器适配 | 查找 Unitree 激光雷达相关定位实现 | [仓库](https://github.com/unitreerobotics/point_lio_unilidar) |
| **Cartographer** | SLAM 系统 | 查看二维或三维定位建图与 ROS 集成 | [项目页 / 文档](https://google-cartographer-ros.readthedocs.io/) |
| **RTAB-Map** | SLAM 系统 | 查看回环检测、地图构建与多传感器配置 | [项目页 / 文档](https://introlab.github.io/rtabmap/) |

<a id="calibration-sensors"></a>

## **标定与传感器**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **Kalibr** | 多传感器标定 | 查看相机和相机/IMU 标定流程 | [仓库](https://github.com/ethz-asl/kalibr) |
| **AprilTag** | 视觉标记检测 | 查看标记检测及位姿估计实现 | [仓库](https://github.com/AprilRobotics/apriltag) |
| **小觅双目相机系列** | 传感器 SDK | 查看双目相机驱动与数据接口 | [仓库](https://github.com/slightech/MYNT-EYE-S-SDK) |

<a id="image-pointcloud"></a>

## **图像与点云处理**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **OpenCV** | 图像与视觉工具库 | 查找图像处理、特征与几何计算接口 | [项目页 / 文档](https://opencv.org/) |
| **Open3D** | 三维数据处理库 | 查找点云、配准和重建接口 | [项目页 / 文档](https://www.open3d.org) |
| **PCL (Point Cloud Library)** | 点云处理库 | 查找点云滤波、分割与几何处理接口 | [项目页 / 文档](https://pointclouds.org/) |

<a id="grasp-perception"></a>

## **抓取感知**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **AnyGrasp** | 抓取检测 SDK | 查看抓取位姿检测接口及示例；SDK 使用条件以项目说明为准 | [仓库](https://github.com/graspnet/anygrasp_sdk) |

<a id="navigation-reference"></a>

## **导航系统与参考资料**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **Nav2 (Navigation2)** | 导航系统 | ROS 2 中的定位、规划与执行工作流；需结合传感器输入和地图配置 | [仓库](https://github.com/ros-navigation/navigation2) |
| **视觉SLAM十四讲** | 教材与配套代码 | 学习视觉 SLAM 的基础方法与实现 | [仓库](https://github.com/gaoxiang12/slambook2) |

## **补充与维护**

新增条目请提供名称、类型、用途和官方入口。代码、权重、数据分别以原项目的开放说明和许可证为准；只有论文或官网的条目不等于已经公开代码。发现失效链接或分类错误，可提交 [Issue](https://github.com/Octoday-Hub/Embodied-AI/issues) 或 [PR](https://github.com/Octoday-Hub/Embodied-AI/pulls)。

