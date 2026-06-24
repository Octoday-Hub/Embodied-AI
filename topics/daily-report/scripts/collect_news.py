#!/usr/bin/env python3
"""
行业新闻采集脚本 —— 具身智能 & 机器人方向
用途：每日自动化搜索昨日行业新闻/信息
方案：调用 anysearch CLI，解析 Markdown 输出
输出：JSON 文件（含待验证的新闻条目）
"""

import json
import sys
import os
import subprocess
import re
from datetime import datetime, timedelta, timezone
from urllib.parse import urlparse

# ---------- 路径配置 ----------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.dirname(SCRIPT_DIR)
DEFAULT_OUTPUT = os.path.join(WORKSPACE, "reports", "news_raw.json")
BEIJING_TZ = timezone(timedelta(hours=8))

# ---------- anysearch CLI 路径 ----------
ANYSEARCH_CLI = [
    "C:\\Users\\D\\.workbuddy\\binaries\\python\\versions\\3.13.12\\python.exe",
    "C:\\Users\\D\\.workbuddy\\skills\\anysearch\\scripts\\anysearch_cli.py"
]

# ---------- 搜索配置 ----------
SEARCH_QUERIES = [
    # 国际
    {"queries": ["embodied AI robotics", "humanoid robot latest news"], "group": "国际"},
    {"queries": ["Boston Dynamics", "Figure AI", "Tesla Optimus", "Agility Robotics"], "group": "国际_公司"},
    # 国内
    {"queries": ["具身智能 最新", "人形机器人 行业", "通用机器人 发布"], "group": "国内"},
    {"queries": ["宇树科技 机器人", "星动纪元", "智元机器人", "小鹏机器人", "银河通用机器人"], "group": "国内_公司"},
    # 产业
    {"queries": ["robot investment funding", "robotics startup"], "group": "产业"}
]

# 官方来源域名列表
OFFICIAL_DOMAINS = [
    "bostondynamics.com", "figure.ai", "tesla.com", "1x.tech",
    "agilityrobotics.com", "apptronik.com", "sanctuary.ai", "skild.ai",
    "unitree.com", "galaxybot.com", "ftt-e.com", "ubtrobot.com"
]

def get_yesterday_bj() -> str:
    bj_now = datetime.now(BEIJING_TZ)
    yesterday = bj_now - timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")

def run_anysearch(query: str, max_results: int = 8) -> str:
    """调用 anysearch CLI 搜索，返回原始 Markdown 文本"""
    cmd = ANYSEARCH_CLI + ["search", query, "--max_results", str(max_results)]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, encoding="utf-8")
        if result.returncode != 0:
            print(f"[WARN] search failed: {query[:40]}... | {result.stderr[:100]}", file=sys.stderr)
            return ""
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        print(f"[WARN] timeout: {query[:40]}...", file=sys.stderr)
        return ""
    except Exception as e:
        print(f"[WARN] error: {query[:40]}... | {e}", file=sys.stderr)
        return ""

def parse_anysearch_markdown(md_text: str) -> list[dict]:
    """
    解析 anysearch 的 Markdown 输出为结构化数据
    格式：
    ### N. Title
    - **URL**: https://...
    - Description text...
    """
    results = []
    # 按 "### " 分割条目
    blocks = re.split(r'\n###\s+', md_text)
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        
        # 提取标题（第一个#号后的文本，到 | 或换行）
        title_match = re.match(r'\d+\.\s*(.+?)(?:\n|$)', block)
        title = title_match.group(1).strip() if title_match else ""
        # 去掉标题中的 | 后缀
        title = re.sub(r'\s*\|.*', '', title).strip()
        
        # 提取 URL
        url_match = re.search(r'\*\*URL\*\*:\s*(https?://[^\s]+)', block)
        url = url_match.group(1).strip() if url_match else ""
        
        # 提取摘要（URL后面的文本）
        if url_match:
            snippet = block[url_match.end():].strip()
        else:
            snippet = block
        
        # 简化摘要
        snippet = re.sub(r'\s+', ' ', snippet).strip()
        snippet = snippet[:500] if len(snippet) > 500 else snippet
        
        if title and url:
            results.append({
                "title": title,
                "url": url,
                "snippet": snippet,
                "source": extract_domain(url)
            })
    
    return results

def extract_domain(url: str) -> str:
    try:
        return urlparse(url).netloc.replace("www.", "")
    except:
        return ""

def is_official_source(url: str) -> bool:
    domain = extract_domain(url)
    for off_domain in OFFICIAL_DOMAINS:
        if off_domain in domain:
            return True
    return False

def is_just_homepage(url: str) -> bool:
    """判断是否只是公司首页（非具体文章）"""
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    return len(path) < 5  # 路径很短就是首页

