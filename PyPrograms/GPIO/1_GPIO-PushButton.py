import RPi.GPIO as GPIO

#Povemo da naj uporabi osnovno razporeditev pinov
GPIO.setmode(GPIO.BOARD)

#Spremenljivke za št. pinov
inPin=15
outPin=23

#Povemo kateri pin je izhod/vhod
GPIO.setup(outPin,GPIO.OUT)
GPIO.setup(inPin,GPIO.IN)

while True:
    #preberemo vrednost na vhodu
    x=GPIO.input(inPin)
    print ('x= ',x)
    
    #Spremenimo vrednost na izhodu
    if x==1:
        GPIO.output(outPin,0)
    else:
        GPIO.output(outPin,1)


#Počistimo vse izhode vhode na vezju
GPIO.cleanup()