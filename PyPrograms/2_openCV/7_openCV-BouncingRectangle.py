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

    frame=cv.rectangle(frame,(posX,posY),(posX+bW,posY+bH),(0,255,0),-1)       #Narišemo kvadrat (slika,(levi zgornji kot x,y), (spodnji desni kot x,y),(barva blue,gree,red),debelina črte)

    cv.imshow('Cam1',frame)
    cv.moveWindow('Cam1',0,0)

    posX+=dX
    posY+=dY
    print(posX,posX+bW,posY,posY+bH)

    if posX<=0 or posX+bW>=dispW:
        dX=dX*(-1)
    if posY<=0 or posY+bH>=dispH:
        dY=dY*(-1)

    if cv.waitKey(1)==ord('q'):
        break
cam.release()
cv.destroyAllWindows()