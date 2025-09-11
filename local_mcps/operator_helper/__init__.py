from mcp.server.fastmcp import FastMCP


_operator_visualization_prompt = """
你是一个算子开发专家，请根据代码绘制算子计算过程可视化图：

- 你精通算子开发，熟悉算子计算过程
- 你知道 cpu 的计算逻辑
- 你熟悉 cuda 相关的编程逻辑
- 请你根据给出代码的语义与计算逻辑，绘制出算子计算过程可视化图
- 要求使用 drawio 格式绘制, 目标是实现一个网格语义解析图
- 需要举例说明其计算过程，其中网格代表矩阵
- 最后生成一个 xxx.drawio 文件,命名规范为 算子名称_算子计算过程可视化.drawio

- 以下是一个参考的 drawio 格式绘制的算子可视化图

```xml
<mxfile host="65bd71144e">
    <diagram name="分块量化矩阵乘法" id="quantized_matmul">
        <mxGraphModel dx="1065" dy="795" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="title" value="分块量化矩阵乘法计算过程可视化" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=20;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="400" y="20" width="300" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="matrix_a_title" value="输入矩阵 A [2×6]" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="50" y="80" width="120" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="a_00" value="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="50" y="110" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="a_01" value="2" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="80" y="110" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="a_02" value="3" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="110" y="110" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="a_03" value="4" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="140" y="110" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="a_04" value="5" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="170" y="110" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="a_05" value="6" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="200" y="110" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="a_10" value="7" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="50" y="140" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="a_11" value="8" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="80" y="140" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="a_12" value="9" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="110" y="140" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="a_13" value="10" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="140" y="140" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="a_14" value="11" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="170" y="140" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="a_15" value="12" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="200" y="140" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="block1_label" value="块1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="95" y="100" width="30" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="block2_label" value="块2" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="155" y="100" width="30" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="lhs_scale_title" value="左缩放因子 As [2×2]" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="50" y="200" width="120" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="as_00" value="0.1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="50" y="230" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="as_01" value="0.2" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="80" y="230" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="as_10" value="0.3" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="50" y="260" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="as_11" value="0.4" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="80" y="260" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="matrix_b_title" value="权重矩阵 B [4×6]" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="300" y="80" width="120" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="b_00" value="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="300" y="110" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_01" value="2" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="330" y="110" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_02" value="3" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="360" y="110" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_03" value="4" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="390" y="110" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_04" value="5" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="420" y="110" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_05" value="6" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="450" y="110" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_10" value="7" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="300" y="140" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_11" value="8" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="330" y="140" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_12" value="9" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="360" y="140" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_13" value="10" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="390" y="140" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_14" value="11" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="420" y="140" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_15" value="12" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="450" y="140" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_20" value="13" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="300" y="170" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_21" value="14" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="330" y="170" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_22" value="15" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="360" y="170" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_23" value="16" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="390" y="170" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_24" value="17" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="420" y="170" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_25" value="18" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="450" y="170" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_30" value="19" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="300" y="200" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_31" value="20" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="330" y="200" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_32" value="21" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="360" y="200" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_33" value="22" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="390" y="200" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_34" value="23" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="420" y="200" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_35" value="24" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="450" y="200" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="b_block1_label" value="块1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="345" y="100" width="30" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="b_block2_label" value="块2" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="405" y="100" width="30" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="b_block3_label" value="块3" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="345" y="180" width="30" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="b_block4_label" value="块4" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="405" y="180" width="30" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="rhs_scale_title" value="右缩放因子 Bs [2×2]" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="300" y="250" width="120" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="bs_00" value="0.5" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="300" y="280" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="bs_01" value="0.6" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="330" y="280" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="bs_10" value="0.7" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="300" y="310" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="bs_11" value="0.8" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="330" y="310" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="step1_title" value="步骤1：分块索引计算" style="text;html=1;strokeColor=none;fillColor=#dae8fc;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontSize=14;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="550" y="80" width="150" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="step1_content" value="K维度分块：[0,0,0,1,1,1]&#10;N维度分块：[0,0,1,1]&#10;&#10;块大小：&#10;block_k = 3&#10;block_n = 2" style="text;html=1;strokeColor=none;fillColor=#f5f5f5;align=left;verticalAlign=top;whiteSpace=wrap;rounded=1;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="550" y="120" width="150" height="100" as="geometry"/>
                </mxCell>
                <mxCell id="step2_title" value="步骤2：缩放因子扩展" style="text;html=1;strokeColor=none;fillColor=#d5e8d4;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontSize=14;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="550" y="240" width="150" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="step2_content" value="A缩放因子扩展：&#10;[0.1,0.1,0.1,0.2,0.2,0.2]&#10;[0.3,0.3,0.3,0.4,0.4,0.4]&#10;&#10;B缩放因子扩展：&#10;[0.5,0.5,0.5,0.6,0.6,0.6]&#10;[0.5,0.5,0.5,0.6,0.6,0.6]&#10;[0.7,0.7,0.7,0.8,0.8,0.8]&#10;[0.7,0.7,0.7,0.8,0.8,0.8]" style="text;html=1;strokeColor=none;fillColor=#f5f5f5;align=left;verticalAlign=top;whiteSpace=wrap;rounded=1;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="550" y="280" width="150" height="140" as="geometry"/>
                </mxCell>
                <mxCell id="step3_title" value="步骤3：应用缩放" style="text;html=1;strokeColor=none;fillColor=#fff2cc;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontSize=14;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="550" y="440" width="150" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="step3_content" value="A_scaled = A × lhs_scale_expanded&#10;B_scaled = B × rhs_scale_expanded&#10;&#10;例如：&#10;A[0,0] × 0.1 = 1 × 0.1 = 0.1&#10;A[0,3] × 0.2 = 4 × 0.2 = 0.8" style="text;html=1;strokeColor=none;fillColor=#f5f5f5;align=left;verticalAlign=top;whiteSpace=wrap;rounded=1;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="550" y="480" width="150" height="120" as="geometry"/>
                </mxCell>
                <mxCell id="step4_title" value="步骤4：矩阵乘法" style="text;html=1;strokeColor=none;fillColor=#f8cecc;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontSize=14;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="550" y="620" width="150" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="step4_content" value="C = A_scaled @ B_scaled^T&#10;&#10;输出矩阵 [2×4]&#10;C[0,0] = 9.94&#10;C[0,1] = 22.54&#10;C[1,0] = 47.58&#10;C[1,1] = 116.70" style="text;html=1;strokeColor=none;fillColor=#f5f5f5;align=left;verticalAlign=top;whiteSpace=wrap;rounded=1;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="550" y="660" width="150" height="120" as="geometry"/>
                </mxCell>
                <mxCell id="output_title" value="输出矩阵 C [2×4]" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="750" y="80" width="120" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="c_00" value="9.94" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=10;" parent="1" vertex="1">
                    <mxGeometry x="750" y="110" width="40" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="c_01" value="22.54" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=10;" parent="1" vertex="1">
                    <mxGeometry x="790" y="110" width="40" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="c_02" value="47.14" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=10;" parent="1" vertex="1">
                    <mxGeometry x="830" y="110" width="40" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="c_03" value="64.06" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=10;" parent="1" vertex="1">
                    <mxGeometry x="870" y="110" width="40" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="c_10" value="47.58" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=10;" parent="1" vertex="1">
                    <mxGeometry x="750" y="140" width="40" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="c_11" value="116.70" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=10;" parent="1" vertex="1">
                    <mxGeometry x="790" y="140" width="40" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="c_12" value="251.14" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=10;" parent="1" vertex="1">
                    <mxGeometry x="830" y="140" width="40" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="c_13" value="344.74" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=10;" parent="1" vertex="1">
                    <mxGeometry x="870" y="140" width="40" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="arrow1" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="a_05" target="b_00" edge="1">
                    <mxGeometry width="50" height="50" relative="1" as="geometry">
                        <mxPoint x="400" y="400" as="sourcePoint"/>
                        <mxPoint x="450" y="350" as="targetPoint"/>
                    </mxGeometry>
                </mxCell>
                <mxCell id="arrow2" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="b_35" target="c_00" edge="1">
                    <mxGeometry width="50" height="50" relative="1" as="geometry">
                        <mxPoint x="400" y="400" as="sourcePoint"/>
                        <mxPoint x="450" y="350" as="targetPoint"/>
                    </mxGeometry>
                </mxCell>
                <mxCell id="legend_title" value="图例" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1;" parent="1" vertex="1">
                    <mxGeometry x="50" y="350" width="60" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="legend1" value="块1 (K维度前3个)" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="50" y="380" width="120" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="legend1_box" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" parent="1" vertex="1">
                    <mxGeometry x="35" y="382.5" width="15" height="15" as="geometry"/>
                </mxCell>
                <mxCell id="legend2" value="块2 (K维度后3个)" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="50" y="400" width="120" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="legend2_box" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" parent="1" vertex="1">
                    <mxGeometry x="35" y="402.5" width="15" height="15" as="geometry"/>
                </mxCell>
                <mxCell id="legend3" value="块3 (N维度前2行)" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="50" y="420" width="120" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="legend3_box" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" parent="1" vertex="1">
                    <mxGeometry x="35" y="420" width="15" height="15" as="geometry"/>
                </mxCell>
                <mxCell id="legend4" value="块4 (N维度后2行)" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;" parent="1" vertex="1">
                    <mxGeometry x="50" y="440" width="120" height="20" as="geometry"/>
                </mxCell>
                <mxCell id="legend4_box" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" parent="1" vertex="1">
                    <mxGeometry x="35" y="440" width="15" height="15" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```
"""


def register_operator_helper_tools(mcp: FastMCP):
    """注册算子相关工具"""
    
    @mcp.tool()
    def operator_visualization_prompt() -> str:
        """绘制算子计算过程可视化图的提示词"""
        return _operator_visualization_prompt