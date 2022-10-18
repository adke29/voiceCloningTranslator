# NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr

r = sr.Recognizer()
def stt(lang):
    with sr.Microphone() as source:
        print("speak now: ")
        audio = r.listen(source)
        result = r.recognize_google(audio, language=lang)
    with open("./voices/original.wav", "wb") as file:
        file.write(audio.get_wav_data())    
    return result

