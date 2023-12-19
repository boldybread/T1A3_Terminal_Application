from colored import Fore, Back, Style
import fontstyle
from time import sleep

def chapter_1a():
    from main import wait_duration
    player_input = ""
    player_options = ["call out", "stay quiet"]
    print(f"The voice calls out again, {Fore.red}'Malice'{Style.reset}, 'are you in here?'")
    while player_input not in player_options:
        print("'call out' | 'stay quiet'")
        player_input = input().lower()
        if player_input == "call out":
            print("Hey I recognise that voice, 'Hey in here! you yell'")
            sleep(wait_duration)
            print("The door swings open, a confident and familiar looking woman stands in the doorway")
            sleep(wait_duration)
            print("'Mal, keep your voice down or Killjoy's goons will hear!'")
            sleep(wait_duration)
            print("'I managed to get the key to your chains, but you'll have to get out of here by yourself, I can't risk Killjoy finding me helping you, you understand'")
            sleep(wait_duration)
            print("The mysterious girl tosses you a key and you hastily start unshackling your cuffs. When you look up, she is already gone.")
            sleep(wait_duration)
            print("Alright, time to make for the exit")
            from chapt_1b import chapter_1b
            chapter_1b()
        elif player_input == "stay quiet":
            print("The voice is coming closer, I think they're going to find me!")
            sleep(wait_duration)
            print("The door swings open quietly revealing a beautiful woman who you feel you have seen before")
            sleep(wait_duration)
            print("'Hey Mal, don't feel like talking to your saviour? Guess what? I got the keys!'")
            sleep(wait_duration)
            print("'You'll have to find your own way out though, if Killjoy's men figure out what I've done they'll kill us both!'")
            sleep(wait_duration)
            print("The mysterious girl tosses you a key and you hastily start unshackling your cuffs. When you look up, she is already gone.")
            sleep(wait_duration)
            print("Alright, time to make for the exit I guess")
            from chapt_1b import chapter_1b
            chapter_1b()
        elif player_input == "malice":
            print("Malice? What kind of name is that?!")
        else:
            print("I need to make a choice quickly!")