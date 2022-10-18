#pip install googletrans==3.1.0a0
from googletrans import Translator
def translate(text,language):
    translator = Translator()
    translation = translator.translate(text, dest=language)
    return translation.text