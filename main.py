from colored import Fore, Back, Style
import fontstyle
from time import sleep
import time, sys
from pygame import mixer



def story_intro():
    print(f"{Fore.black}{Back.white}Welcome to Malice in Chains a text based adventure. You control the journey by your choices. Look out for any red text as this is an optional {Fore.red}'action'{Fore.black} that can be chosen by typing in that input. Sometimes you won't be prompted to input that action so keep an eye out for red text. Remember that choices can have consequences. Good luck!{Style.reset}\n")
    # sleep(10)
    user_input = ""
    options = ["open"]
    while user_input not in options:
        print(f"{Fore.red}open{Style.reset} your eyes")
        user_input = input().lower()
        if user_input == "action":
            print("Well done! Here is your Easter Egg '@'\n")
            sleep(2)
        elif user_input == "@":
            print("Very funny! Please can you start the game already?!\n")
            sleep(2)
        elif user_input == "open":
            print("You wake feeling dizzy with an aching in your head\n")
            # sleep(4) 
            print("The last thing you remember is coming for Killjoy\n")
            # sleep(4) 
            print("Thats right, Killjoy, the one who... wait who is Killjoy, and why was I after him?\n")
            # sleep(4) 
            print("You tracked him down to a warehouse, you think...\n")
            # sleep(4) 
            print("Thats the last thing you remember, something went wrong, why can't I remember?\n")
            # sleep(4) 
            print("My name. Whats my name?\n")
            # sleep(4) 
            print("Nothing, OK where am I? A dimly lit room...\n")
            # sleep(4) 
            print("The room is unfamiliar, and there are chains around your wrists\n")
            # sleep(4) 
            print("Your adventure begins\n")
            # sleep(4) 
            print("Welcome to...\n")
            # sleep(4) 
            print(fontstyle.apply("Malice in Chains", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG')) # Big exciting font
            # sleep(4)
            from chapter_1a import chapter_1a
            chapter_1a()
        else:
            print("I guess I'll keep my eyes closed a little bit longer\n")
            sleep(2)




fname = ""
story_intro()
