
import os

#判断文件是否git仓库
def isGitRepo(path):
    if not os.path.isdir(path):
        return False
    if not os.path.isdir(os.path.join(path, '.git')):
        return False
    return True

#遍历文件夹，找到所有的git仓库
def findAllGitRepo(path):
    gitRepos = []
    for root, dirs, files in os.walk(path):
        if isGitRepo(root):
            gitRepos.append(root)
    return gitRepos

if __name__ == '__main__':
    repos = findAllGitRepo('C:\\Users\\soldi\\Desktop\\youmieyou')
    for repo in repos:
        print(repo)
    print(repos.__len__())
