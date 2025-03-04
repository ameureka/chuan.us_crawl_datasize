# 示例：编号条目转问题对
import re
import os
import json
from pathlib import Path
from datetime import datetime

def generate_qa_from_list(text, source_file=None):
    qa_pairs = []
    title_match = re.search(r"(.+?)：(\d+)[\.、]", text)
    if title_match:
        title = title_match.group(1)
        items = re.findall(r"\d+[\.、](.+?)(?=\n\d+|\Z)", text, re.DOTALL)
        for i, item in enumerate(items, 1):
            qa_pair = {
                "id": f"{title}_{i}",
                "source": source_file,
                "created_at": datetime.now().isoformat(),
                "title": title,
                "index": i,
                "qa_pairs": [
                    {
                        "question": f"{title}中的第{i}条内容是什么？",
                        "answer": f"第{i}条：{item.strip()}"
                    },
                    {
                        "question": f"请解释{title}第{i}条'{item[:15]}...'的具体含义",
                        "answer": f"第{i}条：{item.strip()}"
                    }
                ]
            }
            qa_pairs.append(qa_pair)
    return qa_pairs

def process_md_files():
    # 获取当前文件所在目录
    current_dir = Path(__file__).parent
    # 构建pachong2文件夹路径
    pachong_dir = current_dir / 'pachong2'
    output_dir = current_dir / 'qa_output'
    
    # 创建输出目录
    output_dir.mkdir(exist_ok=True)
    
    all_qa_pairs = []
    
    # 确保文件夹存在
    if not pachong_dir.exists():
        print(f"错误：找不到文件夹 {pachong_dir}")
        return
    
    # 遍历pachong2文件夹下的所有.md文件
    for md_file in pachong_dir.glob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                qa_pairs = generate_qa_from_list(content, str(md_file.name))
                if qa_pairs:
                    print(f"\n处理文件：{md_file.name}")
                    print(f"生成了 {len(qa_pairs)} 个问答对")
                    all_qa_pairs.extend(qa_pairs)
                    
                    # 为每个文件单独保存一份JSON
                    output_file = output_dir / f"{md_file.stem}_qa.json"
                    save_qa_pairs(qa_pairs, output_file)
        except Exception as e:
            print(f"处理文件 {md_file.name} 时出错：{str(e)}")
    
    # 保存所有问答对到一个总的JSON文件
    save_qa_pairs(all_qa_pairs, output_dir / "all_qa_pairs.json")
    
    print(f"\n总共生成了 {len(all_qa_pairs)} 个问答对")
    print(f"结果已保存到: {output_dir}")

def save_qa_pairs(qa_pairs, output_file):
    """保存问答对到JSON文件"""
    data = {
        "metadata": {
            "created_at": datetime.now().isoformat(),
            "total_pairs": len(qa_pairs)
        },
        "qa_pairs": qa_pairs
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    process_md_files()