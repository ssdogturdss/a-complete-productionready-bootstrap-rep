import asyncio
from agent.tools import github, shell, docker_tools, deploy, caddy, filesystem, memory
from agent.config import config
import json

TOOLS = {
    "list_github_repos": github.list_github_repos,
    "clone_repo": github.clone_repo,
    "create_github_pages_deploy": deploy.create_github_pages_deploy,
    "deploy_to_server": deploy.deploy_to_server,
    "run_shell": shell.run_shell,
    "docker_list": docker_tools.docker_list,
    "manage_caddy_site": caddy.manage_caddy_site,
    "read_file": filesystem.read_file,
    "list_directory": filesystem.list_directory,
    "get_deployment_status": memory.get_deployment_status,
}

async def process_message(message: str) -> str:
    # Very basic loop for demo - in production use LLM tool calling
    # For now, echo + simple command routing
    if "list repos" in message.lower():
        return await TOOLS["list_github_repos"]()
    if "deploy" in message.lower():
        return await TOOLS["deploy_to_server"](message)
    if message.startswith("shell "):
        return await TOOLS["run_shell"](message[6:])
    return f"Processed: {message}. (Full LLM loop would call tools here. Try: list repos, deploy static-site, shell ls)"
