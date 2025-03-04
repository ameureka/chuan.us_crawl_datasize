# 使用HanLP的语义角色标注
import hanlp
import os
import datetime
import json

def srl_qa_generation(text):
    try:
        # 初始化HanLP模型（第一次运行时会下载模型）
        print("正在加载HanLP模型...")
        HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH)
        print("模型加载完成，开始处理文本...")
        
        # 确保文本不为空
        if not text or len(text.strip()) == 0:
            print("警告：输入文本为空")
            return []
            
        try:
            srl_result = HanLP(text, tasks=['srl'])['srl']
        except Exception as e:
            print(f"语义角色标注处理失败：{str(e)}")
            return []
            
        qa_pairs = []
        
        # 添加调试信息
        print("SRL结果类型:", type(srl_result))
        if srl_result:
            print("第一个结果示例:", srl_result[0])
        
        for sentence_srl in srl_result:
            # 重组当前句子的语义角色
            current_pred = None
            arguments = {}
            
            for token in sentence_srl:
                if len(token) != 4:  # 确保token包含(文本, 角色类型, 开始位置, 结束位置)
                    continue
                    
                text, role, start, end = token
                
                if role == 'PRED':
                    current_pred = text
                elif role.startswith('ARG') or role.startswith('ARGM'):
                    if role not in arguments:
                        arguments[role] = []
                    arguments[role].append(text)
            
            # 如果找到谓词和参数，生成问答对
            if current_pred:
                # 生成how类问题
                if 'ARG1' in arguments:
                    question = f"如何{current_pred}？"
                    answer = "文中提到：" + '，'.join(arguments['ARG1'])
                    qa_pairs.append({"question": question, "answer": answer})
                    
                # 生成why类问题
                if 'ARGM-CAU' in arguments:
                    question = f"为什么要{current_pred}？"
                    answer = "原因是：" + '；'.join(arguments['ARGM-CAU'])
                    qa_pairs.append({"question": question, "answer": answer})
                
        return qa_pairs
        
    except Exception as e:
        print(f"SRL处理过程中发生错误：{str(e)}")
        return []

def process_folder():
    try:
        # 获取当前文件所在目录下的pachong2文件夹路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(current_dir, 'pachong2')
        
        all_qa_pairs = []
        
        print(f"正在检查文件夹：{folder_path}")
        
        # 确保文件夹存在
        if not os.path.exists(folder_path):
            print(f"错误：找不到文件夹 {folder_path}")
            return []
        
        # 获取并打印文件夹中的所有文件
        files = os.listdir(folder_path)
        print(f"找到{len(files)}个文件")
        
        # 遍历文件夹中的所有文件
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(folder_path, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        print(f"\n正在处理文件：{filename}")
                        print(f"文件大小：{len(content)}字符")
                        
                        # 如果文件太大，可以只处理前面的一部分
                        if len(content) > 10000:  # 如果文本超过10000字符
                            print("文件较大，只处理前10000字符")
                            content = content[:10000]
                            
                        qa_pairs = srl_qa_generation(content)
                        print(f"生成了{len(qa_pairs)}个问答对")
                        all_qa_pairs.extend(qa_pairs)
                except UnicodeDecodeError:
                    print(f"文件编码错误：{filename}，尝试使用其他编码方式...")
                    try:
                        with open(file_path, 'r', encoding='gbk') as f:
                            content = f.read()
                            qa_pairs = srl_qa_generation(content)
                            all_qa_pairs.extend(qa_pairs)
                    except Exception as e:
                        print(f"使用GBK编码仍然失败：{str(e)}")
                except Exception as e:
                    print(f"处理文件 {filename} 时出错：{str(e)}")
                    print(f"错误类型：{type(e)}")
        
        return all_qa_pairs
        
    except Exception as e:
        print(f"文件夹处理过程中发生错误：{str(e)}")
        return []

def save_qa_pairs(qa_pairs):
    try:
        # 创建保存问答对的目录结构
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.join(current_dir, 'conversations')
        
        # 使用当前时间创建子目录
        timestamp = datetime.datetime.now()
        date_dir = timestamp.strftime('%Y-%m-%d')
        time_str = timestamp.strftime('%H-%M-%S')
        
        # 创建完整的目录路径
        save_dir = os.path.join(base_dir, date_dir)
        os.makedirs(save_dir, exist_ok=True)
        
        # 创建保存文件的完整路径
        filename = f'{time_str}_qa_pairs.json'
        filepath = os.path.join(save_dir, filename)
        
        # 准备要保存的数据
        save_data = {
            'timestamp': timestamp.isoformat(),
            'qa_pairs': qa_pairs,
            'total_pairs': len(qa_pairs)
        }
        
        # 保存到JSON文件
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, ensure_ascii=False, indent=2)
            
        print(f"\n问答对已保存到: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"保存问答对时发生错误：{str(e)}")
        return None

if __name__ == "__main__":
    print("开始处理...")
    try:
        qa_results = process_folder()
        
        print(f"\n总共生成的问答对数量：{len(qa_results)}")
        if len(qa_results) > 0:
            print("\n生成的问答对：")
            for i, qa in enumerate(qa_results, 1):
                print(f"\n问答对 {i}:")
                print(f"问题：{qa['question']}")
                print(f"答案：{qa['answer']}")
            
            # 保存问答对到本地
            saved_path = save_qa_pairs(qa_results)
            if saved_path:
                print(f"问答对已成功保存到本地文件系统")
        else:
            print("没有生成任何问答对。")
    except Exception as e:
        print(f"程序执行过程中发生错误：{str(e)}")