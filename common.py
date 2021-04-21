import os
import csv

def create_newcsv(path):
	with open(path, "w+", newline='') as file:
		csv_file = csv.writer(file)

def create_csv(path):
	with open(path, "w+", newline='') as file:
		csv_file = csv.writer(file)
		head = ["student_ID","name","sex","age","class","time"]
		csv_file.writerow(head)

def append_csv(path,datas):
	with open(path, "a+", newline='') as file: 
		csv_file = csv.writer(file)
		#datas = [["hoojjack3", "boy3"]]
		csv_file.writerows(datas)		

def read_csv(path):
	with open(path,"r+") as file:
		csv_file = csv.reader(file)
		for data in csv_file:
			print("data:", data)
			print(data[0])
read_csv('face.csv')

def read_csv_id(path,id):
	with open(path,"r+") as file:
		csv_file = csv.reader(file)
		for data in csv_file:
			# print("datas:", data)
			if data[0]==id:
				return data
print(read_csv_id('face.csv','111111'))
def read_csv_studentid(path):
	with open(path,"r+") as file:
		csv_file = csv.reader(file)
		for data in csv_file:
			# print("datas:", data)
			return data[0]
				
############################################
#	函数名：read_max_id					   #
#	输入：图片的位置path				   #
#	返回值：最大的编号id_max			   #
#	作用：获取人脸数据最大编号			   #
############################################
def read_max_id(path):
	id_max = -1
	image_paths = [os.path.join(path, f) for f in os.listdir(path)]
	for image_path in image_paths:
		if os.path.split(image_path)[-1].split(".")[-1] != 'jpg':
			continue		#查找jpg结尾的图
		image_id = int(os.path.split(image_path)[-1].split(".")[1])
		id = image_id
		if id_max < id:
			id_max = id
		else:
			continue
	return id_max
############################################
#	函数名：del_file     				   #
#	输入：图片的位置path				   #
#	返回值：无							   #
#	作用：递归删除所有人脸数据			   #
############################################
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)