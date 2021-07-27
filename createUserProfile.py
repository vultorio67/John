import os
import pyttsx3
import speech_recognition as sr
import json
from ast import literal_eval


def getProfile():
    engine = pyttsx3.init()

    for voice in engine.getProperty('voices'):
        print('execution cup')

    engine.setProperty('voice', voice.id)

    print("execute getProfile")

    def speak(text):
        engine = pyttsx3.init()
        print(text)
        saidWord = text.split(" ")
        print(saidWord)
        engine.say(text)
        engine.runAndWait()

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                saidWord = said.split(" ")
                print(said)
            except Exception as e:
                print("Exception: " + str(e))

        return said.lower()

    # get the name
    speak("hello i am john, my goal is to help you and learn whith you and your friends")
    speak("I'm going to start bye asking some question.")
    speak("what is your name")
    statement = takeCommand().lower()
    statement = statement.replace("my name is", "")
    statement = statement.replace("i am", "")
    statement = statement.replace("name", "")
    statement = statement.replace(" ", "")
    print(statement)
    name = statement
    speak("is it the good name" + name)
    statement = takeCommand().lower()
    if statement == "yes":
        speak("ok.")
    else:
        name = input("enter your name : ")
    os.rename(r'faces/opencv0.png', r'faces/' + name + '.png')
    jsonLocation = 'userData/' + name + '.json'
    print("execution exit")
    file = open("userData/" + name + ".json", "w+")
    speak("nice to meet you " + name)

    # get the age
    speak("How old are you?")

    statement = takeCommand().lower()
    statement = statement.replace("i am", "")
    statement = statement.replace("i'm", "")
    statement = statement.replace("years old", "")
    age = statement

    speak("how me, I have 1 years.")

    # get the country
    speak("where are you from?")

    statement = takeCommand().lower()

    statement = statement.replace("i came from", "")
    contry = statement

    if "france" in contry:
        speak("How me I was design in france!")
    if "US" in contry:
        speak("I like burger!")
    else:
        speak("cool I like this country but I never went.")

    print(jsonLocation)

    # get the job
    speak("So are you working, or in school.")
    statement = takeCommand().lower()
    statement = statement.replace("me", "")
    statement = statement.replace("i", "")
    statement = statement.replace("am", "")
    statement = statement.replace("do", "")
    statement = statement.replace("in", "")
    statement = statement.replace("   ", "")
    statement = statement.replace("  n ", "")

    job = statement

    # writing the user data in a json file
    with open(jsonLocation, 'w') as file:
        json.dump(str({"name": name, "age": age, "country": contry, "job": job}), file)

# fonction to read json user data
def readInfoUser(what, self):
    with open("userData/" + self.name + ".json", 'r') as file:
        uInfo = json.load(file)
        uInfo = literal_eval(uInfo)
        uInfo = uInfo[what]
        return uInfo