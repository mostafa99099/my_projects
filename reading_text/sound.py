from gtts import gTTS
import playsound
import os


i = 1
while i > 0:
    x = input("...")
    tts = gTTS(text=x, lang="en")
    file1 = str("sound" + str(i) + ".mp3")
    tts.save(file1)
    playsound.playsound(file1, True)
    if x == "stop":
        os.remove(file1)
        break
    os.remove(file1)
    i += 1
        







