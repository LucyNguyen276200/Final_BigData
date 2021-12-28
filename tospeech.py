from gtts import gTTS
import playsound
import os,time


tts = gTTS('hello')
tenfile='audio.mp3'
tts.save(tenfile)
playsound.playsound(tenfile)

