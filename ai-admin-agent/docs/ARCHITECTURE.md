# Architecture

- FastAPI web UI + chat
- Tool-calling loop in agent_loop.py
- Tools live in agent/tools/
- Config via .env + Pydantic
- Deployments stored in JSON (memory.py)
- systemd + Caddy for production

See README for usage.