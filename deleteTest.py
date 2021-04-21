import shutil
import os

def deletedir(num): #num学号
    pathdir = './data/'+ str(num)
    if os.path.exists(pathdir):  # 如果文件目录存在
        # 删除文件夹。
        shutil.rmtree(pathdir) 
        print('已删除')
    else:
        print('no such filedir')  # 则返回文件目录不存在

    pathfile = './trainner/'+ str(num) + '.xml'
    if os.path.exists(pathfile):  # 如果文件存在
        os.remove(pathfile)  
        print('已删除')
    else:
        print('no such file')  # 则返回文件不存在    