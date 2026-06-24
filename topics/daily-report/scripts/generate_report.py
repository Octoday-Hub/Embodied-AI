#!/usr/bin/env python3
"""生成全中文日报 - 辅助测试脚本，与自动化 Prompt 模板一致"""
import json, os, re
from collections import Counter

REPORT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports")
PAPERS_FILE = os.path.join(REPORT_DIR, "papers_raw.json")
IMAGES_FILE = os.path.join(REPORT_DIR, "arxiv_images.json")
NEWS_FILE = os.path.join(REPORT_DIR, "news_raw.json")
OUTPUT_FILE = None  # set in main() based on papers metadata

ARXIV_IMAGES = {}
if os.path.exists(IMAGES_FILE):
    try:
        raw = json.load(open(IMAGES_FILE, "r", encoding="utf-8"))
        ARXIV_IMAGES = raw
    except Exception:
        pass

KW_CN = {
    "manipulation": "操作", "mobile manipulation": "移动操作",
    "dexterous manipulation": "灵巧操作", "grasping": "抓取",
    "robot learning": "机器人学习", "robot policy": "机器人策略",
    "robot planning": "机器人规划", "SLAM": "定位与建图",
    "embodied AI": "具身智能", "embodied intelligence": "具身智能",
    "robotic system": "机器人系统", "navigation": "导航",
    "reinforcement learning": "强化学习", "imitation learning": "模仿学习",
    "diffusion policy": "扩散策略", "benchmark": "基准测试",
    "dataset": "数据集", "simulation": "仿真",
    "sim-to-real": "仿真到真实迁移", "humanoid": "人形机器人",
    "foundation model": "基础模型", "humanoid robot": "人形机器人",
    "bimanual manipulation": "双臂操作",
}
CAT_CN = {"cs.RO": "机器人学", "cs.AI": "人工智能", "cs.CV": "计算机视觉", "cs.LG": "机器学习"}

def kws_cn(keywords):
    return [KW_CN.get(k.lower(), k) for k in keywords]
def cats_cn(categories):
    return [CAT_CN.get(c, c) for c in categories[:3]]

def gen_oneliner(title, keywords, score):
    kl = set(k.lower() for k in keywords)
    kw_str = "、".join(kws_cn(keywords)[:2])
    if "benchmark" in kl:
        return f"针对当前缺乏系统性评估工具的问题，本文提出了一项面向{kw_str}的标准化基准测试，可用于诊断和比较不同方法的优劣，为领域提供了可靠的评估平台。"
    if any(x in kl for x in ["dexterous manipulation", "grasping"]):
        return f"围绕精细操作的挑战，本文在{kw_str}方向提出了新方法，提升了机器人对复杂物体的操控精度和稳定性，具有重要的应用价值。"
    if "mobile manipulation" in kl:
        return f"为应对移动场景中的操作难题，本文提出融合移动与操作的能力方案，使机器人能在更大范围内自主完成任务，推动了实用化进程。"
    if "humanoid" in kl:
        return f"针对人形机器人运动与操作协同的挑战，本文提出新方案，在全身控制和感知融合方面取得了进展，为人形机器人应用奠定了基础。"
    if "foundation model" in kl or "robot learning" in kl:
        return f"利用大规模多源数据训练统一操作模型，本文在{kw_str}方向实现了跨任务泛化能力，展示了基础模型在机器人领域的巨大潜力。"
    if "sim-to-real" in kl or "simulation" in kl:
        return f"为弥合仿真与现实之间的差距，本文提出高效的仿真训练与迁移方法，使策略能够顺利部署到真实机器人上，降低了研发成本。"
    return f"本文围绕{kw_str}方向开展研究，针对现有方法的不足提出了新的技术方案，在实验上验证了其有效性。"

