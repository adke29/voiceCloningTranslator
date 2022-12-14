from translator import translate
from textToSpeech import tts
from speechToText import stt
import os

if __name__ == '__main__':
    #english to mandarin
    cacheDir = './voicescache/' 
    if not os.path.exists(cacheDir):
        os.makedirs(cacheDir)
    language_origin = "en-US"
    language_destination="zh-tw"
    text = stt(language_origin) #get text from user speech via microphone with english language
    translatedText=translate(text,language_destination) #translate user speech to chinese
    tts(translatedText,'zh-TW') #text to speech translated text
