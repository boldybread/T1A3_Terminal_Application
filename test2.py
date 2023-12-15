import time, sys
from pygame import mixer

mixer.init()

sound = mixer.Sound("../T1A3_Terminal_Application/Music.wav")
sound.play()

time.sleep(5)