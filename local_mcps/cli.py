# local_mcps/cli.py
"""命令行接口模块 - 提供各种MCP服务器启动命令"""

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