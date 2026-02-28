# 基础知识 - 入门指南

欢迎来到具身智能的世界！无论你是学生、研究员，还是工程师，这个板块旨在为你提供清晰的学习路径和核心概念参考。

## 📚 推荐书籍
从经典理论到前沿实践，以下书籍是构建知识体系的基石：

| 书名 | 作者 | 简介 | 推荐理由 |
| :--- | :--- | :--- | :--- |
| **《机器人学导论》** | John J. Craig | 机器人学经典教材，涵盖空间描述、运动学、动力学、轨迹规划等。 | 理解机器人底层几何与运动关系的必读书。 |
| **《强化学习（第2版）》** | Richard S. Sutton | 强化学习领域的圣经，包含基础算法到深度强化学习的完整理论。 | 掌握智能体通过交互学习决策的核心范式。 |
| **《计算机视觉：模型、学习和推理》** | Simon J.D. Prince | 系统介绍计算机视觉的概率模型与机器学习方法。 | 为具身智能处理视觉输入提供扎实的数学基础。 |
| **《Probabilistic Robotics》** | Sebastian Thrun 等 | 详细阐述机器人定位、地图构建（SLAM）等核心问题的概率方法。 | 处理真实世界不确定性的关键技术参考。 |
| **《Deep Learning》** | Ian Goodfellow 等 | 深度学习领域奠基性著作，涵盖基础理论和主流模型。 | 构建视觉、语言等感知模块的必备知识。 |

> **建议阅读顺序**：初学者可先读《机器人学导论》建立空间概念，再结合《强化学习》和《Deep Learning》理解智能体的学习机制。

## 🎓 在线课程
顶尖大学的公开课是快速入门的最佳途径：

*   **CS223A：Introduction to Robotics（斯坦福大学）**
    *   **讲师**：Oussama Khatib
    *   **内容**：涵盖机器人运动学、动力学、控制等核心基础。
    *   **链接**：[斯坦福官网课程主页](https://see.stanford.edu/Course/CS223A) (含视频和讲义)

*   **CS285：Deep Reinforcement Learning（UC Berkeley）**
    *   **讲师**：Sergey Levine
    *   **内容**：深度强化学习的前沿课程，涵盖从基础算法（DQN， PPO）到进阶主题（元学习、多智能体）。
    *   **链接**：[课程主页](http://rail.eecs.berkeley.edu/deeprlcourse/) (包含Slides和视频)

*   **MIT 6.S191：Introduction to Deep Learning（MIT）**
    *   **讲师**：Alexander Amini 等
    *   **内容**：深度学习快速入门课程，涵盖RNN、Transformers、生成模型等。
    *   **链接**：[课程官网](http://introtodeeplearning.com/) (提供视频和代码实验)

*   **Robot Perception（University of Pennsylvania）**
    *   **讲师**：Kostas Daniilidis 等
    *   **内容**：侧重于机器人如何通过视觉、深度传感器感知和理解环境。
    *   **链接**：[Coursera专项课程](https://www.coursera.org/specializations/robotics) (需搜索Perception模块)

*   **【中文】动手学强化学习**
    *   **作者**：张伟楠、俞勇等（上海交通大学）
    *   **内容**：理论结合代码实践，非常适合入门。
    *   **链接**：[书籍配套代码及教程](https://github.com/boyu-ai/Hands-on-RL)

## 📖 核心术语表
理解这些关键词，能帮你更快地阅读论文和交流：

*   **具身智能 (Embodied AI / Embodied Intelligence)**
    *   强调智能不仅存在于算法中，更通过物理身体与环境的实时交互来产生和体现。核心是“身体-环境-大脑”的闭环。

*   **Sim2Real (Simulation to Reality)**
    *   将在仿真环境（如MuJoCo、Isaac Sim）中训练得到的策略（Policy），迁移应用到真实物理世界的过程。核心挑战是“仿真到现实的鸿沟”。

*   **VLA模型 (Vision-Language-Action Model)**
    *   一种多模态大模型，能够直接接收视觉和语言指令，并输出机器人的底层动作指令。是当前具身智能的研究热点，如Google的RT-2、清华的Chip等。

*   **Imitation Learning (IL， 模仿学习)**
    *   通过模仿专家的示教数据（如人类遥操作的数据）来学习策略。常用方法包括行为克隆（Behavioral Cloning）。

*   **Reinforcement Learning (RL， 强化学习)**
    *   智能体通过与环境交互，根据获得的奖励信号来学习最大化累积奖励的最优策略。

*   **感知-规划-控制 (Perception-Planning-Control)**
    *   机器人系统的经典三层架构。**感知**理解环境，**规划**决策运动路径，**控制**执行具体动作。

*   **Scene Representation (场景表示)**
    *   机器人如何内部表示和理解环境，例如通过语义地图、占据栅格（Occupancy Grid）、隐式神经表示（NeRF）等。

*   **Manipulation (操作)**
    *   指机器人（特别是机械臂）对物体进行的精细操作，如抓取、放置、组装等。

*   **Locomotion (移动)**
    *   指机器人（如双足、四足机器人）在环境中移动自身的方式。

*   **Simulation Environment (仿真环境)**
    *   用于训练和测试算法的虚拟物理世界，常见的有：**MuJoCo**、**Isaac Sim**、**PyBullet**、**SAPIEN**、**Habitat** 等。

## 🧭 学习路径建议
1.  **筑基期**：通过CS223A掌握机器人学基础，通过MIT 6.S191掌握深度学习基础。
2.  **核心期**：深入学习CS285理解强化学习，同时阅读《Probabilistic Robotics》理解状态估计。
3.  **实践期**：选择一个仿真环境（推荐Isaac Sim或MuJoCo），尝试复现一篇经典论文（如DQN、PPO在机器人控制上的应用）。
4.  **前沿期**：关注顶级会议（CoRL， RSS， ICRA， IROS）的最新论文，特别是VLA、Sim2Real、灵巧操作等方向。