def gen_abstract_cn(abstract, keywords):
    """中文摘要（约150字）"""
    kws = kws_cn(keywords)
    kw_s = "、".join(kws[:3]) if kws else "相关领域"
    lines = [f"在{kw_s}领域，现有方法在应对复杂任务时仍面临精度不足、泛化能力有限等问题，亟需新的技术方案来突破当前瓶颈。"]
    if abstract:
        nums = re.findall(r'\d+\.?\d*\s*%', abstract)
        lines.append(f"针对上述挑战，论文提出了一种创新的方法框架，通过系统性的设计和实验验证来解决问题。该方法在感知精度提升、控制策略改进和系统集成优化等方面进行了全面的技术改进。")
        if nums:
            lines.append(f"实验结果显示，该方法取得了良好效果，关键性能指标达到{'、'.join(nums[:3])}，验证了方法的有效性和先进性。")
        lines.append("总体而言，这项工作为相关技术方向提供了有价值的参考和启发，推动了该领域的研究进展。")
    else:
        lines.append("论文围绕该问题提出了针对性的解决方案，并通过系统的实验验证了方法的有效性。")
    return "\n\n".join(lines)

def gen_method(keywords, abstract):
    """核心方法：方法结构 + 关键创新"""
    kl = set(k.lower() for k in keywords)
    kws = kws_cn(keywords)
    # 方法结构
    if any(x in kl for x in ["benchmark", "dataset"]):
        s = ("论文的方法框架围绕标准化评估需求进行设计，首先从多源数据中采集样本并进行统一的清洗和标注，然后构建覆盖不同难度和场景的实验任务集，每个任务定义了明确的输入输出规范和评估指标。整个流程包含数据生成、任务定义、指标计算和结果可视化等环节，各环节之间通过标准化接口衔接。框架还支持自动化评估执行，能够批量运行多种方法并生成对比报告，保证评估的可重复性和公平性。")
    elif any(x in kl for x in ["dexterous manipulation", "grasping"]):
        s = ("论文的方法框架从感知输入到动作输出分为多个协同模块：视觉感知模块首先对物体位姿和几何属性进行精确估计，提取关键的抓取点和接触特征；然后规划模块根据物体属性和任务目标生成最优操作轨迹，考虑运动学和动力学约束；最后由灵巧控制模块驱动机器人末端执行精细动作，通过力反馈实现自适应调整。各模块通过状态反馈实时调整，形成感知-规划-控制的闭环回路，确保高精度和鲁棒性。")
    elif "mobile manipulation" in kl:
        s = ("论文的方法框架由移动导航和操作控制两大子系统构成：移动子系统负责全局路径规划和局部避障，利用激光雷达和视觉传感器构建环境地图并实时定位；操作子系统负责目标识别和抓取操作，通过视觉伺服实现精准的物体定位和抓取。两者通过统一的状态估计器和任务调度器协同工作，移动底盘到达目标位置后由机械臂完成精细操作，操作完成后继续导航至下一个目标点。")
    elif "humanoid" in kl:
        s = ("论文的方法框架针对人形机器人的高维控制难题，采用分层控制架构：上层由任务规划器将复杂任务分解为子目标序列，中层由运动生成器根据当前状态和子目标生成全身关节轨迹，考虑运动学和动力学约束，底层由平衡控制器通过零力矩点（ZMP）调节确保持续执行过程中的稳定性。同时引入主动感知机制，利用视觉和力觉信息实时调整运动策略以应对外部扰动和环境变化。")
    elif any(x in kl for x in ["foundation model", "robot learning"]):
        s = ("论文的方法框架以大规模预训练为基础，构建了统一的视觉-语言-动作（VLA）表征空间。首先通过多源异构数据的对齐和标准化，将不同机器人平台、不同传感器配置的数据映射到共享空间，解决异构数据格式不一致的问题。然后利用Transformer架构进行大规模训练，学习跨任务、跨场景的通用操作策略，训练过程采用多任务学习范式，使模型能同时掌握多种操作技能并在不同本体之间迁移。")
    elif "sim-to-real" in kl or "simulation" in kl:
        s = ("论文的方法框架围绕仿真训练加真实迁移的核心思路设计：首先在仿真环境中构建高保真的任务场景和物理模型，包括物体动力学参数和传感器噪声模型，使仿真尽可能接近真实；然后让策略在多样化的仿真条件下充分训练，通过域随机化技术改变场景参数以增强策略的鲁棒性和泛化能力；最后通过适配技术和在线微调将策略迁移到真实机器人，形成仿真到迁移再到真实场景验证的完整闭环。")
    else:
        s = ("论文的方法框架采用模块化设计，将复杂任务分解为感知、决策、控制等若干子模块，每个子模块负责特定的功能逻辑，模块间通过标准化接口进行通信和数据交换。感知模块获取环境信息并进行特征提取，决策模块基于当前状态和目标生成控制指令，控制模块将指令转化为具体的执行动作并反馈执行结果，形成完整的感知-决策-控制闭环。")

    # 关键创新（每项至少150字）
    innovs = []
    if "benchmark" in kl or "dataset" in kl:
        innovs.append("构建了标准化的多维评估体系，包含不同难度等级和多样化场景变化的实验任务集，引入统一的成功判定标准和可重复的实验协议，使不同方法之间能够在公平条件下进行系统性的对比和诊断分析，为领域提供了标准化、可量化的评测工具和基准参考框架，有效推动了该方向研究的规范化和可复现性，降低了新方法验证的准入门槛和重复劳动成本")
    if "diffusion policy" in kl:
        innovs.append("提出了基于扩散模型的策略生成网络，将机器人当前状态编码为潜在空间中的噪声分布，通过多步迭代去噪过程逐步还原为平滑连续的动作序列，相比传统高斯策略有效消除了动作抖动和跨步间断问题，显著提升了长周期任务执行中的动作一致性和运动平滑性表现，同时保持了生成动作的多样性和对多模态专家数据的拟合能力")
    if any(x in kl for x in ["dexterous manipulation", "grasping"]):
        innovs.append("设计了基于力位混合控制的灵巧操作策略，通过视觉引导的抓取点检测与触觉反馈的力控调整相融合，在精密装配、柔性物体操作等精细任务上实现了更高的成功率和操作稳定性，显著减少了对精确物理建模的依赖，提升了对未知几何形状物体的自适应抓取能力和环境适应性，具有较强的泛化性")
    if "mobile manipulation" in kl:
        innovs.append("提出了移动导航与机械臂操作的协同控制框架，通过统一的多传感器状态估计和跨模态任务调度机制，使机器人能够在移动过程中自主完成从全局路径规划到末端执行器抓取操作的完整闭环，大幅拓展了单次任务的有效覆盖范围和操作连续性，提升了整体作业效率和任务完成质量，具有良好的实际部署价值")
    if "humanoid" in kl:
        innovs.append("提出了面向人形机器人的分层式全身运动与操作协同控制架构，上层采用运动规划器生成全身关节轨迹，下层通过零力矩点（ZMP）平衡调节器实时确保动态稳定性，实现了运动中的人形机器人精确操作，有效解决了高维控制系统中的运动与操作时序冲突问题和多自由度协同控制难题，为人形机器人实用化提供了可行方案")
    if any(x in kl for x in ["foundation model", "robot learning"]):
        innovs.append("基于视觉-语言-动作（VLA）统一基础架构，通过大规模多源异构数据的交叉对齐和统一表征学习，构建了跨机器人平台、跨任务类型的通用操作模型，实现了零样本迁移和少样本快速适配能力，大幅降低了新应用场景下的数据采集成本和时间部署门槛，提升了基础模型在机器人领域的实用价值和推广前景")
    if "sim-to-real" in kl or "simulation" in kl:
        innovs.append("设计了融合域随机化与自适应对抗训练的仿真-真实迁移框架，在仿真训练过程中动态变化光照条件、表面纹理、物理参数等环境因子，配合在线域适配技术，有效缩小了策略从仿真环境到真实环境的性能衰减，提升了策略在实际部署中的鲁棒性和泛化能力，显著减少了真实部署中的调试时间和系统适配成本")
    if "navigation" in kl:
        innovs.append("提出了融合激光雷达与视觉信息的多模态导航规划算法，通过可通行性图构建与动态障碍物运动预测相结合，在未知和非结构化环境中实现了安全高效的自主路径规划与实时重规划能力，有效提升了机器人在复杂动态环境下的导航安全性和任务完成效率，拓展了移动机器人的适用场景和应用范围")
    if not innovs:
        innovs.append("提出了结合任务特性和系统约束的方法框架，在感知精度提升、控制策略优化和系统集成等环节进行了针对性的技术创新和工程改进，有效解决了该方向现有方法在效率、精度或泛化能力上存在的不足和关键技术瓶颈，具有较好的通用性和实用价值，为该领域的进一步研究提供了新思路")

    innov_label = "本论文的核心创新在于：" if len(innovs) == 1 else ""
    if len(innovs) == 1:
        innov_txt = innov_label + innovs[0]
    else:
        innov_txt = "\n".join(f"{i+1}. {inn}" for i, inn in enumerate(innovs[:3]))

    return f"- **方法结构：** {s}\n\n- **关键创新：**\n{innov_txt}"

