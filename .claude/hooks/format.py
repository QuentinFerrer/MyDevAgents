#!/usr/bin/env python3
"""Auto-format a file after Write/Edit. Called by the PostToolUse hook."""

import subprocess
import sys
import os


FORMATTERS = {
    ".py": ["black", "--quiet"],
    ".js": ["prettier", "--write"],
    ".ts": ["prettier", "--write"],
    ".tsx": ["prettier", "--write"],
    ".jsx": ["prettier", "--write"],
    ".json": ["prettier", "--write"],
    ".css": ["prettier", "--write"],
    ".scss": ["prettier", "--write"],
    ".html": ["prettier", "--write"],
    ".md": ["prettier", "--write"],
    ".yaml": ["prettier", "--write"],
    ".yml": ["prettier", "--write"],
    ".go": ["gofmt", "-w"],
    ".rs": ["rustfmt"],
}


def format_file(file_path: str) -> None:
    if not file_path or not os.path.isfile(file_path):
        return

    ext = os.path.splitext(file_path)[1].lower()
    cmd_base = FORMATTERS.get(ext)
    if not cmd_base:
        return

    try:
        subprocess.run(
            cmd_base + [file_path],
            capture_output=True,
            timeout=30,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        format_file(sys.argv[1])
