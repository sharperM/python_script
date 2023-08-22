# 压缩图片 使用cwebp 命令
import os
import sys
import json
import shutil

# 没有目录就创建目录
def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        
def compress_image(file_path, olddirname, filename1,quality=80,  ):

    part2 = (file_path.replace('.png', '').replace('.pic', '').replace('.jpg', '').replace('.jpeg', '').replace(os.path.join(olddirname,filename1), ''))
    new_file_path = os.path.join(olddirname,filename1+'_webp') 
    new_file_path = os.path.join(new_file_path,part2[1:]) 
    mkdir(os.path.dirname(new_file_path))
    sys_str = '''.\\tools\\libwebp-0.4.1-windows-x64-no-wic\\bin\\cwebp.exe -q {0} {1} -o {2}.webp'''.format(quality, file_path,new_file_path )
    os.system(sys_str)





# 遍历文件夹
def walk_dir(dir_path):
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list


if __name__ == '__main__':
    # 传入的文件夹路径
    file_list = walk_dir(sys.argv[1])
    
    # new_file_path = os.path.abspath(sys.argv[1]).replace('.\\', '.\\_webp\\')
    olddirname = os.path.dirname (os.path.abspath(sys.argv[1]))
    new_file_path2 = os.path.basename (os.path.abspath(sys.argv[1]))
    # print (new_file_path)
    for file_path in file_list:
        # file_path 的 小写
        lower_file_path = file_path.lower()
        if (lower_file_path.endswith('.jpg') or lower_file_path.endswith('.jpeg') or lower_file_path.endswith('.png') or lower_file_path.endswith('.pic')):
            compress_image(file_path, olddirname,new_file_path2 )
        else:
            part2 = (file_path.replace('.png', '').replace('.pic', '').replace('.jpg', '').replace('.jpeg', '').replace(os.path.join(olddirname,new_file_path2), ''))
            new_file_path = os.path.join(olddirname,new_file_path2+'_webp') 
            new_file_path = os.path.join(new_file_path,part2[1:]) 
            mkdir(os.path.dirname(new_file_path))
            shutil.copy(file_path, new_file_path)