
import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np

#različni neti za prepoznavanje slik
net=jetson.inference.detectNet('ssd-mobilenet-v2',threshold=.5)


dispW=1280
dispH=720
flip=0

#web cam
cam=cv2.VideoCapture('/dev/video1')        #poglej parametre v4l2-ctl -d /dev/video1 --list-formats-ext 
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

#PiCam
#camSet='nvarguscamerasrc wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.1 saturation=1.2 ! appsink drop=true'
#cam=cv2.VideoCapture(camSet)

timeMark=time.time()
fpsFilter=0
font=cv2.FONT_HERSHEY_SIMPLEX

while True:
    #preberemo sliko z cv2
    _,img =cam.read()

    width=img.shape[0]
    height=img.shape[1]

    #pretvorimo sliko iz BGR v RGBA v jetson utils
    frame=cv2.cvtColor(img,cv2.COLOR_BGR2RGBA).astype(np.float32)
    frame=jetson.utils.cudaFromNumpy(frame)

    #zaznamo objekt
    detections=net.Detect(frame,width,height)
    
    #razbijemo array detections
    for detect in detections:
        #print(detect)
        id=detect.ClassID
        top=int(detect.Top)
        left=int(detect.Left)
        bot=int(detect.Bottom)
        right=int(detect.Right)
        #print(id)
        item=net.GetClassDesc(id)
        #print(item,' top:',top,' left:',left,' bot:',bot,' right:',right )
        tk=1
        if item=='cat':
            tk=-1


        cv2.putText(img,item,(left,top+20),font,.75,(255,0,0),2)
        cv2.rectangle(img,(left,top),(right,bot),(0,255,0),1)

    
    #izračunamo fps
    dt=time.time()-timeMark
    fps=1/dt
    fpsFilter=.95*fpsFilter+.05*fps
    timeMark=time.time()


    #Napišemo teks
    #cv2.putText(img,str(round(fpsFilter,1))+ ' fps',(0,30),font,1,(255,0,0),2)

    #prikažemo sliko
    cv2.imshow('cam',img)
    cv2.moveWindow('cam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

