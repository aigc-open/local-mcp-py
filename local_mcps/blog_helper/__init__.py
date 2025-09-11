from mcp.server.fastmcp import FastMCP


_write_blog_prompt = """
你是一个博客开发专家，请根据给出标题与内容，撰写一篇博客
## 撰写要求：
- 你精通博客开发，熟悉博客开发过程
- 你精通前后端，运维, 深度学习算法, 数据分析，大模型等技术
- 你精通语言Python，Go，Java，C++，C，Rust，等等
- 请你根据给出标题与内容，撰写一篇博客
- 最后生成一个 xxx.md 文件,命名规范为 博客名称_博客.md
- 内容中可以有代码块，有流程图等辅助理解的内容
"""

def register_blog_helper_tools(mcp: FastMCP):
    """注册博客辅助工具"""
    
    @mcp.tool()
    def write_blog_prompt(title: str, content: str) -> str:
        """撰写技术博客的提示词"""
        return _write_blog_prompt
    