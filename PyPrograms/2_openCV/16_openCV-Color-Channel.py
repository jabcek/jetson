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

moveWindowX=dispW
moveWindowX1=30
moveWindowY=dispH
moveWindowY1=120


blank=np.zeros([480,640,1],np.uint8)

while True:
    ret, frame = cam.read()

    
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    print(frame[50,45,0])
   # print(gray.shape)
   # print(frame.size)

    blue,green,red=cv.split(frame)

    blueWin=cv.merge((blue,blank,blank))
    greenWin=cv.merge((blank,green,blank))
    redWin=cv.merge((blank,blank,red))

    #green[:]=green[:]*0.1
    mergeIm=cv.merge((blue,green,red))

    cv.imshow('blueWin',blueWin)
    cv.moveWindow('blueWin',(moveWindowX+moveWindowX1)*0,(moveWindowY+moveWindowY1)*1)

    cv.imshow('greenWin',greenWin)
    cv.moveWindow('greenWin',(moveWindowX+moveWindowX1)*1,(moveWindowY+moveWindowY1)*1)
    
    cv.imshow('redWin',redWin)
    cv.moveWindow('redWin',(moveWindowX+moveWindowX1)*2,(moveWindowY+moveWindowY1)*1)

    cv.imshow('mergeIm',mergeIm)
    cv.moveWindow('mergeIm',(moveWindowX+moveWindowX1)*1,(moveWindowY+moveWindowY1)*0)

    #blue=cv.split(frame)[0]
    #green=cv.split(frame)[1]
    #red=cv.split(frame)[2]

    #cv.imshow('blue',blue)
    #cv.moveWindow('blue',(moveWindowX+moveWindowX1)*0,(moveWindowY+moveWindowY1)*1)

    #cv.imshow('green',green)
    #cv.moveWindow('green',(moveWindowX+moveWindowX1)*1,(moveWindowY+moveWindowY1)*1)
    
    #cv.imshow('red',red)
    #cv.moveWindow('red',(moveWindowX+moveWindowX1)*2,(moveWindowY+moveWindowY1)*1)

    cv.imshow('Cam1',frame)
    cv.moveWindow('Cam1',(moveWindowX+moveWindowX1)*0,(moveWindowY+moveWindowY1)*0)

    #cv.imshow('blank',blank)
    #cv.moveWindow('blank',(moveWindowX+moveWindowX1)*1,(moveWindowY+moveWindowY1)*0)

    if cv.waitKey(1)==ord('q'):
        break

cam.release()
cv.destroyAllWindows()