# NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr

r = sr.Recognizer()
def stt(lang):
    with sr.Microphone() as source:
        print("speak now: ")
        audio = r.listen(source)
        result = r.recognize_google(audio, language=lang)
        return result

