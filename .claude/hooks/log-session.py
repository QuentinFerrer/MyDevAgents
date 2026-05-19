#!/usr/bin/env python3
"""Log session metadata on Stop. Called by the Stop hook."""

import json
import os
import sys
from datetime import datetime


def log_session() -> None:
    try:
        data = json.loads(sys.stdin.read())
    except Exception:
        data = {}

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    log_dir = os.path.join(project_dir, ".claude", "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "sessions.log")

    entry = {
        "timestamp": datetime.now().isoformat(),
        "session_id": data.get("session_id", "unknown"),
        "cwd": data.get("cwd", "unknown"),
        "stop_reason": data.get("stop_reason", "unknown"),
    }

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    log_session()
