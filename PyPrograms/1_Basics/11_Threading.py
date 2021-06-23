from threading import Thread
import time

def BigBox(color,l):
    while True:
        print(color,' Box is Open with legth of', l)
        time.sleep(5)
        print(color,' Box is Closed with legth of', l)
        time.sleep(5)

def SmallBox(color,l):
    while True:
        print(color,' Box is Open',l)
        time.sleep(1)
        print(color,' Box is Closed',l)
        time.sleep(1)

BigBoxThread=Thread(target=BigBox,args=('red',5))
x=3
SmallBoxThread=Thread(target=SmallBox,args=('blue',x))

BigBoxThread.daemon=True

SmallBoxThread.daemon=True


BigBoxThread.start()
SmallBoxThread.start()

while True:
    pass
