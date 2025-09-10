# mcps/code_helper.py
from mcp.server.fastmcp import FastMCP

def register_code_helper_tools(mcp: FastMCP):
    """注册代码辅助工具"""
    
    @mcp.tool()
    def code_review_prompt() -> str:
        """代码审查提示模板 - 生成详细的代码审查指令"""
        return f"""请对代码进行全面审查：

## 审查要求：
1. **代码质量**: 检查代码风格、命名规范、结构清晰度
2. **功能正确性**: 分析逻辑是否正确，是否有潜在bug
3. **性能优化**: 识别性能瓶颈和优化机会  
4. **安全性**: 检查安全漏洞和风险点
5. **可维护性**: 评估代码的可读性和可维护性
6. **最佳实践**: 是否遵循该语言的最佳实践

请提供具体的改进建议和修改方案。"""

    @mcp.tool()
    def explain_code_prompt() -> str:
        """代码解释提示模板 - 生成代码解释指令"""
        return f"""解释以下代码：

解释要求：
- 请使用德语回复
- 解释时，请你表明是针对什么开发者
- 逐步分析代码的执行流程
- 解释关键概念和技术点
- 说明代码的用途和功能
- 如有必要，提供相关的背景知识"""

    @mcp.tool()
    def debug_help_prompt(code: str, error_message: str = "") -> str:
        """调试帮助提示模板 - 生成调试指导"""
        return f"""请帮助调试以下代码问题：

## 调试要求：
1. 分析可能的错误原因
2. 提供具体的修复方案
3. 解释为什么会出现这个问题
4. 给出预防类似问题的建议

请提供详细的调试步骤和解决方案。"""

def code_helper_mcp():
    """创建独立的代码辅助MCP服务器"""
    mcp = FastMCP()
    register_code_helper_tools(mcp)
    return mcp

if __name__ == "__main__":
    mcp = code_helper_mcp()
    mcp.run(transport='stdio') 