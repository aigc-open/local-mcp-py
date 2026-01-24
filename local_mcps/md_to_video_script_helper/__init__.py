from mcp.server.fastmcp import FastMCP


_md_to_video_script_prompt = """
请你根据md内容来制作一个视频脚本，步骤如下
- 将md内容使用 drawio 来表示
- 文章分页来表示，一页一个drawio文件
- 一个 drawio(xxxx.drawio) 文件，对应一个讲解的旁白文件txt(xxx_tts.txt), 目标是将内容讲清楚
- drawio 格式优美，内容充实，配色搭配得当，看起来像PPT一样美观，PPT风格，科技感
- 做之前请先把分页的大纲梳理好
- 每页内容可以承上启下，并且内容丰富就像PPT一样 
- 注意drawio 绘制时，文字不要越界，不要溢出，不要重叠
- 注意旁白文件 xxx_tts.txt 应该是直接给旁白内容，不要包含其他无关的
- 注意旁白内容不要出现这样 `pip install xxx` 这样的命令，而是要使用中文来描述, 例如 `安装 xxx`，避免语音无法解读
- 但是可以drawio 可以存在代码块，因为需要看这个
- 注意代码块需要注意缩进等，保证美观
- 注意可能存在代码块过长，数据过多，导致撑爆页面，这时需要将数据布局修改一下，能够容纳下所有内容，不要数据重叠
- 注意在 XML 文件中，& 字符是特殊字符，必须转义为 &amp;，否则会导致解析错误。其他需要转义的字符包括：& → &amp; < → &lt; > → &gt;
- 最后对内容写一个简介.md , 不要超过1000字，格式如下：
  - # xxxx
  - 1. xxxx
  - 2. xxxx
- 将上诉内容 写到某个目录中
- 最后可以告知用户使用`python -m txt_images_to_ai_video drawio export --help` 可以将drawio转换png


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


这是一个内容参考绘制drawio示例
<mxfile host="Electron" modified="2025-01-03T00:00:00.000Z" agent="5.0" version="21.0.0" type="device">
  <diagram name="第4页-推理流程" id="inference-flow-page">
    <mxGraphModel dx="1434" dy="844" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1920" pageHeight="1080" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- 背景层 -->
        <mxCell id="bg-light" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#F8F9FA;strokeColor=none;" vertex="1" parent="1">
          <mxGeometry x="0" y="0" width="1920" height="1080" as="geometry" />
        </mxCell>
        
        <!-- 标题 -->
        <mxCell id="title" value="模型推理阶段" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=56;fontStyle=1;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="100" y="50" width="600" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="subtitle" value="异步处理与流式输出的完整流程" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=28;fontColor=#888888;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="100" y="130" width="700" height="50" as="geometry" />
        </mxCell>

        <!-- 左侧流程图 -->
        <mxCell id="phase-title1" value="请求处理阶段" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=32;fontStyle=1;fontColor=#4A90E2;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="100" y="210" width="300" height="50" as="geometry" />
        </mxCell>
        
        <!-- 步骤1 -->
        <mxCell id="step1-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#4A90E2;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="100" y="280" width="550" height="70" as="geometry" />
        </mxCell>
        <mxCell id="step1-num" value="1" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#4A90E2;strokeColor=none;fontColor=#FFFFFF;fontSize=24;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="115" y="295" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="step1-text" value="用户调用 generate" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="170" y="300" width="460" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="arrow1" value="" style="endArrow=classic;html=1;strokeColor=#4A90E2;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="375" y="350" as="sourcePoint" />
            <mxPoint x="375" y="375" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <!-- 步骤2 -->
        <mxCell id="step2-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E9;strokeColor=#4CAF50;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="100" y="375" width="550" height="70" as="geometry" />
        </mxCell>
        <mxCell id="step2-num" value="2" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#4CAF50;strokeColor=none;fontColor=#FFFFFF;fontSize=24;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="115" y="390" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="step2-text" value="add_request 添加请求到队列" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="170" y="395" width="460" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="arrow2" value="" style="endArrow=classic;html=1;strokeColor=#4A90E2;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="375" y="445" as="sourcePoint" />
            <mxPoint x="375" y="470" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <!-- 步骤3 -->
        <mxCell id="step3-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="100" y="470" width="550" height="70" as="geometry" />
        </mxCell>
        <mxCell id="step3-num" value="3" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FF9800;strokeColor=none;fontColor=#FFFFFF;fontSize=24;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="115" y="485" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="step3-text" value="Scheduler 将请求添加到 WAITING 状态" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="170" y="490" width="460" height="30" as="geometry" />
        </mxCell>

        <!-- 中间流程图 -->
        <mxCell id="phase-title2" value="调度执行阶段" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=32;fontStyle=1;fontColor=#FF9800;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="720" y="210" width="300" height="50" as="geometry" />
        </mxCell>
        
        <!-- 步骤4 -->
        <mxCell id="step4-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E5F5;strokeColor=#9C27B0;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="720" y="280" width="550" height="70" as="geometry" />
        </mxCell>
        <mxCell id="step4-num" value="4" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#9C27B0;strokeColor=none;fontColor=#FFFFFF;fontSize=24;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="735" y="295" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="step4-text" value="output_handler 后台循环拉取输出" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="790" y="300" width="460" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="arrow4" value="" style="endArrow=classic;html=1;strokeColor=#4A90E2;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="995" y="350" as="sourcePoint" />
            <mxPoint x="995" y="375" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <!-- 步骤5 -->
        <mxCell id="step5-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#E91E63;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="720" y="375" width="550" height="70" as="geometry" />
        </mxCell>
        <mxCell id="step5-num" value="5" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#E91E63;strokeColor=none;fontColor=#FFFFFF;fontSize=24;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="735" y="390" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="step5-text" value="Scheduler.schedule 智能调度请求" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="790" y="395" width="460" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="arrow5" value="" style="endArrow=classic;html=1;strokeColor=#4A90E2;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="995" y="445" as="sourcePoint" />
            <mxPoint x="995" y="470" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <!-- 步骤6 -->
        <mxCell id="step6-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E0F2F1;strokeColor=#00BCD4;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="720" y="470" width="550" height="70" as="geometry" />
        </mxCell>
        <mxCell id="step6-num" value="6" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#00BCD4;strokeColor=none;fontColor=#FFFFFF;fontSize=24;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="735" y="485" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="step6-text" value="ModelExecutor.execute_model 执行推理" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="790" y="490" width="460" height="30" as="geometry" />
        </mxCell>

        <!-- 底部流程图 -->
        <mxCell id="phase-title3" value="结果处理阶段" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=32;fontStyle=1;fontColor=#9C27B0;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="1340" y="210" width="300" height="50" as="geometry" />
        </mxCell>
        
        <!-- 步骤7 -->
        <mxCell id="step7-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#4A90E2;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="1340" y="280" width="480" height="70" as="geometry" />
        </mxCell>
        <mxCell id="step7-num" value="7" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#4A90E2;strokeColor=none;fontColor=#FFFFFF;fontSize=24;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1355" y="295" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="step7-text" value="模型前向传播计算" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="1410" y="300" width="390" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="arrow7" value="" style="endArrow=classic;html=1;strokeColor=#4A90E2;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="1580" y="350" as="sourcePoint" />
            <mxPoint x="1580" y="375" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <!-- 步骤8 -->
        <mxCell id="step8-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E9;strokeColor=#4CAF50;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="1340" y="375" width="480" height="70" as="geometry" />
        </mxCell>
        <mxCell id="step8-num" value="8" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#4CAF50;strokeColor=none;fontColor=#FFFFFF;fontSize=24;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1355" y="390" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="step8-text" value="采样解码生成 token" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="1410" y="395" width="390" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="arrow8" value="" style="endArrow=classic;html=1;strokeColor=#4A90E2;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="1580" y="445" as="sourcePoint" />
            <mxPoint x="1580" y="470" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <!-- 步骤9 -->
        <mxCell id="step9-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FF9800;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="1340" y="470" width="480" height="70" as="geometry" />
        </mxCell>
        <mxCell id="step9-num" value="9" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FF9800;strokeColor=none;fontColor=#FFFFFF;fontSize=24;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1355" y="485" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="step9-text" value="更新调度器状态" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="1410" y="490" width="390" height="30" as="geometry" />
        </mxCell>

        <!-- 关键特性 -->
        <mxCell id="features-title" value="推理阶段关键特性" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=36;fontStyle=1;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="100" y="590" width="1720" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="feature1-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E0E0E0;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="100" y="670" width="380" height="120" as="geometry" />
        </mxCell>
        <mxCell id="feature1-icon" value="🔄" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=50;" vertex="1" parent="1">
          <mxGeometry x="120" y="690" width="70" height="70" as="geometry" />
        </mxCell>
        <mxCell id="feature1-title" value="异步处理" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=26;fontStyle=1;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="200" y="690" width="260" height="35" as="geometry" />
        </mxCell>
        <mxCell id="feature1-desc" value="完全异步的 API 设计&#xa;非阻塞处理流程" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=20;fontColor=#666666;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="200" y="725" width="260" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="feature2-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E0E0E0;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="510" y="670" width="380" height="120" as="geometry" />
        </mxCell>
        <mxCell id="feature2-icon" value="📦" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=50;" vertex="1" parent="1">
          <mxGeometry x="530" y="690" width="70" height="70" as="geometry" />
        </mxCell>
        <mxCell id="feature2-title" value="连续批处理" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=26;fontStyle=1;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="610" y="690" width="260" height="35" as="geometry" />
        </mxCell>
        <mxCell id="feature2-desc" value="动态组织不同长度序列&#xa;消除等待时间" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=20;fontColor=#666666;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="610" y="725" width="260" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="feature3-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E0E0E0;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="920" y="670" width="380" height="120" as="geometry" />
        </mxCell>
        <mxCell id="feature3-icon" value="💾" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=50;" vertex="1" parent="1">
          <mxGeometry x="940" y="690" width="70" height="70" as="geometry" />
        </mxCell>
        <mxCell id="feature3-title" value="PagedAttention" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=26;fontStyle=1;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="1020" y="690" width="260" height="35" as="geometry" />
        </mxCell>
        <mxCell id="feature3-desc" value="高效内存管理&#xa;智能 KV 缓存分配" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=20;fontColor=#666666;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="1020" y="725" width="260" height="50" as="geometry" />
        </mxCell>
        
        <mxCell id="feature4-bg" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E0E0E0;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="1330" y="670" width="380" height="120" as="geometry" />
        </mxCell>
        <mxCell id="feature4-icon" value="📊" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=50;" vertex="1" parent="1">
          <mxGeometry x="1350" y="690" width="70" height="70" as="geometry" />
        </mxCell>
        <mxCell id="feature4-title" value="流式输出" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=26;fontStyle=1;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="1430" y="690" width="260" height="35" as="geometry" />
        </mxCell>
        <mxCell id="feature4-desc" value="实时返回生成结果&#xa;AsyncGenerator 支持" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=20;fontColor=#666666;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="1430" y="725" width="260" height="50" as="geometry" />
        </mxCell>

        <!-- 性能指标 -->
        <mxCell id="perf-title" value="推理性能指标" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=32;fontStyle=1;fontColor=#333333;fontFamily=Microsoft YaHei;" vertex="1" parent="1">
          <mxGeometry x="100" y="830" width="1720" height="45" as="geometry" />
        </mxCell>
        
        <mxCell id="perf-box" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#4A90E2;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="100" y="895" width="1720" height="90" as="geometry" />
        </mxCell>
        <mxCell id="perf-items" value="首 token 延迟: 50-200ms   |   生成速度: 20-100 tokens/s   |   批处理效率: 2-4倍提升   |   内存利用率: 80-95%   |   并发支持: 数百个请求" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontColor=#333333;fontFamily=Microsoft YaHei;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="150" y="920" width="1620" height="40" as="geometry" />
        </mxCell>

        <!-- 页码 -->
        <mxCell id="page-number" value="04" style="text;html=1;strokeColor=none;fillColor=none;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=80;fontStyle=1;fontColor=#E0E0E0;fontFamily=Arial;" vertex="1" parent="1">
          <mxGeometry x="1750" y="950" width="120" height="100" as="geometry" />
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
