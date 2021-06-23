
import jetson.inference
import jetson.utils
  
net=jetson.inference.imageNet('googlenet') 
#WebCam '/dev/video1'
#PiCam '0'

dispW=640
dispH=480

cam=jetson.utils.gstCamera(dispW,dispH,'/dev/video1')        #poglej parametre v4l2-ctl -d /dev/video1 --list-formats-ext 
display=jetson.utils.glDisplay()
font=jetson.utils.cudaFont()

while display.IsOpen():
    frame, width, height =cam.CaptureRGBA()
    
    classID, cinfident=net.Classify(frame,width,height)
    item=net.GetClassDesc(classID)

    #Napišemo tekst
    #slika, širina, višina, teks (nazaj dobimo v item), zamik po x, zamik po y, barva črk, barva ozadja 
    font.OverlayText(frame,width,height,item,5,5,font.Magenta,font.Blue)

    display.RenderOnce(frame,width,height)