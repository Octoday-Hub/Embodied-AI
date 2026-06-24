#!/usr/bin/env python3
"""Extract figure image URLs from arXiv HTML pages for a set of papers.

Usage:
    python scripts/fetch_arxiv_images.py <papers_json> [output_json]

Input: papers JSON file with arxiv_id fields
Output: JSON mapping arxiv_id -> [{url, alt, figure_order}, ...]
"""
import json, os, sys, time, urllib.request
from html.parser import HTMLParser

TIMEOUT = 8
USER_AGENT = "Mozilla/5.0 (compatible; DailyReportBot/1.0)"
MAX_RETRIES = 1
RETRY_DELAY = 1

class ArxivImageParser(HTMLParser):
    """Find figures/teaser images in arXiv HTML."""
    def __init__(self):
        super().__init__()
        self.images = []
        self.skip_logos = {"arxiv", "logo", "icon", "arrow", "spacer", "px"}
        self.fig_num = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ("img",):
            src = d.get("src", "")
            alt = d.get("alt", "")
            if not self._is_valid(src, alt):
                return
            self.fig_num += 1
            self.images.append({
                "url": src,
                "alt": alt or f"Figure {self.fig_num}",
                "figure_order": self.fig_num,
            })
        # Also check <object> tags (arXiv sometimes uses them)
        if tag == "object":
            src = d.get("data", "")
            alt = d.get("alt", "")
            if not self._is_valid(src, alt):
                return
            self.fig_num += 1
            self.images.append({
                "url": src,
                "alt": alt or f"Figure {self.fig_num}",
                "figure_order": self.fig_num,
            })

    def _is_valid(self, src, alt):
        """Filter out logos and non-image assets."""
        if not src:
            return False
        ext = src.split("?")[0].rsplit(".", 1)[-1].lower() if "." in src else ""
        if ext not in ("png", "jpg", "jpeg", "gif", "svg"):
            return False
        src_lower = src.lower()
        alt_lower = alt.lower()
        for skip in self.skip_logos:
            if skip in src_lower or skip in alt_lower:
                return False
        return True

def try_fetch_arxiv_html(arxiv_id):
    """Try to fetch the HTML version of an arXiv paper."""
    url = f"https://arxiv.org/html/{arxiv_id}v1"
    for attempt in range(1 + MAX_RETRIES):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                raw = resp.read()
            # Try UTF-8 first, fall back to latin-1
            try:
                html = raw.decode("utf-8")
            except UnicodeDecodeError:
                html = raw.decode("latin-1")
            return html, url
        except urllib.error.HTTPError as e:
            # 404 means no HTML version
            if e.code == 404:
                return None, url
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
            continue
        except Exception:
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
            continue
    return None, url

def resolve_image_url(src, html_base_url):
    """Convert a relative image path to an absolute URL."""
    if src.startswith("http://") or src.startswith("https://"):
        return src
    # relative path: strip trailing path segments from base URL
    # base is like https://arxiv.org/html/2606.18239v1
    base = html_base_url.rstrip("/")
    if src.startswith("/"):
        # absolute path relative to domain root
        from urllib.parse import urlparse
        parsed = urlparse(base)
        domain = f"{parsed.scheme}://{parsed.netloc}"
        return domain + src
    else:
        # arXiv HTML pages use src="xxxxv1/x1.png" where relative resolution
        # would give /html/xxxxv1/xxxxv1/x1.png which 404s.
        # The correct path is /html/xxxxv1/x1.png.
        # Solution: extract the version dir name from the base URL and strip it.
        from urllib.parse import urlparse
        parsed = urlparse(base)
        path_parts = parsed.path.strip("/").split("/")
        # base path is like /html/2606.18646v1
        # src might be "2606.18646v1/x1.png" → extract x1.png
        if path_parts and src.startswith(path_parts[-1]):
            # Strip the version prefix from src
            stripped = src[len(path_parts[-1]):].lstrip("/")
            domain_part = f"{parsed.scheme}://{parsed.netloc}"
            new_path = "/".join(path_parts[:-1]) + "/" + path_parts[-1]
            return f"{domain_part}/{new_path}/{stripped}"
        # Normal relative resolution
        return base.rstrip("/") + "/" + src.lstrip("/")

def fetch_images(arxiv_id):
    """Main entry point: fetch images for a single paper."""
    result = try_fetch_arxiv_html(arxiv_id)
    if result is None:
        return []  # no HTML version available
    html_content, html_url = result
    parser = ArxivImageParser()
    try:
        parser.feed(html_content)
    except Exception:
        return []
    
    resolved = []
    for img in parser.images:
        full_url = resolve_image_url(img["url"], html_url)
        resolved.append({
            "url": full_url,
            "alt": img["alt"],
            "figure_order": img["figure_order"],
        })
    return resolved

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <papers_json> [output_json]")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
        os.path.dirname(input_path), "arxiv_images.json"
    )
    
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    papers = data.get("papers", data) if isinstance(data, dict) else data
    
    # Collect unique arxiv IDs
    arxiv_ids = []
    seen = set()
    for p in papers:
        aid = p.get("arxiv_id", "")
        if aid and aid not in seen:
            seen.add(aid)
            arxiv_ids.append(aid)
    
    print(f"Fetching images for {len(arxiv_ids)} papers from arXiv HTML...")
    
    image_map = {}
    for i, aid in enumerate(arxiv_ids, 1):
        print(f"  [{i}/{len(arxiv_ids)}] {aid}...", end=" ", flush=True)
        images = fetch_images(aid)
        if images:
            image_map[aid] = images
            print(f"OK ({len(images)} images)")
        else:
            image_map[aid] = []
            print("no images / no HTML version")
        # Small delay between requests to be polite
        time.sleep(0.5)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(image_map, f, ensure_ascii=False, indent=2)
    print(f"\nDone! Image map saved to {output_path}")
    print(f"  Papers with images: {sum(1 for v in image_map.values() if v)}/{len(image_map)}")

if __name__ == "__main__":
    main()
