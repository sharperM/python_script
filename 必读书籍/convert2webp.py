import os
import sys
# 遍历文件夹
def walk_dir(dir_path):
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

# 压缩图片 使用cwebp 命令
def compress_image(file_path,old_dir,new_dir,quality=80):
    new_file_path = file_path.lower().replace('.png', '').replace('.pic', '').replace('.jpg', '').replace('.jpeg', '').replace(old_dir, new_dir)
    mkdir(os.path.dirname(new_file_path))
    sys_str = '''..\\tools\\libwebp-0.4.1-windows-x64-no-wic\\bin\\cwebp.exe -q {0} {1} -o {2}.webp'''.format(quality, file_path,new_file_path )
    os.system(sys_str)

# 没有目录就创建目录
def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

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

    file_list = walk_dir(old_dir)
    print(file_list)
    for file_path in file_list:
        file_path = file_path.lower()
        if (file_path.endswith('.jpg') or file_path.endswith('.jpeg') or file_path.endswith('.png') or file_path.endswith('.pic') or file_path.endswith('.JPEG') or file_path.endswith('.PNG')):
            compress_image(file_path,old_dir,new_dir,50)