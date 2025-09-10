# mcps/cli.py
"""命令行接口模块 - 提供各种MCP服务器启动命令"""

import sys
import argparse
from mcp.server.fastmcp import FastMCP
from .code_helper import register_code_helper_tools


def run():
    """创建包含所有工具的完整MCP服务器"""
    mcp = FastMCP()
    register_code_helper_tools(mcp)
    return mcp


if __name__ == "__main__":
    run() 