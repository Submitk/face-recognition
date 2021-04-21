
import cv2


def up_Clicked():
    print("up")
    # i = i - 10
    # if i<=50:
          # i=50
    # p2.ChangeDutyCycle(2.5 + 10 * i / 180) #设置转动角度
    # time.sleep(0.02)                      #等该20ms周期结束
    # p2.ChangeDutyCycle(0)                  #归零信号
    # time.sleep(0.2)


def down_Clicked():
    print("down")
    # i = i + 10
    # if i>=140:
          # i=140
    # p2.ChangeDutyCycle(2.5 + 10 * i / 180) #设置转动角度
    # time.sleep(0.02)                      #等该20ms周期结束
    # p2.ChangeDutyCycle(0)                  #归零信号
    # time.sleep(0.2)


def left_Clicked():
    print("left")
    #j = j + 10
    # if j>=140:
          # j=140
    # p1.ChangeDutyCycle(2.5 + 10 * j / 180) #设置转动角度
    # time.sleep(0.02)                      #等该20ms周期结束
    # p1.ChangeDutyCycle(0)                  #归零信号
    # time.sleep(0.2)


def right_Clicked():
    print("right")
    #j = j - 10
    # if j<=50:
          # j=50
    # p1.ChangeDutyCycle(2.5 + 10 * j / 180) #设置转动角度
    # time.sleep(0.02)                      #等该20ms周期结束
    # p1.ChangeDutyCycle(0)                  #归零信号
    # time.sleep(0.2)


def change_direction(direction):

    if direction == 1:
        up_Clicked()
    elif direction == 2:
        down_Clicked()
    elif direction == 3:
        left_Clicked()
    elif direction == 4:
        right_Clicked()

############################################
#	函数名：generate					   #
#	输入：录入的人脸编号Id				   #
#	返回值：无							   #
#	作用：保存人脸数据					   #
############################################


def generate(mkpath,number):
    ###############初始化摄像头舵机##################
    # import RPi.GPIO as GPIO
    # import signal
    # import atexit

    # atexit.register(GPIO.cleanup)
    # servopin1 = 17
    # servopin2 = 27
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(servopin1, GPIO.OUT, initial=False)
    # GPIO.setup(servopin2, GPIO.OUT, initial=False)
    # p1 = GPIO.PWM(servopin1,50) #50HZ
    # p1.start(0)
    # p2 = GPIO.PWM(servopin2,50) #50HZ
    # p2.start(0)
    # time.sleep(2)
    ################################################

    detector = cv2.CascadeClassifier(
        'haarcascade/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    sampleNum = 0
    # i = 1
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, 1)

        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(img, 1.3, 5)
        for (x, y, w, h) in faces:
            # print(x,y)
            # #############方向自己调试#############
            # #向上
            # if y>=0 and y<200:
            # 	change_direction(1)
            # #向下
            # if y>=300 and y<500:
            # 	change_direction(2)
            # #向左
            # if x>=0 and x<200:
            # 	change_direction(3)
            # #向右
            # if x>=300 and x<500:
            # 	change_direction(4)

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            gray_than = (h)/(w)
            f = cv2.resize(img[y:y+h, x:x+w], (200, int(200*gray_than)))
        # incrementing sample number
            sampleNum = sampleNum + 1
        # saving the captured face in the dataset folder
            # cv2.imwrite("data_user/User." + str(Id) +
            #             '.' + str(sampleNum) + ".jpg", f)  #
            cv2.imwrite(mkpath + "/User." + str(number) +
                            '.' + str(sampleNum) + ".jpg", f)
            cv2.putText(img, str((x, y)), (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
            cv2.putText(img, str(sampleNum), (x, y - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)

        cv2.imshow('GetFace', img)
        # wait for 1 miliseconds
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # break if the sample number is morethan 300
        elif sampleNum >= 30:
            break

    cap.release()
    cv2.destroyAllWindows()


# generate(123)
