import cv2
import os
# import numpy as np
import time
# import common
# import sqlTest
from PyQt5.QtCore import *#QCoreApplication
from PyQt5.QtGui import *#QIcon,QPalette,QBrush,QPixmap,QColor
from PyQt5.QtWidgets import *#QWidget,QLabel,QPushButton,QGridLayout,QApplication
############################################
#	函数名：predict  					   #
#	输入：最大的编号id					   #
#	返回值：t							   #
#	作用：识别人脸						   #
############################################
def predict(num):
	if os.path.exists('trainner/'+str(num) + '.xml'):
		recognizer = cv2.face.LBPHFaceRecognizer_create()
		# recognizer = cv2.createLBPHFaceRecognizer() # in OpenCV 2
		#recognizer.read('trainner/trainner.xml')
		recognizer.read('trainner/'+str(num) + '.xml')
		# recognizer.load('trainner/trainner.yml') # in OpenCV 2

		cascade_path = "haarcascade/haarcascade_frontalface_default.xml"
		face_cascade = cv2.CascadeClassifier(cascade_path)
		cam = cv2.VideoCapture(0)
		font = cv2.FONT_HERSHEY_SIMPLEX
		j = 1
		t = 3
		
		while True:
			time_go=time.time()
			if j==1:
				time_start = time_go
				j = j - 1
			time_tal = int(time_go-time_start)
			ret, im = cam.read()
			im = cv2.flip(im,1)
			gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(gray, 1.3, 5)
			for (x, y, w, h) in faces:
				cv2.rectangle(im, (x - 50, y - 50), (x + w + 50, y + h + 50), (225, 0, 0), 2)
				my_id, conf = recognizer.predict(gray[y:y + h, x:x + w])
				# print(my_id, conf)
				if conf > 0 and conf <50:
					# facedata = sqlTest.find_data(str(my_id)[1])
					img_id = "master" + str(my_id)
					t=1
				else:
					img_id = "Unknown"
					t=0
				# cv2.cv.PutText(cv2.cv.fromarray(im), str(Id), (x, y + h), font, 255)
				# print ("Label: %s, Confidence: %.2f" % (img_id, 100-conf))
				cv2.putText(im, str(img_id), (x, y - 20), font, 1, 255, 2)
			cv2.imshow('im', im)
			if time_tal >= 300:
				t = 0
				return 0
				break
			if t == 1:
				# dat1 = [[str(facedata[0]),str(facedata[1]),str(facedata[2]),str(facedata[3]),str(facedata[4]),time.strftime("%H:%M:%S",time.localtime())]]
				# common.append_csv("record.csv",dat1)
				print('hello')
				return 1
				break
			if cv2.waitKey(1) & 0xFF == ord('q'):
				return 0
				break
		cam.release()
		cv2.destroyAllWindows()
	else:
		print('不存在此学生的数据')
	# return t,my_id
# predict('216')