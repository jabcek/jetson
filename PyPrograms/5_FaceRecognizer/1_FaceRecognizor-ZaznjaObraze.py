import cv2 as cv
import sys
import numpy as np
import nanocamera as nano
import face_recognition

#Kamera
dispW=640
dispH=480
#PiCam= camera_type=0,device_id=0
#WebCam= camera_type=1,device_id=1
cam= nano.Camera(camera_type=1,device_id=1,width=dispW,height=dispH)

moveWindowX=680
moveWindowY=580

image=face_recognition.load_image_file('/home/jure/Desktop/PyPrograms/5_FaceRecognizer/demoImages/unknown/u3.jpg')
face_locations=face_recognition.face_locations(image)
print(face_locations)

image=cv.cvtColor(image,cv.COLOR_RGB2BGR)

for(row1,col1,row2,col2) in face_locations:
    cv.rectangle(image,(col1,row1),(col2,row2),(0,0,255),2)

cv.imshow('Image',image)
cv.moveWindow('Image',0,0)

if cv.waitKey(0)==ord('q'):
    cv.destroyAllWindows()
