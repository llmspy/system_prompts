import json
import os
from pathlib import Path

from aiohttp import web

default_prompts = [
    {"name": "Helpful Assistant", "prompt": "You are a helpful assistant."},
]


def install(ctx):
    # helper to get user or default prompts
    def get_user_prompts(request):
        candidate_paths = []
        username = ctx.get_username(request)
        if username:
            candidate_paths.append(
                os.path.join(Path.home(), ".llms", "user", username, "system_prompts", "prompts.json")
            )
        candidate_paths.append(os.path.join(Path.home(), ".llms", "user", "default", "system_prompts", "prompts.json"))
        candidate_paths.append(os.path.join(ctx.path, "ui", "prompts.json"))

        # iterate all candidate paths and when exists return its json
        for path in candidate_paths:
            if os.path.exists(path):
                with open(path, encoding="utf-8") as f:
                    txt = f.read()
                    return json.loads(txt)
        return default_prompts

    # API Handler to get prompts
    async def get_prompts(request):
        prompts_json = get_user_prompts(request)
        return web.json_response(prompts_json)

    ctx.add_get("prompts.json", get_prompts)


__install__ = install
