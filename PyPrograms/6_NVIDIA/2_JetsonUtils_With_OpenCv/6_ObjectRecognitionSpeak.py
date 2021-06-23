import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np 
import os
from gtts import gTTS
import threading


#različni neti za prepoznavanje slik
net=jetson.inference.imageNet('googlenet') 

dispW=640
dispH=480
flip=0

#Web cam
cam=cv2.VideoCapture('/dev/video1')
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

#PiCam
#camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.1 saturation=1.2 ! appsink drop=true'
#cam=cv2.VideoCapture(camSet)

font=cv2.FONT_HERSHEY_SIMPLEX

timeMark=time.time()
fpsFilter=0


speak=True
item='Welcome to my identify. Are you ready to rumble?'
confidence=0
itemOld=''

def sayItem():
    global speak
    global item
    while True:
        if(speak==True):
            output=gTTS(text=item,lang='en',slow=False)
            output.save('output.mp3')
            os.system('mpg123 output.mp3')
            speak=False

x=threading.Thread(target=sayItem,daemon=True)
x.start()

while True:
    #preberemo sliko z cv2
    _,frame =cam.read()

    #pretvorimo sliko iz BGR v RGBA v jetson utils
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    img=jetson.utils.cudaFromNumpy(frame)

    if speak==False:
        classID, confidence=net.Classify(img,dispW,dispH)
        if confidence>=.5:
            item=net.GetClassDesc(classID)
            if item!=itemOld:
                speak=True
        if confidence<.5:
            item=''
        itemOld=item

    dt=time.time()-timeMark
    fps=1/dt
    fpsFilter=.95*fpsFilter+.05*fps
    timeMark=time.time()

    #Napišemo teks
    cv2.putText(frame,str(round(fpsFilter,1))+ ' fps  '+item+'   '+str(round(confidence,2)),(0,30),font,1,(255,0,0),2)

    #prikažemo sliko
    cv2.imshow('cam',frame)
    cv2.moveWindow('cam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()