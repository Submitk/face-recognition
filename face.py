import sys
from PyQt5.uic import loadUi
# from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

import cv2
from sqlTest import *
from mulu import *
import face_train
import face_predict
import face_save
import panduan
import deleteTest
import savecsv
# qflag = 0
sampleNum = 0
luru = 0
# facecheck = 0
class informationTest:
    def __init__(self):
        self.ui = uic.loadUi("information.ui")
        self.ui.setFixedSize(self.ui.width(), self.ui.height()) #禁止拉伸和最大化窗口
        
        self.ui.timer_camera = QTimer()  # 初始化定时器
        self.ui.cap = cv2.VideoCapture()  # 初始化摄像头
        fourcc = cv2.VideoWriter_fourcc(*'XVID') #XVID 支持avi格式
        # self.ui.out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))
        self.CAM_NUM = 0# 'http://admin:123456@192.168.0.108:8081' # 摄像头设备，0是内置 1是外设
        
        self.text_init()
        self.slot_init()
        self.pushbtn_init()
        
    def slot_init(self):
        self.ui.timer_camera.timeout.connect(self.show_camera)
                #信号和槽连接
        # self.returnButton.clicked.connect(self.returnSignal)
        self.ui.camera.clicked.connect(self.slotCameraButton)

    def show_camera(self):
        # global qflag 保存图片
        
        # global Id
        # mkpath = "./data/test"
        global sampleNum
        global luru 
        global mkpath
        global number
        global facecheck
        # Id = self.ui.lineEdit_2.text()
        # if Id:
        #     luru = 1
        #     mkpath = "./data/" + Id
        #     mkdir(mkpath)
            
        # self.clear_text()
        detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
        
        flag,self.imagefan = self.ui.cap.read()
        self.image = cv2.flip(self.imagefan,1)
        # print(luru)
        if luru:
            faces = detector.detectMultiScale(self.image, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                gray_than = (h)/(w)
                f = cv2.resize(self.image[y:y+h, x:x+w], (200, int(200*gray_than)))
            # incrementing sample number
                sampleNum = sampleNum + 1
                # print(mkpath + "/User." + str(number) +'.' + str(sampleNum) + ".jpg")
            # saving the captured face in the dataset folder
                cv2.imwrite(mkpath + "/User." + str(number) +
                            '.' + str(sampleNum) + ".jpg", f)  #
                cv2.putText(self.image, str((x, y)), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
                cv2.putText(self.image, str(sampleNum), (x, y - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
                
                show = cv2.resize(self.image,(800,600))
                show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
                showImage = QImage(show.data, show.shape[1],show.shape[0],QImage.Format_RGB888)
                self.ui.label_6.setPixmap(QPixmap.fromImage(showImage))
                if sampleNum >= 30:
                    self.closeCamera()
                    face_train.train(mkpath,number)
                    luru = 0
            # cv2.imshow('frame', self.image)
            # wait for 1 miliseconds
               # self.image = self.imagefan


        # elif facecheck == 1:
        #     recognizer = cv2.face.LBPHFaceRecognizer_create()
        #     # recognizer = cv2.createLBPHFaceRecognizer() # in OpenCV 2
        #     recognizer.read('trainner/trainner.xml')
        #     # recognizer.load('trainner/trainner.yml') # in OpenCV 2

        #     cascade_path = "haarcascade/haarcascade_frontalface_default.xml"
        #     face_cascade = cv2.CascadeClassifier(cascade_path)
        #     font = cv2.FONT_HERSHEY_SIMPLEX
        #     j = 1
        #     t = 3
        #     time_go=time.time()
        #     if j==1:
        #         time_start = time_go
        #         j = j - 1
        #     time_tal = int(time_go-time_start)
        #     gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        #     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        #     for (x, y, w, h) in faces:
        #         cv2.rectangle(self.image, (x - 50, y - 50), (x + w + 50, y + h + 50), (225, 0, 0), 2)
        #         my_id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        #         print(my_id, conf)
        #         if conf > 0 and conf <50:
        #             # facedata = sqlTest.find_data(str(my_id)[1])
        #             img_id = "master" + str(my_id)
        #             t=1
        #         else:
        #             img_id = "Unknown"
        #             t=0
        #         # cv2.cv.PutText(cv2.cv.fromarray(im), str(Id), (x, y + h), font, 255)
        #         # print ("Label: %s, Confidence: %.2f" % (img_id, 100-conf))
        #         cv2.putText(self.image, str(img_id), (x, y - 20), font, 1, 255, 2)
        #         show = cv2.resize(self.image,(800,600))
        #         show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        #         showImage = QImage(show.data, show.shape[1],show.shape[0],QImage.Format_RGB888)
        #         self.ui.label_6.setPixmap(QPixmap.fromImage(showImage))
        #         if time_tal >= 300:
        #             t = 0
        #             self.closeCamera()
        #             facecheck = 0
        #         if t == 1:
        #             self.closeCamera()
        #             # dat1 = [[str(facedata[0]),str(facedata[1]),str(facedata[2]),str(facedata[3]),str(facedata[4]),time.strftime("%H:%M:%S",time.localtime())]]
        #             # common.append_csv("record.csv",dat1)
        #             print('hello')


        else:
            
            show = cv2.resize(self.image,(800,600))
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            showImage = QImage(show.data, show.shape[1],show.shape[0],QImage.Format_RGB888)
            self.ui.label_6.setPixmap(QPixmap.fromImage(showImage))
            # if qflag:
            #     print(qflag)
            #     # 存储图片
            #     cv2.imwrite(mkpath + "/camera.jpg", self.image)
            #     qflag = 0
           
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     self.closeCamera()
            # # break if the sample number is morethan 300
            # elif sampleNum >= 50:
            #     self.closeCamera()
            #     face_train.train(mkpath)
         
     # 打开关闭摄像头控制

    def slotCameraButton(self):
        if self.ui.timer_camera.isActive() == False:
            # 打开摄像头并显示图像信息
            self.openCamera()
        else:
            # 关闭摄像头并清空显示信息
            self.closeCamera()

     # 打开摄像头
    def openCamera(self):
        flag = self.ui.cap.open(self.CAM_NUM)
        if flag == False:
            QMessageBox.warning(self.ui,"提示","请正确打开摄像头。",QMessageBox.Yes | QMessageBox.No)
            return
        else:
            self.ui.timer_camera.start(30)
            self.ui.camera.setText('关闭摄像头')

        # 关闭摄像头
    def closeCamera(self):
        global sampleNum
        # global mkpath
        # global number
        # if sampleNum < 30:
        #     face_train.train(mkpath,number)
        #     luru = 0
        self.ui.timer_camera.stop()
        # self.ui.cap.release()
        self.ui.label_6.clear()
        self.ui.camera.setText('打开摄像头')
        # self.ui.label_6.setPixmap(self.pix)
        self.ui.cap.release()
        sampleNum = 0
        # self.ui.out.release()



    def text_init(self):
        self.ui.lineEdit.setPlaceholderText('请在这里输入姓名')
        self.ui.lineEdit_2.setPlaceholderText('请在这里输入学号')
        self.ui.lineEdit_3.setPlaceholderText('请在这里输入班级')
        self.ui.lineEdit_4.setPlaceholderText('请在这里输入性别')
        self.ui.lineEdit_5.setPlaceholderText('请在这里输入年龄')
        self.ui.lineEdit_6.setPlaceholderText('输入学号进行签到')
        self.ui.lineEdit_7.setPlaceholderText('输入学号删除信息')
        self.ui.label_8.setText(str(panduan.peple()))
    def clear_text(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
    def pushbtn_init(self):
        self.ui.pushButton.clicked.connect(self.EditInfo)
        # self.ui.pushButton_2.clicked.connect(self.savePic)
        self.ui.pushButton_3.clicked.connect(self.facheck)
        self.ui.pushButton_4.clicked.connect(self.clear_text)
        self.ui.pushButton_5.clicked.connect(self.delete_info)


    # def up_buttonClicked(self):
    #     print("up")

    #     self.i = self.i - 10
    #     if self.i<=50:
    #         self.i=50
    #     self.p2.ChangeDutyCycle(2.5 + 10 * self.i / 180) #设置转动角度  
    #     time.sleep(0.02)                      #等该20ms周期结束  
    #     self.p2.ChangeDutyCycle(0)                  #归零信号  
    #     time.sleep(0.2) 

    def delete_info(self):
        denum = self.ui.lineEdit_7.text()
        if denum:
            deleteTest.deletedir(denum)
        else:
            QMessageBox.question(self.ui, '提示', '请先输入要删除的学号', QMessageBox.Yes)

    def savePic(self):
        global qflag
        qflag = 1

    def EditInfo(self):
        global luru
        global mkpath
        global number
        name = self.ui.lineEdit.text()
        number = self.ui.lineEdit_2.text()
        cla = self.ui.lineEdit_3.text()
        sex = self.ui.lineEdit_4.text()
        age = self.ui.lineEdit_5.text()
        if number:
            mkpath = "./data/" + number
            mkdir(mkpath)
            if find_data(number):
                # tim = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                #GUI嵌入摄像头
                # self.openCamera()
                # luru = 1
                #重新打开摄像头窗口
                reply = QMessageBox.question(self.ui, '信息已存在', '确认重新采集人脸？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No) 
                if reply == QMessageBox.Yes:
                    face_save.generate(mkpath,number)
                    face_train.train(mkpath,number)
                else:
                     QMessageBox.question(self.ui, '提示', '可直接签到', QMessageBox.Yes)

            else:
                if name and number and cla and sex and age:
                    # tim = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    add_data(name,number,cla,sex,age)
                    #GUI嵌入摄像头
                    # self.openCamera()
                    # luru = 1
                    #重新打开摄像头窗口
                    face_save.generate(mkpath,number)
                    face_train.train(mkpath,number)
                    self.ui.label_8.setText(str(panduan.peple()))
                else:
                    QMessageBox.question(self.ui, '提示', '请先输入信息', QMessageBox.Yes)           
        else:
            QMessageBox.question(self.ui, '提示', '未确认到信息输入', QMessageBox.Yes)
            # print("未确认到信息输入")
    def facheck(self):
        # global facecheck 
        # self.openCamera()
        # facecheck = 1
        num = self.ui.lineEdit_6.text()
        if num:
            if face_predict.predict(num) == 1:
                checktime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                QMessageBox.question(self.ui, '提示', '签到成功', QMessageBox.Yes)
                self.ui.textBrowser.append('学号：'+num+' ' + '时间：'+checktime)
                self.ui.textBrowser.ensureCursorVisible()
                dat = [[num,checktime]]
                if  not os.path.exists('facetime.csv'):
                    savecsv.create_csv('facetime.csv')
                savecsv.append_csv('facetime.csv',dat)
                cv2.destroyAllWindows()
            else:
                QMessageBox.question(self.ui, '提示', '签到超时，请重新签到', QMessageBox.Yes)
                cv2.destroyAllWindows()
        else:
            QMessageBox.question(self.ui, '提示', '请输入学号', QMessageBox.Yes)
    def closeEvent(self, event):
        reply = QMessageBox.question(self.ui, '信息', '确认退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No) 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
if __name__ == '__main__':
    app = QApplication([])
    w = informationTest()
    w.ui.show()
    # app.exec_()
    sys.exit(app.exec_())
