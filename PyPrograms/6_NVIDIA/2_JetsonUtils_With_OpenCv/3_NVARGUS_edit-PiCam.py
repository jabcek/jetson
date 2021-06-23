
import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np 

#različni neti za prepoznavanje slik
net=jetson.inference.imageNet('googlenet') 

dispW=640
dispH=480
flip=0

#Web cam
#cam=cv2.VideoCapture('/dev/video1')
#cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

#PiCam
camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.1 saturation=1.2 ! appsink drop=true'
cam=cv2.VideoCapture(camSet)

font=cv2.FONT_HERSHEY_SIMPLEX

timeMark=time.time()
fpsFilter=0

while True:
    #preberemo sliko z cv2
    _,frame =cam.read()
    #pretvorimo sliko iz BGR v RGBA
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    #pretvorimo sliko v cuda
    img=jetson.utils.cudaFromNumpy(img)

    classID, cinfident=net.Classify(img,dispW,dispH)
    item=net.GetClassDesc(classID)

    dt=time.time()-timeMark
    fps=1/dt
    fpsFilter=.95*fpsFilter+.05*fps
    timeMark=time.time()

    #Napišemo teks
    cv2.putText(frame,str(round(fpsFilter,1))+ ' fps  '+item,(0,30),font,1,(255,0,0),2)

    #prikažemo sliko
    cv2.imshow('cam',frame)
    cv2.moveWindow('cam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()