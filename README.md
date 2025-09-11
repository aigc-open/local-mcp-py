# Local MCP Python

一个基于 MCP (Model Context Protocol) 的 Python 代码辅助工具服务器。

## 🚀 特性

- **代码辅助工具**: 提供代码审查、代码解释、调试帮助等功能
- **MCP 协议支持**: 基于标准的 Model Context Protocol
- **Fire 命令行接口**: 使用 Python Fire 提供灵活的命令行接口
- **易于扩展**: 模块化设计，便于添加新功能

## 📦 安装

### 方式1: 从源码安装

```bash
# 克隆项目
git clone https://github.com/aigc-open/local-mcp-py.git
cd local-mcp-py

# 安装依赖并构建
pip install build
python -m build

# 安装构建的包
pip install dist/local_mcp_py-0.1.0-py3-none-any.whl
```

### 方式2: 开发模式安装

```bash
# 在项目根目录
pip install -e .
```

## 🔧 工具模块

### 代码辅助工具 (`code_helper`)
- `code_review_prompt()` - 生成代码审查提示模板
- `explain_code_prompt()` - 生成代码解释提示模板  
- `debug_help_prompt(code, error_message)` - 生成调试帮助提示

## 🎯 使用方法

### 命令行工具

项目使用 Python Fire 提供命令行接口，支持以下使用方式：

```bash
# 启动主 MCP 服务器
python -m local_mcps.cli main

# 启动代码辅助工具服务器
python -m local_mcps.cli code_helper

# 查看所有可用命令
python -m local_mcps.cli --help
```

### 编程方式使用

```python
from local_mcps.cli import MCP

# 方式1: 使用主服务器
mcp_instance = MCP.main()

# 方式2: 使用代码辅助服务器
mcp_instance = MCP.code_helper()
```

### 直接使用模块

```python
from mcp.server.fastmcp import FastMCP
from local_mcps.code_helper import register_code_helper_tools

# 创建自定义 MCP 服务器
mcp = FastMCP()
register_code_helper_tools(mcp)
mcp.run(transport='stdio')
```

### MCP 工具调用示例

```python
# 代码审查提示
review_prompt = code_review_prompt()

# 代码解释提示  
explain_prompt = explain_code_prompt()

# 调试帮助提示
debug_prompt = debug_help_prompt(
    code="your_code_here", 
    error_message="error_details"
)
```

## 🛠️ 开发

### 项目结构

```
local-mcp-py/
├── local_mcps/                    # 主包
│   ├── __init__.py         # 包初始化
│   ├── cli.py              # Fire 命令行接口
│   ├── code_helper.py      # 代码辅助工具
│   └── cpu_operator.py     # CPU操作工具
├── setup.py                # 传统打包配置
├── pyproject.toml          # 现代打包配置
├── MANIFEST.in             # 包含文件配置
└── README.md               # 项目说明
```

### 构建和打包

```bash
# 构建包
python -m build

# 只构建 wheel
python -m build --wheel

# 只构建源码包
python -m build --sdist

# 验证包
python -m twine check dist/*
```

### 添加新模块

1. 在 `local_mcps/` 目录创建新的模块文件
2. 实现 `register_xxx_tools(mcp)` 函数
3. 在模块中添加 MCP 工具装饰器 `@mcp.tool()`
4. 在 `local_mcps/cli.py` 的 `MCP` 类中添加对应的方法
5. 使用 Fire 自动生成命令行接口

### 开发示例

```python
# local_mcps/your_module.py
from mcp.server.fastmcp import FastMCP

def register_your_tools(mcp: FastMCP):
    """注册你的工具"""
    
    @mcp.tool()
    def your_tool_function(param: str) -> str:
        """工具描述"""
        return f"处理结果: {param}"

# 在 local_mcps/cli.py 中添加方法
class MCP:
    @staticmethod
    def your_module():
        """启动你的模块服务器"""
        mcp = FastMCP()
        register_your_tools(mcp)
        mcp.run(transport='stdio')
        return mcp
```

### 本地开发和测试

```bash
# 直接运行 CLI
python local_mcps/cli.py main
python local_mcps/cli.py code_helper

# 使用 Fire 查看帮助
python local_mcps/cli.py --help
python local_mcps/cli.py main --help
```

## 📋 依赖

- Python >= 3.8
- mcp >= 1.0.0
- fire >= 0.7.0

## 🌟 项目信息

- **作者**: AIGC-Open
- **邮箱**: aigc-open@gmail.com
- **仓库**: https://github.com/aigc-open/local-mcp-py
- **许可证**: MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 支持

如有问题，请在 [GitHub](https://github.com/aigc-open/local-mcp-py/issues) 上创建 Issue。