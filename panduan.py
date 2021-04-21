# name = 'ly'
# number = '213'
# cla = '1'
# sex = '男'
# age = '22'
# if name and number and cla and sex and age:
#     print("hello")

import os
def peple():
    dirnum = 0
    filenum = 0
    data = []
    path = './trainner/'
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        # print(sub_path)
        data.append(sub_path)
        if os.path.isfile(sub_path):
            filenum = filenum+1
        elif os.path.isdir(sub_path):
            dirnum = dirnum+1
    # print(data)
    # print(filenum)
    return filenum
# peple()
# print('dirnum: ',dirnum)
# print('filenum: ',filenum)