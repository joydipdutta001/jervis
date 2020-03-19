import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import time


engine = pyttsx3.init()
client = wolframalpha.Client('R9H998-R88PKEQYE9')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)


def speak(audio):
    print('Jervis: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')




def myCommand():
    query = ''

    r = sr.Recognizer()
    print("Listening...")
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print('You: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    return query


if __name__ == '__main__':

    greetMe()

    speak('How may I help you?')

    while True:

        query = myCommand()

        if 'ok' in query:
            speak('Hello joy')