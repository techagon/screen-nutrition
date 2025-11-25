#!/usr/bin/env python3
"""Generate Markdown pages from the provided Squarespace WordPress export."""
import re
from pathlib import Path
import xml.etree.ElementTree as ET

from markdownify import markdownify as md

EXPORT = Path("page_captures/Squarespace-Wordpress-Export-11-21-2025.xml")
OUTPUT_ROOT = Path(".")
PAGES_DIR = Path("pages")


def link_to_path_and_permalink(link: str) -> tuple[Path, str]:
    slug = link.strip("/")
    if slug in ("", "home"):
        return Path("index.md"), "/"
    permalink = f"/{slug}/"
    filename = slug.replace("/", "-") + ".md"
    return PAGES_DIR / filename, permalink


def clean_markdown(md_text: str) -> str:
    # Remove excessive blank lines and artifacts from converters.
    md_text = re.sub(r"\n{3,}", "\n\n", md_text).strip()
    return md_text


def main() -> None:
    ns = {"content": "http://purl.org/rss/1.0/modules/content/"}
    tree = ET.parse(EXPORT)
    root = tree.getroot()
    items = root.findall("./channel/item")

    PAGES_DIR.mkdir(parents=True, exist_ok=True)

    for item in items:
        title = item.find("title").text or "Untitled"
        link = item.find("link").text or "/"
        if title.startswith("attachment-"):
            continue  # skip image attachments

        content = item.find("content:encoded", ns)
        html = content.text or ""
        body_md = clean_markdown(md(html, heading_style="ATX"))

        path, permalink = link_to_path_and_permalink(link)
        path.parent.mkdir(parents=True, exist_ok=True)

        front_matter = f"""---
layout: default
title: "{title}"
original_url: "https://keyboard-finch-92nf.squarespace.com{link}"
permalink: {permalink}
---

"""
        path.write_text(front_matter + body_md + "\n", encoding="utf-8")
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
