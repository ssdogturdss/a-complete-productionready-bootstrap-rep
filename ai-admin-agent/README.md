# AI Admin Agent

Production-ready bootstrap for an autonomous AI server administration and deployment agent.

## One-line Install (Ubuntu 22.04)

```bash
curl -fsSL https://raw.githubusercontent.com/<USERNAME>/ai-admin-agent/main/install.sh | bash
```

Or after cloning:

```bash
git clone https://github.com/<USERNAME>/ai-admin-agent.git
cd ai-admin-agent
./install.sh
```

## What You Get

- Interactive wizard that configures GitHub, LLM, domain, and safety level
- FastAPI web chat UI at port 8080
- Real tool-calling agent with GitHub, Docker, Caddy, shell, filesystem, and memory tools
- Automatic deployment of static sites to Docker + optional Caddy + Let's Encrypt
- systemd service with auto-restart
- Persistent deployment history

## After Install

```bash
sudo systemctl status ai-admin-agent
journalctl -u ai-admin-agent -f
```

Open http://your-server:8080 and chat with the agent:

- "list repos"
- "deploy static site"
- "shell ls -la"

## Security

- Non-root `aiadmin` user
- Confirmation levels (strict/normal/autonomous)
- Dangerous commands blocked by default
- All actions logged

## Update / Uninstall

See docs/ARCHITECTURE.md for full details.

MIT License.