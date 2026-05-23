
from doc_parser import DocumentParser
from ppt_generator import PPTGenerator
from config import DOC_CONFIG, PPT_CONFIG
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='AI驱动的PPT生成工具')
    parser.add_argument('input_file', help='输入文档路径（.docx或.txt）')
    parser.add_argument('output_file', help='输出PPT路径（.pptx）')
    parser.add_argument('--title', help='自定义PPT标题')
    args = parser.parse_args()
    
    # 验证输入文件
    if not os.path.exists(args.input_file):
        print(f"错误：输入文件不存在 - {args.input_file}")
        return
    
    # 解析文档
    print(f"正在解析文档: {args.input_file}")
    parser = DocumentParser(DOC_CONFIG)
    
    if args.input_file.endswith('.docx'):
        structured_content = parser.parse_word(args.input_file)
    elif args.input_file.endswith('.txt'):
        structured_content = parser.parse_txt(args.input_file)
    else:
        print("错误：不支持的文件格式，仅支持.docx和.txt")
        return
    
    print(f"解析完成，共识别 {len(structured_content)} 个内容块")
    
    # 生成PPT
    print("正在生成PPT...")
    generator = PPTGenerator(PPT_CONFIG)
    
    if args.title:
        structured_content.insert(0, {"type": "title", "content": args.title, "level": 1})
    
    generator.generate_from_structured_content(structured_content)
    generator.save(args.output_file)
    
    print("PPT生成完成！")

if __name__ == "__main__":
    main()
