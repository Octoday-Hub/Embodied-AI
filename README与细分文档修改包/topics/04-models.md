# **具身模型与策略实现**

[返回工具与项目导航](04-tools.md#toc) · [学习与训练](04-learning.md) · [SLAM 与感知](04-perception.md)

本页按模型的主要输出分类：动作策略、感知与推理、系统集成。训练框架和数据采集工具见学习与训练页；数据集入口见[数据集目录](06-datasets.md#索引)。

[动作策略与模型](#action-models) · [感知与推理模型](#perception-models) · [系统与论文](#systems-papers)

<a id="action-models"></a>

## **动作策略与模型**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **OpenVLA** | VLA 模型 | 视觉与语言条件下的机器人操作，查找推理、微调与评测代码 | [仓库](https://github.com/openvla/openvla) |
| **Octo** | 通用机器人策略 | 查找策略推理、微调和跨机器人数据使用方法 | [仓库](https://github.com/octo-models/octo) |
| **Diffusion Policy** | 策略方法与实现 | 学习如何用扩散模型生成机器人动作序列 | [仓库](https://github.com/real-stanford/diffusion_policy) |
| **VLA-Adapter** | VLA 适配方法 | 查找 VLA 适配与训练实现 | [仓库](https://github.com/OpenHelix-Team/VLA-Adapter) |
| **XR-1** | 具身模型项目 | 查找模型说明、推理代码及配套资源 | [仓库](https://github.com/Open-X-Humanoid/XR-1) |
| **DexVLA** | VLA 模型 | 查找机器人操作的模型训练与推理实现 | [仓库](https://github.com/juruobenruo/DexVLA) |
| **ManiFoundation** | 操作模型 | 查找机器人操作与接触建模的模型实现 | [仓库](https://github.com/NUS-LinS-Lab/ManiFM) |
| **WholebodyVLA** | 全身控制模型 | 查找人形机器人移动操作的模型实现 | [仓库](https://github.com/OpenDriveLab/WholebodyVLA) |
| **X-VLA** | 跨本体 VLA 模型 | 查找多种机器人形态下的操作策略实现 | [仓库](https://github.com/2toinf/X-VLA) |
| **RoboticsDiffusionTransformer (RDT-1B)** | 扩散策略模型 | 查找双臂机器人操作的训练与推理实现 | [仓库](https://github.com/thu-ml/RoboticsDiffusionTransformer) |
| **面壁智能 MiniCPM-RobotManip** | 操作模型 | 查找 MiniCPM-Robot 中的操作模型与使用说明 | [仓库](https://github.com/OpenBMB/MiniCPM-Robot) |
| **GR-1 (ByteDance Model)** | 机器人操作模型 | 查找视觉与语言条件下的动作预测实现；与同名机器人硬件区分 | [仓库](https://github.com/bytedance/GR-1) |

<a id="perception-models"></a>

## **感知与推理模型**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **LLaVA-OneVision** | 通用视觉语言模型 | 图像与视频理解相关实现；不等同于可直接控制机器人的动作策略 | [仓库](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision) |
| **Otter** | 通用多模态模型 | 多模态指令理解与上下文学习相关实现 | [仓库](https://github.com/EvolvingLMMs-Lab/Otter) |
| **RoboBrain 2.5** | 具身感知与推理模型 | 查找空间理解与具身任务推理相关实现 | [仓库](https://github.com/FlagOpen/RoboBrain2.5) |
| **面壁智能 MiniCPM-RobotTrack** | 视觉跟踪模型 | 查找视觉指令跟踪相关实现 | [仓库](https://github.com/OpenBMB/MiniCPM-Robot) |

<a id="systems-papers"></a>

## **系统集成与相关论文**

| **资源** | **类型** | **用途与使用说明** | **官方入口** |
| :--- | :--- | :--- | :--- |
| **OK-Robot** | 系统集成 | 查看感知、导航和操作模块的组合方式；不是单个可替换的模型权重 | [项目页 / 文档](https://ok-robot.github.io/) |
| **Dexterity-BEV** | 相关论文 | 查看论文中的方法与实验；原索引仅提供论文入口，代码开放状态需另查 | [论文](https://arxiv.org/abs/2606.02274) |

## **补充与维护**

新增条目请提供名称、类型、用途和官方入口。代码、权重、数据分别以原项目的开放说明和许可证为准；只有论文或官网的条目不等于已经公开代码。发现失效链接或分类错误，可提交 [Issue](https://github.com/Octoday-Hub/Embodied-AI/issues) 或 [PR](https://github.com/Octoday-Hub/Embodied-AI/pulls)。

