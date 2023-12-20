from colored import Fore, Back, Style
import fontstyle
from time import sleep
from computational_stopwatch import Stopwatch
from pygame import mixer

sw = Stopwatch() # Starts the timer which times completion time

wait_duration = 4 # This is the variable used for most of the pauses between output lines of text. This enabled me to change to 0 for testing, or 4 for the proper game

#Instantiate mixer
mixer.init()
#Load audio file
mixer.music.load('Music.mp3')
#Set preferred volume
mixer.music.set_volume(0.2)
#Play the music
mixer.music.play()

from intro import prologue
prologue()
