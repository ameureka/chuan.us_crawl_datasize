import jieba
import jieba.posseg as pseg
import os
from pathlib import Path
import json

def entity_driven_qa(text):
    qa_pairs = []
    words = pseg.cut(text)
    valid_types = {
        'n': '名词',
        'v': '动词',
        'nr': '人名',
        'ns': '地名',
        'nt': '机构名',
        'nz': '其他专名'
    }
    
    # 将文本按句子分割
    sentences = text.split('。')
    word_context = {}
    
    # 先找出每个词在哪些句子中出现
    for i, sentence in enumerate(sentences):
        for word, flag in pseg.cut(sentence):
            if flag in valid_types and len(word) >= 2:
                if word not in word_context:
                    word_context[word] = []
                word_context[word].append(sentence)
    
    # 生成问答对
    for word, sentences in word_context.items():
        flag = next(flag for w, flag in pseg.cut(word) if w == word)
        if flag in valid_types:
            question = f"文章中提到的{valid_types[flag]}'{word}'具体指什么？"
            # 使用包含该词的句子作为答案
            context = "；".join(sentences[:2])  # 最多使用前两个句子作为上下文
            answer = f"根据文章内容，'{word}'在以下语境中出现：{context}"
            
            qa_pairs.append({
                "question": question,
                "answer": answer,
                "word": word,
                "type": valid_types[flag]
            })
    
    return qa_pairs

def process_markdown_files():
    # 获取当前文件所在目录下的pachong2文件夹
    current_dir = Path(__file__).parent
    pachong_dir = current_dir / "pachong2"
    
    all_qa_pairs = []
    
    # 遍历pachong2目录下所有.md文件
    if pachong_dir.exists():
        for md_file in pachong_dir.glob("*.md"):
            try:
                # 读取文件内容
                content = md_file.read_text(encoding='utf-8')
                
                # 生成问题对
                qa_pairs = entity_driven_qa(content)
                
                # 添加来源信息
                for qa in qa_pairs:
                    qa["source"] = md_file.name
                
                all_qa_pairs.extend(qa_pairs)
                
                print(f"已处理文件: {md_file.name}, 生成{len(qa_pairs)}个问题对")
                
            except Exception as e:
                print(f"处理文件 {md_file.name} 时出错: {str(e)}")
    
    return all_qa_pairs

if __name__ == "__main__":
    # 执行处理
    qa_pairs = process_markdown_files()
    
    # 输出结果
    print(f"\n总共生成 {len(qa_pairs)} 个问题对")
    
    # 保存结果到文件
    output_file = Path(__file__).parent / "qa_pairs.json"
    with open(output_file, "w", encoding='utf-8') as f:
        json.dump(qa_pairs, f, ensure_ascii=False, indent=2)
    
    print(f"问题对已保存到: {output_file}")