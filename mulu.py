import os
def mkdir(path):
    # 去除首位空格
    # path = path.strip()
    # # 去除尾部 \ 符号
    # path = path.rstrip("/")
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录# 创建目录操作函数
        os.makedirs(path)
        print (path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False
# 定义要创建的目录
# test = str(2017188)
# # mkpath = "./data/" + test
# # # 调用函数
# mkdir("./data/" + test)
