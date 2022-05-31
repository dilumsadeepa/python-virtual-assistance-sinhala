import eel
import wikipedia

import wolframalpha
import pywhatkit
import datetime
from googletrans import Translator
import webbrowser


eel.init('web')

translator = Translator()



app_id = '4L5L58-WVPHPQP9G8'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)

def speek(text):
    result = translator.translate(text, dest='sinhala')
    text = result.text
    return text

@eel.expose
def main(data):
    print(data)
    translation = translator.translate(data)
    data = translation.text
    data = data.lower()

    if 'information' in data:
        data = data.replace('information about','')
        text = wikipedia.summary(data, sentences=3)

        speek(text)
        return text
    elif 'play' in data:
        data = data.replace('play', '')
        pywhatkit.playonyt(data)
    elif 'search' in data:
        data = data.replace('search', '')
        pywhatkit.search(data)
    elif 'go' in data:
        data = data.replace('go', '')
        pywhatkit.search(data)
    elif 'date'in data:
        now = datetime.now()
        text = now.strftime("%m/%d/%Y, %H:%M:%S")
        speek(text)
        return text
    elif 'good morning' in data:
        now = datetime.now()
        nd = now.strftime("%m/%d/%Y, %H:%M:%S")
        webbrowser.open("https://calendar.google.com/calendar/u/0/r", new=1)
    elif 'set remainder' in data:
        webbrowser.open("https://calendar.google.com/calendar/u/0/r", new=1)
    elif 'who are you' in data:
        text = 'I am Sera, virtual assistant. develop by kodeuwa in 2021. I can listen you in sinhala,English or' \
               ' broken English. but i speak in English only. Now a days i have been developed in kodeuwa. As soon as posible' \
               ' my update will come with many features. Thank you'
        return text
    else:
        try:
            res = client.query(data)
            text = next(res.results).text
            result = translator.translate(text, dest='sinhala')
            text = result.text

            return text
        except:
            pywhatkit.search(data)
            text = data
            return text




def wiki(data):
    text = wikipedia.summary(data, sentences=3)

    speek(text)
    return text

def all(data):

    res = client.query(data)
    text = next(res.results).text

    return text
def gm():
    now = datetime.now()
    nd = now.strftime("%m/%d/%Y, %H:%M:%S")
    webbrowser.open("https://calendar.google.com/calendar/u/0/r", new=1)





eel.start('main.html',port=8080)