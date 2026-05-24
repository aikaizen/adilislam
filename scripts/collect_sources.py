#!/usr/bin/env python3
"""Collect AI/agent research from Tier 1 & 2 sources for the Daily Signal bulletin.

Outputs structured JSON to stdout. Each source returns a list of items with:
  title, url, source, score (optional relevance 1-10), description

Tier 1: GitHub Trending, HN Algolia, Latent Space, Simon Willison, r/LocalLLaMA
Tier 2: arXiv cs.AI+cs.CL, r/MachineLearning, HN Firebase top stories
"""

import json
import re
import sys
import urllib.request
import urllib.error
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

TIMEOUT = 25
HEADERS = {"User-Agent": "AdilIslamSignal/1.0 (adilislam.com)"}

def fetch(url, raw=False):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"WARN: Failed to fetch {url}: {e}", file=sys.stderr)
        return None

# ── GitHub Trending ──────────────────────────────────────────────
def github_trending():
    html = fetch("https://github.com/trending?since=daily")
    if not html:
        return []
    items = []
    # Extract articles (GitHub's current DOM structure)
    articles = re.findall(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    ai_keywords = ['ai', 'llm', 'agent', 'model', 'ml', 'gpt', 'claude', 'neural',
                   'transformer', 'diffusion', 'rag', 'mcp', 'embedding', 'inference',
                   'training', 'deep-learning', 'machine-learning', 'nlp', 'cv']
    for art in articles[:25]:
        # Repo link from h2
        h2_links = re.findall(r'<h2[^>]*>.*?href="(/[^"]+)"', art, re.DOTALL)
        repo_path = h2_links[0] if h2_links else ""
        if not repo_path or repo_path.count('/') != 2 or not repo_path.startswith('/'):
            continue
        # Description
        desc_match = re.search(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', art, re.DOTALL)
        desc = ""
        if desc_match:
            desc = re.sub(r'<[^>]+>', '', desc_match.group(1)).strip()
        # Stars today
        stars_match = re.search(r'([\d,]+)\s*stars today', art)
        stars = stars_match.group(1) if stars_match else ""
        desc_full = desc + (f" ({stars} stars today)" if stars else "")
        repo_lower = (repo_path + " " + desc).lower()
        score = 7 if any(kw in repo_lower for kw in ai_keywords) else 3
        items.append({
            "title": repo_path.strip("/"),
            "url": f"https://github.com{repo_path}",
            "source": "GitHub Trending",
            "score": score,
            "description": desc_full[:200]
        })
    return items

# ── Hacker News (Algolia) ───────────────────────────────────────
def hacker_news_algolia():
    queries = [
        "AI agent",
        "LLM open source",
        "AI startup funding",
    ]
    items = []
    seen = set()
    for q in queries:
        url = f"https://hn.algolia.com/api/v1/search?query={urllib.parse.quote(q)}&tags=story&numericFilters=points>30&hitsPerPage=10"
        data = fetch(url)
        if not data:
            continue
        try:
            results = json.loads(data)
        except json.JSONDecodeError:
            continue
        for hit in results.get("hits", []):
            oid = hit.get("objectID", "")
            if oid in seen:
                continue
            seen.add(oid)
            items.append({
                "title": hit.get("title", ""),
                "url": hit.get("url") or f"https://news.ycombinator.com/item?id={oid}",
                "source": "Hacker News",
                "score": min(10, (hit.get("points", 0) or 0) // 50 + 5),
                "description": f"HN points: {hit.get('points', 0)}"
            })
    return items

# ── Latent Space ────────────────────────────────────────────────
def latent_space():
    xml = fetch("https://latent.space/feed")
    if not xml:
        return []
    items = []
    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        return []
    # Substack serves RSS 2.0 (<item>), not Atom (<entry>)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    # Try Atom first (unlikely but harmless)
    atom_entries = root.findall(".//atom:entry", ns)
    if atom_entries:
        for entry in atom_entries[:10]:
            title_el = entry.find("atom:title", ns)
            link_el = entry.find("atom:link", ns)
            summary_el = entry.find("atom:summary", ns) or entry.find("atom:content", ns)
            title = title_el.text if title_el is not None else ""
            url = link_el.get("href", "") if link_el is not None else ""
            desc = ""
            if summary_el is not None and summary_el.text:
                desc = re.sub(r'<[^>]+>', '', summary_el.text)[:200].strip()
            if title:
                items.append({
                    "title": title,
                    "url": url,
                    "source": "Latent Space",
                    "score": 9,
                    "description": desc
                })
    else:
        # RSS 2.0 parsing (Substack format)
        for item in root.findall(".//item")[:10]:
            title_el = item.find("title")
            link_el = item.find("link")
            desc_el = item.find("description")
            title = title_el.text if title_el is not None else ""
            url = link_el.text if link_el is not None else ""
            desc = ""
            if desc_el is not None and desc_el.text:
                desc = re.sub(r'<[^>]+>', '', desc_el.text)[:200].strip()
            if title:
                items.append({
                    "title": title,
                    "url": url,
                    "source": "Latent Space",
                    "score": 9,
                    "description": desc
                })
    return items[:10]

# ── Simon Willison ──────────────────────────────────────────────
def simon_willison():
    xml = fetch("https://simonwillison.net/atom/everything/")
    if not xml:
        return []
    items = []
    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        return []
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for entry in root.findall(".//atom:entry", ns)[:15]:
        title_el = entry.find("atom:title", ns)
        link_el = entry.find("atom:link", ns)
        summary_el = entry.find("atom:summary", ns) or entry.find("atom:content", ns)
        title = title_el.text if title_el is not None else ""
        url = link_el.get("href", "") if link_el is not None else ""
        desc = ""
        if summary_el is not None and summary_el.text:
            desc = re.sub(r'<[^>]+>', '', summary_el.text)[:200].strip()
        ai_keywords = ['ai', 'llm', 'agent', 'gpt', 'claude', 'model', 'dataset', 'tool']
        score = 8 if any(kw in (title + " " + desc).lower() for kw in ai_keywords) else 4
        if title:
            items.append({
                "title": title,
                "url": url,
                "source": "Simon Willison",
                "score": score,
                "description": desc
            })
    return items

# ── Reddit r/LocalLLaMA ────────────────────────────────────────
def reddit_localllama():
    data = fetch("https://www.reddit.com/r/LocalLLaMA/hot.json")
    if not data:
        return []
    items = []
    try:
        results = json.loads(data)
    except json.JSONDecodeError:
        return []
    for child in results.get("data", {}).get("children", [])[:15]:
        post = child.get("data", {})
        title = post.get("title", "")
        url = post.get("url", "")
        score_val = post.get("score", 0)
        permalink = post.get("permalink", "")
        if not url.startswith("http"):
            url = f"https://reddit.com{permalink}"
        if title:
            items.append({
                "title": title,
                "url": url,
                "source": "r/LocalLLaMA",
                "score": min(10, score_val // 100 + 5),
                "description": f"↑{score_val}"
            })
    return items

# ── arXiv cs.AI + cs.CL ────────────────────────────────────────
def arxiv():
    url = "http://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.CL&sortBy=submittedDate&sortOrder=descending&max_results=15"
    xml = fetch(url)
    if not xml:
        # Retry with alternate endpoint
        xml = fetch(f"https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.CL&sortBy=submittedDate&sortOrder=descending&max_results=15")
    if not xml:
        return []
    items = []
    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        return []
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for entry in root.findall("atom:entry", ns):
        title_el = entry.find("atom:title", ns)
        link_el = entry.find("atom:link[@type='text/html']", ns)
        summary_el = entry.find("atom:summary", ns)
        title = title_el.text.strip().replace("\n", " ") if title_el is not None else ""
        url_val = link_el.get("href", "") if link_el is not None else ""
        desc = ""
        if summary_el is not None and summary_el.text:
            desc = summary_el.text.strip().replace("\n", " ")[:200]
        ai_keywords = ['agent', 'llm', 'language model', 'in-context', 'reasoning', 'tool-use', 'planning']
        score = 8 if any(kw in (title + " " + desc).lower() for kw in ai_keywords) else 5
        if title:
            items.append({
                "title": title,
                "url": url_val,
                "source": "arXiv",
                "score": score,
                "description": desc
            })
    return items

# ── Reddit r/MachineLearning ───────────────────────────────────
def reddit_ml():
    data = fetch("https://www.reddit.com/r/MachineLearning/hot.json")
    if not data:
        return []
    items = []
    try:
        results = json.loads(data)
    except json.JSONDecodeError:
        return []
    for child in results.get("data", {}).get("children", [])[:10]:
        post = child.get("data", {})
        title = post.get("title", "")
        url = post.get("url", "")
        score_val = post.get("score", 0)
        permalink = post.get("permalink", "")
        if not url.startswith("http"):
            url = f"https://reddit.com{permalink}"
        if title:
            items.append({
                "title": title,
                "url": url,
                "source": "r/MachineLearning",
                "score": min(10, score_val // 100 + 5),
                "description": f"↑{score_val}"
            })
    return items

# ── Main ────────────────────────────────────────────────────────
def main():
    collectors = [
        ("github_trending", github_trending),
        ("hacker_news", hacker_news_algolia),
        ("latent_space", latent_space),
        ("simon_willison", simon_willison),
        ("reddit_localllama", reddit_localllama),
        ("arxiv", arxiv),
        ("reddit_ml", reddit_ml),
    ]
    
    all_items = []
    errors = []
    for name, fn in collectors:
        try:
            items = fn()
            all_items.extend(items)
            print(f"  {name}: {len(items)} items", file=sys.stderr)
        except Exception as e:
            errors.append(f"{name}: {e}")
            print(f"  {name}: ERROR - {e}", file=sys.stderr)
    
    # Sort by score descending
    all_items.sort(key=lambda x: x.get("score", 0), reverse=True)
    
    output = {
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "total_items": len(all_items),
        "errors": errors,
        "items": all_items
    }
    
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
