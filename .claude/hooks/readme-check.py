#!/usr/bin/env python3
"""Inject a README update reminder when a relevant file is modified.

Reads the PostToolUse hook JSON from stdin. Outputs additionalContext
(exit 0 + JSON) so Claude is reminded to update the README in the same turn.
Must run synchronously (no async) to inject context before Claude responds.
"""

import fnmatch
import json
import os
import sys

README_IMPACTING_PATTERNS = [
    # Python
    "requirements*.txt",
    "pyproject.toml",
    "setup.py",
    "setup.cfg",
    "Pipfile",
    "poetry.lock",
    # Node
    "package.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    # Go / Rust
    "go.mod",
    "Cargo.toml",
    # Docker / infra
    "Dockerfile*",
    "docker-compose*.yml",
    "docker-compose*.yaml",
    "Makefile",
    # Config / env
    ".env.example",
    ".gitignore",
    "*.config.js",
    "*.config.ts",
    ".claude/settings.json",
]


def is_readme_impacting(file_path: str) -> bool:
    if not file_path:
        return False
    filename = os.path.basename(file_path)
    for pattern in README_IMPACTING_PATTERNS:
        if fnmatch.fnmatch(filename, pattern) or fnmatch.fnmatch(file_path, pattern):
            return True
    return False


def main() -> None:
    try:
        data = json.loads(sys.stdin.read())
    except Exception:
        return

    file_path = data.get("tool_input", {}).get("file_path", "")
    if not is_readme_impacting(file_path):
        return

    filename = os.path.basename(file_path)
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": (
                        f"Le fichier `{filename}` vient d'être modifié. "
                        "Vérifie si le README doit être mis à jour en conséquence "
                        "(prérequis, installation, configuration, variables d'environnement, etc.). "
                        "Si une bonne pratique ou amélioration est applicable, suggère-la à l'utilisateur."
                    ),
                }
            }
        )
    )


if __name__ == "__main__":
    main()
