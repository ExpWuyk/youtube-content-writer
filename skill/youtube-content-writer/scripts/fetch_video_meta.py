#!/usr/bin/env python3
"""Fetch YouTube video metadata using yt-dlp and output as structured text."""
import json
import sys
import io
import subprocess

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def main():
    if len(sys.argv) < 2:
        print("Usage: fetch_video_meta.py <youtube_url>")
        sys.exit(1)

    url = sys.argv[1]
    result = subprocess.run(
        ["yt-dlp", "--dump-json", url],
        capture_output=True,
        text=False,
    )
    if result.returncode != 0:
        print("ERROR: yt-dlp failed")
        print(result.stderr.decode("utf-8", errors="replace"))
        sys.exit(1)

    d = json.loads(result.stdout.decode("utf-8"))
    fields = {
        "TITLE": d.get("title", ""),
        "CHANNEL": d.get("channel", ""),
        "UPLOADER": d.get("uploader", ""),
        "UPLOAD_DATE": d.get("upload_date", ""),
        "DURATION": d.get("duration", ""),
        "VIEW_COUNT": d.get("view_count", ""),
        "LIKE_COUNT": d.get("like_count", ""),
        "DESCRIPTION": d.get("description", ""),
        "TAGS": d.get("tags", []),
        "CATEGORIES": d.get("categories", []),
        "LICENSE": d.get("license", ""),
    }
    for k, v in fields.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
