#!/usr/bin/env python3
import json
from pathlib import Path

DB = Path("/tmp/ai_admin_deployments.json")

def store_deployment(name: str, path: str, url: str):
    data = {}
    if DB.exists():
        data = json.loads(DB.read_text())
    data[name] = {"path": path, "url": url}
    DB.write_text(json.dumps(data, indent=2))

def get_deployment_status(name: str = None) -> str:
    if not DB.exists():
        return "No deployments recorded."
    data = json.loads(DB.read_text())
    if name:
        return str(data.get(name, "Not found"))
    return json.dumps(data, indent=2)