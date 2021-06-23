import cv2 as cv
import sys
import numpy as np
import nanocamera as nano
import face_recognition
import os
import pickle
import time

#Kamera
dispW=640
dispH=480
#PiCam= camera_type=0,device_id=0
#WebCam= camera_type=1,device_id=1
camPi=nano.Camera(camera_type=0,device_id=0,width=dispW,height=dispH)
camWeb= nano.Camera(camera_type=1,device_id=1,width=dispW,height=dispH)


moveWindowX=dispW+70
moveWindowY=dispH+60

dtAvg=0
startTime=time.time()
Font=cv.FONT_HERSHEY_SIMPLEX

while True:
    frameWeb = camWeb.read()
    framePi = camPi.read()

    frameCombined=np.hstack((frameWeb,framePi))
    dt=time.time()-startTime
    startTime=time.time()

    dtAvg=.9*dtAvg+.1*dt
    fps=1/dtAvg
    cv.rectangle(frameCombined,(0,0),(130,40),(0,0,255),-1)
    cv.putText(frameCombined,str(round(fps,1)),(0,25),Font,0.75,(255,0,0,),2)

    #cv.imshow('camWeb',frameWeb)
    #cv.moveWindow('camWeb',0,0)

    #cv.imshow('camPi',framePi)
    #cv.moveWindow('camPi',moveWindowX,0)

    cv.imshow('Combo',frameCombined)
    cv.moveWindow('Combo',0,0)

    if cv.waitKey(1)==ord('q'):
        break

camPi.release()
camWeb.release()
cv.destroyAllWindows()
