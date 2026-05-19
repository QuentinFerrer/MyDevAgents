#!/usr/bin/env python3
"""Send a desktop notification when Claude finishes. Called by the Stop hook."""

import subprocess
import sys


TITLE = "Claude Code"
MESSAGE = "Tâche terminée"


def notify_windows(title: str, message: str) -> None:
    ps_script = f"""
Add-Type -AssemblyName System.Windows.Forms
$n = New-Object System.Windows.Forms.NotifyIcon
$n.Icon = [System.Drawing.SystemIcons]::Information
$n.BalloonTipTitle = "{title}"
$n.BalloonTipText = "{message}"
$n.Visible = $true
$n.ShowBalloonTip(3000)
Start-Sleep -Milliseconds 3500
$n.Dispose()
"""
    subprocess.run(
        ["powershell", "-NoProfile", "-NonInteractive", "-Command", ps_script],
        capture_output=True,
        timeout=10,
    )


def notify_macos(title: str, message: str) -> None:
    subprocess.run(
        ["osascript", "-e", f'display notification "{message}" with title "{title}"'],
        capture_output=True,
        timeout=10,
    )


def notify_linux(title: str, message: str) -> None:
    subprocess.run(
        ["notify-send", title, message],
        capture_output=True,
        timeout=10,
    )


def notify(title: str = TITLE, message: str = MESSAGE) -> None:
    try:
        platform = sys.platform
        if platform == "win32":
            notify_windows(title, message)
        elif platform == "darwin":
            notify_macos(title, message)
        else:
            notify_linux(title, message)
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        pass


if __name__ == "__main__":
    notify()
