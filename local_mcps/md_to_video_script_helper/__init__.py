from mcp.server.fastmcp import FastMCP


_md_to_video_script_prompt = """
请你根据md内容来制作一个视频脚本，步骤如下，
- 将md内容使用 drawio 来表示
- 文章分页来表示，一页一个drawio文件
- 一个 drawio(xxxx.drawio) 文件，对应一个讲解的旁白文件txt(xxx_script.txt), 目标是将内容讲清楚
- drawio 格式优美，内容充实，配色搭配得当，看起来像PPT一样美观
- 做之前请先把分页的大纲梳理好
- 每页内容可以承上启下，并且内容丰富就像PPT一样 
- 注意旁白文件 xxx_script.txt 应该是直接给旁白内容，不要包含其他无关的
- 注意旁白内容不要出现这样 `pip install xxx` 这样的命令，而是要使用中文来描述, 例如 `安装 xxx`，避免语音无法解读
- 将上诉内容 写到某个目录中
"""

def register_md_to_video_script_helper_tools(mcp: FastMCP):
    """注册markdown转视频的脚本工具"""
    
    @mcp.tool()
    def md_to_video_script_prompt() -> str:
        """markdown转视频脚本的提示词"""
        return _md_to_video_script_prompt