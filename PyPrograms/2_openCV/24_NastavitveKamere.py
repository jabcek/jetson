import cv2 as cv
print(cv.__version__)

dispW=640
dispH=480
flip=0

#PiCam= camera_type=0,device_id=0
#WebCam= camera_type=1,device_id=1
# Gstreamer code for improvded Raspberry Pi Camera Quality
camSet='nvarguscamerasrc wbmode=1 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=2.0 brightness=-.1 saturation=1.5 ! appsink'
cam=cv.VideoCapture(camSet)


moveWindowX=dispW+60
moveWindowY=dispH+120

while True:
    _,frame = cam.read()

    

    cv.imshow('Cam',frame)
    cv.moveWindow('Cam',moveWindowX*0,moveWindowY*0)


    if cv.waitKey(1)==ord('q'):
        break

cam.release()
cv.destroyAllWindows()