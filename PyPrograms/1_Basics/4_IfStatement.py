number=float(input("Please Input Your Number: "))                               #input float

if(number>0):
    print("Your number is Positive")
    print("Thank you for playing")

elif (number<0):
    print("Your number is Negative")
    print("Thank you for playing")

elif (number==0):
    print("Your number is zero")
    print("Thank you for playing")

if(number>0 and number%2==0):                                                   # %2 pomeni ostanek pri deljenju z 2
    print("Your number is Positive")
    print("Your number is Even")

elif(number<0 and number%2==0):                                                   # %2 pomeni ostanek pri deljenju z 2
    print("Your number is Negative")
    print("Your number is Even")

elif(number>0 and number%2!=0):                                                   # %2 pomeni ostanek pri deljenju z 2
    print("Your number is Positive")
    print("Your number is Odd")

elif(number<0 and number%2!=0):                                                   # %2 pomeni ostanek pri deljenju z 2
    print("Your number is Negative")
    print("Your number is Odd")
else:
    print("Your number is zero")
