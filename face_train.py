import cv2
import os
import numpy as np
from PIL import Image

# recognizer = cv2.createLBPHFaceRecognizer()
#detector = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
#recognizer = cv2.face.LBPHFaceRecognizer_create()
############################################
#	函数名：get_images_and_labels		   #
#	输入：人脸数据的地址path			   #
#	返回值：脸的数据集face_samples		   #
#			编号的数据集ids				   #
#	作用：获取人脸数据集和编号数据集	   #
############################################


def get_images_and_labels(path):
    detector = cv2.CascadeClassifier(
        "haarcascade/haarcascade_frontalface_default.xml")
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []

    for image_path in image_paths:
        image = Image.open(image_path).convert('L')  # 转成灰度图
        image_np = np.array(image, 'uint8')  # 将灰度图转成矩阵
        if os.path.split(image_path)[-1].split(".")[-1] != 'jpg':
            continue  # 查找jpg结尾的图
        image_id = int(os.path.split(image_path)[-1].split(".")[1])
        faces = detector.detectMultiScale(image_np)
        for (x, y, w, h) in faces:
            face_samples.append(image_np[y:y+h, x:x+w])
            ids.append(image_id)

    return face_samples, ids
############################################
#	函数名：train	 					   #
#	输入：无							   #
#	返回值：无							   #
#	作用：训练人脸模型					   #
############################################


def train(facepath,num):
    print(facepath)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # recognizer = cv2.face.EigenFaceRecognizer_create()
    # recognizer = cv2.face.FisherFaceRecognizer_create()
    faces, Ids = get_images_and_labels(facepath)
    # print(faces, Ids)
    recognizer.train(faces, np.array(Ids))
    #recognizer.save('trainner/trainner.xml')
    recognizer.save('trainner/'+str(num) + '.xml')
# train()
