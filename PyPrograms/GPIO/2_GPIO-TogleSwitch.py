import RPi.GPIO as GPIO

#Povemo da naj uporabi osnovno razporeditev pinov
GPIO.setmode(GPIO.BOARD)

#Spremenljivke
inPin=15
outPin=23
lightState=0        #Nastavimo luč na ugasnjeno
buttonStateOld=1    #Osnovna vrednost tipke 0=pritisnjen; 1=spuščen


#Povemo kateri pin je izhod/vhod
GPIO.setup(outPin,GPIO.OUT)
GPIO.setup(inPin,GPIO.IN)

while True:
    
    buttonStateNew=GPIO.input(inPin)
    
    #Spremenimo vrednost na izhodu
    if buttonStateOld==1 and buttonStateNew==0:
        lightState=not(lightState)
           
    GPIO.output(outPin,lightState)
    x=GPIO.input(inPin)
    print ('x= ',x)

    buttonStateOld=buttonStateNew


#Počistimo vse izhode vhode na vezju
GPIO.cleanup()