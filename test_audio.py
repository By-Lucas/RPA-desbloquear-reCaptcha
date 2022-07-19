import pydub
import os
import speech_recognition as sr
import speech_recognition

src = os.getcwd()+"\\audios\\sample.mp3"
test = os.getcwd()+"\\audios\\sample.wav"

# convert wav to mp3  
song  = pydub.AudioSegment.from_mp3(src)
song.export(test, format="wav")

# Creating a recognition object
r = sr.Recognizer()

# Extracting the audio & removing ambient noice
audio_file = sr.WavFile(test)
with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    print('passou')

# Recognize the audio
tradu = r.recognize_google(audio)
print("[INFO] Audio traduzido: %s" %tradu)
