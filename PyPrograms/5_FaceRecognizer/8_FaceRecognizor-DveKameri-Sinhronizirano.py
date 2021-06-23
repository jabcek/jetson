import cv2 as cv
import nanocamera as nano
import time
from threading import Thread
import numpy as np

#Kamera
dispW=640
dispH=480
#PiCam= camera_type=0,device_id=0
#WebCam= camera_type=1,device_id=1
#camPi=nano.Camera(camera_type=0,device_id=0,width=dispW,height=dispH)
#camWeb= nano.Camera(camera_type=1,device_id=1,width=dispW,height=dispH)

moveWindowX=dispW+70
moveWindowY=dispH+60

class vStream:
    def __init__ (self,cam_type,dev_id,w,h):
        self.cam_type=cam_type
        self.dev_id=dev_id
        self.w=w
        self.h=h
        self.capture=nano.Camera(camera_type=cam_type,device_id=dev_id,width=w,height=h,fps=30)
        self.thread=Thread(target=self.update,args=())
        self.thread.daemon=True
        self.thread.start()
    def update(self):
        while True:
            self.frame=self.capture.read()
    def getFrame(self):
        return self.frame

camPi=vStream(0,0,dispW,dispH)
camWeb=vStream(1,1,dispW,dispH)


dtAvg=0
startTime=time.time()
Font=cv.FONT_HERSHEY_SIMPLEX

while True:
    try:
        frameWeb = camWeb.getFrame()
        
        framePi = camPi.getFrame()

        
        frameCombined=np.hstack((frameWeb,framePi))
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
        test='test'

    if cv.waitKey(1)==ord('q'):
        break

camPi.capture.release()
camWeb.capture.release()
cv.destroyAllWindows()
exit(1)
