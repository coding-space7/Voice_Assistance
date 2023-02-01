import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_Me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir")
    speak("How may I help you")


def take_Command():
    """ It takes input from the user and returns string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query} \\n')

    except Exception as es:
        print("Say that again please...")
        return "None"
    return query


def send_Email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
     wish_Me()
#     take_Command()
     while True:
         query = take_Command().lower()

         # Logic for executing tasks based on query
         if 'wikipedia' in query:
             speak('Searching Wikipedia...')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak("According to Wikipedia")
             print(results)
             speak(results)

         elif 'open youtube' in query:
             webbrowser.open("youtube.com")

         elif 'open google' in query:
             webbrowser.open("google.com")

         elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")


         elif 'play music' in query:
             music_dir = 'location of your music directory in your computer'
             songs = os.listdir(music_dir)
             rand = random.randint(0,len(songs)-1)
             print(songs)
             os.startfile(os.path.join(music_dir, songs[rand]))

         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f'Sir, the time is {strTime}')

         elif 'open code' in query:
             codePath = "location of your code file"
             os.startfile(codePath)

         elif 'email to bharat' in query:
             try:
                 speak("What should I say?")
                 content = take_Command()
                 to = "sawbharat2001@gmail.com"
                 send_Email(to, content)
                 speak("Email has been sent!")
             except Exception as e:
                 print(e)
                 speak("Sorry my friend  i was not able to send email")