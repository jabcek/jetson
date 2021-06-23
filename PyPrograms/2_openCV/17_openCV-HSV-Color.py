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

moveWindowX=680
moveWindowY=580

def nothing(x):
    pass

cv.namedWindow('Trackbars')
cv.createTrackbar('hue1Low','Trackbars',50,179,nothing)
cv.createTrackbar('hue1High','Trackbars',100,179,nothing)
cv.createTrackbar('hue2Low','Trackbars',50,179,nothing)
cv.createTrackbar('hue2High','Trackbars',100,179,nothing)
cv.createTrackbar('satLow','Trackbars',100,255,nothing)
cv.createTrackbar('satHigh','Trackbars',255,255,nothing)
cv.createTrackbar('valLow','Trackbars',100,255,nothing)
cv.createTrackbar('valHigh','Trackbars',255,255,nothing)

hue1Low=cv.getTrackbarPos('hue1Low','Trackbars')
hue1High=cv.getTrackbarPos('hue1High','Trackbars')
hue2Low=cv.getTrackbarPos('hue2Low','Trackbars')
hue2High=cv.getTrackbarPos('hue2High','Trackbars')
satLow=cv.getTrackbarPos('satLow','Trackbars')
satHigh=cv.getTrackbarPos('satHigh','Trackbars')
valLow=cv.getTrackbarPos('valLow','Trackbars')
valHigh=cv.getTrackbarPos('valHigh','Trackbars')
cv.moveWindow('Trackbars',(moveWindowX)*2,(moveWindowY)*1)

while True:
    ret, frame = cam.read()

    #frame=cv.imread('smarties.png')

    cv.imshow('Cam1',frame)
    cv.moveWindow('Cam1',(moveWindowX)*0,(moveWindowY)*0)

    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    hue1LowVal=cv.getTrackbarPos('hue1Low','Trackbars')
    hue1HighVal=cv.getTrackbarPos('hue1High','Trackbars')
    hue2LowVal=cv.getTrackbarPos('hue2Low','Trackbars')
    hue2HighVal=cv.getTrackbarPos('hue2High','Trackbars')
    satLowVal=cv.getTrackbarPos('satLow','Trackbars')
    satHighVal=cv.getTrackbarPos('satHigh','Trackbars')
    valLowVal=cv.getTrackbarPos('valLow','Trackbars')
    valHighVal=cv.getTrackbarPos('valHigh','Trackbars')

    lowValues1=np.array([hue1LowVal,satLowVal,valLowVal])
    highValues1=np.array([hue1HighVal,satHighVal,valHighVal])

    lowValues2=np.array([hue2LowVal,satLowVal,valLowVal])
    highValues2=np.array([hue2HighVal,satHighVal,valHighVal])


    FGmask1=cv.inRange(hsv,lowValues1,highValues1)
    FGmask2=cv.inRange(hsv,lowValues2,highValues2)

    FGmaskComp=cv.add(FGmask1,FGmask2)

    cv.imshow('FGmaskComp',FGmaskComp)
    cv.moveWindow('FGmaskComp',(moveWindowX)*0,(moveWindowY)*1)


    FG=cv.bitwise_and(frame,frame,mask=FGmaskComp)
    cv.imshow('FG',FG)
    cv.moveWindow('FG',(moveWindowX)*1,(moveWindowY)*0)

    BGmask=cv.bitwise_not(FGmaskComp)
    cv.imshow('BGmask',BGmask)
    cv.moveWindow('BGmask',(moveWindowX)*1,(moveWindowY)*1)

    BG=cv.cvtColor(BGmask,cv.COLOR_GRAY2BGR)
    #cv.imshow('BG',BG)
    #cv.moveWindow('BG',(moveWindowX)*2,(moveWindowY)*0)

    final=cv.add(FG,BG)
    cv.imshow('final',final)
    cv.moveWindow('final',(moveWindowX)*2,(moveWindowY)*0)

    if cv.waitKey(1)==ord('q'):
        break

cam.release()
cv.destroyAllWindows()

