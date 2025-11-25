#!/usr/bin/env python3
"""
Fetch Squarespace pages from a sitemap and convert them to Markdown for Jekyll.
Links to pages listed in the sitemap are rewritten to local permalinks.
"""

import argparse
import os
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


def fetch_sitemap(url: str) -> List[str]:
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "xml")
    return [loc.text.strip() for loc in soup.find_all("loc")]


def build_mapping(urls: List[str]) -> Dict[str, Tuple[str, Path]]:
    mapping: Dict[str, Tuple[str, Path]] = {}
    for u in urls:
        parsed = urlparse(u)
        slug = parsed.path.strip("/")
        if slug in ("", "home"):
            permalink = "/"
            path = Path("index.md")
        else:
            permalink = f"/{slug}/"
            path = Path("pages") / f"{slug}.md"
        mapping[u] = (permalink, path)
    return mapping


def sanitize_links(soup: BeautifulSoup, mapping: Dict[str, Tuple[str, Path]], base: str) -> None:
    for a in soup.find_all("a", href=True):
        href = a["href"]
        absolute = urljoin(base, href)
        if absolute in mapping:
            a["href"] = mapping[absolute][0]


def html_to_markdown(html: str) -> str:
    return md(html, heading_style="ATX")


def extract_title(soup: BeautifulSoup, default: str) -> str:
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        return h1.get_text(strip=True)
    return default


def write_page(path: Path, title: str, permalink: str, original_url: str, body_md: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    front_matter = f"""---
layout: default
title: {title}
original_url: {original_url}
permalink: {permalink}
---

"""
    path.write_text(front_matter + body_md, encoding="utf-8")


def scrape(sitemap_url: str, base_url: str) -> None:
    urls = fetch_sitemap(sitemap_url)
    mapping = build_mapping(urls)

    for url in urls:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")

        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        sanitize_links(soup, mapping, base_url)

        title = extract_title(soup, default=urlparse(url).path.strip("/") or "Home")
        body_html = soup.body or soup
        body_md = html_to_markdown(str(body_html))

        permalink, path = mapping[url]
        write_page(path, title, permalink, url, body_md)
        print(f"Wrote {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sitemap_url", help="Squarespace sitemap URL")
    parser.add_argument(
        "--base-url",
        default="https://keyboard-finch-92nf.squarespace.com",
        help="Base URL for resolving relative links",
    )
    args = parser.parse_args()

    scrape(args.sitemap_url, args.base_url)


if __name__ == "__main__":
    main()
