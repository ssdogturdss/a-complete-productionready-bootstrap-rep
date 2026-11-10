# Architecture

- install.sh: Bootstrap
- wizard/: Collects config and provisions
- agent/: FastAPI + tool-calling loop
- Tools implement real GitHub API, Docker, Caddy, shell with safety
- Memory: SQLite for deployments

All operations logged. Safety via confirmation_level.
