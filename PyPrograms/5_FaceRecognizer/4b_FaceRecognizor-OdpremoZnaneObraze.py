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


Encodings=[]
Names=[]
counter=0

#Odpremo podatke iz datoteke train.pkl
#Ime datoteke, read

with open('train.pkl','rb') as f:
    Names=pickle.load(f)
    Encodings=pickle.load(f)


#Nalozimo neznane slike        
image_dir='/home/jure/Desktop/PyPrograms/5_FaceRecognizer/demoImages/unknown'

Font=cv.FONT_HERSHEY_SIMPLEX

for root,dirs,files in os.walk(image_dir):
    #print (files)

    for file in files:
        path=os.path.join(root,file)
        testImage=face_recognition.load_image_file(path)
        
        #Poiscemo obraze na sliki
        face_locations=face_recognition.face_locations(testImage)
        
        #Poiscemo encodinge od vseh obrazov na sliki, kjer iščemo obraze
        allEncodings=face_recognition.face_encodings(testImage,face_locations)

        #spremenimo sliko v črnobelo
        testImage=cv.cvtColor(testImage,cv.COLOR_RGB2BGR)
        
        for(top,right,bot,left), face_encoding in zip(face_locations,allEncodings):
            name='Unknown Person'
            matches=face_recognition.compare_faces(Encodings,face_encoding)
            
            if True in matches:
                first_match_index=matches.index(True)
                name=Names[first_match_index]
                
            cv.rectangle(testImage,(left,top),(right,bot),(0,0,255),2)
            cv.putText(testImage,name,(left,top-6),Font,.75,(0,255,255),2)

        cv.imshow('Image',testImage)
        cv.moveWindow('Image',0,0)

        if cv.waitKey(0)==ord('q'):
            cv.destroyAllWindows()
