#!/usr/bin/env python3
from pathlib import Path

async def list_directory(path: str = ".") -> str:
    try:
        return "\n".join(p.name for p in Path(path).iterdir())
    except Exception as e:
        return str(e)

async def read_file(path: str) -> str:
    try:
        return Path(path).read_text()[:2000]
    except Exception as e:
        return str(e)