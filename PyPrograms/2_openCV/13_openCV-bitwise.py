import cv2 as cv
import sys
import numpy as np
print(sys.version)
print(cv.__version__)

dispW=640
dispH=480
flip=0
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc sensor_mode=0 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv.VideoCapture(0)

img1=np.zeros((480,640,1),np.uint8)
img1[0:480,0:320]=[255]

img2=np.zeros((480,640,1),np.uint8)
img2[190:290,270:370]=[255]

bitAnd=cv.bitwise_and(img1,img2)

bitOr=cv.bitwise_or(img1,img2)

bitXOr=cv.bitwise_xor(img1,img2)

while True:
    ret, frame = cam.read()

    cv.moveWindow('img1',0,500)
    cv.imshow('img1',img1)

    cv.moveWindow('img2',710,0)
    cv.imshow('img2',img2)

    cv.moveWindow('bitAnd',710,500)
    cv.imshow('bitAnd',bitAnd)

    cv.moveWindow('bitOr',1350,0)
    cv.imshow('bitOr',bitOr)

    cv.moveWindow('bitXOr',1350,500)
    cv.imshow('bitXOr',bitXOr)

    frame=cv.bitwise_and(frame,frame,mask=bitXOr)
    cv.moveWindow('Cam1',0,0)
    cv.imshow('Cam1',frame)

    if cv.waitKey(1)==ord('q'):
        break
cam.release()
cv.destroyAllWindows()