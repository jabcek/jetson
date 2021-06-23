import os
import pyttsx3

engine=pyttsx3.init()
engine.setProperty('rate',150)
#English= angl. jezik; m2=moški glas 2 (m1-m4) (f1-f4)
engine.setProperty('voice','english+m2')

text='get ready player 1. The play will be rough. Are you ready to rumble!'

engine.say(text)
engine.runAndWait()

