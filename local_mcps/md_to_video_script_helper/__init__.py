from mcp.server.fastmcp import FastMCP


_md_to_video_script_prompt = """
请你根据md内容来制作一个视频脚本，步骤如下，
- 将md内容使用 drawio 来表示
- 文章分页来表示，一页一个drawio文件
- 一个 drawio(xxxx.drawio) 文件，对应一个讲解的旁白文件txt(xxx_script.txt), 目标是将内容讲清楚
- drawio 格式优美，内容充实，配色搭配得当，看起来像PPT一样美观，PPT风格，科技感
- 做之前请先把分页的大纲梳理好
- 每页内容可以承上启下，并且内容丰富就像PPT一样 
- 注意drawio 绘制时，文字不要越界，不要溢出，不要重叠
- 注意旁白文件 xxx_script.txt 应该是直接给旁白内容，不要包含其他无关的
- 注意旁白内容不要出现这样 `pip install xxx` 这样的命令，而是要使用中文来描述, 例如 `安装 xxx`，避免语音无法解读
- 但是可以drawio 可以存在代码块，因为需要看这个
- 注意可能存在代码块过长，数据过多，导致撑爆页面，这时需要将数据布局修改一下，能够容纳下所有内容，不要数据重叠
- 注意在 XML 文件中，& 字符是特殊字符，必须转义为 &amp;，否则会导致解析错误。其他需要转义的字符包括：& → &amp; < → &lt; > → &gt;
- 最后对内容写一个简介.md , 格式如下：
  - # xxxx
  - 1. xxxx
  - 2. xxxx
- 将上诉内容 写到某个目录中


以下是一个带有科技感drawio绘制示例，风格美化可以借鉴这个
```xml
<mxfile host="Electron" modified="2025-12-24T00:00:00.000Z" agent="5.0" version="21.0.0" etag="xxx" type="device">
  <diagram name="第1页-封面" id="cover-page">
    <mxGraphModel dx="1434" dy="844" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1920" pageHeight="1080" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- 1. 背景层 -->
        <!-- 深色科技背景 -->
        <mxCell id="bg-dark" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#111111;strokeColor=none;" vertex="1" parent="1">
          <mxGeometry x="0" y="0" width="1920" height="1080" as="geometry" />
        </mxCell>
        
        <!-- 装饰网格 (右上) -->
        <mxCell id="grid-pattern-1" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#333333;strokeWidth=1;dashed=1;dashPattern=1 4;" vertex="1" parent="1">
          <mxGeometry x="1200" y="-100" width="800" height="800" as="geometry" />
        </mxCell>
        
        <!-- 装饰光晕 (左上) -->
        <mxCell id="glow-1" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#76FF03;strokeColor=none;opacity=10;gradientColor=none;" vertex="1" parent="1">
          <mxGeometry x="-200" y="-200" width="800" height="800" as="geometry" />
        </mxCell>
        
        <!-- 装饰光晕 (右下) -->
        <mxCell id="glow-2" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#00B0FF;strokeColor=none;opacity=10;gradientColor=none;" vertex="1" parent="1">
          <mxGeometry x="1400" y="600" width="800" height="800" as="geometry" />
        </mxCell>

        <!-- 装饰代码背景 (左侧隐约可见) -->
        <mxCell id="bg-code" value="@ct.kernel&#xa;def vector_add(a, b, c):&#xa;    pid = ct.bid(0)&#xa;    tile = ct.load(a, index=pid)&#xa;    res = tile * 2&#xa;    ct.store(c, index=pid, tile=res)" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=24;fontFamily=Courier New;fontColor=#444444;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="100" y="100" width="600" height="300" as="geometry" />
        </mxCell>

        <!-- 2. 主体内容层 -->
        
        <!-- 品牌标识 -->
        <mxCell id="brand-tag" value="NVIDIA TILE PROGRAMMING" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#76FF03;strokeWidth=2;fontSize=20;fontColor=#76FF03;fontStyle=1;spacingLeft=20;spacingRight=20;" vertex="1" parent="1">
          <mxGeometry x="200" y="320" width="340" height="50" as="geometry" />
        </mxCell>

        <!-- 主标题 -->
        <mxCell id="title-main" value="cuTile Python" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=140;fontStyle=1;fontColor=#FFFFFF;fontFamily=Arial;" vertex="1" parent="1">
          <mxGeometry x="190" y="380" width="1200" height="160" as="geometry" />
        </mxCell>
        
        <!-- 副标题 -->
        <mxCell id="title-sub" value="QUICK START GUIDE" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=60;fontColor=#B0BEC5;fontFamily=Arial;fontStyle=1;letterSpacing=5;" vertex="1" parent="1">
          <mxGeometry x="200" y="540" width="800" height="80" as="geometry" />
        </mxCell>
        
        <!-- 装饰线条 -->
        <mxCell id="line-accent" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#76FF03;strokeColor=none;" vertex="1" parent="1">
          <mxGeometry x="200" y="640" width="120" height="8" as="geometry" />
        </mxCell>

        <!-- 3. 特性展示层 (右侧卡片组) -->
        
        <!-- 卡片容器 (半透明玻璃效果模拟) -->
        <!-- 特性 1 -->
        <mxCell id="card-1" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#212121;strokeColor=#424242;strokeWidth=2;opacity=90;" vertex="1" parent="1">
          <mxGeometry x="1200" y="300" width="500" height="140" as="geometry" />
        </mxCell>
        <mxCell id="card-1-icon" value="🚀" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=60;" vertex="1" parent="1">
          <mxGeometry x="1230" y="330" width="80" height="80" as="geometry" />
        </mxCell>
        <mxCell id="card-1-title" value="High Performance" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=36;fontStyle=1;fontColor=#FFFFFF;" vertex="1" parent="1">
          <mxGeometry x="1330" y="325" width="350" height="50" as="geometry" />
        </mxCell>
        <mxCell id="card-1-desc" value="极致的 GPU 并行计算性能" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#9E9E9E;" vertex="1" parent="1">
          <mxGeometry x="1330" y="375" width="350" height="40" as="geometry" />
        </mxCell>

        <!-- 特性 2 -->
        <mxCell id="card-2" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#212121;strokeColor=#424242;strokeWidth=2;opacity=90;" vertex="1" parent="1">
          <mxGeometry x="1250" y="470" width="500" height="140" as="geometry" />
        </mxCell>
        <mxCell id="card-2-icon" value="🧩" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=60;" vertex="1" parent="1">
          <mxGeometry x="1280" y="500" width="80" height="80" as="geometry" />
        </mxCell>
        <mxCell id="card-2-title" value="Tile Abstraction" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=36;fontStyle=1;fontColor=#FFFFFF;" vertex="1" parent="1">
          <mxGeometry x="1380" y="495" width="350" height="50" as="geometry" />
        </mxCell>
        <mxCell id="card-2-desc" value="以数据块为核心的高层抽象" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#9E9E9E;" vertex="1" parent="1">
          <mxGeometry x="1380" y="545" width="350" height="40" as="geometry" />
        </mxCell>

        <!-- 特性 3 -->
        <mxCell id="card-3" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#212121;strokeColor=#424242;strokeWidth=2;opacity=90;" vertex="1" parent="1">
          <mxGeometry x="1300" y="640" width="500" height="140" as="geometry" />
        </mxCell>
        <mxCell id="card-3-icon" value="🐍" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=60;" vertex="1" parent="1">
          <mxGeometry x="1330" y="670" width="80" height="80" as="geometry" />
        </mxCell>
        <mxCell id="card-3-title" value="Python Native" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=36;fontStyle=1;fontColor=#FFFFFF;" vertex="1" parent="1">
          <mxGeometry x="1430" y="665" width="350" height="50" as="geometry" />
        </mxCell>
        <mxCell id="card-3-desc" value="简洁优雅的 Python 接口" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#9E9E9E;" vertex="1" parent="1">
          <mxGeometry x="1430" y="715" width="350" height="40" as="geometry" />
        </mxCell>

        <!-- 4. 底部信息 -->
        
        <mxCell id="footer-logo" value="NVIDIA" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=32;fontStyle=1;fontColor=#76FF03;fontFamily=Arial;" vertex="1" parent="1">
          <mxGeometry x="200" y="900" width="200" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="footer-text" value="Developer Zone" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#B0BEC5;" vertex="1" parent="1">
          <mxGeometry x="340" y="904" width="200" height="40" as="geometry" />
        </mxCell>

        <mxCell id="page-number" value="01" style="text;html=1;strokeColor=none;fillColor=none;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=120;fontStyle=1;fontColor=#333333;fontFamily=Arial;" vertex="1" parent="1">
          <mxGeometry x="1650" y="880" width="200" height="150" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>

```

"""

def register_md_to_video_script_helper_tools(mcp: FastMCP):
    """注册markdown转视频的脚本工具"""
    
    @mcp.tool()
    def md_to_video_script_prompt() -> str:
        """markdown转视频脚本的提示词"""
        return _md_to_video_script_prompt
