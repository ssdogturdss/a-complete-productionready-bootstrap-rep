#!/usr/bin/env python3
import os
import getpass
from pathlib import Path

print("=== AI Admin Agent Setup Wizard ===")
github_token = getpass.getpass("GitHub PAT (ghp_...): ")
llm_key = getpass.getpass("LLM API Key: ")
domain = input("Domain (or leave blank for IP): ").strip() or "localhost"
port = input("Port [8080]: ").strip() or "8080"
caddy = input("Enable Caddy HTTPS? [y/N]: ").lower().startswith("y")
level = input("Confirmation level (strict/normal/autonomous) [normal]: ").strip() or "normal"
base_dir = input("Deploy base dir [/opt/apps]: ").strip() or "/opt/apps"

env_path = Path(".env")
env_path.write_text(f"""GITHUB_TOKEN={github_token}
LLM_PROVIDER=openai
LLM_API_KEY={llm_key}
LLM_MODEL=gpt-4o-mini
DOMAIN={domain}
AGENT_PORT={port}
BASE_DEPLOY_DIR={base_dir}
CONFIRMATION_LEVEL={level}
CADDY_ENABLED={'true' if caddy else 'false'}
""")

print("Config written. Creating venv and installing agent deps...")
os.system("python3 -m venv agent/venv")
os.system("agent/venv/bin/pip install -r agent/requirements.txt -q")

print("Starting service setup...")
# In real run would call setup scripts
print("Wizard complete. Run healthcheck and start service manually or via systemd.")
print(f"Access: http://{domain}:{port}")
