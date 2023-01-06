import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import datetime

listener = sr.Recognizer()
tts = pyttsx3.init()

def speak(text):
    tts.say(text)
    tts.runAndWait()

def get_command():
    print('Listening for a command')
    with sr.Microphone() as source:
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'hello' in command:
            command = command.replace('hello', '')
        elif 'bye' in command: 
            command = "stop listening"
    except:
        pass
    return command

def run_bot():
    command = get_command()
    print(command)
    if 'lookup' in command:
        command = command.replace('lookup','')
        webbrowser.open('https://www.google.com/search?q=' + command)
        speak('Looking up' + command)
    # play vid on YT
    elif 'play' in command:
        song = command.replace('play','')
        speak('Playing' + song)
        pywhatkit.playonyt(song)
    # gives the time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('The current time is ' + time)
    # gives the date
    elif 'date' in command:
        date = datetime.date.today().__str__()
        speak('The date today is ' + date)
    elif 'stop listening' in command:
        exit()
    else:
        speak('Please say the command again.')

while True:
    run_bot()