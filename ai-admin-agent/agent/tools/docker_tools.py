#!/usr/bin/env python3
import subprocess

async def docker_list() -> str:
    try:
        result = subprocess.run(["docker", "ps", "--format", "{{.Names}} {{.Status}}"], capture_output=True, text=True, check=True)
        return result.stdout.strip() or "No containers running."
    except:
        return "Docker not available or not running."