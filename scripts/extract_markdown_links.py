#!/usr/bin/env python3
"""Extract Markdown links from the source repo into a JSON index."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / "ai-infra-learning"
OUTPUT_PATH = ROOT / "ai-infra-study-work" / "source-link-index.json"
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def classify(url: str) -> str:
    if url.startswith("#"):
        return "repo_anchor"
    if url.startswith("./"):
        return "internal_doc"
    if "github.com" in url:
        return "github_repo"
    if any(domain in url for domain in ("coursera.org", "udemy.com", "skills.google", "nvidia.com", "cisco.com")):
        return "course_or_training"
    if any(domain in url for domain in ("cloud.google.com", "flexential.com")):
        return "report"
    if any(domain in url for domain in ("rudderstack.com", "splunk.com", "nexla.com", "tailscale.com", "f5.com")):
        return "blog_or_resource"
    return "external_other"


def main() -> None:
    entries = []

    for path in sorted(SOURCE_DIR.glob("*.md")):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for match in LINK_RE.finditer(line):
                title, url = match.groups()
                entries.append(
                    {
                        "file": path.name,
                        "line": lineno,
                        "title": title,
                        "url": url,
                        "category": classify(url),
                    }
                )

    counts: dict[str, int] = {}
    for entry in entries:
        counts[entry["category"]] = counts.get(entry["category"], 0) + 1

    payload = {
        "source_repo": str(SOURCE_DIR),
        "total_links": len(entries),
        "counts_by_category": counts,
        "links": entries,
    }

    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(entries)} links to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
