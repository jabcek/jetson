import RPi.GPIO as GPIO

#Povemo da naj uporabi osnovno razporeditev pinov
GPIO.setmode(GPIO.BOARD)

#Spremenljivke
outPin=32

#Povemo kateri pin je izhod/vhod
GPIO.setup(outPin,GPIO.OUT)

#PWM objekt
myPWM=GPIO.PWM(outPin,100)

myPWM.start(1)

while True:

    myPWM.ChangeDutyCycle(10)