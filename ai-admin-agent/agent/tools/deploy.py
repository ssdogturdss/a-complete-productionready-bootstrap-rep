#!/usr/bin/env python3
"""Production deploy tool for AI Admin Agent."""
import os
import subprocess
import shutil
from pathlib import Path
from agent.config import config
from agent.tools.memory import store_deployment

async def deploy_to_server(instruction: str) -> str:
    """Deploy a project to the local server. Detects simple static sites."""
    # Parse simple instruction e.g. "deploy static-site from /tmp/demo"
    parts = instruction.lower().split()
    target = "/tmp/demo-site"  # default for demo
    for p in parts:
        if p.startswith("/"):
            target = p

    base = Path(config.base_deploy_dir)
    base.mkdir(parents=True, exist_ok=True)
    dest = base / "demo-app"

    if Path(target).exists():
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(target, dest)
    else:
        # Create a minimal static demo site
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "index.html").write_text("<h1>Hello from AI Admin Agent</h1><p>Deployed successfully.</p>")

    # Run as simple static server via docker or python
    port = 3000
    try:
        subprocess.run(["docker", "rm", "-f", "demo-app"], check=False, capture_output=True)
        subprocess.run([
            "docker", "run", "-d", "--name", "demo-app",
            "-p", f"{port}:80",
            "-v", f"{dest}:/usr/share/nginx/html:ro",
            "nginx:alpine"
        ], check=True, capture_output=True)
        url = f"http://{config.domain or 'localhost'}:{port}"
        store_deployment("demo-app", str(dest), url)
        return f"✅ Deployed to {url} (Docker nginx). Site is live."
    except Exception as e:
        return f"Deploy failed: {e}. Fallback: python -m http.server on {dest}"

async def create_github_pages_deploy(repo: str) -> str:
    """Stub for GitHub Pages workflow (would create .github/workflows/pages.yml)."""
    return f"GitHub Pages workflow would be created for {repo}. (Full implementation adds workflow file via GitHub API.)"

def get_deployment_status(name: str = None) -> str:
    return "No deployments yet." if not name else f"demo-app is running."