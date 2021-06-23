
import cv2 as cv
import nanocamera as nano
import time
from threading import Thread
import numpy as np
import face_recognition
import pickle

class vStream:
    def __init__ (self,cam_type,dev_id,w,h):
        self.cam_type=cam_type
        self.dev_id=dev_id
        self.w=w
        self.h=h
        self.capture=nano.Camera(camera_type=cam_type,device_id=dev_id,width=w,height=h)
        self.thread=Thread(target=self.update,args=())
        self.thread.daemon=True
        self.thread.start()
    def update(self):
        while True:
            self.frame=self.capture.read()
    def getFrame(self):
        return self.frame

#Kamera
dispW=640
dispH=480
#PiCam= camera_type=0,device_id=0
#WebCam= camera_type=1,device_id=1
#camPi=nano.Camera(camera_type=0,device_id=0,width=dispW,height=dispH)
#camWeb= nano.Camera(camera_type=1,device_id=1,width=dispW,height=dispH)
camPi=vStream(0,0,dispW,dispH)
camWeb=vStream(1,1,dispW,dispH)

moveWindowX=dispW+70
moveWindowY=dispH+60

#Preberemo znane obraze
with open ('train.pkl','rb') as f:
    Names=pickle.load(f)
    Encodings=pickle.load(f)


scaleFactor=.3


dtAvg=0
startTime=time.time()
Font=cv.FONT_HERSHEY_SIMPLEX
napakaCount=0
facesCounter=0

while True:
    try:
        frameWeb = camWeb.getFrame()
        framePi = camPi.getFrame()

        frameCombined=np.hstack((frameWeb,framePi))

        frameRGB=cv.cvtColor(frameCombined,cv.COLOR_BGR2RGB)
        frameRGBsmall=cv.resize(frameRGB,(0,0),fx=scaleFactor,fy=scaleFactor)

        facePositions=face_recognition.face_locations(frameRGBsmall)    
        allEncodings=face_recognition.face_encodings(frameRGBsmall,facePositions)

        for(top,right,bot,left), face_encoding in zip(facePositions,allEncodings):
            name='Unknown Person'
            matches=face_recognition.compare_faces(Encodings,face_encoding)
            if True in matches:
                firstIndex=matches.index(True)
                name=Names[firstIndex]
                facesCounter+=1
                print(name, 'faces Counter=',facesCounter)

                
            top=int(top/scaleFactor)
            left=int(left/scaleFactor)
            bot=int(bot/scaleFactor)
            right=int(right/scaleFactor)

            cv.rectangle(frameCombined,(left,top),(right,bot),(255,0,0),2)
            cv.putText(frameCombined,name,(left,top-6),Font,.75,(0,255,255),2)

        dt=time.time()-startTime
        startTime=time.time()

        dtAvg=.9*dtAvg+.1*dt
        fps=1/dtAvg
        cv.rectangle(frameCombined,(0,0),(130,40),(0,0,255),-1)
        cv.putText(frameCombined,str(round(fps,1)),(0,25),Font,0.75,(255,0,0,),2)

        
        cv.imshow('Combined',frameCombined)
        cv.moveWindow('Combined',0,0)
        
        #cv.imshow('Web',frameWeb)
        #cv.moveWindow('Web',0,0)

        #cv.imshow('Pi',framePi)
        #cv.moveWindow('Pi',moveWindowX,0)
        
    except:
        #V primeru napake
        napakaCount+=1
        print('napaka counter=',napakaCount)

    if cv.waitKey(1)==ord('q'):
        break

camPi.capture.release()
camWeb.capture.release()
cv.destroyAllWindows()
exit(1)
