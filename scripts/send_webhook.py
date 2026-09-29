"""Fire a repository_dispatch event to trigger the webhook workflow."""

import json
import os
import sys
import urllib.request

REPO = os.environ.get("GITHUB_REPOSITORY", "elinam-dev/qa-toolkit")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

if not TOKEN:
    sys.exit("Set GITHUB_TOKEN environment variable.")

payload = json.dumps({"event_type": "deploy-requested"}).encode()
req = urllib.request.Request(
    f"https://api.github.com/repos/{REPO}/dispatches",
    data=payload,
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
    },
    method="POST",
)
with urllib.request.urlopen(req) as resp:
    print(f"Dispatched — HTTP {resp.status}")
