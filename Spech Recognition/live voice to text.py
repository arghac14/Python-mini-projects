import speech_recognition as sr
import pyaudio
import time
r=sr.Recognizer()
#audio = ("1.wav")
#r=energy_threshold=500
with sr.Microphone() as source:
   print("Say Something..",end='')
   time.sleep(.3)
   print(".",end='')
   time.sleep(0.01)
   print(".")
   audio=r.listen(source)
   r.adjust_for_ambient_noise(source, duration=4)
   #r.adjust_ambient_noise(audio)
   text=r.recognize_google(audio)
   
try:
    print(text)
except sr.RequestError:
    print("API not available.")
except sr.UnknownValuerror :
    print("Could not recognize!")
