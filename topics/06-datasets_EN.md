# Embodied AI Dataset Catalog

> Embodied AI scaling relies on large-scale real-world physical interaction data. This catalog collects the world's major open-source/commercial datasets covering manipulation, navigation, teleoperation, and simulation, helping you quickly locate training resources.

- [📦 Manipulation & Grasping Datasets](#manipulation-datasets)
- [🏠 Home & Mobile Manipulation Datasets](#mobile-datasets)
- [🔄 Teleoperation & Data Collection](#teleop-datasets)
- [🎮 Simulation & Synthetic Datasets](#sim-datasets)
- [📊 Multimodal & Tactile Datasets](#multimodal-datasets)

<a id="manipulation-datasets" name="manipulation-datasets"></a>

## 📦 Manipulation & Grasping Datasets

- **Open X-Embodiment (OXE)** — [`robotics-transformer-x.github.io`](https://robotics-transformer-x.github.io/)
  📄 Built by Google DeepMind with 33 partners: 1M+ trajectories across 22+ robot embodiments, CC-BY/Apache 2.0, the pretraining foundation for RT-1/RT-2 class VLA models.

- **AgiBot World Colosseo** — [`github.com/OpenDriveLab/AgiBot-World`](https://github.com/OpenDriveLab/AgiBot-World)
  📄 By AgiBot + Shanghai AI Lab + National Innovation Center: 1M+ trajectories (~2,976 hours), 217 tasks, 87 atomic skills, 3,000+ objects, 106 real scenes across home/retail/industry/restaurant/office, the first large-scale dataset with failure-recovery data.

- **AgiBot World 2026 (Diverse Interaction)** — [`agibot.com`](https://www.agibot.com/)
  📄 Phase-2 open-source release that deliberately retains failure data for world-model training; backed by a 4,000 m² data factory with 1:1 digital-twin scenes, releasing real + simulation data together.

- **DROID** — [`droid-dataset.github.io`](https://droid-dataset.github.io/)
  📄 Stanford/Berkeley/Google + 13 North American labs: ~76,000 trajectories, 564 scenes, 86 tasks on standardized Franka Panda, CC-BY 4.0, a common benchmark for behavior cloning and RLHF.

- **BridgeData V2** — [`rail.eecs.berkeley.edu`](https://rail.eecs.berkeley.edu/)
  📄 UC Berkeley & Stanford: ~60,000 demos across 70+ task categories on WidowX arms, CC-BY 4.0, a standard fine-tuning baseline for VLA models.

- **RoboSet** — [`huggingface.co`](https://huggingface.co/)
  📄 IIT Delhi et al.: multi-task kitchen manipulation data (Franka Panda) with RGB-D and language annotations for language-conditioned policy evaluation.

- **RH20T** — [`rh20t.github.io`](https://rh20t.github.io/)
  📄 Multi-institution (CN/EU): 110,000+ contact-rich manipulation trajectories with synchronized proprioception, RGB, depth, tactile, and audio streams, CC-BY-NC 4.0.

- **RoboMIND** — [`x-humanoid-robomind.github.io`](https://x-humanoid-robomind.github.io/)
  📄 Jointly released by Beijing Humanoid Robot Innovation Center and Peking University (RSS 2025); V2.0 contains 310K+ high-quality demo trajectories (1,000+ hours), 759 tasks across 11 core scenes, 6 robot embodiments, plus 12K+ tactile-augmented trajectories and Isaac Sim digital-twin assets.

- **Xiaomi-Robotics-1 Dataset** — [`robotics.xiaomi.com`](https://robotics.xiaomi.com/)
  📄 Xiaomi: 100,000+ hours of real-world manipulation trajectories collected via UMI devices with a scalable auto-labeling pipeline, powering a VLA model that hits 57.6% on RoboCasa365.

- **Qwen-RobotManip Corpus** — [`github.com/QwenLM/Qwen-RobotManip`](https://github.com/QwenLM/Qwen-RobotManip)
  📄 Alibaba Qwen team: ~38,100 hours of pretraining corpus built from open-source data plus a human-to-robot synthesis pipeline across 15 platforms.

- **MolmoAct2-BimanualYAM** — [`allenai.org`](https://allenai.org/)
  📄 By AllenAI (May 2026): 720 hours of bimanual teleoperation trajectories (largest open-source bimanual dataset), covering 8 real-robot tasks including cup stacking, test-tube tidying, tool hanging, and cup organizing.

- **Daimon-Infinity** — [`dmrobot.com`](https://www.dmrobot.com/)
  📄 By Daimon Robotics with Google DeepMind, China Mobile, NUS, HKUST, PKU, THU et al.: the world's largest all-modal physical world dataset with tactile sensing; self-developed 110K sensing units, 120Hz visuo-tactile sensors; 10,000 hours open-sourced; pretraining on it needs only 1/10 data to significantly boost fine-manipulation success.

- **PhysInOne** — [`vlar-group.github.io/PhysInOne.html`](https://vlar-group.github.io/PhysInOne.html)
  📄 By vLAR Group (HK PolyU) + Meta (CVPR 2026, arXiv 2604.09415): a unified visual-physical learning dataset with 2M multi-view videos, 150K+ dynamic 3D scenes, 71 basic physical phenomena, and 3,284 composite physical activities, providing standardized benchmarks for world models, video generation, and physical reasoning.

- **Unitree unifolm-wbt-dataset** — [`github.com/unitreerobotics`](https://github.com/unitreerobotics)
  📄 By Unitree: whole-body teleoperation real-robot data supporting whole-body control (WBC) and mobile manipulation training.

- **NeoData (NeoteAI × Fudan)** — [`research.neoteai.com`](https://research.neoteai.com)
  📄 By NeoteAI with Fudan University's Trusted Embodied AI Research Institute (N0-Foundation technical report, Jul 2026): 30,000+ hours of visuo-tactile interaction data (~1.4M segments, 3.3B timesteps, 8B RGB frames and 10B tactile frames), covering 450 real long-horizon tasks, 5,000 hours open-sourced, with the NeoForce unified tactile representation model.

<a id="mobile-datasets" name="mobile-datasets"></a>

## 🏠 Home & Mobile Manipulation Datasets

- **BEHAVIOR-1K** — [`behavior.stanford.edu`](https://behavior.stanford.edu/)
  📄 Stanford benchmark with 1,000 everyday household activities, built on the SAPIEN engine.

- **RoboCasa** — [`robocasa.ai`](https://robocasa.ai/)
  📄 Large-scale simulation framework and dataset for everyday household manipulation with diverse scenes and objects.

- **LIBERO** — [`libero-project.github.io`](https://libero-project.github.io/)
  📄 Long-horizon manipulation learning benchmark with 4 task suites and simulation data, a mainstream VLA evaluation suite.

- **CALVIN** — [`github.com/mees/calvin`](https://github.com/mees/calvin)
  📄 Long-horizon language-conditioned manipulation benchmark with 34+ hours of interaction data.

- **RoboTwin 2.0** — [`github.com/RoboTwin-Platform/RoboTwin`](https://github.com/RoboTwin-Platform/RoboTwin)
  📄 Data generation and benchmark platform for bimanual manipulation emphasizing strong domain randomization and standardized evaluation.

- **EgoInfinity** — [`arxiv.org/abs/2606.17385`](https://arxiv.org/abs/2606.17385)
  📄 Automatically generates 4D hand-object interaction data from internet videos for any-view retargeting and video-to-action learning.

<a id="teleop-datasets" name="teleop-datasets"></a>

## 🔄 Teleoperation & Data Collection

- **UMI (Universal Manipulation Interface)** — [`github.com/real-stanford/universal_manipulation_interface`](https://github.com/real-stanford/universal_manipulation_interface)
  📄 Stanford hand-held data collection tool for low-cost high-quality dexterous manipulation data with cross-embodiment transfer.

- **ALOHA** — [`tonyzhaozh.github.io/aloha`](https://tonyzhaozh.github.io/aloha/)
  📄 Low-cost bimanual teleoperation platform for imitation learning, spawning the Mobile ALOHA line of work.

- **RoboPocket** — [`noematrix.ai`](https://www.noematrix.ai/)
  📄 Equinox's hardware-agnostic data collection system (released at WAIC 2026), managing nearly 10,000 entries/day without teleoperation dependency.

- **EgoGuide** — [`arxiv.org/abs/2606.14665`](https://arxiv.org/abs/2606.14665)
  📄 Synchronizes wrist/head views with online visual-geometric quality guidance for efficient robot-free demonstration collection.

- **Human-as-Humanoid** — [`arxiv.org/abs/2606.32009`](https://arxiv.org/abs/2606.32009)
  📄 Converts large-scale human demonstration videos into executable action supervision for high-DoF humanoids, enabling zero-shot learning.

<a id="sim-datasets" name="sim-datasets"></a>

## 🎮 Simulation & Synthetic Datasets

- **NVIDIA Cosmos** — [`nvidia.com/cosmos`](https://www.nvidia.com/cosmos/)
  📄 World foundation model platform generating photorealistic robot interaction videos from text/images, used as a data augmentation layer to close the visual sim-to-real gap.

- **DexVerse (KWAISEM)** — [`dexforce.com`](https://www.dexforce.com/)
  📄 Generative simulation engine (released at WAIC 2026) with self-developed physics and real-time multi-physics simulation, having accumulated 70TB+ of robot factory data.

- **RoboSnap** — [`arxiv.org/abs/2607.06699`](https://arxiv.org/abs/2607.06699)
  📄 One-shot real-to-sim scene generation converting a single RGB image into physically stable, visually realistic trainable scenes.

- **Actuator Reality Shaping** — [`arxiv.org/abs/2607.02205`](https://arxiv.org/abs/2607.02205)
  📄 Paradigm that matches physical actuators with ideal reference dynamics in simulation for zero-shot sim-to-real transfer.

- **GRUtopia** — [`github.com/OpenRobotLab/GRUtopia`](https://github.com/OpenRobotLab/GRUtopia)
  📄 Shanghai AI Lab's general embodied simulation platform with massive interactive scenes and data.

<a id="multimodal-datasets" name="multimodal-datasets"></a>

## 📊 Multimodal & Tactile Datasets

- **Wh0 (World model Hand-Object)** — [`arxiv.org/abs/2606.22136`](https://arxiv.org/abs/2606.22136)
  📄 Uses generative world models as scalable sources of egocentric human hand manipulation data, bridging the human-robot data gap.

- **H-Tac** — [`arxiv.org/abs/2607.01067`](https://arxiv.org/abs/2607.01067)
  📄 Large-scale tactile-action dataset unifying tactile and action spaces for transferable tactile pretraining.

- **OpenLoong Dataset** — [`github.com/loongOpen`](https://github.com/loongOpen)
  📄 Data system accompanying Shanghai Humanoid Innovation Center's full-stack open-source project, covering large-scale skill scheduling for humanoids.

- **MOBILE-ALOHA Dataset** — [`mobile-aloha.github.io`](https://mobile-aloha.github.io/)
  📄 Stanford Mobile ALOHA companion dataset with bimanual mobile manipulation demos (cooking shrimp, wiping tables, pushing chairs), a classic benchmark for mobile manipulation imitation learning.

- **Dobb·E** — [`dobb-e.com`](https://dobb-e.com/)
  📄 NYU home manipulation dataset collected by non-expert users with a hand-held tool, covering folding clothes, tidying toys, and other real home scenes.

- **RLBench** — [`github.com/stepjam/RLBench`](https://github.com/stepjam/RLBench)
  📄 Large-scale vision-guided manipulation benchmark and data-generation environment with 100+ tasks and multi-stage procedural generation for RL/IL/multi-task evaluation.

- **Meta-World** — [`metaworld.farama.org`](https://metaworld.farama.org/)
  📄 Classic manipulation benchmark with 50 tasks, commonly used for multi-task learning and meta-RL evaluation.

- **Adroit** — [`openai.com/index/learning-dexterity`](https://openai.com/index/learning-dexterity/)
  📄 OpenAI dexterous hand manipulation dataset (Door/Hammer/Pen/Relocate) paired with human demos and RL training, a classic benchmark for dexterous-hand research.

- **Franka Kitchen** — [`github.com/google-research/relay-policy-learning`](https://github.com/google-research/relay-policy-learning)
  📄 Kitchen multi-skill dataset paired with Relay Policy Learning (RPL) and Implicit Behavior Cloning (IBC).

- **RoboTwin 2.0** — [`github.com/RoboTwin-Platform/RoboTwin`](https://github.com/RoboTwin-Platform/RoboTwin)
  📄 Data generation and benchmark platform for bimanual manipulation emphasizing strong domain randomization and standardized evaluation.

---

*Data updated: July 31, 2026*
*Scale and license terms are subject to each dataset's official repository*
