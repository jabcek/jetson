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
while True:
    ret, frame = cam.read()

    frame=cv.rectangle(frame,(340,100),(400,170),(0,255,0),7)       #Narišemo kvadrat (slika,(levi zgornji kot x,y), (spodnji desni kot x,y),(barva blue,gree,red),debelina črte)
    
    frame=cv.circle(frame,(320,240),50,(0,0,255),5)                 #Narišemo krog (slika,(koordinate center x,y), radij, (barva),debelina črte)

    frame=cv.circle(frame,(500,240),50,(0,0,255),-1)                #narišemo krog debelina črte=-1, polni krog
    
    fnt=cv.FONT_HERSHEY_DUPLEX
    frame=cv.putText(frame,'MyText',(300,300),fnt,2.0,(255,0,150),2)  #Napišemo tekst, (slika, (koordinate levi zgornji kot x,y),font,povečava teksta, (barva), debelina)

    fame=cv.line(frame,(10,10),(630,470),(0,0,0),4)                 #Narišemo črto (slika, levi zgornji kot x,y), (desni spodnji kot x,y), (barva), debelina)

    frame=cv.arrowedLine(frame,(10,470),(630,10),(255,255,255),1)

    cv.imshow('Cam1',frame)
    cv.moveWindow('Cam1',0,0)




    if cv.waitKey(1)==ord('q'):
        break
cam.release()
cv.destroyAllWindows()