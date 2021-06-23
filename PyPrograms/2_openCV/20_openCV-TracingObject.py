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

#Servo motorji
from adafruit_servokit import ServoKit
import time
kit=ServoKit(channels=16)
panServo=0
tiltServo=1
panServoVal=90
tiltServoVal=45
kit.servo[panServo].angle=panServoVal
kit.servo[tiltServo].angle=tiltServoVal

#Trackbari
def nothing(x):
    pass

cv.namedWindow('Trackbars')
"""
cv.createTrackbar('hue1Low','Trackbars',50,179,nothing)
cv.createTrackbar('hue1High','Trackbars',100,179,nothing)
cv.createTrackbar('hue2Low','Trackbars',50,179,nothing)
cv.createTrackbar('hue2High','Trackbars',100,179,nothing)
cv.createTrackbar('satLow','Trackbars',100,255,nothing)
cv.createTrackbar('satHigh','Trackbars',255,255,nothing)
cv.createTrackbar('valLow','Trackbars',100,255,nothing)
cv.createTrackbar('valHigh','Trackbars',255,255,nothing)
"""

cv.createTrackbar('hue1Low','Trackbars',110,179,nothing)
cv.createTrackbar('hue1High','Trackbars',130,179,nothing)
cv.createTrackbar('hue2Low','Trackbars',50,179,nothing)
cv.createTrackbar('hue2High','Trackbars',0,179,nothing)
cv.createTrackbar('satLow','Trackbars',150,255,nothing)
cv.createTrackbar('satHigh','Trackbars',255,255,nothing)
cv.createTrackbar('valLow','Trackbars',50,255,nothing)
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
    frame = cam.read()


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

   

    tmp = cv.findContours(FGmaskComp,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    contours = tmp[0] if len(tmp) == 2 else tmp[1]
    #cv.drawContours()(frame,contours,-1,(255,0,0),3)

    contours=sorted(contours,key=lambda x:cv.contourArea(x),reverse=True)
    for cnt in contours:
        area=cv.contourArea(cnt)
        (x,y,w,h)=cv.boundingRect(cnt)
        if area>=50:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            objX=x+w/2
            objY=y+h/2
            errorPan=objX-dispW/2
            errorTilt=objY-dispH/2
            """Simple control system
            if errorPan>0:
                panServoVal-=.5
            else:
                panServoVal+=.5
            if errorTilt>0:
                tiltServoVal-=.5
            else:
                tiltServoVal+=.5
            """
            """P control system
            """
            if abs(errorPan)>15:
                panServoVal-=errorPan/75
            if abs(errorTilt)>15:
                tiltServoVal-=errorTilt/75


            if panServoVal>180:
                panServoVal=180
                print("Pan out of range")
            if panServoVal<0:
                panServoVal=0
                print("Pan out of range")
            if tiltServoVal>180:
                tiltServoVal=180
                print("Tilt out of range")
            if tiltServoVal<0:
                tiltServoVal=0
                print("Tilt out of range")
            
            kit.servo[panServo].angle=panServoVal
            kit.servo[tiltServo].angle=tiltServoVal
            break
     
    cv.imshow('Cam1',frame)
    cv.moveWindow('Cam1',(moveWindowX)*0,(moveWindowY)*0)

    if cv.waitKey(1)==ord('q'):
        break

cam.release()
cv.destroyAllWindows()

