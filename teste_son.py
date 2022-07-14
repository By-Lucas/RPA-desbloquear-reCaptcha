import pydub
import os
import speech_recognition as sr
import speech_recognition

src = os.getcwd()+"\\audios\\sample.mp3"
test = os.getcwd()+"\\audios\\teste.wav"

# convert wav to mp3  
song  = pydub.AudioSegment.from_mp3(src)
song.export(test, format="wav")

sample_audio = sr.WavFile('audios/teste.wav')

r = sr.Recognizer()
with sr.WavFile(test) as src:
    print(dir(src))              # use "test.wav" as the audio source
    audio = r.record(src)                        # extract audio data from the file
    print('passou')
try:
    list = r.recognize(audio,True)                  # generate a list of possible transcriptions
    print("Possible transcriptions:")
    for prediction in list:
        print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")