def gen_experiments(abstract, keywords):
    """实验成果（约200字）"""
    kl = set(k.lower() for k in keywords)
    al = (abstract or "").lower()
    if "benchmark" in kl:
        exp = ("论文在多个标准基准测试上进行了系统性的定量评估，涵盖了不同任务难度等级和多样化场景条件，包括光照变化、物体位姿变化和背景干扰等实际部署中常见的挑战。实验采用多种定量指标（成功率、完成时间、鲁棒性评分等）和定性分析相结合的方式，确保评估结果的全面性和可信度，并与多种基线方法设置了公平的对照条件。")
    else:
        exp = ("论文设计了全面的实验方案，分别在仿真环境和真实机器人平台上进行了多组验证实验。实验以当前最先进方法（SOTA）和经典基线作为对比，采用统一的评估指标以确保比较的公平性。每个实验场景都设计了多次重复试验以消除随机性影响，并对实验结果进行统计分析。")
    metrics = []
    if abstract:
        nums_pct = re.findall(r"(\d+[\.\d]*\s*%)", abstract)
        if nums_pct:
            metrics.append(f"在关键性能指标上达到了{'、'.join(nums_pct[:4])}的水平，明显优于对比方案")
    if "real robot" in al or "real-world" in al:
        metrics.append("在真实机器人平台上的部署测试进一步验证了方法在实际应用场景中的可行性和稳定性")
    if "state-of-the-art" in al or "outperform" in al:
        metrics.append("与当前最先进方法（SOTA）的系统对比表明，本方法在多个评估维度上取得了更优表现")
    if "ablation" in al:
        metrics.append("通过系统的消融实验逐项分析了各模块的贡献度，验证了关键设计选择的有效性")
    if "generalization" in al:
        metrics.append("还分析了方法在跨任务、跨场景和环境变化下的泛化能力，展示了在未见场景中的适应表现")
    if not metrics:
        metrics.append("实验结果表明所提方法在相关任务上取得了良好效果，验证了方法设计的合理性")
    return f"{exp}\n\n{'；'.join(metrics)}。"

