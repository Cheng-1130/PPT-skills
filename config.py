# PPT生成配置
PPT_CONFIG = {
    "default_layout": "标题页",
    "theme_color": "blue",
    "font_title": "微软雅黑",
    "font_content": "微软雅黑",
    "slide_size": (16, 9),  # 宽屏比例
    "max_pages": 50
}

# 文档解析配置
DOC_CONFIG = {
    "max_content_length": 5000,
    "min_paragraph_length": 10,
    "section_separators": ["一、", "二、", "三、", "1.", "2.", "3."]
}

# 模板配置
TEMPLATE_CONFIG = {
    "templates": {
        "business": "templates/business.pptx",
        "academic": "templates/academic.pptx",
        "creative": "templates/creative.pptx"
    }
}
