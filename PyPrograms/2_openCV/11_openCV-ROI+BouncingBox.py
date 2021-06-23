import cv2 as cv
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

posX=2
posY=200
bW=int(.25*dispW)
bH=int(.25*dispH)
dX=2
dY=2


while True:
    ret, frame = cam.read()
    roi=frame[posY:posY+bH,posX:posX+bW].copy()  

    frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)  
    frame=cv.cvtColor(frame,cv.COLOR_GRAY2BGR)   
    frame[posY:posY+bH,posX:posX+bW]=roi    
    cv.rectangle(frame,(posX,posY),(posX+bW,posY+bH),(0,0,255),2) 

    

    cv.imshow('Cam1',frame)
    cv.moveWindow('Cam1',0,0)

    #cv.imshow('Cam2',frame)
    #cv.moveWindow('Cam2',0,550)

    posX+=dX
    posY+=dY


    if posX<=0 or posX+bW>=dispW:
        dX=dX*(-1)
    if posY<=0 or posY+bH>=dispH:
        dY=dY*(-1)

    if cv.waitKey(1)==ord('q'):
        break
cam.release()
cv.destroyAllWindows()