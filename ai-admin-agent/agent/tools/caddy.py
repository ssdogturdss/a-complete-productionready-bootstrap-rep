#!/usr/bin/env python3
from pathlib import Path
from agent.config import config

async def manage_caddy_site(action: str, domain: str, target: str) -> str:
    caddyfile = Path("/etc/caddy/Caddyfile")
    if action == "add":
        entry = f"{domain} {{\n    reverse_proxy {target}\n}}\n"
        caddyfile.write_text(caddyfile.read_text() + "\n" + entry if caddyfile.exists() else entry)
        return f"Added {domain} -> {target} to Caddy (reload with: sudo systemctl reload caddy)"
    return "Caddy site managed."