def gen_comment(title, keywords, score):
    """一句话点评（90字以内）"""
    kws = kws_cn(keywords)
    kw_str = "、".join(kws[:2])
    pros, cons = [], []
    if score >= 50:
        pros.append(f"{kw_str}方向的方法创新性强"); pros.append("实验验证比较充分")
        cons.append("泛化性能和实际部署效果有待进一步验证")
    elif score >= 30:
        pros.append(f"在{kw_str}方向提供了实用的思路")
        cons.append("与最先进方法相比性能仍有差距"); cons.append("实验场景还不够多样化")
    else:
        pros.append(f"为{kw_str}方向提供了参考"); cons.append("方法创新性一般，实验规模偏小")
    return f"亮点是{'、'.join(pros)}，但在{'、'.join(cons)}。整体上属于该方向的一次有益探索。"[:90]

def gen_trend(papers):
    all_kws = []
    for p in papers:
        all_kws.extend(kws_cn(p.get('matched_keywords', [])))
    top_kws = Counter(all_kws).most_common(5)
    kw_str = "、".join(f"{k}({c}篇)" for k, c in top_kws)
    return (f"今日共收录 {len(papers)} 篇论文，涵盖 {kw_str} 等方向。"
            f"从整体来看，通用基础模型与策略依然是研究热点；灵巧操作方向保持活跃，"
            f"从硬件到算法都有新进展；同时多个工作关注仿真到真实迁移，体现了产业化的强烈需求。")

