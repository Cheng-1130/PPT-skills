from docx import Document
import re
from nltk.tokenize import sent_tokenize
import nltk

# 下载必要的NLTK数据
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

class DocumentParser:
    """文档解析器：支持Word/TXT文档解析"""
    
    def __init__(self, config):
        self.config = config
    
    def parse_word(self, file_path):
        """解析Word文档"""
        doc = Document(file_path)
        content = []
        
        for para in doc.paragraphs:
            text = para.text.strip()
            if text and len(text) >= self.config["min_paragraph_length"]:
                content.append(text)
        
        return self._structure_content(content)
    
    def parse_txt(self, file_path):
        """解析TXT文档"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        paragraphs = re.split(r'\n\n+', content)
        filtered = [p.strip() for p in paragraphs if p.strip() and len(p.strip()) >= self.config["min_paragraph_length"]]
        
        return self._structure_content(filtered)
    
    def _structure_content(self, paragraphs):
        """结构化内容：提取标题和正文"""
        structured = []
        separators = self.config["section_separators"]
        
        for para in paragraphs:
            # 检测是否为标题
            is_title = any(para.startswith(sep) for sep in separators)
            
            if is_title:
                # 提取标题文本
                title = re.sub(r'^[一二三四五六七八九十\d]+[、.．]', '', para).strip()
                structured.append({
                    "type": "title",
                    "content": title,
                    "level": self._detect_title_level(para)
                })
            else:
                # 正文内容
                sentences = sent_tokenize(para)
                structured.append({
                    "type": "content",
                    "content": sentences,
                    "word_count": len(para)
                })
        
        return structured
    
    def _detect_title_level(self, text):
        """检测标题级别"""
        if text.startswith(('一、', '二、', '三、')):
            return 1
        elif text.startswith(('（一）', '（二）')):
            return 2
        elif text.startswith(tuple(str(i) + '.' for i in range(1, 10))):
            return 3
        return 4