def needs_verify(title: str, snippet: str, url: str) -> bool:
    """判断是否需要去官方来源核实"""
    if is_official_source(url):
        return False
    company_keywords = [
        "boston dynamics", "figure ai", "tesla optimus", "1x", "agility robotics",
        "apptronik", "sanctuary ai", "skild ai", "unitree", "xiaomi robot",
        "宇树", "星动纪元", "智元", "小鹏", "银河通用", "傅利叶", "优必选"
    ]
    text = (title + " " + snippet).lower()
    return any(kw in text for kw in company_keywords)

def find_official_domain(title: str, snippet: str) -> str:
    text = (title + " " + snippet).lower()
    for off_domain in OFFICIAL_DOMAINS:
        if off_domain.split(".")[0] in text:
            return off_domain
    return ""

def parse_date(text: str, group: str = "") -> str:
    """Extract date from text, with fallback to yesterday."""
    yesterday = get_yesterday_bj()
    # First check if yesterday's date appears in text
    if yesterday in text:
        return yesterday
    # Try common date patterns
    for pattern in [
        r'(\d{4}[-/]\d{2}[-/]\d{2})',
        r'(\w+ \d{1,2},?\s*\d{4})',
        r'(\d{1,2}\s+\w+\s+\d{4})',
        r'(\d{4}\s+年\s+\d{1,2}\s+月\s+\d{1,2}\s+日)',
    ]:
        m = re.search(pattern, text)
        if m:
            raw = m.group(1)
            # Normalize to YYYY-MM-DD
            try:
                from datetime import datetime
                for fmt in ["%Y-%m-%d", "%Y/%m/%d", "%B %d %Y", "%d %B %Y", "%b %d %Y", "%d %b %Y"]:
                    try:
                        return datetime.strptime(raw, fmt).strftime("%Y-%m-%d")
                    except ValueError:
                        continue
            except:
                pass
            return raw
    # Fallback: if this is a known news source, assume yesterday
    return yesterday

def main():
    yesterday = get_yesterday_bj()
    print(f"[info] 目标日期: {yesterday}", file=sys.stderr)
    
    seen_urls = set()
    all_items = []
    
    for group_cfg in SEARCH_QUERIES:
        group = group_cfg["group"]
        for query in group_cfg["queries"]:
            print(f"[search] [{group}] {query}", file=sys.stderr)
            md_output = run_anysearch(query)
            if not md_output:
                continue
            items = parse_anysearch_markdown(md_output)
            for item in items:
                url = item["url"]
                if url in seen_urls:
                    continue
                seen_urls.add(url)
                item["group"] = group
                item["date"] = parse_date(item["title"] + " " + item["snippet"])
                item["is_official"] = is_official_source(url)
                item["needs_official_verify"] = needs_verify(item["title"], item["snippet"], url)
                item["official_domain"] = find_official_domain(item["title"], item["snippet"])
                item["relevance_score"] = 1.0
                all_items.append(item)
    
    # 去重并排序
    seen_titles = set()
    deduped = []
    for item in all_items:
        key = item["title"][:40].lower()
        if key and key not in seen_titles:
            seen_titles.add(key)
            deduped.append(item)
    
    # 排序：有新闻内容的官方源 > 需验证的新闻 > 官方首页 > 一般
    def sort_key(item):
        is_home = is_just_homepage(item["url"])
        snippet_len = len(item["snippet"])
        return (
            4 if (item["is_official"] and not is_home) else
            3 if (not is_home and item["needs_official_verify"]) else
            2 if (item["is_official"] and is_home) else
            1,
            snippet_len  # 摘要长的优先
        )
    deduped.sort(key=sort_key, reverse=True)
    
    top_5 = deduped[:5]
    
    print(f"\n[result] 总计 {len(all_items)} 条 → 去重 {len(deduped)} 条 → Top {len(top_5)} 条", file=sys.stderr)
    for i, item in enumerate(top_5, 1):
        verify_flag = " [需核实]" if item["needs_official_verify"] else (" [官方]" if item["is_official"] else "")
        print(f"  {i}. {item['title'][:60]} | {item['source']}{verify_flag}", file=sys.stderr)
    
    result = {
        "metadata": {
            "run_time": datetime.now(BEIJING_TZ).isoformat(),
            "yesterday_date": yesterday,
            "total_raw": len(all_items),
            "after_dedup": len(deduped),
            "top_n": len(top_5),
            "pending_verify": sum(1 for n in top_5 if n["needs_official_verify"])
        },
        "news": top_5
    }
    
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n输出: {output_path}", file=sys.stderr)
    print(output_path)

if __name__ == "__main__":
    main()
