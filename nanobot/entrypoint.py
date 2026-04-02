#!/usr/bin/env python3
import os
import json
import shutil
import sys
from pathlib import Path

def main():
    config_path = Path("/app/nanobot/config.json")
    resolved_path = Path("/app/nanobot/config.resolved.json")
    
    # Load config
    with open(config_path) as f:
        config = json.load(f)
    
    # Override with env vars
    if os.getenv("LLM_API_KEY"):
        config.setdefault("providers", {}).setdefault("custom", {})["apiKey"] = os.getenv("LLM_API_KEY")
    if os.getenv("LLM_API_BASE_URL"):
        config.setdefault("providers", {}).setdefault("custom", {})["apiBase"] = os.getenv("LLM_API_BASE_URL")
    if os.getenv("LLM_API_MODEL"):
        config.setdefault("agents", {}).setdefault("defaults", {})["model"] = os.getenv("LLM_API_MODEL")
    
    # LMS MCP env vars
    if os.getenv("NANOBOT_LMS_BACKEND_URL") and "tools" in config and "mcpServers" in config["tools"] and "lms" in config["tools"]["mcpServers"]:
        config["tools"]["mcpServers"]["lms"].setdefault("env", {})["NANOBOT_LMS_BACKEND_URL"] = os.getenv("NANOBOT_LMS_BACKEND_URL")
    if os.getenv("NANOBOT_LMS_API_KEY") and "tools" in config and "mcpServers" in config["tools"] and "lms" in config["tools"]["mcpServers"]:
        config["tools"]["mcpServers"]["lms"].setdefault("env", {})["NANOBOT_LMS_API_KEY"] = os.getenv("NANOBOT_LMS_API_KEY")
    
    # Write resolved config
    with open(resolved_path, "w") as f:
        json.dump(config, f, indent=2)
    
    # Run nanobot gateway
    os.execvp("nanobot", ["nanobot", "gateway", "--config", str(resolved_path)])

if __name__ == "__main__":
    main()
