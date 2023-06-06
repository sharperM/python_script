import os
import sys
import json


#解析json文件
def parse_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data

def walk_dir(dir_path):
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list


if __name__ == '__main__':
    # 命令行参数1：json文件路径
    # 命令行参数2：图片文件夹路径
    datat = parse_json(sys.argv[1])

    filepathlist = walk_dir(sys.argv[2])

    filename = []
    for d in datat:
        for d2 in d["dataList"]:
            newname = d2["imageUrl"][27:]
            tryname = newname.replace("《》","").replace("《","").replace("》","").replace(" ","").replace(".webp","")
            tryname = tryname[tryname.rfind("-")+1:]
            # print(tryname)
            bfind1 = False
            bfind2 = False
            for filepath in filepathlist:
                if filepath.find(newname) != -1:
                    bfind1 = True
                    break
            if bfind1 == False:
                print(newname,"not found")
                for filepath in filepathlist:
                    if filepath.find(tryname) != -1:
                        bfind2 = True
                        os.rename(filepath, os.path.join(os.path.dirname(filepath), newname))
                        break
                if bfind2 == False:
                    print(tryname," ------------not found")
            # if not os.path.exists(sys.argv[2] + d2["imageUrl"][27:]):
            #     print("not found")
            #     sys.exit(1)