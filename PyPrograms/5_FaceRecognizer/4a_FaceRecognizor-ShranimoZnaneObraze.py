import cv2 as cv
import sys
import numpy as np
import nanocamera as nano
import face_recognition
import os
import pickle

#Kamera
dispW=640
dispH=480
#PiCam= camera_type=0,device_id=0
#WebCam= camera_type=1,device_id=1
cam= nano.Camera(camera_type=1,device_id=1,width=dispW,height=dispH)

moveWindowX=680
moveWindowY=580


#Naložimo znane obraze
image_dir='/home/jure/Desktop/PyPrograms/5_FaceRecognizer/demoImages/known'
Encodings=[]
Names=[]

for root,dirs,files in os.walk(image_dir):
    #print (files)

    for file in files:
        path=os.path.join(root,file)
        #print (path)
        name=os.path.splitext(file)[0]
        print(name)
        person=face_recognition.load_image_file(path)
        encoding=face_recognition.face_encodings(person)[0]
        Encodings.append(encoding)
        Names.append(name)

#Shranimo podatke v datoteko train.pkl
#Ime datoteke, write
with open('train.pkl','wb') as f:
    pickle.dump(Names,f)
    pickle.dump(Encodings,f)
