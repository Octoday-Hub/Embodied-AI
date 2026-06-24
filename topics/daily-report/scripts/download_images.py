#!/usr/bin/env python3
"""Download arXiv paper images to local images/ directory.

Usage:
    python scripts/download_images.py reports/arxiv_images.json reports/images/
"""
import json, os, sys, urllib.request, time

def download_images(img_map_path, img_dir):
    os.makedirs(img_dir, exist_ok=True)
    with open(img_map_path, "r", encoding="utf-8") as f:
        img_map = json.load(f)
    
    ok, fail = 0, 0
    for aid, images in img_map.items():
        for img in images[:2]:
            url = img["url"]
            fname = f"{aid}_{img['figure_order']}.png"
            fpath = os.path.join(img_dir, fname)
            if os.path.exists(fpath) and os.path.getsize(fpath) > 1000:
                print(f"[skip] {fname}")
                ok += 1
                continue
            for attempt in range(3):
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                    with urllib.request.urlopen(req, timeout=15) as resp:
                        data = resp.read()
                    with open(fpath, "wb") as f:
                        f.write(data)
                    print(f"[OK] {fname} ({len(data)} bytes)")
                    ok += 1
                    break
                except Exception as e:
                    if attempt < 2:
                        time.sleep(2)
                    else:
                        print(f"[FAIL] {fname}: {e}")
                        fail += 1
            time.sleep(0.3)
    print(f"\nDone: {ok} OK, {fail} failed")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <images_json> [images_dir]")
        sys.exit(1)
    img_map_path = sys.argv[1]
    img_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
        os.path.dirname(img_map_path), "images"
    )
    download_images(img_map_path, img_dir)
