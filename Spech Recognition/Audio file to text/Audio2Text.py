import speech_recognition as sr
import pyaudio
import time
r=sr.Recognizer()
audio = ("1.wav")
#r=energy_threshold=500
with sr.AudioFile(audio) as source:
   print("Recognizing..",end='')
   time.sleep(.3)
   print(".",end='')
   time.sleep(0.01)
   print(".")
   audio=r.record(source)
   r.adjust_for_ambient_noise(source, duration=5)
   text=r.recognize_google(audio)
   
try:
    print(text)
except sr.RequestError:
    print("API not available.")
except sr.UnknownValuerror :
    print("Could not recognize!")
