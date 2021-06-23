
import jetson.inference
import jetson.utils
import time

#različni neti za prepoznavanje slik
net=jetson.inference.detectNet('ssd-mobilenet-v2',threshold=.5)


dispW=1280
dispH=720
flip=0

#web cam
cam=jetson.utils.gstCamera(dispW,dispH,'/dev/video1')        #poglej parametre v4l2-ctl -d /dev/video1 --list-formats-ext 

#pi cam
#cam=jetson.utils.gstCamera(dispW,dispH,'0')

display=jetson.utils.glDisplay()

timeMark=time.time()
fpsFilter=0

while display.IsOpen():
    img, width, height =cam.CaptureRGBA()

    #zaznamo objekt
    detections=net.Detect(img,width,height)

    #zapišemo sliko
    display.RenderOnce(img,width,height)
    
    #izračunamo fps
    dt=time.time()-timeMark
    fps=1/dt
    fpsFilter=.95*fpsFilter+.05*fps
    timeMark=time.time()

    print(str(round(fps))+'fps')

