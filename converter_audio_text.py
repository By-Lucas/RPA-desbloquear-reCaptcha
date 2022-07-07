import wave
import json
from vosk import Model, KaldiRecognizer, SetLogLevel 
SetLogLevel(-1)

modelo = Model("model")

def fala_para_texto(arquivo):
  
    with wave.open(arquivo, "rb") as arq:
        rec = KaldiRecognizer(modelo, arq.getframerate())            
        while True:
            data = arq.readframes(4000)
            rec.AcceptWaveform(data)
            if len(data) == 0:
                break
                        
    resultado = json.loads(rec.FinalResult())
    return resultado["text"]    

if __name__ == "__main__":
    print(fala_para_texto("test.wav")) 