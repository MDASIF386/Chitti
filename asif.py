import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():

    hou = int(datetime.datetime.now().hour)

    if hou >= 0 and hou < 12:
        speak("Good Morning!")

    elif hou >= 12 and hou < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Asif... pari brother,Sir  Please tell me how can I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query

    # def sendEmail(to, content):
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo()
    # server.starttls()
    # server.login('youremail@gmail.com', 'your-password')
    # server.sendmail('youremail@gmail.com', to, content)
    # server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak('I am great .What about u')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ANPL\\Desktop"
            os.startfile(codePath)
        elif 'quit' in query:
            exit()
        # elif 'email to asif' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "asifdanish7654@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend asif bhai. I am not able to send this email")
