import os
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

# 压缩图片 使用cwebp 命令
def compress_image(file_path, quality=80):
    new_file_path = file_path.replace('.png', '').replace('.pic', '').replace('.jpg', '').replace('.jpeg', '').replace('gogo31', 'gogo32')
    mkdir(os.path.dirname(new_file_path))
    sys_str = '''C:\\Users\\soldi\\Downloads\\libwebp-0.4.1-windows-x64-no-wic\\bin\\cwebp.exe -q {0} {1} -o {2}.webp'''.format(quality, file_path,new_file_path )
    os.system(sys_str)

# 没有目录就创建目录
def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


#解析json文件
def parse_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data


# 遍历数组数据
def walk_json(json_data):
    for data in json_data:
        shen = data['title']
        for dat2 in data["dataList"]:
            funt = dat2['title']
            # print(shen + funt)
            dat2["imageUrl"] = 'file:///android_asset/place/' + get_pinyin(shen) + '-' + get_pinyin(funt) + '.webp'
    
    return json_data


# 保存成json格式
def save_json(file_path, json_data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

# 主函数
def main():
    file_list = walk_dir('gogo31')
    print(file_list)
    for file_path in file_list:
        if (file_path.endswith('.jpg') or file_path.endswith('.jpeg') or file_path.endswith('.png') or file_path.endswith('.pic') or file_path.endswith('.JPEG') or file_path.endswith('.PNG')):
            compress_image(file_path)


#遍历文件夹 拷贝webp 文件
def copy_webp(file_path):
    file_list = walk_dir(file_path)
    for file_path in file_list:
        if (file_path.endswith('.webp')):
            # 文件名
            file_name = os.path.basename(file_path)
            # print(file_name)

            # 一级文件夹名字
            file_path1 = os.path.dirname(file_path)
            dirname = file_path1[(file_path1.rfind("\\")+1):]
            # 二级目录
            file_path2 = os.path.dirname(file_path1)

            
            newPath = ( os.path.join('gogo32',get_pinyin(dirname)+"-"+get_pinyin(file_name)))
            shutil.copy(file_path, newPath)

# 生成拼音
def get_pinyin(name):
    return pinyin.get(name, format="numerical")

if __name__ == '__main__':
    # main()
    # json_data = parse_json('place.json')
    # save_json("place2.json",walk_json(json_data))
    copy_webp('gogo32\\掌上果农假页面图片\\水果产地')

# main()