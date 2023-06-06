import os
import sys
import json
import shutil

import pinyin


# 遍历文件夹
def walk_dir(dir_path):
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

#遍历文件夹 拷贝webp 文件
def copy_webp(file_path,new_dir):
    file_list = walk_dir(file_path)
    for file_path in file_list:
        if (file_path.endswith('.webp')):
            # 文件名
            file_name = os.path.basename(file_path)
            # print(file_name)
            # 一级文件夹名字
            file_path1 = os.path.dirname(file_path)
            dirname = file_path1[(file_path1.rfind("\\")+1):]
            
            newPath = ( os.path.join(new_dir,get_pinyin(dirname)+"-"+get_pinyin(file_name)))
            shutil.copy(file_path, newPath)


# 生成拼音
def get_pinyin(name):
    return pinyin.get(name, format="numerical")

if __name__ == '__main__':
    # 命令行参数1：文件夹路径
    local_path = os.getcwd()
    if (len(sys.argv) < 3):
        print('参数错误')
        sys.exit(1)
    old_dir = sys.argv[1]
    new_dir = sys.argv[2]
    print(sys.argv[1])
    print(sys.argv[2])
    # 参数2：新文件夹路径
    copy_webp(old_dir,new_dir)