# **机器人学习、训练与数据采集**

[返回工具与项目导航](04-tools.md#toc) · [模型与策略](04-models.md) · [数据集目录](06-datasets.md#索引)

按工作环节查找：先选模型与任务，再选择训练框架、采集工具和评测环境。遥操作工具负责采集，仿真平台负责环境，二者都不等同于训练算法。

[学习框架](#frameworks) · [机器人训练实现](#robot-training) · [采集与遥操作](#data-collection) · [数据生成与评测](#generation-evaluation) · [推理与相关资料](#inference-reference)

<a id="frameworks"></a>

## **学习框架**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **LeRobot** | 采集、训练与部署工具链 | 查找数据记录、策略训练和机器人部署流程 | [官方仓库](https://github.com/huggingface/lerobot) · [文档](https://huggingface.co/docs/lerobot/main/en/index) |
| **robomimic** | 示教学习框架 | 查找示教数据格式、算法基线和离线训练流程 | [仓库](https://github.com/ARISE-Initiative/robomimic) |
| **RLinf** | 强化学习基础设施 | 查找分布式训练、采样和模型更新流程 | [仓库](https://github.com/RLinf/RLinf) |
| **AllenAct** | 具身任务训练框架 | 查找任务配置和具身环境中的学习算法 | [项目页 / 文档](https://allenact.org/) |
| **Habitat-Lab** | 任务与训练库 | 配置导航等任务，并连接 Habitat 仿真环境 | [仓库](https://github.com/facebookresearch/habitat-lab) |
| **NVIDIA Isaac Lab** | 机器人学习框架 | 查找机器人任务配置与仿真训练工作流 | [项目页 / 文档](https://developer.nvidia.com/isaac/lab) |
| **Unity ML-Agents** | 仿真智能体训练工具 | 查找 Unity 环境中的训练接口与示例 | [仓库](https://github.com/Unity-Technologies/ml-agents) |

<a id="robot-training"></a>

## **机器人训练实现**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **unitree_rl_gym** | 机器人强化学习 | 基于 Isaac Gym 的机器人运动策略训练 | [仓库](https://github.com/unitreerobotics/unitree_rl_gym) |
| **unitree_rl_lab** | 机器人强化学习 | 查找基于 Isaac Lab 与 MuJoCo 相关环境的训练实现 | [IsaacLab](https://github.com/unitreerobotics/unitree_rl_lab) · [MuJoCo](https://github.com/unitreerobotics/unitree_rl_mjlab) |
| **unitree_IL_lerobot** | 机器人模仿学习 | 查找 Unitree 双臂与 LeRobot 结合的训练流程 | [仓库](https://github.com/unitreerobotics/unitree_IL_lerobot) |
| **Humanoid-Gym** | 人形机器人训练 | 查找人形运动策略训练与迁移实现 | [仓库](https://github.com/roboterax/humanoid-gym) |
| **Booster Gym** | 机器人训练项目入口 | 查找 Booster 相关训练资源；原链接为组织主页，需要进一步选择仓库 | [组织主页](https://github.com/BoosterRobotics) |
| **OpenLoong (Brain)** | 控制与训练项目入口 | 查找 OpenLoong 的控制与训练资源；原链接为组织主页，硬件入口仍见机器人项目 | [组织主页](https://github.com/loongOpen) |

<a id="data-collection"></a>

## **采集与遥操作**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **Universal Manipulation Interface (UMI)** | 手持采集接口 | 查找采集硬件、数据处理和策略使用流程 | [仓库](https://github.com/real-stanford/universal_manipulation_interface) |
| **Open-TeleVision** | 遥操作系统 | 查找机器人双臂遥操作的系统实现 | [仓库](https://github.com/OpenTeleVision/TeleVision) |
| **宇树科技 XR 遥操作** | XR 遥操作 | 查找机器人遥操作与数据采集实现 | [仓库](https://github.com/unitreerobotics/xr_teleoperate) |
| **DexCap** | 动作采集系统 | 查看灵巧操作的数据采集流程 | [项目页 / 文档](https://dex-cap.github.io/) |
| **Dobb-E** | 采集与学习方案 | 查看采集硬件、示教数据和策略训练的配合方式 | [项目页 / 文档](https://dobb-e.com/) |

<a id="generation-evaluation"></a>

## **数据生成与评测环境**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **MimicGen** | 示教数据生成 | 从已有示教扩展机器人操作训练数据 | [仓库](https://github.com/NVlabs/mimicgen) |
| **RoboTwin 2.0** | 数据生成与评测 | 查找双臂任务的数据生成和评测流程 | [仓库](https://github.com/RoboTwin-Platform/RoboTwin) |
| **Meta-World** | 操作任务基准 | 进行多任务操作策略训练与评测 | [项目页 / 文档](https://metaworld.farama.org/) |
| **VIMA** | 多模态任务基准 | 查找多模态指令操作任务与相关资源 | [项目页 / 文档](https://vimalabs.github.io/) |
| **AgiBot-World** | 数据与配套学习资源 | 查看操作数据及其配套资源；数据下载与开放范围见项目说明 | [仓库](https://github.com/OpenDriveLab/AgiBot-World) |

更多仿真平台见[仿真平台](04-tools.md#simulation-platforms)。更多训练数据见[数据集目录](06-datasets.md#索引)。

<a id="inference-reference"></a>

## **推理工具与相关资料**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **面壁智能 PhyAI 推理框架** | 推理工具 | 查找 MiniCPM-Robot 中的推理与执行相关实现 | [仓库](https://github.com/OpenBMB/MiniCPM-Robot) |
| **OpenR1-Multimodal** | 通用多模态强化学习研究 | 查看多模态模型的推理与强化学习方法；不是机器人运动控制训练框架 | [仓库](https://github.com/EvolvingLMMs-Lab/open-r1-multimodal) |
| **every-embodied** | 教程 | 学习 VLA 与机器人学习相关实践 | [仓库](https://github.com/datawhalechina/every-embodied) |
| **宇树科技机器人控制教程** | 教程 | 查找机器人控制学习材料与示例 | [仓库](https://github.com/unitreerobotics/unitree_guide) |

## **补充与维护**

新增条目请提供名称、类型、用途和官方入口。代码、权重、数据分别以原项目的开放说明和许可证为准；只有论文或官网的条目不等于已经公开代码。发现失效链接或分类错误，可提交 [Issue](https://github.com/Octoday-Hub/Embodied-AI/issues) 或 [PR](https://github.com/Octoday-Hub/Embodied-AI/pulls)。

