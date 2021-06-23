import cv2 as cv
import sys
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
while True:
    ret, frame = cam.read()
    roi=frame[50:250,200:400].copy()                        #Naredimo kopijo glavne slike
    roiGray=cv.cvtColor(roi,cv.COLOR_BGR2GRAY)              #Naredimko novo sliko z BW barvo
    roiGray=cv.cvtColor(roiGray,cv.COLOR_GRAY2BGR)          #Spremenimo barvo iz BW v Color, (v bistvu samo postavimo pravi format)
    frame[50:250,200:400]=roiGray                           #Postavimo BW okvir v barvno sliko

    cv.moveWindow('Cam1',0,0)
    cv.imshow('Cam1',frame)

    cv.moveWindow('ROI',0,580)
    cv.imshow('ROI',roi)


    cv.moveWindow('ROIgray',300,580)
    cv.imshow('ROIgray',roiGray)

    if cv.waitKey(1)==ord('q'):
        break
cam.release()
cv.destroyAllWindows()