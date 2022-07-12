import pydub
import os

src = os.getcwd()+"\\audios\\sample.mp3"
test = os.getcwd()+"\\audios\\teste.wav"

# convert wav to mp3  
song  = pydub.AudioSegment.from_mp3(src)
song.export(test, format="wav")