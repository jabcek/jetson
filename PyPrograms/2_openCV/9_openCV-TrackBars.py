import cv2 as cv
import numpy as np
import sys

print(cv.__version__)
print(sys.version)

dispW=640
dispH=480
flip=0
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc sensor_mode=0 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv.VideoCapture(camSet)


#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv.VideoCapture(0)

def nothing(x):
    pass

cv.namedWindow('Cam1')
cv.createTrackbar('xVal','Cam1',0,dispW,nothing)
cv.createTrackbar('yVal','Cam1',0,dispH,nothing)
cv.createTrackbar('width','Cam1',50,200,nothing)
cv.createTrackbar('height','Cam1',50,200,nothing)




while True:
    ret, frame = cam.read()

    xVal=cv.getTrackbarPos('xVal','Cam1')
    yVal=cv.getTrackbarPos('yVal','Cam1')
    width=cv.getTrackbarPos('width','Cam1')
    height=cv.getTrackbarPos('height','Cam1')

    frame=cv.rectangle(frame,(xVal,yVal),(xVal+width,yVal+height),(0,255,0),3)

    cv.imshow('Cam1',frame)
    cv.moveWindow('Cam1',0,0)

    keyEvent=cv.waitKey(1)
    if keyEvent==ord('q'):
        break


cam.release()
cv.destroyAllWindows()