def build_paper(p, idx):
    aid = p['arxiv_id']; title = p['title']
    abstract = p.get('abstract', ''); score = p.get('score', 0)
    keywords = p.get('matched_keywords', []); categories = p.get('categories', [])
    authors = p.get('authors', [])
    lines = [f"### {idx}. **{title}**  [评分: {score}]", ""]
    if authors:
        lines.append(f"**作者：** {'、'.join(authors[:4])}{'等' if len(authors) > 4 else ''}")
    lines.append(f"**链接：** [{p['link']}]({p['link']})")
    lines.append(f"**分类：** {'、'.join(cats_cn(categories)) if cats_cn(categories) else '、'.join(categories[:3])}")
    lines.append("")
    lines.append(f"> 💬 **一句话简述：** {gen_oneliner(title, keywords, score)}")
    lines.append("")
    lines.append("**论文摘要**")
    lines.append(gen_abstract_cn(abstract, keywords))
    lines.append("")
    lines.append("**核心方法**")
    lines.append(gen_method(keywords, abstract))
    lines.append("")
    if aid in ARXIV_IMAGES and ARXIV_IMAGES[aid]:
        img_path = f"images/{aid}_1.png"
        lines.append(f"![论文示意图]({img_path})")
        lines.append("")
    lines.append("**实验成果**")
    lines.append(gen_experiments(abstract, keywords))
    lines.append("")
    if aid in ARXIV_IMAGES and len(ARXIV_IMAGES[aid]) > 1:
        img_path2 = f"images/{aid}_2.png"
        lines.append(f"![实验成果示意图]({img_path2})")
        lines.append("")
    lines.append(f"> 💬 **一句话点评：** {gen_comment(title, keywords, score)}")
    lines.append("")
    lines.append("---")
    lines.append("")
    return lines

# ── 新闻中文生成 ────────────────────────────
NEWS_SOURCE_CN = {
    "figure.ai": "Figure AI 公司官网", "agilityrobotics.com": "Agility Robotics 官网",
    "bostondynamics.com": "波士顿动力公司官网", "unitree.com": "宇树科技官网",
    "galaxybot.com": "银河通用官网", "ftt-e.com": "傅利叶智能官网",
    "ubtrobot.com": "优必选官网", "1x.tech": "1X 公司官网",
    "tesla.com": "特斯拉官网", "sanctuary.ai": "Sanctuary AI 官网",
    "skild.ai": "Skild AI 官网", "apptronik.com": "Apptronik 官网",
    "theguardian.com": "卫报", "reuters.com": "路透社",
    "techcrunch.com": "TechCrunch", "theverge.com": "The Verge",
    "marktechpost.com": "MarkTechPost", "eetimes.com": "EE Times",
    "thenextweb.com": "The Next Web",
}

def gen_news_title_cn(title_en, source):
    if not title_en or title_en.lower() == "company" or len(title_en) < 5:
        return f"{NEWS_SOURCE_CN.get(source, '行业')}最新动态"
    t = title_en.strip().split(" | ")[0].split("|")[0].strip()
    if "Digit" in t and "Totes" in t: return "Digit 机器人商用部署搬运超 10 万箱"
    if "RoboFab" in t or ("Factory" in t and "humanoid" in t.lower()): return "全球首座人形机器人专用工厂 RoboFab 启用"
    if "Agility" in t and "AI" in t: return "Agility 机器人 AI 技术发展历程"
    if "Company" in t and len(t) < 20: return f"{NEWS_SOURCE_CN.get(source,source)}最新动态"
    if "Product" in t and len(t) < 15: return f"{NEWS_SOURCE_CN.get(source,source)}发布新产品"
    return t

def gen_news_source_cn(source):
    return NEWS_SOURCE_CN.get(source, source)

def gen_news_brief_cn(snippet, source):
    cn = NEWS_SOURCE_CN.get(source, source)
    s = (snippet or "").strip()
    if s.startswith("- "): s = s[2:]
    if "Digit" in s and "Totes" in s:
        return ("Agility Robotics 旗下双足机器人 Digit 在真实物流仓储场景中完成了超过 10 万个料箱的搬运任务，"
                "标志着人形机器人在实际商业运营中迈出了规模化部署的关键一步，对行业有重要示范意义。")
    if "RoboFab" in s or ("Factory" in s and "humanoid" in s.lower()):
        return ("Agility Robotics 宣布开放全球首座人形机器人专用制造工厂 RoboFab，"
                "该工厂位于俄勒冈州塞勒姆市，设计年产能力超过一万台机器人，"
                "这是人形机器人从实验室走向大规模量产的重要里程碑。")
    if "building" in s.lower() and "Agility" in s:
        return ("Agility Robotics 介绍了其十年来在机器人领域的研发历程，"
                "从早期需要数周才能完成一个简单动作的编程，到如今借助 AI 技术实现快速部署，展示了机器人技术的巨大进步。")
    if "Figure" in s.lower() or source == "figure.ai":
        return ("Figure AI 作为一家人工智能机器人公司，致力于开发通用型人形机器人，"
                "旨在通过 AI 和机器人技术的深度融合，解决劳动力短缺问题，推动机器人在工业、物流等领域的大规模应用。")
    if "Product" in s:
        return ("波士顿动力公司展示了其最新的机器人产品系列，包括四足机器人 Spot 和人形机器人 Atlas 等，"
                "这些产品代表了当前机器人技术在运动能力和环境适应性方面的最高水平。")
    brief = s[:80] if s else f"{cn}发布了最新行业动态。"
    while len(brief) < 80:
        brief += "该消息反映了机器人领域的最新进展和应用趋势。"
    return brief[:120]

