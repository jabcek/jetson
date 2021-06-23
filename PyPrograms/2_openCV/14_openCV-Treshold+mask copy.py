import cv2 as cv
import sys
print(sys.version)
print(cv.__version__)

dispW=320
dispH=240
flip=0
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc sensor_mode=0 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv.VideoCapture(0)

windowWidth=390
windowHeight=360
def nothing(x):
    pass

cv.namedWindow('Blended')
cv.createTrackbar('BlendVal','Blended',50,100,nothing)

while True:
    ret, frame = cam.read()

    cvLogo=cv.imread('Bacteria.jpg')
    cvLogo=cv.resize(cvLogo,(320,240))
    cvLogoGray=cv.cvtColor(cvLogo,cv.COLOR_BGR2GRAY)
    cv.imshow('cv Logo Gray',cvLogoGray)
    cv.moveWindow('cv Logo Gray',windowWidth*1,windowHeight*0)

    _,BGMask=cv.threshold(cvLogoGray,225,255,cv.THRESH_BINARY)
    cv.imshow('BGMask', BGMask)
    cv.moveWindow('BGMask',windowWidth*2,windowHeight*0)

    FGMask=cv.bitwise_not(BGMask)
    cv.imshow('FGMask', FGMask)
    cv.moveWindow('FGMask',windowWidth*3,windowHeight*0)

    FG=cv.bitwise_and(cvLogo,cvLogo,mask=FGMask)
    cv.imshow('FG', FG)
    cv.moveWindow('FG',windowWidth*0,windowHeight*1)

    BG=cv.bitwise_and(frame,frame,mask=BGMask)
    cv.imshow('BG',BG)
    cv.moveWindow('BG',windowWidth*1,windowHeight*1)

    compImage=cv.add(BG,FG)
    cv.moveWindow('compImage',windowWidth*2,windowHeight*1)
    cv.imshow('compImage',compImage)

    #trackBarq
    BV1=cv.getTrackbarPos('BlendVal','Blended')/100
    print(BV1)
    BV2=1-BV1

    Blended=cv.addWeighted(frame,BV1,cvLogo,BV2,0)
    cv.moveWindow('Blended',windowWidth*3,windowHeight*1)
    cv.imshow('Blended',Blended)

    FG2=cv.bitwise_and(Blended,Blended,mask=FGMask)
    cv.moveWindow('FG2',windowWidth*0,windowHeight*2)
    cv.imshow('FG2',FG2)

    compFinal=cv.add(BG,FG2)
    cv.moveWindow('compFinal',windowWidth*1,windowHeight*2)
    cv.imshow('compFinal',compFinal)
 
    cv.moveWindow('Cam1',windowWidth*0,windowHeight*0)
    cv.imshow('Cam1',frame)




    if cv.waitKey(1)==ord('q'):
        break
    
cam.release()
cv.destroyAllWindows()