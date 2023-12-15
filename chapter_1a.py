from colored import Fore, Back, Style
import fontstyle
from time import sleep

def chapter_1a():
    user_input = ""
    options = ["call out", "stay quiet"]
    print(f"Suddenly a voice calls out, {Fore.red}'Malice'{Style.reset}, 'are you in here?'")
    while user_input not in options:
        print("'call out' | 'stay quiet'")
        user_input = input().lower()
        if user_input == "call out":
            print("Hey I recognise that voice, 'Hey in here! you yell'")
            sleep(4)
            print("The door swings open, a confident and familiar looking woman stands in the doorway")
            sleep(4)
            print("'Mal, keep your voice down or Killjoy's goons will hear!'")
            sleep(4)
            print("'I managed to get the key to your chains, but you'll have to get out of here by yourself, I can't risk Killjoy finding me helping you, you understand'")
            sleep(4)
            print("The mysterious girl tosses you a key and you hastily start unshackling your cuffs. When you look up, she is already gone.")
            sleep(4)
            print("Alright, time to make for the exit")
            from chapter_1b import chapter_1b
            chapter_1b()
        elif user_input == "stay quiet":
            print("The voice is coming closer, I think they're going to find me!")
            sleep(4)
            print("The door swings open quietly revealing a beautiful woman who you feel you have seen before")
            sleep(4)
            print("'Hey Mal, don't feel like talking to your saviour? Guess what? I got the keys!'")
            sleep(4)
            print("'You'll have to find your own way out though, if Killjoy's men figure out what I've done they'll kill us both!'")
            sleep(4)
            print("The mysterious girl tosses you a key and you hastily start unshackling your cuffs. When you look up, she is already gone.")
            sleep(4)
            print("Alright, time to make for the exit I guess")
            from chapter_1b import chapter_1b
            chapter_1b()
        elif user_input == "malice":
            print("Malice? What kind of name is that?!")
        else:
            print("I need to make a choice quickly!")