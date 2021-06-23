from adafruit_servokit import ServoKit
import time
myKit=ServoKit(channels=16)
panServo=0
tiltServo=1

panServo90=90
panServo0=panServo90-90
panServo180=panServo90+90
tiltServo90=90
tiltServo0=tiltServo90-90
tiltServo180=tiltServo90+90

myKit.servo[panServo].angle=panServo90
myKit.servo[tiltServo].angle=tiltServo90

while True:
    for i in range (0,180,1):
        myKit.servo[panServo].angle=i
        myKit.servo[tiltServo].angle=i
        time.sleep(.005)
    
    for i in range (180,0,-11):
        myKit.servo[panServo].angle=i
        myKit.servo[tiltServo].angle=i
        time.sleep(.005)


