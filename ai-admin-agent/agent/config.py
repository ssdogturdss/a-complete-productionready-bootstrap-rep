#!/usr/bin/env python3
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Config(BaseModel):
    github_token: str = os.getenv("GITHUB_TOKEN", "")
    llm_provider: str = os.getenv("LLM_PROVIDER", "openai")
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_model: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    domain: str = os.getenv("DOMAIN", "localhost")
    port: int = int(os.getenv("AGENT_PORT", "8080"))
    base_deploy_dir: str = os.getenv("BASE_DEPLOY_DIR", "/opt/apps")
    confirmation_level: str = os.getenv("CONFIRMATION_LEVEL", "normal")
    caddy_enabled: bool = os.getenv("CADDY_ENABLED", "false").lower() == "true"

config = Config()