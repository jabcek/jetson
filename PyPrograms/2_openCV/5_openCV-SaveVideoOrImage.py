import cv2 as cv
import nanocamera as nano
print(cv.__version__)
dispW=640
dispH=480
flip=0
#PiCam= camera_type=0,device_id=0
#WebCam= camera_type=1,device_id=1
cam= nano.Camera(camera_type=1,device_id=1,width=dispW,height=dispH)
#video
#outVid=cv.VideoWriter('3_Videos_Images/myCam.avi',cv.VideoWriter_fourcc(*'XVID'),21,(dispW,dispH))

while True:
    frame = cam.read()

    #image
    #"""
    if cv.waitKey(1)==ord('i'):
        cv.imwrite('3_Videos_Images/myImage.jpg', frame)
        break
    #"""


    #video
    """
    outVid.write(frame)

    if cv.waitKey(1)==ord('q'):
        break
    """

    cv.imshow('Cam1',frame)
    cv.moveWindow('Cam1',0,0)

cam.release()
#outVid.release()
cv.destroyAllWindows()