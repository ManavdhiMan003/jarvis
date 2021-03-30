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
import pyjokes

r = sr.Recognizer()


def speak(data):
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()
starting()
ask_name()
speak('How can i help you')
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
        elif 'how are you' in cmd:
            speak('I am fine sir,Thank you')
            speak('how are you sir')
        elif 'fine' in cmd or 'good' in cmd:
            speak("Its good to know that your fine")    
        elif 'time' in cmd:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f'Time is {strTime}')
        elif 'joke' in cmd:
            speak('Searching for a joke')
            speak('i get it')
            speak(pyjokes.get_joke())
            speak('hahahahahahah')
        elif 'search' in cmd or 'play' in cmd:
            cmd = cmd.replace('search','')
            cmd = cmd.replace('play','')
            webbrowser.open(cmd)
        elif 'who created you' in cmd or 'who made you' in cmd:
            speak('I have been created by legend Manav Dhiman')
        elif 'who is manav dhiman' in cmd or 'manav' in cmd or 'dhiman' in cmd:
            speak('he is a legend and most handsome man on this planet')
        elif 'stop' in cmd or 'exit' in cmd:
            speak('Good Bye sir')
            break