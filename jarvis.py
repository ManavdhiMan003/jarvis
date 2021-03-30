# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:35:56 2021

@author: Nitro 7
"""

import speech_recognition as sr
import pyttsx3
from scripts import * 
r = sr.Recognizer()


def speak(data):
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()
# starting()
# ask_name()
# speak('How can i help you')
while 1:
    cmd = get_command() 
    if cmd=='':
        speak("sorry I didn't get it please repeat")
    else:
        if 'send a mail' in cmd or 'send email' in cmd:
            try:
                speak("what is the message sir?")
                message = get_command()
                speak("whome should i send")
                to = input()
                send_email(to,message)
                speak("Email send successfully")
            except Exception as e:
                print(e)
                speak("sorry sir i am unable to send email")
        elif 'stop' in cmd or 'exit' in cmd:
            speak('Good Bye sir')
            break