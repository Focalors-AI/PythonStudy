# 打工人: 张博文
# 打工时间: 2023/7/7 19:20
# 打工主题: txt转json
import copy
import json


def txt_to_json(txt_path, json_path):
    data = []  # 存储字典的列表
    current_dict = {}  # 当前的字典
    i = 0  # 每段对话的字典数
    j = 0
    rows = 3  # 定义矩阵的行数和列数
    cols = 2
    history = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(None)  # 这里将矩阵的元素设为 None，你也可以使用其他默认值
        history.append(row)

    with open(txt_path, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()

        for line in lines:
            line = line.strip()  # 去除首尾空格

            if line == '':  # 遇到空行时创建新的字典
                if current_dict:  # 当前字典不为空时将其添加到数据列表中
                    data.append(current_dict)
                current_dict = {}  # 创建新的字典
                i = 0
                j = 0
                # print("清空矩阵")
                for a in range(len(history)):  # 清空矩阵
                    for b in range(len(history[a])):
                        history[a][b] = None

            else:
                if j < 2:
                    key_value = line.split('：', 1)
                    if len(key_value) == 2:  # 确保成功拆分出键和值
                        key, value = key_value
                        key = key.strip()
                        value = value.strip()
                        current_dict[key] = value
                        history[i][j] = value
                        j += 1
                    else:
                        # 处理无法拆分为键和值的情况
                        print(f"Ignored line: {line}")

                elif j >= 2 and j % 2 == 0:
                    if current_dict:  # 当前字典不为空时将其添加到数据列表中
                        data.append(current_dict)
                    current_dict = {}  # 创建新的字典
                    i += 1
                    f = 0

                    key_value = line.split('：', 1)  # 拆分新的行
                    if len(key_value) == 2:  # 确保成功拆分出键和值
                        key, value = key_value
                        key = key.strip()
                        value = value.strip()
                        current_dict[key] = value
                        history[i][f] = value
                        j += 1
                        f = 1
                    else:
                        # 处理无法拆分为键和值的情况
                        print(f"Ignored line: {line}")
                else:
                    key_value = line.split('：', 1)  # 拆分新的行
                    if len(key_value) == 2:  # 确保成功拆分出键和值
                        key, value = key_value
                        key = key.strip()
                        value = value.strip()
                        current_dict[key] = value
                        history[i][f] = value
                        # 输出矩阵的内容
                        # print(i)
                        # print(history[:i])
                        current_dict["上下文"] = copy.deepcopy(history[:i])
                        j += 1
                    else:
                        # 处理无法拆分为键和值的情况
                        print(f"Ignored line: {line}")

        if current_dict:  # 处理最后一个字典
            data.append(current_dict)

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print("转换成功！")


txt_file_path = 'data.txt'
json_file_path = 'data.json'

txt_to_json(txt_file_path, json_file_path)
