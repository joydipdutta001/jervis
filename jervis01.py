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

def operations():
    list_1 = ["YouTube","Google","Music","Manage Folders"]
    for i in range(len(list_1)):
        speak(list_1[i]+'?')

if __name__ == '__main__':

    greetMe()
    speak('what do you want to do ?')
    operations()
    speak('How may I help you?')

    while True:

        query = myCommand()

        if 'YouTube' in query:

            answer1 = myCommand()

            webbrowser.open('https://www.youtube.com/results?search_query=' + answer1)
            speak('Here is some results about' + answer1)

        elif 'Google' in query:
            speak('okay what do you want to search?')
            answer1 = myCommand()

            webbrowser.open('https://www.google.com/search?q='+answer1)
            speak('Here is some results about'+answer1)

        elif 'music' in query:
            music_folder ='E:/Main Projects/Python/jervis/music/'
            music1 = 'music1'
            music2 = 'music2'
            music3 = 'music3'
            music4 = 'music4'
            music5 = 'music5'
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            speak('Okay, here is your music! Enjoy!')
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=4)
                    speak('Got it.')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')
