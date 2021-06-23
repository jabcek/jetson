import numpy as np                                                                  #as np pomeni da smo preimenovali knjižnico ki jo uporabljamo

for i in range (1,11,1):
    print(i)

print("Thats all folks 1")

for i in np.arange (-.5,.6,.1):
    print(i)

print("Thats all folks 2")

for i in np.linspace(1,10,25):                                                      #Začetna št. končna številka, število korakov
    print(i)

print("Thats all folks 3")