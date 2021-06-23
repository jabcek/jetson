import cv2 as cv
import sys
import numpy as np
import nanocamera as nano

#Kamera
dispW=640
dispH=480
#PiCam= camera_type=0,device_id=0
#WebCam= camera_type=1,device_id=1
cam= nano.Camera(camera_type=1,device_id=1,width=dispW,height=dispH)

moveWindowX=680
moveWindowY=580

face_cascade=cv.CascadeClassifier('/home/jure/Desktop/PyPrograms/4_Cascades/Face.xml')


while True:
    frame = cam.read()

    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)


    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    cv.imshow('Cam1',frame)
    cv.moveWindow('Cam1',(moveWindowX)*0,(moveWindowY)*0)

    if cv.waitKey(1)==ord('q'):
        break

cam.release()
cv.destroyAllWindows()

