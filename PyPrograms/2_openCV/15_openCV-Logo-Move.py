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

moveWindowX=dispW+60     #dispW+60
moveWindowY=dispH+120     #dispH+120

def nothing(x):
    pass

#cv.namedWindow('Blended')
#cv.createTrackbar('BlendVal','Blended',50,100,nothing)

bW=75
bH=75
posX=10
posY=10
dX=3
dY=3



while True:
    ret, frame = cam.read()



    pl=cv.imread('pl.jpg')
    pl=cv.resize(pl,(75,75))
    cv.imshow('pl',pl)
    cv.moveWindow('pl',moveWindowX*1,moveWindowY*0)

    plBW=cv.cvtColor(pl,cv.COLOR_BGR2GRAY)
    cv.imshow('plBW',plBW)
    cv.moveWindow('plBW',moveWindowX*2,moveWindowY*0)


    _,BGMask=cv.threshold(plBW,250,255,cv.THRESH_BINARY)
    cv.imshow('BGMask', BGMask)
    cv.moveWindow('BGMask',moveWindowX*3,moveWindowY*0)

    FGMask=cv.bitwise_not(BGMask)
    cv.imshow('FGMask', FGMask)
    cv.moveWindow('FGMask',moveWindowX*0,moveWindowY*1)

    FG=cv.bitwise_and(pl,pl,mask=FGMask)
    cv.imshow('FG', FG)
    cv.moveWindow('FG',moveWindowX*1,moveWindowY*1)

    ROI=frame[posY:posY+bH,posX:posX+bW]
    ROIBG=cv.bitwise_and(ROI,ROI,mask=BGMask)
    cv.imshow('ROIBG', ROIBG)
    cv.moveWindow('ROIBG',moveWindowX*2,moveWindowY*1)

    ROInew=cv.add(FG,ROIBG)
    cv.imshow('ROInew', ROInew)
    cv.moveWindow('ROInew',moveWindowX*3,moveWindowY*1)

    frame[posY:posY+bH,posX:posX+bW]=ROInew

    posX+=dX
    posY+=dY

    if posX<=0 or posX+bW>=dispW:
        dX=dX*(-1)
    if posY<=0 or posY+bH>=dispH:
        dY=dY*(-1)

    if(posX+bW>dispW):
        posX=dispW-bW
    if(posY+bH>dispH):
        posY=dispH-bH
    if(posX<0):
        posX=0  
    if(posY<0):
        posY=0  

    cv.moveWindow('Cam1',moveWindowX*0,moveWindowY*0)
    cv.imshow('Cam1',frame)

    print(posX,posX+bW,posY,posY+bH)


    if cv.waitKey(1)==ord('q'):
        break
    
cam.release()
cv.destroyAllWindows()