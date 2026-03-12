#!/usr/bin/env python3
"""Fetch YouTube video metadata using yt-dlp and output as structured text."""
import json
import re
import shutil
import sys
import io
import subprocess

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

YOUTUBE_URL_PATTERN = re.compile(
    r"^https?://(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w\-]+"
)


def validate_url(url: str) -> bool:
    """Validate that the URL is a legitimate YouTube video URL."""
    return bool(YOUTUBE_URL_PATTERN.match(url))


def main():
    if len(sys.argv) < 2:
        print("Usage: fetch_video_meta.py <youtube_url>")
        print("Example: fetch_video_meta.py https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        sys.exit(1)

    url = sys.argv[1]

    if not validate_url(url):
        print(f"ERROR: Invalid YouTube URL: {url}")
        print("URL must match: https://www.youtube.com/watch?v=... or https://youtu.be/...")
        sys.exit(1)

    ytdlp_path = shutil.which("yt-dlp")
    if not ytdlp_path:
        print("ERROR: yt-dlp not found. Install it via: pip install yt-dlp")
        sys.exit(1)

    result = subprocess.run(
        [ytdlp_path, "--dump-json", "--no-playlist", url],
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
