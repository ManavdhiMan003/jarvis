import datetime
import pyttsx3
import speech_recognition as sr

user_name = ""
def speak(data):
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()

def starting():
    hr = int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("Good morning sir!")
    elif hr>=12 and hr<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("I am your assitant Jarvis")  

def ask_name():
    speak("What should i call you sir")
    while 1:
        name = get_command()
        if name!='':
            arg = 'hello '+name
            global user_name    
            user_name = name
            speak(arg)
            break
        else: 
            speak("Sorry I didn't get it, Please try again")

def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Speak...")
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            print("Did you say: "+text)
            return text
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ''
            
        except sr.UnknownValueError:
            print("unknown error occured")    
            return ''

