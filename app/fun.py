import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import wolframalpha
from googletrans import Translator

translator = Translator()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

app_id = '4L5L58-WVPHPQP9G8'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
    return text


def take_command():
    try:
        with sr.Microphone() as source:
            command = ''
            print('listening...')
            voice = listener.listen(source)
            print('get voice...')
            command = listener.recognize_google(voice, language="si-LK")
            command = command.lower()
            if 'sera' in command:
                command = command.replace('sera', '')
                print(command)
    except:
        pass
    return command


def main():
    command = take_command()
    translation = translator.translate(command)
    command = translation.text
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'information' in command:
        command = command.replace('information about','')
        command = wikipedia.summary(command, sentences=3)

        talk(command)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        try:
            res = client.query(command)
            command = next(res.results).text
            #result = translator.translate(text, dest='sinhala')
            #text = result.text
            talk(command)
        except:
            talk('Please say the command again.')



