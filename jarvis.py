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
starting()
while 1:
    with sr.Microphone() as source:
        try:
            print("Speak")
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            print("Did you say: "+text)
            speak(text)
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occured")    