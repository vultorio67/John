import wave
import gtts
import pyttsx3
import speech_recognition as sr
import json
from ast import literal_eval

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
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()


if userName == "opencv0":
    print("Your profile is not know bye the system so I start getFaceName")
    createUserProfile.getProfile()

def speakingModule():
    speak("I am on your disposition")
    while True:
        text = get_audio()

        if "hello" in text:
            speak(str(rwdb.getWord1('helloWord', 4, True))+userName+"How can I help you")
        if "bye" in text:
            speak(str(rwdb.getWord1('byeWord', 3, True))+userName)
            break

speakingModule()