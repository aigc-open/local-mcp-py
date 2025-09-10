# mcps/cli.py
"""命令行接口模块 - 提供各种MCP服务器启动命令"""

import sys
import argparse
from mcp.server.fastmcp import FastMCP
from .code_helper import register_code_helper_tools

class MCP:
    """MCP服务器"""
    
    @staticmethod
    def main():
        mcp = FastMCP()
        register_code_helper_tools(mcp)
        mcp.run(transport='stdio')
        return mcp

    @staticmethod
    def code_helper():
        mcp = FastMCP()
        register_code_helper_tools(mcp)
        mcp.run(transport='stdio')
        return mcp


if __name__ == "__main__":
    from fire import Fire
    Fire(MCP)