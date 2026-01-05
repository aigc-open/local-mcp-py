from mcp.server.fastmcp import FastMCP



_draw_system_architecture_prompt = """
你是一个绘图专家，请根据给出内容，绘制一个系统架构图
## 绘制要求：
- 你精通绘图，熟悉绘图过程
- 你精通系统架构图，熟悉系统架构图的绘制过程
- 请你根据给出内容，绘制一个系统架构图
- 架构图层与层竖向布局，也就是从上到下布局，只有一大列
- 架构图层与层之间用箭头连接
- 架构图中尽量不要使用特殊字符
- 架构图中布局排列整齐，结构清晰
- 颜色协调
- 注意在 XML 文件中，& 字符是特殊字符，必须转义为 &amp;，否则会导致解析错误。其他需要转义的字符包括：& → &amp; < → &lt; > → &gt;
- 绘图时使用 drawio 来绘制，最后生成一个 xxx.drawio 文件,命名规范为 xxx_架构图.drawio

## 模版
```xml
<mxfile host="app.diagrams.net" modified="2024-01-01T00:00:00.000Z" agent="5.0" etag="xxx" version="22.0.0" type="device">
  <diagram name="系统整体架构图" id="system-architecture">
    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- 标题 -->
        <mxCell id="title" value="数字人系统整体架构图" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontStyle=1;fontColor=#2c3e50;" vertex="1" parent="1">
          <mxGeometry x="400" y="20" width="300" height="40" as="geometry" />
        </mxCell>

        <!-- 前端应用层 -->
        <mxCell id="frontend-layer" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1f5fe;strokeColor=#01579b;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="80" y="100" width="960" height="120" as="geometry" />
        </mxCell>
        <mxCell id="frontend-title" value="前端应用层" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;fontColor=#01579b;" vertex="1" parent="1">
          <mxGeometry x="100" y="110" width="100" height="30" as="geometry" />
        </mxCell>
        
        <!-- Windows桌面应用 -->
        <mxCell id="desktop-app" value="Windows桌面应用&#xa;WPF/Electron&#xa;本地处理优先" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff3e0;strokeColor=#ff6f00;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="120" y="150" width="150" height="60" as="geometry" />
        </mxCell>
        
        <!-- Web管理界面 -->
        <mxCell id="web-interface" value="Web管理界面&#xa;React/Vue&#xa;云端管理" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f3e5f5;strokeColor=#8e24aa;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="320" y="150" width="150" height="60" as="geometry" />
        </mxCell>
        
        <!-- 移动端轻量版 -->
        <mxCell id="mobile-app" value="移动端轻量版&#xa;React Native&#xa;云端处理" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e8f5e8;strokeColor=#388e3c;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="520" y="150" width="150" height="60" as="geometry" />
        </mxCell>
        
        <!-- API接口 -->
        <mxCell id="api-service" value="API服务接口&#xa;RESTful API&#xa;第三方集成" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fce4ec;strokeColor=#c2185b;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="720" y="150" width="150" height="60" as="geometry" />
        </mxCell>

        <!-- 核心处理层 -->
        <mxCell id="core-layer" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f3e5f5;strokeColor=#8e24aa;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="80" y="260" width="960" height="120" as="geometry" />
        </mxCell>
        <mxCell id="core-title" value="核心处理层" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;fontColor=#8e24aa;" vertex="1" parent="1">
          <mxGeometry x="100" y="270" width="100" height="30" as="geometry" />
        </mxCell>
        
        <!-- 数字人生成引擎 -->
        <mxCell id="avatar-engine" value="数字人生成引擎&#xa;3D建模 + 动画&#xa;实时渲染" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff3e0;strokeColor=#ff6f00;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="120" y="310" width="180" height="60" as="geometry" />
        </mxCell>
        
        <!-- 音视频处理模块 -->
        <mxCell id="media-processing" value="音视频处理模块&#xa;音频分析 + 编码&#xa;格式转换" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1f5fe;strokeColor=#01579b;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="340" y="310" width="180" height="60" as="geometry" />
        </mxCell>
        
        <!-- 实时渲染引擎 -->
        <mxCell id="render-engine" value="实时渲染引擎&#xa;GPU加速渲染&#xa;效果后处理" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e8f5e8;strokeColor=#388e3c;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="560" y="310" width="180" height="60" as="geometry" />
        </mxCell>
        
        <!-- 文件管理系统 -->
        <mxCell id="file-system" value="文件管理系统&#xa;项目管理 + 存储&#xa;版本控制" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fce4ec;strokeColor=#c2185b;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="780" y="310" width="180" height="60" as="geometry" />
        </mxCell>

        <!-- AI模型层 -->
        <mxCell id="ai-layer" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e8f5e8;strokeColor=#388e3c;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="80" y="420" width="960" height="120" as="geometry" />
        </mxCell>
        <mxCell id="ai-title" value="AI模型层" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;fontColor=#388e3c;" vertex="1" parent="1">
          <mxGeometry x="100" y="430" width="100" height="30" as="geometry" />
        </mxCell>
        
        <!-- 人脸重建模型 -->
        <mxCell id="face-model" value="人脸重建模型&#xa;3DMM/FLAME&#xa;高精度建模" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff3e0;strokeColor=#ff6f00;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="120" y="470" width="140" height="60" as="geometry" />
        </mxCell>
        
        <!-- 口型同步模型 -->
        <mxCell id="lipsync-model" value="口型同步模型&#xa;Wav2Lip++&#xa;多语言支持" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1f5fe;strokeColor=#01579b;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="300" y="470" width="140" height="60" as="geometry" />
        </mxCell>
        
        <!-- 动作生成模型 -->
        <mxCell id="motion-model" value="动作生成模型&#xa;骨骼动画系统&#xa;音乐驱动" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f3e5f5;strokeColor=#8e24aa;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="480" y="470" width="140" height="60" as="geometry" />
        </mxCell>
        
        <!-- 表情生成模型 -->
        <mxCell id="expression-model" value="表情生成模型&#xa;情感分析&#xa;微表情合成" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fce4ec;strokeColor=#c2185b;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="660" y="470" width="140" height="60" as="geometry" />
        </mxCell>
        
        <!-- 优化加速模块 -->
        <mxCell id="optimization" value="模型优化模块&#xa;量化加速&#xa;缓存机制" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e0f2f1;strokeColor=#00695c;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="840" y="470" width="140" height="60" as="geometry" />
        </mxCell>

        <!-- 部署层 -->
        <mxCell id="deploy-layer" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff3e0;strokeColor=#ff6f00;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="80" y="580" width="960" height="120" as="geometry" />
        </mxCell>
        <mxCell id="deploy-title" value="部署层" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;fontColor=#ff6f00;" vertex="1" parent="1">
          <mxGeometry x="100" y="590" width="100" height="30" as="geometry" />
        </mxCell>
        
        <!-- 本地部署 -->
        <mxCell id="local-deploy" value="本地部署&#xa;RTX 3060+&#xa;一键安装包&#xa;离线处理" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e8f5e8;strokeColor=#388e3c;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="150" y="620" width="150" height="70" as="geometry" />
        </mxCell>
        
        <!-- 云端部署 -->
        <mxCell id="cloud-deploy" value="云端部署&#xa;GPU集群&#xa;弹性扩容&#xa;高并发处理" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1f5fe;strokeColor=#01579b;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="370" y="620" width="150" height="70" as="geometry" />
        </mxCell>
        
        <!-- 混合部署 -->
        <mxCell id="hybrid-deploy" value="混合部署&#xa;智能调度&#xa;本地预览&#xa;云端渲染" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f3e5f5;strokeColor=#8e24aa;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="590" y="620" width="150" height="70" as="geometry" />
        </mxCell>
        
        <!-- 监控运维 -->
        <mxCell id="monitoring" value="监控运维&#xa;性能监控&#xa;日志分析&#xa;自动告警" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fce4ec;strokeColor=#c2185b;strokeWidth=2;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="810" y="620" width="150" height="70" as="geometry" />
        </mxCell>

        <!-- 数据流箭头 -->
        <mxCell id="arrow1" value="" style="endArrow=classic;html=1;strokeColor=#666666;strokeWidth=3;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="200" y="220" as="sourcePoint" />
            <mxPoint x="200" y="260" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="arrow2" value="" style="endArrow=classic;html=1;strokeColor=#666666;strokeWidth=3;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="400" y="220" as="sourcePoint" />
            <mxPoint x="400" y="260" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="arrow3" value="" style="endArrow=classic;html=1;strokeColor=#666666;strokeWidth=3;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="210" y="380" as="sourcePoint" />
            <mxPoint x="190" y="420" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="arrow4" value="" style="endArrow=classic;html=1;strokeColor=#666666;strokeWidth=3;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="430" y="380" as="sourcePoint" />
            <mxPoint x="370" y="420" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="arrow5" value="" style="endArrow=classic;html=1;strokeColor=#666666;strokeWidth=3;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="550" y="540" as="sourcePoint" />
            <mxPoint x="550" y="580" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 数据流标签 -->
        <mxCell id="flow-label1" value="用户请求" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#666666;" vertex="1" parent="1">
          <mxGeometry x="140" y="230" width="60" height="20" as="geometry" />
        </mxCell>
        
        <mxCell id="flow-label2" value="模型调用" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#666666;" vertex="1" parent="1">
          <mxGeometry x="140" y="390" width="60" height="20" as="geometry" />
        </mxCell>
        
        <mxCell id="flow-label3" value="部署执行" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#666666;" vertex="1" parent="1">
          <mxGeometry x="490" y="550" width="60" height="20" as="geometry" />
        </mxCell>

        <!-- 性能指标标注 -->
        <mxCell id="perf-note" value="性能目标：&#xa;• RTX 3060: 1080p@30fps&#xa;• 口型同步精度: 95%+&#xa;• 响应时间: &lt;5秒" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff9c4;strokeColor=#d4af37;strokeWidth=2;fontSize=10;fontStyle=0;align=left;" vertex="1" parent="1">
          <mxGeometry x="80" y="720" width="200" height="80" as="geometry" />
        </mxCell>
        
        <!-- 技术栈标注 -->
        <mxCell id="tech-note" value="核心技术栈：&#xa;• 前端: WPF, React, RN&#xa;• AI: PyTorch, ONNX&#xa;• 渲染: Unity, OpenGL&#xa;• 部署: Docker, K8s" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e0f7fa;strokeColor=#00acc1;strokeWidth=2;fontSize=10;fontStyle=0;align=left;" vertex="1" parent="1">
          <mxGeometry x="300" y="720" width="200" height="80" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

"""

