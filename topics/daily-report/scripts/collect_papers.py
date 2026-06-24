#!/usr/bin/env python3
"""
arXiv 论文采集脚本 —— 具身智能 & 机器人方向
用途：每日自动化采集昨日新提交论文，按相关性排序输出 Top 20
输出：JSON 文件（标准输出或指定路径）
"""

import json
import sys
import os
import xml.etree.ElementTree as ET
import re
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timedelta, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional

# ---------- 路径配置（使用 D 盘，C 盘空间不足） ----------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.dirname(SCRIPT_DIR)
CONFIG_PATH = os.path.join(WORKSPACE, "sources", "arxiv_keywords.json")
DEFAULT_OUTPUT = os.path.join(WORKSPACE, "reports", "papers_raw.json")
BEIJING_TZ = timezone(timedelta(hours=8))

# ---------- 数据类型 ----------
@dataclass
class Paper:
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str
    link: str
    categories: list[str]
    published: str
    updated: str
    score: float = 0.0
    score_breakdown: dict = field(default_factory=dict)
    matched_keywords: list[str] = field(default_factory=list)

# ---------- 工具函数 ----------
def get_yesterday_bj() -> str:
    """获取北京时间的"昨天"日期，格式 YYYYMMDD"""
    bj_now = datetime.now(BEIJING_TZ)
    yesterday = bj_now - timedelta(days=1)
    return yesterday.strftime("%Y%m%d")

def get_yesterday_bj_human() -> str:
    """获取北京时间的"昨天"可读日期"""
    bj_now = datetime.now(BEIJING_TZ)
    yesterday = bj_now - timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")

def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def clean_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

def fetch_arxiv(query_url: str, timeout: int = 30) -> tuple[Optional[str], Optional[str]]:
    try:
        req = urllib.request.Request(
            query_url,
            headers={"User-Agent": "WorkBuddy-DailyReport/1.0 (mailto:research@example.com)"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8"), None
    except Exception as e:
        return None, str(e)

def parse_arxiv_response(xml_text: str) -> list[dict]:
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(xml_text)
    entries = []
    for entry in root.findall("atom:entry", ns):
        paper = {}
        paper["id"] = (entry.find("atom:id", ns).text.strip() 
                       if entry.find("atom:id", ns) is not None else "")
        paper["title"] = (clean_text(entry.find("atom:title", ns).text) 
                         if entry.find("atom:title", ns) is not None else "")
        
        authors = []
        for author in entry.findall("atom:author", ns):
            name = author.find("atom:name", ns)
            if name is not None:
                authors.append(clean_text(name.text))
        paper["authors"] = authors
        
        paper["abstract"] = (clean_text(entry.find("atom:summary", ns).text) 
                           if entry.find("atom:summary", ns) is not None else "")
        paper["published"] = (entry.find("atom:published", ns).text 
                            if entry.find("atom:published", ns) is not None else "")
        paper["updated"] = (entry.find("atom:updated", ns).text 
                          if entry.find("atom:updated", ns) is not None else "")
        
        arxiv_id = paper["id"].split("/abs/")[-1] if "/abs/" in paper["id"] else paper["id"]
        arxiv_id = re.sub(r'v\d+$', '', arxiv_id)
        paper["arxiv_id"] = arxiv_id
        paper["link"] = f"https://arxiv.org/abs/{arxiv_id}"
        
        cats = []
        for cat in entry.findall("arxiv:primary_category", ns):
            term = cat.get("term", "")
            if term: cats.append(term)
        for cat in entry.findall("atom:category", ns):
            term = cat.get("term", "")
            if term and term not in cats: cats.append(term)
        paper["categories"] = cats
        
        entries.append(paper)
    return entries

def score_paper(paper: dict, config: dict) -> tuple[float, dict, list[str]]:
    title_lower = paper["title"].lower()
    abstract_lower = paper["abstract"].lower()
    text = title_lower + " " + abstract_lower
    total_score = 0.0
    breakdown = {}
    matched = []
    for tier, tier_config in config["relevance_keywords"].items():
        weight = tier_config["weight"]
        for kw in tier_config["keywords"]:
            kw_lower = kw.lower()
            count_title = title_lower.count(kw_lower)
            count_abstract = abstract_lower.count(kw_lower)
            if count_title > 0 or count_abstract > 0:
                score = (count_title * 2 + count_abstract) * weight
                total_score += score
                if kw not in matched: matched.append(kw)
                breakdown[kw] = score
    return total_score, breakdown, matched

def is_blacklisted(paper: dict, config: dict) -> bool:
    text = (paper["title"] + " " + paper["abstract"]).lower()
    for kw in config["blacklist_keywords"]:
        if kw.lower() in text: return True
    return False

def build_query(category: str, config: dict) -> str:
    base_url = config["api_base_url"]
    query_params = urllib.parse.urlencode({
        "search_query": f"cat:{category}",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": 200
    }, quote_via=urllib.parse.quote)
    return f"{base_url}?{query_params}"

def parse_date_to_bj(published_str: str) -> Optional[str]:
    try:
        dt = datetime.strptime(published_str[:10], "%Y-%m-%d")
        return dt.strftime("%Y%m%d")
    except:
        return None

def main():
    errors = []
    config = load_config()
    yesterday = get_yesterday_bj()
    yesterday_human = get_yesterday_bj_human()
    all_papers = []
    
    for cat in config["categories"]:
        query_url = build_query(cat, config)
        xml_text, err = fetch_arxiv(query_url)
        if err:
            errors.append(f"[{cat}] 请求失败: {err[:200]}")
            continue
        if xml_text is None:
            errors.append(f"[{cat}] 无返回数据")
            continue
        entries = parse_arxiv_response(xml_text)
        for entry in entries:
            if parse_date_to_bj(entry.get("published", "")) == yesterday:
                all_papers.append(entry)
    
    # 去重
    seen_ids = set()
    unique_papers = []
    for p in all_papers:
        if p["arxiv_id"] not in seen_ids:
            seen_ids.add(p["arxiv_id"])
            unique_papers.append(p)
    
    # 打分 & 过滤
    scored_papers = []
    for p in unique_papers:
        if is_blacklisted(p, config): continue
        score, breakdown, matched = score_paper(p, config)
        scored_papers.append({
            "arxiv_id": p["arxiv_id"],
            "title": p["title"],
            "authors": p["authors"][:5],
            "abstract": p["abstract"],
            "link": p["link"],
            "categories": p["categories"],
            "published": p["published"],
            "score": round(score, 1),
            "score_breakdown": breakdown,
            "matched_keywords": matched[:10]
        })
    
    scored_papers.sort(key=lambda x: x["score"], reverse=True)
    top_n = config.get("max_papers", 10)
    top_20 = scored_papers[:top_n]
    
    result = {
        "metadata": {
            "run_time": datetime.now(BEIJING_TZ).isoformat(),
            "yesterday_date": yesterday_human,
            "total_fetched": len(all_papers),
            "after_dedup": len(unique_papers),
            "after_filter_scoring": len(scored_papers),
            "top_n": len(top_20)
        },
        "errors": errors,
        "papers": top_20
    }
    
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(output_path)

if __name__ == "__main__":
    main()
