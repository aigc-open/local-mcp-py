from mcp.server.fastmcp import FastMCP


_ppt_helper_by_html_prompt = """
你是一个ppt开发专家，请根据给出内容，生成一个基于html的ppt
## PPT(html)要求：
- 你精通ppt开发，熟悉ppt开发过程
- 你精通html，熟悉html开发过程
- 参考模版生成一个PPT的页面
- 每页ppt高度 height: 720px; 严格准守
- 页面不允许出现滚动条
- 内容不宜过多，导致撑爆页面
- ppt布局可以考虑左右和上下都居中
- 也页面风格清爽
- 如果有数据，可以考虑使用表格/统计等来展示
- 多页ppt，则生成多个html，比如slider1.html. slider2.html...，最后使用 index.html 来引用汇总成一个完成ppt

## 模版

```markdown
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>智能汽车技术革新</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
    <style>
        /* 自定义样式 */
        .slide-container {
            height: 720px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center; /* 水平居中 */
            padding: 20px;
            background-color: #f3f4f6;
        }

        .slide-header {
            text-align: center;
            margin-bottom: 20px;
        }

        .slide-content {
            flex: 1;
            display: flex;
            justify-content: center; /* 水平居中 */
            align-items: center; /* 垂直居中 */
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }

        .grid-item {
            background-color: #1a202c;
            color: #cbd5e0;
            padding: 20px;
            border-radius: 8px;
            text-align: center; /* 文字水平居中 */
        }

        .grid-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .grid-description {
            font-size: 1rem;
        }

        .slide-footer {
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="slide-container">
        <div class="slide-header">
            <h1 class="slide-title">智能汽车技术革新</h1>
        </div>
        
        <div class="slide-content">
            <div class="grid">
                <div class="grid-item">
                    <h2 class="grid-title">自动驾驶技术</h2>
                    <p class="grid-description">实现无人驾驶，提升行车安全性。</p>
                </div>
                <div class="grid-item">
                    <h2 class="grid-title">智能交互系统</h2>
                    <p class="grid-description">人机交互更加智能，提升驾驶体验。</p>
                </div>
                <div class="grid-item">
                    <h2 class="grid-title">车联网技术</h2>
                    <p class="grid-description">实现车辆之间的互联互通，推动智慧交通发展。</p>
                </div>
            </div>
        </div>
        
        <div class="slide-footer">
            1 / 10
        </div>
    </div>
</body>
</html>

"""


_ppt_helper_by_md_prompt = """
你是一个ppt开发专家，请根据给出内容，生成一个基于md的ppt
## PPT(md)要求：
- 你精通ppt开发，熟悉ppt开发过程
- 你精通md，熟悉md开发过程
- 参考模版生成一个PPT的页面
- 界面清爽，背景体现科技感，背景有颜色渐变
- 每页标题放左上角
- 字体颜色使用黑色
- 每页内容不宜过多
- 如果需要放图片，则允许对图片进行缩放
- 内容区不能超过PPT的高度和宽度
- 每页内容需要言简意赅
- 每页内容只能包含一部分，例如智能包含里面的 表格，列表，图片，文段等中的一种，每页内容不宜过多
- 如果一页内容太多了，就分多页
- 背景图选择：
    - ./images/背景库/简约蓝色背景图.png
    - ./images/背景库/简约灰白背景图.png
- 贴图全屏的尺寸：w:1000 h:600
- 某页PPT添加图片，则使用以下来布局：
    - ![bg right](./images/素材库/人工智能-暗灰主题.png)
    - ![bg left](./images/素材库/人工智能-暗灰主题.png)
    
    
## 模版
```
---
marp: true
theme: gaia
_class: lead
paginate: true
header: 人工智能技术分享 | 2024年演示 | AI研究团队
color: #000000
backgroundImage: url('./images/背景库/简约蓝色背景图.png')
# 使用说明：
# 当某一页内容过多时，可以在该页面添加 <!-- _class: dense-content --> 来应用更小的字体和紧凑布局

---
<!-- _class: dense-content -->

# 人工智能
## Artificial Intelligence

探索智能时代的无限可能



---

![w:1000 h:600](./images/素材库/人工智能-暗灰主题.png)

---


## 目录

1. **AI发展历程**
   - 从概念到现实的演进

2. **核心技术架构**
   - 机器学习、深度学习、神经网络

3. **应用场景展示**
   - AI在各行业的实际应用

---


## 目录

4. **技术实现示例**
   - 核心算法代码展示

5. **未来发展趋势**
   - AI技术的前景与挑战

---

## AI发展历程

![bg right](./images/素材库/人工智能-暗灰主题.png)

- **1950年代**：图灵测试，AI概念诞生
- **1980年代**：专家系统兴起
- **2010年代**：深度学习革命
- **2020年代**：大语言模型突破

---



## 核心技术架构

- **三大支柱技术**
    - 机器学习算法
    - 神经网络结构
    - 大数据处理

---



## AI名言

> "人工智能将是人类发明的最后一项发明"

> —— 尼克·博斯特罗姆

> "AI不会取代人类，但会使用AI的人会取代不会使用AI的人"

---



## 神经网络示例

```python
import tensorflow as tf

# 构建简单神经网络
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# 编译模型
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
```

---



## AI技术总结

- **算法突破**：深度学习推动技术革新
- **应用广泛**：覆盖医疗、金融、教育等领域
- **发展迅速**：技术迭代加速，应用场景扩展
- **未来可期**：通用人工智能成为新目标

---



# 感谢聆听
## 开启AI时代新篇章
```
    
"""


def register_ppt_helper_tools(mcp: FastMCP):
    """注册ppt辅助工具"""
    
    @mcp.tool()
    def ppt_helper_by_html_prompt() -> str:
        """根据内容生成一个基于html的ppt的提示词"""
        return _ppt_helper_by_html_prompt
    
    
    @mcp.tool()
    def ppt_helper_by_md_prompt() -> str:
        """根据内容生成一个基于md(marp格式)的ppt的提示词"""
        return _ppt_helper_by_md_prompt