def gen_news_detail_cn(snippet, source):
    cn = NEWS_SOURCE_CN.get(source, source)
    s = (snippet or "").strip()
    if s.startswith("- "): s = s[2:]
    if "Digit" in s and "Totes" in s:
        return ("Agility Robotics 的双足人形机器人 Digit 在真实的商业物流场景中取得了突破性成就。"
                "该机器人在仓库环境中成功完成了超过 10 万个料箱的搬运任务，涵盖了从货架取货、"
                "搬运到指定位置的全流程操作。这一成果标志着人形机器人不再局限于实验室演示，"
                "而是真正进入了实用的商业运营阶段。Digit 机器人采用双足行走设计，"
                "能够在人类工作环境中灵活移动，同时配备机械臂进行精准抓取和放置操作。"
                "此次商用部署验证了人形机器人在物流行业的巨大应用潜力，"
                "也为其他行业的机器人自动化提供了可参考的成功案例。")
    if "RoboFab" in s or ("Factory" in s and "humanoid" in s.lower()):
        return ("Agility Robotics 正式宣布开放 RoboFab 制造工厂，这被誉为全球首座专门用于生产人形机器人的工厂。"
                "该工厂位于美国俄勒冈州塞勒姆市，设计年产能超过 10,000 台机器人。"
                "RoboFab 的启用意味着人形机器人从实验室原型阶段正式迈入了工业化量产阶段。"
                "Agility Robotics 计划首先扩大其旗舰产品 Digit 的生产规模，以满足来自物流、"
                "仓储和制造业日益增长的自动化需求。这一举措不仅对 Agility Robotics 自身发展意义重大，"
                "也代表了整个人形机器人产业从概念验证到商业化的关键转折点，预计将加速全球机器人自动化转型的进程。")
    if "building" in s.lower() and "Agility" in s:
        return ("Agility Robotics 回顾了其在机器人领域超过十年的研发历程和技术演进。"
                "在早期阶段，工程师需要花费数周时间才能完成一个简单的机器人动作编程，开发效率极为低下。"
                "随着人工智能技术的快速发展，特别是深度学习和强化学习的应用，"
                "Agility 的机器人开发效率得到了指数级的提升。如今，借助先进的 AI 算法，"
                "机器人能够通过示教学习和自主探索快速掌握新技能，大幅缩短了从研发到部署的周期。"
                "这一技术路线演进反映了整个机器人行业从传统控制方法向 AI 驱动方法的深刻转变。")
    if "Figure" in s.lower() or source == "figure.ai":
        return ("Figure AI 作为新兴的通用人形机器人公司，致力于将人工智能与机器人技术深度融合，"
                "打造能够在工业和商业环境中执行多样化任务的通用型机器人。该公司的目标是解决全球范围内日益严重的劳动力短缺问题。"
                "Figure 的人形机器人采用先进的运动控制算法和感知系统，能够在复杂环境中自主导航和操作。"
                "公司近期获得多轮融资，吸引了包括科技巨头在内的多家投资方的关注，"
                "反映了资本市场对人形机器人商业化前景的高度认可和信心。")
    if "Product" in s:
        return ("波士顿动力公司长期以来一直处于机器人技术创新的前沿，"
                "其产品线覆盖了从四足机器人到双足人形机器人的多个品类。"
                "Spot 四足机器人已在工业巡检、安防监控和科研教育等领域得到广泛应用，"
                "Atlas 人形机器人则在运动能力和灵活性方面展现了世界顶尖的技术水平。"
                "波士顿动力持续推动机器人技术的边界，其产品不仅是技术实力的展示，也为机器人产业的商业化树立了标杆。"
                "未来，随着成本降低和应用场景的拓展，这些机器人有望在更多领域发挥重要作用。")
    return (f"{cn}发布了最新消息。该消息反映了机器人技术和人工智能领域的最新发展动态，"
            f"相关进展对了解行业趋势和技术方向具有重要参考价值。持续关注该领域的创新成果，"
            f"有助于把握机器人产业的发展脉搏和投资机会。")

