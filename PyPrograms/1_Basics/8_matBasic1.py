import matplotlib.pyplot as plt
import numpy as np
import cv2

''' Multiline comment
x=[1,2,3,4]
y=[3,5,7,9]
z=[10,8,6,4]

plt.grid(True)
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.title("My first graph")
plt.axis([0,5,2,11])                                                        #merilo [xMin,xMax,yMin,yMax]
plt.plot(x,y,'b-*',linewidth=3,markersize=10,label="Blue")                  #b... modra barva (r,g,y); - (polna črta) -.(črta pika) :(pikice); * točke (lahko tudi x,o,^)
plt.plot(x,z,'r-.o',linewidth=3,markersize=10,label="Red")
plt.legend(loc="lower left")                                                #upper left, center, right; lower left,center,right  -položaj legende
plt.show()

'''

#x=np.arange(-4,4,.1)
#x=np.linspace(-4,4,25)
#y=np.square(x)
#y2=np.square(x)+2
#y3=np.square(x)+4

x=np.linspace(0,2*np.pi,50)
y=np.sin(x)
y2=np.cos(x)

plt.grid(True)
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.title("My first graph")
#plt.axis([0,5,2,11])                                                        #merilo [xMin,xMax,yMin,yMax]
#plt.plot(x,y,'b-*',linewidth=3,markersize=8,label="Blue")                  #b... modra barva (r,g,y); - (polna črta) -.(črta pika) :(pikice); * točke (lahko tudi x,o,^)
#plt.plot(x,y2,'r-o',linewidth=3,markersize=5,label="Red")                  #b... modra barva (r,g,y); - (polna črta) -.(črta pika) :(pikice); * točke (lahko tudi x,o,^)
#plt.plot(x,y3,'g-^',linewidth=3,markersize=5,label="Green")                  #b... modra barva (r,g,y); - (polna črta) -.(črta pika) :(pikice); * točke (lahko tudi x,o,^)
plt.plot(x,y,'b-*',linewidth=3,markersize=8,label="Sin (x)") 
plt.plot(x,y2,'r-o',linewidth=3,markersize=5,label="Cos (x)") 

plt.legend(loc="upper center")                                                #upper left, center, right; lower left,center,right  -položaj legende
plt.show()