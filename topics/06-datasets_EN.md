# Embodied AI Datasets

> Six representative datasets covering real-world collection, cross-embodiment aggregation, RGB-D / force / tactile sensing, tabletop manipulation, simulation benchmarks, and automated data generation. Statistics follow official pages, repositories, and papers.

---

### Index

| Dataset | Positioning | Type | Scale | Key modalities | Official homepage |
|---|---|---|---|---|---|
| [DROID](#droid) | Large-scale in-the-wild teleoperated manipulation from 13 North American labs | Real-world collection | ~76k trajectories / 564 scenes | RGB + proprioception + language | [Homepage](https://droid-dataset.github.io/) |
| [Open X-Embodiment / RT-X](#open-x-embodiment--rt-x) | Aggregation of real robot datasets from 21 institutions | Real-world + aggregated | 1M+ trajectories / 22 embodiments | RGB + language | [Homepage](https://robotics-transformer-x.github.io/) |
| [RH20T](#rh20t) | Contact-rich manipulation with force / tactile / audio modalities | Real-world collection | 110k+ sequences / 147 tasks | RGB-D + force + tactile + audio | [Homepage](https://rh20t.github.io/) |
| [BridgeData V2](#bridgedata-v2) | Tabletop manipulation via VR teleoperation | Real-world collection | 60k trajectories / 24 environments | RGB-D + language | [Homepage](https://rail-berkeley.github.io/bridgedata/) |
| [LIBERO](#libero) | Simulation benchmark for lifelong robot learning / knowledge transfer | Simulation + demonstrations | 130 tasks / 4 suites | Sim RGB + language | [Homepage](https://libero-project.github.io/) |
| [MimicGen](#mimicgen) | Automated large-scale simulation data from few human demos | Simulation + generation | 50k+ trajectories / 18 tasks | Sim RGB + robot state | [Homepage](https://mimicgen.github.io/) |

---

### DROID

[Homepage](https://droid-dataset.github.io/) · [Download](https://droid-dataset.github.io/droid/the-droid-dataset) · [Paper](https://arxiv.org/abs/2403.12945) · [Sample](#droid-sample)

<a id="droid-sample"></a>

<div align="center">
  <img src="datasets-img/droid-sample-01.jpg" alt="DROID official Dataset Visualizer" height="520">
</div>

<table>
<tbody>
<tr><td rowspan="4">Overview</td><td>Dataset Visualizer</td><td>The [official interactive viewer](https://droid-dataset.github.io/visualizer/) — randomly samples 1000 trajectories with real-time filtering and browsing across Scene, Object, and Task dimensions.</td></tr>
<tr><td>Source</td><td>13 North American labs led by Stanford / UC Berkeley / Google, unified on the Franka Panda robot hardware.</td></tr>
<tr><td>Recommendations</td><td>In-the-wild robot manipulation across scenes, institutions, and tasks. Spans 8 indoor scene categories (industrial office, kitchen, office, living room, bedroom, bathroom, hallway, laundry room). A common benchmark for behavior cloning and RLHF. DROID is designed to let the research community collect large-scale real interaction data beyond the lab.</td></tr>
<tr><td>Use</td><td><ul><li><strong>Download</strong>: The full RLDS release is ~1.7 TB, accessed via <code>gsutil</code> commands on Google Cloud Storage (<code>gs://gresearch/robotics/</code>); the documentation page lists per-file commands. Raw stereo HD video (~8.7 TB) and the <code>droid_100</code> debugging subset (~2 GB, ~100 episodes) are also available;</li><li><strong>Example code</strong>: The official <a href="https://colab.research.google.com/drive/1b4PPH4XGht4Jve2xPKMCh-AXXAQziNQa?usp=sharing">Dataset Colab</a> loads and visualizes a small number of episodes;</li><li><strong>Schema docs</strong>: <a href="https://droid-dataset.github.io/droid/the-droid-dataset">The DROID Dataset</a>.</li></ul></td></tr>
<tr><td rowspan="3">Design</td><td>Collection</td><td>Human-in-the-loop robot teleoperation across diverse scenes, with face blurring before release.</td></tr>
<tr><td>Scale distribution</td><td>~76,000 trajectories / 350 hours of interaction / 564 scenes / 52 buildings / 86 tasks / 18 robots / 13 institutions / 50 data collectors.</td></tr>
<tr><td>Modalities</td><td><ul><li><strong>Vision</strong>: Three ZED stereo RGB cameras, including 1 wrist and 2 exterior cameras; the raw release contains monocular videos, concatenated stereo videos, and SVO files. The RLDS release exposes left-view RGB image fields with an example schema size of 180×320×3; the raw release is high-definition</li><li><strong>Proprioception</strong>: joint position (7D), Cartesian position (6D), gripper position; the raw <code>trajectory.h5</code> files contain action and proprioceptive trajectories</li><li><strong>Actions and control</strong>: gripper position / velocity, Cartesian position / velocity, joint position / velocity; the RLDS <code>action</code> example is 7D, composed of joint velocity and gripper position</li><li><strong>Force</strong>: None</li><li><strong>Tactile</strong>: None</li><li><strong>Other</strong>: Natural-language task instructions and alternative instruction fields</li></ul></td></tr>
</tbody>
</table>

---

### Open X-Embodiment / RT-X

[Homepage](https://robotics-transformer-x.github.io/) · [Download](https://github.com/google-deepmind/open_x_embodiment) · [Paper](https://arxiv.org/abs/2310.08864) · [Sample](#open-x-sample)

<a id="open-x-sample"></a>

<div align="center">
  <img src="datasets-img/open-x-embodiment-sample-01.jpg" alt="Open X-Embodiment collection overview" height="520">
</div>

<table>
<tbody>
<tr><td rowspan="4">Overview</td><td>Dataset Visualizer</td><td>The [official homepage](https://robotics-transformer-x.github.io/) carries representative videos across 60 contributing datasets and 22 embodiments, plus RT-1 / RT-2 task demos.</td></tr>
<tr><td>Source</td><td>An aggregation of real robot datasets by Google DeepMind and 21 collaborating institutions.</td></tr>
<tr><td>Recommendations</td><td>A unified training set across 22 robot embodiments (single-arm, bimanual, quadruped, etc.); the pretraining foundation for RT-1 / RT-2 class VLA models; provides the data basis for "one model, many embodiments".</td></tr>
<tr><td>Use</td><td><ul><li><strong>Download and load</strong>: Provided through TensorFlow Datasets (TFDS). The Dataset Access section of the <a href="https://github.com/google-deepmind/open_x_embodiment">google-deepmind/open_x_embodiment</a> repository lists the <code>tfds.load</code> names and commands for each contributing dataset; datasets are downloaded individually;</li><li><strong>Metadata</strong>: The official dataset spreadsheet records the source, license, citation, and field description of every contributing dataset (linked from the repository README).</li></ul></td></tr>
<tr><td rowspan="3">Design</td><td>Collection</td><td>Aggregation of public real-robot datasets from 21 institutions, unified into the RLDS episode format.</td></tr>
<tr><td>Scale distribution</td><td>&gt;1,000,000 real robot trajectories / 22 embodiments / 527 skills / 160,266 tasks / 60 datasets / 1,798 attributes / 5,228 objects / 23,486 spatial relations.</td></tr>
<tr><td>Modalities</td><td><ul><li><strong>Vision</strong>: Workspace RGB images from single-arm / bimanual / quadruped robots, one of the unified inputs; the contributing datasets also include demonstration videos</li><li><strong>Proprioception</strong>: None</li><li><strong>Actions and control</strong>: RLDS episode sequences; action spaces and control frequencies are inherited from each contributing dataset</li><li><strong>Force</strong>: None</li><li><strong>Tactile</strong>: None</li><li><strong>Other</strong>: Natural-language task strings / task labels (one of the unified inputs); metadata includes robot state and scene descriptions</li></ul></td></tr>
</tbody>
</table>

---

### RH20T

[Homepage](https://rh20t.github.io/) · [Download](https://rh20t.github.io/#download) · [Paper](https://arxiv.org/abs/2307.00595) · [Sample](#rh20t-sample)

<a id="rh20t-sample"></a>

<div align="center">
  <img src="datasets-img/rh20t-sample-01.jpg" alt="RH20T teleoperation data collection platform" height="520">
</div>

<table>
<tbody>
<tr><td rowspan="4">Overview</td><td>Dataset Visualizer</td><td>The [official homepage](https://rh20t.github.io/) showcases 110k+ contact-rich manipulation sequences, multiple robot configurations, and paired human demonstration videos.</td></tr>
<tr><td>Source</td><td>Shanghai Jiao Tong University (Cewu Lu's group / MVIG Lab).</td></tr>
<tr><td>Recommendations</td><td>A real-world manipulation dataset emphasizing contact-rich interaction and multi-modal perception; every robot sequence is paired with a corresponding human demonstration video and a language description, targeting one-shot imitation research; covers complex skills such as cutting, plugging, pouring, folding, and rotating that require visual and force / tactile perception together.</td></tr>
<tr><td>Use</td><td><ul><li><strong>Download</strong>: The raw data is ~40 TB; a 640×360 resized version is also provided (~5 TB RGB, ~10 TB RGBD). Data is split into seven hardware configurations (Cfg1–Cfg7), available via the Google Drive / Baidu Cloud links on the homepage;</li><li><strong>Parsing</strong>: The official <a href="https://github.com/rh20t/rh20t_api">rh20t_api</a> package parses the data (per-config robot info in <code>configs/configs.json</code>).</li></ul></td></tr>
<tr><td rowspan="3">Design</td><td>Collection</td><td>The robot is equipped with a force / torque sensor and teleoperated via a haptic device with force rendering for precise, efficient collection suited to contact-rich interaction; a corresponding human demonstration video is recorded for each sequence.</td></tr>
<tr><td>Scale distribution</td><td>110,000+ contact-rich manipulation sequences / 147 tasks (48 from RLBench, 29 from MetaWorld, 70 self-proposed) / 7 hardware configurations / 4 robot arms (Flexiv, UR5, Franka, Kuka) / 50M+ image frames / 110k+ paired human demonstration videos.</td></tr>
<tr><td>Modalities</td><td><ul><li><strong>Vision</strong>: 8–10 global RGB-D cameras plus 1–2 in-hand cameras per configuration; includes RGB, depth, and binocular IR images</li><li><strong>Proprioception</strong>: joint angle / joint torque, gripper state, end-effector (EE) pose</li><li><strong>Actions and control</strong>: 6–7 DoF joint + gripper; EE / gripper Cartesian pose is also provided</li><li><strong>Force</strong>: 6-DoF force-torque</li><li><strong>Tactile</strong>: fingertip tactile (Cfg7 only)</li><li><strong>Other</strong>: audio; each sequence has a language description and a paired human demonstration video</li></ul></td></tr>
</tbody>
</table>

---

### BridgeData V2

[Homepage](https://rail-berkeley.github.io/bridgedata/) · [Download](https://rail.eecs.berkeley.edu/datasets/bridge_release/data/) · [Paper](https://arxiv.org/abs/2308.12952) · [Sample](#bridgedata-sample)

<a id="bridgedata-sample"></a>

<div align="center">
  <img src="datasets-img/bridgedata-v2-sample-01.jpg" alt="BridgeData V2 task collage overview" height="520">
</div>

<table>
<tbody>
<tr><td rowspan="4">Overview</td><td>Dataset Visualizer</td><td>The [official homepage](https://rail-berkeley.github.io/bridgedata/) offers a "Sample" button to draw a random trajectory, showing its initial / final states with the corresponding natural-language annotation.</td></tr>
<tr><td>Source</td><td>UC Berkeley RAIL Lab (Sergey Levine's group).</td></tr>
<tr><td>Recommendations</td><td>Collected on the low-cost, easy-to-source WidowX 250 platform (hardware ~$4,000), so other institutions can reproduce it; each trajectory carries a crowdsourced post-hoc natural-language instruction, supporting goal-conditioned, language-conditioned, imitation-learning, and offline-RL methods; a common real-world fine-tuning benchmark for VLAs such as OpenVLA and Octo, and a major contributor to the Open X-Embodiment mix.</td></tr>
<tr><td>Use</td><td><ul><li><strong>Download</strong>: The raw data is provided as NumPy shards (~400 GB), with teleoperated demonstrations and scripted-policy data in separate zips; an RLDS copy can also be streamed from the Open X-Embodiment GCS bucket (<code>gs://gresearch/robotics</code>);</li><li><strong>Training code</strong>: The official <a href="https://github.com/rail-berkeley/bridge_data_v2">rail-berkeley/bridge_data_v2</a> provides training / evaluation code and pretrained weights.</li></ul></td></tr>
<tr><td rowspan="3">Design</td><td>Collection</td><td>Collected by teleoperating a WidowX 250 6-DoF arm with a VR controller at 5 Hz control frequency, averaging ~38 timesteps per trajectory; camera poses, objects, and workspace positions are randomized roughly every 50 trajectories for generalization; a portion is autonomously collected by a scripted pick-and-place policy; task labels are crowdsourced post-hoc natural-language annotations.</td></tr>
<tr><td>Scale distribution</td><td>60,096 trajectories (50,365 teleoperated demonstrations + 9,731 scripted-policy rollouts) / 13 skills / 24 environments / 100+ objects; image resolution 640×480.</td></tr>
<tr><td>Modalities</td><td><ul><li><strong>Vision</strong>: 1 fixed over-the-shoulder RGB-D camera + 2 randomized-pose RGB cameras + 1 wrist RGB camera; resolution 640×480</li><li><strong>Proprioception</strong>: robot state / gripper state</li><li><strong>Actions and control</strong>: WidowX 250 6-DoF actions at 5 Hz; each trajectory provides an initial observation, a goal state (image or text), and an action sequence</li><li><strong>Force</strong>: None</li><li><strong>Tactile</strong>: None</li><li><strong>Other</strong>: each trajectory carries a crowdsourced post-hoc natural-language instruction</li></ul></td></tr>
</tbody>
</table>

---

### LIBERO

[Homepage](https://libero-project.github.io/) · [Download](https://libero-project.github.io/datasets) · [Paper](https://arxiv.org/abs/2306.03310) · [Sample](#libero-sample)

<a id="libero-sample"></a>

<div align="center">
  <img src="datasets-img/libero-sample-01.jpg" alt="LIBERO task suites overview" height="520">
</div>

<table>
<tbody>
<tr><td rowspan="4">Overview</td><td>Dataset Visualizer</td><td>The [official homepage](https://libero-project.github.io/) presents representative tasks from the four task suites and the lifelong-learning benchmark description.</td></tr>
<tr><td>Source</td><td>The University of Texas at Austin and collaborators (authors include Yuke Zhu and Peter Stone).</td></tr>
<tr><td>Recommendations</td><td>A simulation benchmark for lifelong robot learning / knowledge transfer; provides a procedural generation pipeline that can in principle create infinitely many tasks; the four suites separately probe distribution shifts in objects, spatial layout, and task goals, plus their mixture — suited to systematic study of transferring declarative and procedural knowledge.</td></tr>
<tr><td>Use</td><td><ul><li><strong>Download</strong>: The official script <code>benchmark_scripts/download_libero_datasets.py</code> downloads human-teleoperated demonstrations for all four suites; use <code>--datasets</code> to select a specific suite, or <code>--use-huggingface</code> to download from the HuggingFace mirror;</li><li><strong>Environment</strong>: Built on MuJoCo simulation and requires Linux; simulation assets are auto-loaded from the HuggingFace Hub (<code>lerobot/libero-assets</code>) and cached locally.</li></ul></td></tr>
<tr><td rowspan="3">Design</td><td>Collection</td><td>Tasks are created by a procedural generation pipeline, and high-quality human-teleoperated demonstrations are provided for all 130 tasks.</td></tr>
<tr><td>Scale distribution</td><td>130 language-conditioned manipulation tasks in four suites: LIBERO-Spatial (10), LIBERO-Object (10), LIBERO-Goal (10), and LIBERO-100 (100, further split into LIBERO-90 for pretraining + LIBERO-10 for long-horizon testing).</td></tr>
<tr><td>Modalities</td><td><ul><li><strong>Vision</strong>: Simulation-rendered RGB images (example camera resolution 128×128)</li><li><strong>Proprioception</strong>: robot state / gripper state</li><li><strong>Actions and control</strong>: 7-D actions (joint + gripper); MuJoCo-based OffScreenRenderEnv stepping</li><li><strong>Force</strong>: None</li><li><strong>Tactile</strong>: None</li><li><strong>Other</strong>: each task is language-conditioned; BDDL task-definition files</li></ul></td></tr>
</tbody>
</table>

---

### MimicGen

[Homepage](https://mimicgen.github.io/) · [Download](https://github.com/NVlabs/mimicgen) · [Paper](https://arxiv.org/abs/2310.17596) · [Sample](#mimicgen-sample)

<a id="mimicgen-sample"></a>

<div align="center">
  <img src="datasets-img/mimicgen-sample-01.jpg" alt="MimicGen data generation system overview" height="520">
</div>

<table>
<tbody>
<tr><td rowspan="4">Overview</td><td>Dataset Visualizer</td><td>The [official homepage](https://mimicgen.github.io/) visualizes generated trajectories per task, task reset distributions, and side-by-side comparisons from source human demos to generated data.</td></tr>
<tr><td>Source</td><td>NVIDIA and The University of Texas at Austin (authors include Ajay Mandlekar, Yuke Zhu, and Dieter Fox).</td></tr>
<tr><td>Recommendations</td><td>Essentially a data-generation system rather than a plain dataset: it decomposes human demos into object-centric subtask segments, re-anchors them to new scenes / object poses, and replays them in simulation to auto-scale large datasets from few demos; targets long-horizon and high-precision (millimeter-level) contact tasks and is simulator-agnostic (robosuite/MuJoCo, Isaac Gym); follow-on work such as LIBERO and RoboCasa adopts its approach to extend benchmarks.</td></tr>
<tr><td>Use</td><td><ul><li><strong>Download</strong>: The pre-generated datasets are HDF5 files in standard robomimic format (~60 GB), fetched via the official <code>download_datasets.py</code>;</li><li><strong>Generate your own</strong>: <code>generate_dataset.py</code> starts from a few source demos, runs subtask decomposition, object-pose resampling, simulation replay, and success filtering to produce new HDF5 files; code at <a href="https://github.com/NVlabs/mimicgen">NVlabs/mimicgen</a> (depends on robomimic + robosuite).</li></ul></td></tr>
<tr><td rowspan="3">Design</td><td>Collection</td><td>Automated data generation: starting from ~200 human teleoperated demos, it spatially transforms object-centric subtask segments, replays and stitches them in simulation, and filters for success — roughly 250x amplification.</td></tr>
<tr><td>Scale distribution</td><td>50,000+ generated trajectories / 18 tasks / multiple robots (Franka Panda, Sawyer, UR5e, bimanual Panda) / multiple simulators; ~200 source human demonstrations.</td></tr>
<tr><td>Modalities</td><td><ul><li><strong>Vision</strong>: Simulation-rendered RGB (agent view + wrist view)</li><li><strong>Proprioception</strong>: low-dimensional robot state, object poses</li><li><strong>Actions and control</strong>: standard robomimic action format; includes subtask segmentation information</li><li><strong>Force</strong>: None</li><li><strong>Tactile</strong>: None</li><li><strong>Other</strong>: task reset distributions; generated trajectories are amplified from source demonstrations</li></ul></td></tr>
</tbody>
</table>