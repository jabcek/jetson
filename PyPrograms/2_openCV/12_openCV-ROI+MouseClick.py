import cv2 as cv
import numpy as np

print(cv.__version__)

dispW=640
dispH=480
flip=0
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv.VideoCapture(0)

goFlag=0

#ClickMouse
def mouse_click(event,x,y,flags,params):
    global x1,y1,x2,y2
    global goFlag
    if(event==cv.EVENT_LBUTTONDOWN):
        x1=x
        y1=y
        goFlag=0
    if(event==cv.EVENT_LBUTTONUP):
        x2=x
        y2=y
        goFlag=1



cv.namedWindow('Cam1')
cv.setMouseCallback('Cam1',mouse_click)


while True:
    ret, frame = cam.read()

    if(goFlag==1):
        frame=cv.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),3)
        roi=frame[y1:y2,x1:x2]
        cv.imshow('rectImage',roi)
        cv.moveWindow('rectImage',705,0)

    cv.moveWindow('Cam1',0,0)
    cv.imshow('Cam1',frame)


    keyEvent=cv.waitKey(1)
    if keyEvent==ord('q'):
        break
    if keyEvent==ord('c'):
        coord=[]

cam.release()
cv.destroyAllWindows()

