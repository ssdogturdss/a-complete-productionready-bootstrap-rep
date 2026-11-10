#!/usr/bin/env python3
"""Safe shell execution with confirmation support."""
import subprocess
import os
from agent.config import config

async def run_shell(cmd: str, confirm: bool = False) -> str:
    if config.confirmation_level == "strict" and not confirm:
        return f"Confirmation required for: {cmd}. Reply 'yes' to run."
    if any(danger in cmd for danger in ["rm -rf /", "shutdown", "reboot"]):
        return "Blocked dangerous command."
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return result.stdout or result.stderr or "Command completed with no output."
    except Exception as e:
        return f"Error: {str(e)}"