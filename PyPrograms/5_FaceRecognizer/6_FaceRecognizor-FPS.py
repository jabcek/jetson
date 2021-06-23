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
cam= nano.Camera(camera_type=1,device_id=1,width=dispW,height=dispH)
#cam=cv.VideoCapture('dev/video1')
moveWindowX=680
moveWindowY=580


Encodings=[]
Names=[]
counter=0

#Odpremo podatke iz datoteke train.pkl
#Ime datoteke, read

with open('train.pkl','rb') as f:
    Names=pickle.load(f)
    Encodings=pickle.load(f)

Font=cv.FONT_HERSHEY_SIMPLEX

scaleFactor=0.3

startTime=time.time()
dtAvg=0
while True:
    frame = cam.read()
    frameSmall=cv.resize(frame,(0,0),fx=scaleFactor,fy=scaleFactor)
    frameRGB=cv.cvtColor(frameSmall,cv.COLOR_BGR2RGB)
    facePositions=face_recognition.face_locations(frameRGB, model='CNN')
    allEncodings=face_recognition.face_encodings(frameRGB,facePositions)

    for(top,right,bot,left), face_encoding in zip(facePositions,allEncodings):
        name='Unknown Person'
        matches=face_recognition.compare_faces(Encodings,face_encoding)
        if True in matches:
            firstIndex=matches.index(True)
            name=Names[firstIndex]

        top=int(top/scaleFactor)
        left=int(left/scaleFactor)
        bot=int(bot/scaleFactor)
        right=int(right/scaleFactor)

        cv.rectangle(frame,(left,top),(right,bot),(255,0,0),2)
        cv.putText(frame,name,(left,top-6),Font,.75,(0,255,255),2)

    dt=time.time()-startTime
    startTime=time.time()

    dtAvg=.9*dtAvg+.1*dt

    fps=1/dtAvg
    print ('fps=',round(fps,1))
    timeStamp=time.time()
    cv.rectangle(frame,(0,0),(100,40),(0,0,255),-1)
    cv.putText(frame,str(round(fps,1))+' fps',(0,25),Font,.75,(0,255,255),2)

    cv.imshow('Image',frame)
    cv.moveWindow('Image',0,0)

    if cv.waitKey(1)==ord('q'):
        break

cam.release()
cv.destroyAllWindows()
