from gtts import gTTS
import os
def tts(text, language):
    tts=gTTS(text=text, lang=language)
    tts.save('%s.mp3' % os.path.join("./voices/result"))