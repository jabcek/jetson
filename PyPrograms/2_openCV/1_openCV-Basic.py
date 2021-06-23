import cv2 as cv
import sys
import nanocamera as nano
print(sys.version)
print(cv.__version__)

dispW=640
dispH=480

#PiCam= camera_type=0,device_id=0
#WebCam= camera_type=1,device_id=1
cam= nano.Camera(camera_type=0,device_id=0,width=dispW,height=dispH)

moveWindowX=dispW+60
moveWindowY=dispH+120

while True:
    frame = cam.read()

    

    cv.imshow('Cam',frame)
    cv.moveWindow('Cam',moveWindowX*0,moveWindowY*0)


    if cv.waitKey(1)==ord('q'):
        break

cam.release()
cv.destroyAllWindows()