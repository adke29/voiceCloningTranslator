from gtts import gTTS
import os
def tts(text, language, filename):
    tts=gTTS(text=text, lang=language)
    tts.save('%s.mp3' % os.path.join("./voices/",filename))