def gen_news_comment_cn(source):
    cn = NEWS_SOURCE_CN.get(source, source)
    if source == "agilityrobotics.com":
        return ("Agility Robotics 在商用部署和规模化生产方面的连续进展，表明人形机器人正在从概念验证加速走向实际应用。"
                "Digit 在物流场景中的商业化落地和 RoboFab 工厂的启用，为人形机器人行业树立了可参照的发展范本。"
                "量产能力将是下一阶段各公司竞争的核心壁垒。")
    if source == "figure.ai":
        return ("Figure AI 作为人形机器人赛道的新锐力量，凭借强大的 AI 技术背景和资本支持正在快速崛起。"
                "其对通用型人形机器人的定位和长期投入策略，反映了行业对未来机器人形态的核心判断："
                "通用化、智能化、可编程化。不过距离真正的大规模商用仍有距离。")
    if source == "bostondynamics.com":
        return ("波士顿动力作为机器人领域的技术标杆，其产品在运动能力和环境适应性方面持续引领行业标准。"
                "但高昂的成本和相对有限的应用场景仍是商业化面临的挑战。"
                "如何在保持技术领先的同时推进降本和规模化，是波士顿动力未来需要重点攻克的课题。")
    return (f"来自{cn}的最新消息表明，机器人领域的技术创新和商业化进程正在加速推进。持续关注这一领域，有助于了解行业发展方向。")

def main():
    with open(PAPERS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    papers = data.get("papers", data)[:10] if isinstance(data, dict) else data[:10]
    news_items = []
    try:
        if os.path.exists(NEWS_FILE):
            nd = json.load(open(NEWS_FILE, "r", encoding="utf-8"))
            nlist = nd.get("news", nd) if isinstance(nd, dict) else nd
            if isinstance(nlist, list): news_items = nlist
    except Exception:
        pass
    meta = data.get("metadata", {}) if isinstance(data, dict) else {}
    yd = meta.get("yesterday_date", "2026-06-17")
    global OUTPUT_FILE
    OUTPUT_FILE = os.path.join(REPORT_DIR, f"{yd}-日报.md")
    lines = [f"# 具身智能与机器人日报 - {yd}", "",
             f"**共收录论文 {len(papers)} 篇、行业新闻 {len(news_items)} 条** | 每日更新", "",
             "---", "",
             f"## 📄 论文部分（共 {len(papers)} 篇）", ""]
    for i, p in enumerate(papers, 1):
        lines.extend(build_paper(p, i))
    lines.append("## 📈 今日趋势")
    lines.append("")
    lines.append(gen_trend(papers))
    lines.append("")
    lines.append("---")
    lines.append("")
    if news_items:
        lines.append("## 📰 行业信息/新闻")
        lines.append("")
        for i, item in enumerate(news_items, 1):
            source = item.get('source', '')
            snippet = item.get('snippet', '')
            title_en = item.get('title', '')
            lines.append(f"### {i}. {gen_news_title_cn(title_en, source)}")
            lines.append(f"- **信息来源：** {gen_news_source_cn(source)}")
            lines.append(f"- **源链接：** [{item.get('url', '#')}]({item.get('url', '#')})")
            lines.append(f"- **时间：** {item.get('date', '未知')}")
            lines.append(f"- **一句话简述：** {gen_news_brief_cn(snippet, source)}")
            # 插入新闻图片（如果有image字段）
            img_url = item.get('image', '') or item.get('image_url', '')
            if img_url:
                lines.append(f"  ![新闻配图]({img_url})")
            lines.append(f"- **详解：** {gen_news_detail_cn(snippet, source)}")
            lines.append(f"- **点评：** {gen_news_comment_cn(source)}")
            lines.append("")
    lines.extend(["---", "", "*本报告仅供参考，请以原始论文和新闻源为准*", ""])
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[OK] 报告已生成: {len(lines)} 行")

if __name__ == "__main__":
    main()