_draw_system_flowchart_prompt = """
你是一个绘图专家，请根据给出内容，绘制一个系统流程图
## 绘制要求：
- 你精通绘图，熟悉绘图过程
- 你精通系统流程图，熟悉系统流程图的绘制过程
- 请你根据给出内容，绘制一个系统流程图
- 流程图中尽量不要使用特殊字符
- 流程图中布局排列整齐，结构清晰
- 节点与节点之间逻辑清晰
- 颜色协调
- 绘图时使用 drawio 来绘制，最后生成一个 xxx.drawio 文件,命名规范为 xxx_流程图.drawio
- 注意在 XML 文件中，& 字符是特殊字符，必须转义为 &amp;，否则会导致解析错误。其他需要转义的字符包括：& → &amp; < → &lt; > → &gt;

## 模版
```xml
<mxfile host="65bd71144e">
    <diagram name="便携式指针式仪表数据智能读取装置系统交互流程图" id="interaction-flow-diagram">
        <mxGraphModel dx="4006" dy="1211" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2400" pageHeight="2000" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="background" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=none;opacity=50;" parent="1" vertex="1">
                    <mxGeometry x="-60" width="2400" height="1040" as="geometry"/>
                </mxCell>
                <mxCell id="main-title" value="便携式指针式仪表数据智能读取装置系统交互流程图" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=32;fontStyle=1;fontColor=#1565c0;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="800" y="30" width="800" height="60" as="geometry"/>
                </mxCell>
                <mxCell id="sub-title" value="端-边-云协同工作流程 | 从图像采集到智能分析的完整数据链路" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontColor=#666666;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="800" y="90" width="800" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="step1" value="1⃣&lt;br&gt;&lt;b&gt;巡检人员&lt;/b&gt;&lt;br&gt;&lt;b&gt;现场拍摄&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;手持拍摄杆对准仪表&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4caf50;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="80" y="200" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step2" value="2⃣&lt;br&gt;&lt;b&gt;图像采集&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;4K高清拍摄&lt;br&gt;&lt;br&gt;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1976d2;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="280" y="200" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step3" value="3⃣&lt;br&gt;&lt;b&gt;元数据记录&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;时间戳、GPS位置&lt;br&gt;设备编号&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1976d2;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="480" y="200" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="quality-check" value="图像质量&lt;br&gt;是否合格？" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontFamily=Microsoft YaHei;shadow=1;" parent="1" vertex="1">
                    <mxGeometry x="500" y="320" width="100" height="80" as="geometry"/>
                </mxCell>
                <mxCell id="error-process" value="❌&lt;br&gt;&lt;b&gt;异常处理&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;重新拍摄&lt;br&gt;或人工校验&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffebee;strokeColor=#f44336;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="480" y="440" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step4" value="4⃣&lt;br&gt;&lt;b&gt;本地缓存&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;图片暂存&lt;br&gt;网络检测&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1976d2;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="680" y="200" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step5" value="5⃣&lt;br&gt;&lt;b&gt;数据传输&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;局域网&lt;br&gt;至边缘设备&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1976d2;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="880" y="200" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="network-check" value="网络&lt;br&gt;是否可用？" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontFamily=Microsoft YaHei;shadow=1;" parent="1" vertex="1">
                    <mxGeometry x="900" y="320" width="100" height="80" as="geometry"/>
                </mxCell>
                <mxCell id="offline-storage" value="📴&lt;br&gt;&lt;b&gt;离线存储&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;本地缓存&lt;br&gt;等待网络&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffebee;strokeColor=#f44336;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="880" y="440" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step6" value="6⃣&lt;br&gt;&lt;b&gt;图像预处理&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;去噪、增强&lt;br&gt;格式转换&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#7b1fa2;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1080" y="200" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step7" value="7⃣&lt;br&gt;&lt;b&gt;目标检测&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;PPYOLOE-Plus&lt;br&gt;仪表定位&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#7b1fa2;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1280" y="200" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step8" value="8⃣&lt;br&gt;&lt;b&gt;指针分割&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;OCRNet分割&lt;br&gt;角度计算&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#7b1fa2;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1480" y="200" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step9" value="9⃣&lt;br&gt;&lt;b&gt;刻度定位&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;HRNet定位&lt;br&gt;关键刻度&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#7b1fa2;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1680" y="200" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="confidence-check" value="识别置信度&lt;br&gt;是否足够？" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontFamily=Microsoft YaHei;shadow=1;" parent="1" vertex="1">
                    <mxGeometry x="1700" y="320" width="100" height="80" as="geometry"/>
                </mxCell>
                <mxCell id="manual-verify" value="👁️&lt;br&gt;&lt;b&gt;人工校验&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;专家审核&lt;br&gt;结果确认&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffebee;strokeColor=#f44336;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1680" y="440" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step10" value="10&lt;br&gt;&lt;b&gt;数值读取&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;PPOCR&lt;br&gt;量程解析&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#7b1fa2;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1880" y="200" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step11" value="11⃣&lt;br&gt;&lt;b&gt;融合计算&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;角度计算&lt;br&gt;数值转换&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#7b1fa2;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="2080" y="200" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step12" value="1⃣2⃣&lt;br&gt;&lt;b&gt;云端传输&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;网络上传&lt;br&gt;断点续传&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#f57c00;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="280" y="600" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step13" value="1⃣3⃣&lt;br&gt;&lt;b&gt;大模型辅助&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;异常检测&lt;br&gt;趋势分析&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#f57c00;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="480" y="600" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="anomaly-result" value="数据&lt;br&gt;是否异常？" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontFamily=Microsoft YaHei;shadow=1;" parent="1" vertex="1">
                    <mxGeometry x="500" y="720" width="100" height="80" as="geometry"/>
                </mxCell>
                <mxCell id="alert-trigger" value="⚠️&lt;br&gt;&lt;b&gt;预警触发&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;异常通知&lt;br&gt;紧急处理&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffebee;strokeColor=#f44336;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="480" y="840" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step14" value="1⃣4⃣&lt;br&gt;&lt;b&gt;数据存储&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;分布式数据库&lt;br&gt;设备档案&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#f57c00;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="680" y="600" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step15" value="1⃣5⃣&lt;br&gt;&lt;b&gt;智能分析&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;AI智能分析&lt;br&gt;&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#f57c00;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="880" y="600" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step16" value="1⃣6⃣&lt;br&gt;&lt;b&gt;实时监控&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;关键指标&lt;br&gt;预警触发&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#f57c00;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1080" y="600" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step17" value="1⃣7⃣&lt;br&gt;&lt;b&gt;结果反馈&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;终端显示&lt;br&gt;状态提示&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1976d2;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1280" y="600" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step18" value="1⃣8⃣&lt;br&gt;&lt;b&gt;数据大屏&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;可视化展示&lt;br&gt;实时监控&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#e91e63;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1480" y="600" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step19" value="1⃣9⃣&lt;br&gt;&lt;b&gt;管理平台&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;数据分析&lt;br&gt;报表生成&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#e91e63;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1680" y="600" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="step20" value="2⃣0⃣&lt;br&gt;&lt;b&gt;系统优化&lt;/b&gt;&lt;br&gt;&lt;font color=&quot;#666666&quot;&gt;模型更新&lt;br&gt;性能调优&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#e91e63;strokeWidth=2;shadow=1;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1880" y="600" width="140" height="70" as="geometry"/>
                </mxCell>
                <mxCell id="flow-1-2" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976d2;strokeWidth=3;endArrow=classic;" parent="1" source="step1" target="step2" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-1-2-label" value="拍摄指令" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=11;fontFamily=Microsoft YaHei;fillColor=#e3f2fd;rounded=1;" parent="flow-1-2" vertex="1" connectable="0">
                    <mxGeometry x="-0.1" y="1" relative="1" as="geometry">
                        <mxPoint as="offset"/>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-2-3" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976d2;strokeWidth=3;endArrow=classic;" parent="1" source="step2" target="step3" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-3-quality" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#ff9800;strokeWidth=2;endArrow=classic;dashed=1;" parent="1" source="step3" target="quality-check" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-quality-error" value="不合格" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f44336;strokeWidth=2;endArrow=classic;fontFamily=Microsoft YaHei;fontSize=10;" parent="1" source="quality-check" target="error-process" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-quality-ok" value="合格" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4caf50;strokeWidth=2;endArrow=classic;fontFamily=Microsoft YaHei;fontSize=10;" parent="1" source="quality-check" target="step4" edge="1">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="550" y="300"/>
                            <mxPoint x="750" y="300"/>
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-3-4" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976d2;strokeWidth=3;endArrow=classic;" parent="1" source="step3" target="step4" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-4-5" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976d2;strokeWidth=3;endArrow=classic;" parent="1" source="step4" target="step5" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-5-network" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#ff9800;strokeWidth=2;endArrow=classic;dashed=1;" parent="1" source="step5" target="network-check" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-network-offline" value="断网" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f44336;strokeWidth=2;endArrow=classic;fontFamily=Microsoft YaHei;fontSize=10;" parent="1" source="network-check" target="offline-storage" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-network-ok" value="联网" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4caf50;strokeWidth=2;endArrow=classic;fontFamily=Microsoft YaHei;fontSize=10;" parent="1" source="network-check" target="step6" edge="1">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="950" y="300"/>
                            <mxPoint x="1150" y="300"/>
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-5-6" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#7b1fa2;strokeWidth=3;endArrow=classic;" parent="1" source="step5" target="step6" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-5-6-label" value="数据传输" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=11;fontFamily=Microsoft YaHei;fillColor=#f3e5f5;rounded=1;" parent="flow-5-6" vertex="1" connectable="0">
                    <mxGeometry x="-0.1" y="1" relative="1" as="geometry">
                        <mxPoint as="offset"/>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-6-7" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#7b1fa2;strokeWidth=3;endArrow=classic;" parent="1" source="step6" target="step7" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-7-8" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#7b1fa2;strokeWidth=3;endArrow=classic;" parent="1" source="step7" target="step8" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-8-9" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#7b1fa2;strokeWidth=3;endArrow=classic;" parent="1" source="step8" target="step9" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-9-confidence" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#ff9800;strokeWidth=2;endArrow=classic;dashed=1;" parent="1" source="step9" target="confidence-check" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-confidence-manual" value="置信度低" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f44336;strokeWidth=2;endArrow=classic;fontFamily=Microsoft YaHei;fontSize=10;" parent="1" source="confidence-check" target="manual-verify" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-confidence-ok" value="置信度高" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4caf50;strokeWidth=2;endArrow=classic;fontFamily=Microsoft YaHei;fontSize=10;" parent="1" source="confidence-check" target="step10" edge="1">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1750" y="300"/>
                            <mxPoint x="1950" y="300"/>
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-9-10" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#7b1fa2;strokeWidth=3;endArrow=classic;" parent="1" source="step9" target="step10" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-10-11" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#7b1fa2;strokeWidth=3;endArrow=classic;" parent="1" source="step10" target="step11" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-11-12" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f57c00;strokeWidth=3;endArrow=classic;" parent="1" source="step11" target="step12" edge="1">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="2150" y="400"/>
                            <mxPoint x="350" y="400"/>
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-11-12-label" value="云端处理" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=11;fontFamily=Microsoft YaHei;fillColor=#fff3e0;rounded=1;" parent="flow-11-12" vertex="1" connectable="0">
                    <mxGeometry x="-0.1" y="1" relative="1" as="geometry">
                        <mxPoint as="offset"/>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-12-13" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f57c00;strokeWidth=3;endArrow=classic;" parent="1" source="step12" target="step13" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-13-anomaly" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#ff9800;strokeWidth=2;endArrow=classic;dashed=1;" parent="1" source="step13" target="anomaly-result" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-anomaly-alert" value="异常" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f44336;strokeWidth=2;endArrow=classic;fontFamily=Microsoft YaHei;fontSize=10;" parent="1" source="anomaly-result" target="alert-trigger" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-anomaly-ok" value="正常" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4caf50;strokeWidth=2;endArrow=classic;fontFamily=Microsoft YaHei;fontSize=10;" parent="1" source="anomaly-result" target="step14" edge="1">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="550" y="680"/>
                            <mxPoint x="750" y="680"/>
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-13-14" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f57c00;strokeWidth=3;endArrow=classic;" parent="1" source="step13" target="step14" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-14-15" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f57c00;strokeWidth=3;endArrow=classic;" parent="1" source="step14" target="step15" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-15-16" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f57c00;strokeWidth=3;endArrow=classic;" parent="1" source="step15" target="step16" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-16-17" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1976d2;strokeWidth=3;endArrow=classic;" parent="1" source="step16" target="step17" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-16-17-label" value="结果反馈" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=11;fontFamily=Microsoft YaHei;fillColor=#e3f2fd;rounded=1;" parent="flow-16-17" vertex="1" connectable="0">
                    <mxGeometry x="-0.1" y="1" relative="1" as="geometry">
                        <mxPoint as="offset"/>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-16-18" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#e91e63;strokeWidth=3;endArrow=classic;" parent="1" source="step16" target="step18" edge="1">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1150" y="500"/>
                            <mxPoint x="1550" y="500"/>
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-16-18-label" value="展示输出" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=11;fontFamily=Microsoft YaHei;fillColor=#fce4ec;rounded=1;" parent="flow-16-18" vertex="1" connectable="0">
                    <mxGeometry x="-0.1" y="1" relative="1" as="geometry">
                        <mxPoint as="offset"/>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-17-18" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#e91e63;strokeWidth=3;endArrow=classic;" parent="1" source="step17" target="step18" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-18-19" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#e91e63;strokeWidth=3;endArrow=classic;" parent="1" source="step18" target="step19" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-19-20" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#e91e63;strokeWidth=3;endArrow=classic;" parent="1" source="step19" target="step20" edge="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="flow-error-retry" value="重新拍摄" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#f44336;strokeWidth=2;endArrow=classic;dashed=1;dashPattern=5 5;fontFamily=Microsoft YaHei;fontSize=10;" parent="1" source="error-process" target="step1" edge="1">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="550" y="540"/>
                            <mxPoint x="50" y="540"/>
                            <mxPoint x="50" y="150"/>
                            <mxPoint x="150" y="150"/>
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-offline-retry" value="网络恢复" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#ff9800;strokeWidth=2;endArrow=classic;dashed=1;dashPattern=5 5;fontFamily=Microsoft YaHei;fontSize=10;" parent="1" source="offline-storage" target="step6" edge="1">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="950" y="540"/>
                            <mxPoint x="1150" y="540"/>
                            <mxPoint x="1150" y="300"/>
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-manual-continue" value="校验完成" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4caf50;strokeWidth=2;endArrow=classic;dashed=1;dashPattern=5 5;fontFamily=Microsoft YaHei;fontSize=10;" parent="1" source="manual-verify" target="step10" edge="1">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1750" y="540"/>
                            <mxPoint x="1950" y="540"/>
                            <mxPoint x="1950" y="300"/>
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="flow-optimize-feedback" value="模型优化" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#9c27b0;strokeWidth=2;endArrow=classic;dashed=1;dashPattern=5 5;fontFamily=Microsoft YaHei;fontSize=10;" parent="1" source="step20" target="step6" edge="1">
                    <mxGeometry relative="1" as="geometry">
                        <Array as="points">
                            <mxPoint x="1950" y="700"/>
                            <mxPoint x="2200" y="700"/>
                            <mxPoint x="2200" y="150"/>
                            <mxPoint x="1150" y="150"/>
                        </Array>
                    </mxGeometry>
                </mxCell>
                <mxCell id="layer-terminal" value="📱 端侧设备层" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;fontColor=#1565c0;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="80" y="140" width="150" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="layer-edge" value="⚡ 边缘计算层" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;fontColor=#6a1b9a;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1080" y="140" width="150" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="layer-cloud" value="☁️ 云端服务层" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;fontColor=#e65100;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="280" y="540" width="150" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="layer-management" value="📊 管理展示层" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;fontColor=#c2185b;fontFamily=Microsoft YaHei;" parent="1" vertex="1">
                    <mxGeometry x="1480" y="540" width="150" height="30" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```
"""

def register_draw_helper_tools(mcp: FastMCP):
    """注册绘图辅助工具"""
    
    @mcp.tool()
    def draw_system_architecture_prompt() -> str:
        """绘制系统架构图的提示词"""
        return _draw_system_architecture_prompt
    
    
    @mcp.tool()
    def draw_system_flowchart_prompt() -> str:
        """绘制系统流程图的提示词"""
        return _draw_system_flowchart_prompt