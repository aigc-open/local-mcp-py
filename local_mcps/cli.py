# local_mcps/cli.py
"""命令行接口模块 - 提供各种MCP服务器启动命令"""

import json
import sys
import argparse
from typing import Literal
from mcp.server.fastmcp import FastMCP
from .code_helper import register_code_helper_tools
from .operator_helper import register_operator_helper_tools

class MCP:
    """MCP服务器"""
    
    @staticmethod
    def main(transport: Literal['stdio', 'sse', 'streamable-http'] = 'stdio'):
        mcp = FastMCP()
        register_code_helper_tools(mcp)
        register_operator_helper_tools(mcp)
        mcp.run(transport=transport)
        return mcp
    
    @staticmethod
    def init_cursor_mcp():
        import os

        cursor_dir = os.path.expanduser("~/.cursor")
        os.makedirs(cursor_dir, exist_ok=True)
        mcp_json_path = os.path.join(cursor_dir, "mcp.json")

        # 先读取原有内容
        if os.path.exists(mcp_json_path):
            with open(mcp_json_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except Exception:
                    data = {}
        else:
            data = {}

        # 保证mcpServers为dict
        if "mcpServers" not in data or not isinstance(data["mcpServers"], dict):
            data["mcpServers"] = {}

        # 替换或新加 code_helper
        data["mcpServers"]["local_mcps"] = {
            "command": "python",
            "args": ["-m", "local_mcps.cli", "main"],
            "env": {}
        }

        with open(mcp_json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def code_helper(transport: Literal['stdio', 'sse', 'streamable-http'] = 'stdio'):
        mcp = FastMCP()
        register_code_helper_tools(mcp)
        mcp.run(transport=transport)
        return mcp
    
    @staticmethod
    def operator_helper(transport: Literal['stdio', 'sse', 'streamable-http'] = 'stdio'):
        mcp = FastMCP()
        register_operator_helper_tools(mcp)
        mcp.run(transport=transport)
        return mcp


if __name__ == "__main__":
    from fire import Fire
    Fire(MCP)