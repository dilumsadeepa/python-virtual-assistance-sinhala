from googletrans import Translator

def tra(data):
    # init the Google API translator
    translator = Translator()

    # translate a spanish text to english text (by default)
    translation = translator.translate(data)
    result = translation.text

    print(result)

    return data