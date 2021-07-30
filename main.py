import wave
import gtts
import pyttsx3
import speech_recognition as sr
import json
from ast import literal_eval
import random

import createUserProfile
import getFaceName
import ReadWordDataBase as rwdb

#this is the main file

test = "test"

test = str(rwdb.getWord1('byeWord', 3, True))


#rint(createUserProfile.readLanguage("helloWord", self=test))

engine = pyttsx3.init()

for voice in engine.getProperty('voices'):
    print(voice)

engine.setProperty('voice', voice.id)


print("activation de la reconaissance faciale.")
userName = getFaceName.getName()
print("detection of "+userName)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=1)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                return said.lower()
            except Exception as e:
                print("Exception: " + str(e))
        except :
            print("You don't have speak or I don't hear")

def getAudioMaybe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=1)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                return said.lower()
            except Exception as e:
                print("Exception: " + str(e))
        except :
            print("You don't have speak or I don't hear")




if userName == "opencv0":
    print("Your profile is not know bye the system so I start getFaceName")
    createUserProfile.getProfile()

def speakingModule():

    speak("hello")
    print(rwdb.startSentences(rwdb.getNumber('wordDataBase.json')))


    while True:
        text = get_audio()

        if "hello" in text or "good morning" in text:
            speak(str(rwdb.getWord1('helloWord', 4, True))+userName+"How can I help you")
        if "bye" in text or "see you" in text:
            speak(str(rwdb.getWord1('byeWord', 3, True))+userName)
            break

speakingModule()