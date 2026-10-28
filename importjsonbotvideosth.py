import json, os
import requests, feedparser

CHANNEL_ID = "UCmQpItAN6ugyWJYnefzVDpA"
WEBHOOK = os.environ["WEBHOOK"]
FEED = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
SEEN_FILE = "seen.json"

entries = feedparser.parse(FEED).entries

if os.path.exists(SEEN_FILE):
    seen = set(json.load(open(SEEN_FILE)))
    for e in reversed(entries):
        if e.yt_videoid not in seen:
            requests.post(WEBHOOK, json={
                "content": f"🎬 Nuevo video de Team Heretics Brawl Stars:\n{e.link}"
            })
            seen.add(e.yt_videoid)
else:
    seen = {e.yt_videoid for e in entries}

json.dump(list(seen), open(SEEN_FILE, "w"))