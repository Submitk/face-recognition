import os
import csv

def create_csv(path):
	with open(path, "w+", newline='') as file:
		csv_file = csv.writer(file)
		head = ["student_ID","time"]
		csv_file.writerow(head)

def append_csv(path,datas):
	with open(path, "a+", newline='') as file: 
		csv_file = csv.writer(file)
		# datas = [["hoojjack3", "boy3"]]
		csv_file.writerows(datas)		

				

# if  not os.path.exists('facetime.csv'):
#     create_csv('facetime.csv')
# append_csv('facetime.csv',[["213","2020-04-21 17:43:23"]])