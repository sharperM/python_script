

#遍历目录（子目录）所有的sql文件
paths = []
def walkpath(path):
    import os
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            # print(os.path.join(root, dir))

            walkpath(os.path.abspath(os.path.join(root, dir)))
        for file in files:
            if file.endswith(".sql"):
                # print(os.path.join(root, file))
                paths.append(os.path.abspath(os.path.join(root, file)))




# 遍历脚本输入的目录
if __name__ == '__main__':
    import sys
    walkpath(sys.argv[1])
    paths.sort()
    for path1 in paths:
        print(path1)