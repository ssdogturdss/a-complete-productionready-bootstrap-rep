#!/usr/bin/env python3
"""GitHub integration tools."""
import os
import subprocess
from agent.config import config

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

async def list_github_repos() -> str:
    if not GITHUB_TOKEN:
        return "No GITHUB_TOKEN set. Please configure in .env"
    # Use GitHub CLI if available, else curl
    try:
        result = subprocess.run(
            ["gh", "repo", "list", "--json", "nameWithOwner", "--limit", "10"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip() or "No repos found."
    except:
        return "Install GitHub CLI (gh) or set token for API access. Example repos: user/repo1, user/repo2"

async def clone_repo(repo: str, dest: str = None) -> str:
    dest = dest or f"/tmp/{repo.split('/')[-1]}"
    if os.path.exists(dest):
        return f"Already cloned to {dest}"
    try:
        subprocess.run(["git", "clone", f"https://{GITHUB_TOKEN}@github.com/{repo}.git", dest], check=True, capture_output=True)
        return f"Cloned {repo} to {dest}"
    except Exception as e:
        return f"Clone failed: {e}"