# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:35:56 2021

@author: Nitro 7
"""

import speech_recognition as sr
import pyttsx3
from scripts import * 
import datetime
import wikipedia
import webbrowser
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
    cmd =  cmd.lower()
    if cmd=='':
        speak("sorry I didn't get it please repeat")
    else:
        if 'send a mail' in cmd or 'send email' in cmd or 'mail' in cmd or 'email' in cmd:
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
        elif 'wikipedia' in cmd:
            speak('Searching Wikipedia...')
            cmd = cmd.replace('wikipedia',"")
            result = wikipedia.summary(cmd,sentences=1)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'youtube' in cmd:
            speak('opening youtube')
            webbrowser.open('youtube.com')    
        elif 'google' in cmd:
            speak('opening google')
            webbrowser.open('google.com')    
        elif 'time' in cmd:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f'Time is {strTime}')
        elif 'stop' in cmd or 'exit' in cmd:
            speak('Good Bye sir')
            break