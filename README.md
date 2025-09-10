# Local MCP Python

一个基于 MCP (Model Context Protocol) 的 Python 代码辅助工具服务器。

## 🚀 特性

- **代码辅助工具**: 提供代码审查、代码解释、调试帮助等功能
- **MCP 协议支持**: 基于标准的 Model Context Protocol
- **命令行支持**: 提供简单易用的命令行接口
- **易于扩展**: 模块化设计，便于添加新功能

## 📦 安装

### 方式1: 从源码安装

```bash
# 克隆项目
git clone https://github.com/yourusername/local-mcp-py.git
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

安装后，你将获得以下命令：

```bash
# 主要命令
local-mcp           # 启动 MCP 服务器
local-mcp-code      # 启动代码辅助工具服务器
```

### 编程方式使用

```python
from mcps.cli import run
from mcps.code_helper import code_helper_mcp

# 方式1: 使用主服务器
mcp = run()
mcp.run(transport='stdio')

# 方式2: 使用代码辅助服务器
mcp = code_helper_mcp()
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
├── mcps/                    # 主包
│   ├── __init__.py         # 包初始化
│   ├── cli.py              # 命令行接口
│   ├── code_helper.py      # 代码辅助工具
│   └── operator.py         # 操作工具（待开发）
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

1. 在 `mcps/` 目录创建新的模块文件
2. 实现 `register_xxx_tools(mcp)` 函数
3. 在模块中添加 MCP 工具装饰器 `@mcp.tool()`
4. 在 `mcps/cli.py` 中添加对应的命令行入口
5. 更新 `setup.py` 或 `pyproject.toml` 中的入口点

### 开发示例

```python
# mcps/your_module.py
from mcp.server.fastmcp import FastMCP

def register_your_tools(mcp: FastMCP):
    """注册你的工具"""
    
    @mcp.tool()
    def your_tool_function(param: str) -> str:
        """工具描述"""
        return f"处理结果: {param}"

def your_module_mcp():
    """创建独立的MCP服务器"""
    mcp = FastMCP()
    register_your_tools(mcp)
    return mcp
```

## 📋 依赖

- Python >= 3.8
- mcp >= 1.0.0

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 支持

如有问题，请在 GitHub 上创建 Issue。