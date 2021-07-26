import wave
import gtts
import pyttsx3
import speech_recognition as sr

import createUserProfile
import getFaceName

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
text = get_audio()

def speakingModule():

    if "hello" in text:
        speak("hello, i know you"+userName)
    elif "what is your name" in text:
        speak("My name is Tim")
