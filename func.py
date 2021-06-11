import speech_recognition as sr
import pyaudio
import playsound
from gtts import gTTS
import os

r = sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang="pt-br")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def ouvir():
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except:
            speak("Desculpe, não entendi")
    return said.lower()




