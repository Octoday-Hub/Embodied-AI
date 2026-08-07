# 具身智能数据集目录

> 具身智能的 Scaling Law 依赖大规模真实物理世界数据。本目录汇总全球主流开源/商用数据集，涵盖操作、导航、遥操作、仿真合成等类型，帮助你快速定位训练数据资源。

- [📦 操作与抓取数据集](#manipulation-datasets)
- [🏠 家庭与移动操作数据集](#mobile-datasets)
- [🔄 遥操作与数据采集](#teleop-datasets)
- [🎮 仿真合成数据集](#sim-datasets)
- [📊 多模态与触觉数据集](#multimodal-datasets)

<a id="manipulation-datasets" name="manipulation-datasets"></a>

## 📦 操作与抓取数据集

- **Open X-Embodiment (OXE)** — [`robotics-transformer-x.github.io`](https://robotics-transformer-x.github.io/)
  📄 Google DeepMind 联合 33 家机构构建，100 万+ 条轨迹、22+ 种机器人形态，CC-BY/Apache 2.0 许可，是 RT-1/RT-2 等 VLA 模型的预训练基石。

- **AgiBot World Colosseo** — [`github.com/OpenDriveLab/AgiBot-World`](https://github.com/OpenDriveLab/AgiBot-World)
  📄 智元机器人 + 上海AI Lab + 国家地方共建人形机器人创新中心发布，100 万+ 条轨迹（约 2,976 小时）、217 个任务、87 种原子技能、3,000+ 物体、106 个真实场景，覆盖家庭/零售/工业/餐饮/办公五大域，首个含失败恢复数据的大规模数据集。

- **AgiBot World 2026 (多样交互)** — [`agibot.com`](https://www.agibot.com/)
  📄 2026 第二期开源，主动保留失败数据，面向世界模型训练；基于 4,000 平方米数据采集工厂，数字孪生 1:1 重建真实场景，真实+仿真数据同步开源。

- **DROID** — [`droid-dataset.github.io`](https://droid-dataset.github.io/)
  📄 斯坦福/UC Berkeley/谷歌等 13 个北美实验室，约 76,000 条轨迹、564 个场景、86 项任务，统一 Franka Panda 硬件，CC-BY 4.0，行为克隆与 RLHF 常用基准。

- **BridgeData V2** — [`rail.eecs.berkeley.edu`](https://rail.eecs.berkeley.edu/)
  📄 UC Berkeley 与斯坦福，约 60,000 条演示、70+ 任务类别，WidowX 机械臂，CC-BY 4.0，VLA 微调常用基线。

- **RoboSet** — [`huggingface.co`](https://huggingface.co/)
  📄 IIT Delhi 等机构，多任务厨房操作数据（Franka Panda），含 RGB-D 与语言标注，用于语言条件策略评测。

- **RH20T** — [`rh20t.github.io`](https://rh20t.github.io/)
  📄 多机构（中/欧）构建，110,000+ 条接触丰富操作轨迹，同步机器人本体感知、RGB 视频、深度、触觉与音频多模态流，CC-BY-NC 4.0。

- **RoboMIND** — [`x-humanoid-robomind.github.io`](https://x-humanoid-robomind.github.io/)
  📄 北京人形机器人创新中心与北京大学联合推出（RSS 2025），V2.0 含 31 万+ 高质量演示轨迹（超 1,000 小时）、759 种任务、11 个核心场景，覆盖 6 种机器人本体，新增 1.2 万+ 条带触觉数据，配套 Isaac Sim 数字孪生仿真资产。

- **Xiaomi-Robotics-1 Dataset** — [`robotics.xiaomi.com`](https://robotics.xiaomi.com/)
  📄 小米发布，100,000+ 小时真实操作轨迹（UMI 设备采集），配套可扩展自动标注管线，训练出 RoboCasa365 达 57.6% 的 VLA 基础模型。

- **Qwen-RobotManip Corpus** — [`github.com/QwenLM/Qwen-RobotManip`](https://github.com/QwenLM/Qwen-RobotManip)
  📄 通义团队，纯开源数据+人类视频合成管线，构建约 38,100 小时预训练语料，覆盖 15 个平台。

- **MolmoAct2-BimanualYAM** — [`allenai.org`](https://allenai.org/)
  📄 AllenAI 推出（2026年5月），720 小时双手遥操作轨迹数据（当前开源最大），覆盖叠杯子、收纳试管、挂工具、整理杯子等 8 种真实机器人任务。

- **Daimon-Infinity** — [`dmrobot.com`](https://www.dmrobot.com/)
  📄 戴盟机器人联合 Google DeepMind、中国移动、新加坡国立大学、港科大、北大、清华等发布，全球最大规模含触觉全模态物理世界数据集；自研 11 万感知单元、120Hz 视触觉传感器，开源 10,000 小时数据，预训练后仅需 1/10 数据量即可显著提升精细操作成功率。

- **PhysInOne** — [`vlar-group.github.io/PhysInOne.html`](https://vlar-group.github.io/PhysInOne.html)
  📄 vLAR Group（香港理工）+ Meta 发布（CVPR 2026，arXiv 2604.09415），面向视觉-物理联合学习与推理的统一数据集：200 万条多视角视频、15 万+ 动态 3D 场景、71 种基础物理现象与 3,284 种复合物理活动，为世界模型/视频生成/物理推理提供标准化基准。

- **Unitree unifolm-wbt-dataset** — [`github.com/unitreerobotics`](https://github.com/unitreerobotics)
  📄 宇树科技发布，主打全身遥操作真机数据，支撑全身控制（WBC）与移动操作训练。

- **NeoData (NeoteAI × 复旦)** — [`research.neoteai.com`](https://research.neoteai.com)
  📄 新智具身（NeoteAI）联合复旦可信具身智能研究院发布（N0-Foundation 技术报告，2026年7月），超 3 万小时视觉-触觉交互操作数据（约 140 万条片段、33 亿时间步、80 亿帧 RGB 与 100 亿帧触觉图像），覆盖 450 项真实长程任务，已开源 5,000 小时，配套 NeoForce 统一触觉表征模型。

<a id="mobile-datasets" name="mobile-datasets"></a>

## 🏠 家庭与移动操作数据集

- **BEHAVIOR-1K** — [`behavior.stanford.edu`](https://behavior.stanford.edu/)
  📄 斯坦福 1,000 种日常活动具身基准与仿真数据集，SAPIEN 引擎构建。

- **RoboCasa** — [`robocasa.ai`](https://robocasa.ai/)
  📄 面向日常家居操作的大规模仿真框架与数据集，支持多场景、多对象与示教数据。

- **LIBERO** — [`libero-project.github.io`](https://libero-project.github.io/)
  📄 面向长时程操作的学习基准，含 4 个任务套件与仿真数据，VLA 评测主流基准。

- **CALVIN** — [`github.com/mees/calvin`](https://github.com/mees/calvin)
  📄 长时程语言条件操作基准，提供 34 小时以上交互数据。

- **RoboTwin 2.0** — [`github.com/RoboTwin-Platform/RoboTwin`](https://github.com/RoboTwin-Platform/RoboTwin)
  📄 面向双臂操作的数据生成与基准平台，强调强 domain randomization、规模化生成与标准化评测。

- **EgoInfinity** — [`arxiv.org/abs/2606.17385`](https://arxiv.org/abs/2606.17385)
  📄 从互联网视频自动生成 4D 手物交互数据，实现任意视角重定向与视频到动作学习。

<a id="teleop-datasets" name="teleop-datasets"></a>

## 🔄 遥操作与数据采集

- **UMI (Universal Manipulation Interface)** — [`github.com/real-stanford/universal_manipulation_interface`](https://github.com/real-stanford/universal_manipulation_interface)
  📄 斯坦福手持式数据采集工具，低成本采集高质量灵巧操作数据，跨本体迁移至真实机器人。

- **ALOHA** — [`tonyzhaozh.github.io/aloha`](https://tonyzhaozh.github.io/aloha/)
  📄 低成本双臂遥操作平台，支持模仿学习，催生了 Mobile ALOHA 等系列工作。

- **RoboPocket** — [`noematrix.ai`](https://www.noematrix.ai/)
  📄 穹彻智能无本体数据采集系统（WAIC 2026 发布），单日可管理近万条数据，摆脱遥操作依赖。

- **EgoGuide** — [`arxiv.org/abs/2606.14665`](https://arxiv.org/abs/2606.14665)
  📄 通过同步腕部/头部视角与在线视觉-几何质量引导，实现无机器人演示数据高效采集。

- **Human-as-Humanoid** — [`arxiv.org/abs/2606.32009`](https://arxiv.org/abs/2606.32009)
  📄 将大规模人类演示视频转化为高自由度人形机器人的可执行动作监督，实现零样本学习。

<a id="sim-datasets" name="sim-datasets"></a>

## 🎮 仿真合成数据集

- **NVIDIA Cosmos** — [`nvidia.com/cosmos`](https://www.nvidia.com/cosmos/)
  📄 世界基础模型平台，从文本/图像生成逼真机器人交互视频，作为数据增强层弥合视觉 Sim2Real 差距。

- **DexVerse (跨维智能)** — [`dexforce.com`](https://www.dexforce.com/)
  📄 跨维智能生成式仿真引擎（WAIC 2026 发布），自研物理引擎+实时多物理场仿真，已沉淀超 70TB 机器人工厂数据。

- **RoboSnap** — [`arxiv.org/abs/2607.06699`](https://arxiv.org/abs/2607.06699)
  📄 一次性 Real-to-Sim 场景生成，单张 RGB 图像转物理稳定、视觉逼真的可训练场景。

- **Actuator Reality Shaping** — [`arxiv.org/abs/2607.02205`](https://arxiv.org/abs/2607.02205)
  📄 执行器现实塑造范式，匹配物理执行器与仿真参考动力学，实现零样本 Sim2Real。

- **GRUtopia** — [`github.com/OpenRobotLab/GRUtopia`](https://github.com/OpenRobotLab/GRUtopia)
  📄 上海AI Lab 通用具身仿真平台，提供海量高质量可交互场景与数据。

<a id="multimodal-datasets" name="multimodal-datasets"></a>

## 📊 多模态与触觉数据集

- **Wh0 (World model Hand-Object)** — [`arxiv.org/abs/2606.22136`](https://arxiv.org/abs/2606.22136)
  📄 利用生成式世界模型作为可扩展的自我中心人手操作数据源，弥合人手-机器人数据鸿沟。

- **H-Tac** — [`arxiv.org/abs/2607.01067`](https://arxiv.org/abs/2607.01067)
  📄 大规模触觉-动作数据集，统一触觉与动作空间，支撑可迁移触觉预训练。

- **OpenLoong 数据集** — [`github.com/loongOpen`](https://github.com/loongOpen)
  📄 上海人形机器人创新中心全栈开源项目附带的数据体系，覆盖人形机器人大规模技能调度。

- **MOBILE-ALOHA 数据集** — [`mobile-aloha.github.io`](https://mobile-aloha.github.io/)
  📄 斯坦福 Mobile ALOHA 配套数据集，双臂移动操作演示数据（煮虾、擦拭桌面、推椅子等），是移动操作模仿学习的经典基准。

- **Dobb·E** — [`dobb-e.com`](https://dobb-e.com/)
  📄 NYU 家庭操作数据集，非专家用户在家中用单手工具采集，覆盖折叠衣物、收纳玩具等真实家庭场景。

- **RLBench** — [`github.com/stepjam/RLBench`](https://github.com/stepjam/RLBench)
  📄 大规模视觉引导机器人操作基准与数据生成环境，100+ 任务、多阶段程序生成，支持 RL/IL/多任务评测。

- **Meta-World** — [`metaworld.farama.org`](https://metaworld.farama.org/)
  📄 经典操作 benchmark，50 个操作任务，常用于多任务学习与 meta-RL 评测。

- **Adroit** — [`openai.com/index/learning-dexterity`](https://openai.com/index/learning-dexterity/)
  📄 OpenAI 灵巧手操作数据集（Door/Hammer/Pen/Relocate），配合人类演示与 RL 训练，灵巧手研究经典基准。

- **Franka Kitchen** — [`github.com/google-research/relay-policy-learning`](https://github.com/google-research/relay-policy-learning)
  📄 家居厨房多技能数据集，配合 Relay Policy Learning（RPL）与 Implicit Behavior Cloning（IBC）训练。

- **RoboTwin 2.0** — [`github.com/RoboTwin-Platform/RoboTwin`](https://github.com/RoboTwin-Platform/RoboTwin)
  📄 面向双臂操作的数据生成与基准平台，强调强 domain randomization、规模化生成与标准化评测。

---

*数据更新日期：2026年7月31日*
*数据规模与许可条款以各数据集官方仓库为准*
