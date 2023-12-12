# from playsound import playsound
from colored import Fore, Back, Style
import fontstyle
from time import sleep



print(f"{Fore.black}{Back.white}Welcome to Malice in Chains a text based adventure. You control the journey by your choices. Lookout for text in quotations as this is an optional 'action' that can be chosen by typing in that input. Remember that choices can have consequences. Good luck!{Style.reset}\n")
sleep(1) # Set to 10 once complete

def story_intro():
    user_input = ""
    options = ["open"]
    while user_input not in options:
        print("open your eyes")
        user_input = input().lower()
        if user_input == "action":
            print("Well done! Here is your Easter Egg '@'\n")
            sleep(2)
        elif user_input == "@":
            print("Very funny! Please can you start the game already?!\n")
            sleep(2)
        elif user_input == "open":
            print("You wake feeling dizzy with an aching in your head\n")
            sleep(1) # Set to 4 once complete
            print("The last thing you remember is coming for Killjoy\n")
            sleep(1) # Set to 4 once complete
            print("Thats right, Killjoy, the one who... wait who is Killjoy, and why was I after him?\n")
            sleep(1) # Set to 4 once complete
            print("You tracked him down to a warehouse, you think...\n")
            sleep(1) # Set to 4 once complete
            print("Thats the last thing you remember, something went wrong, why can't I remember?\n")
            sleep(1) # Set to 4 once complete
            print("My name. Whats my name?\n")
            sleep(1) # Set to 4 once complete
            print("Nothing, OK where am I? A dimly lit room...\n")
            sleep(1) # Set to 4 once complete
            print("The room is unfamiliar, and there are chains around your wrists\n")
            sleep(1) # Set to 4 once complete
            print("Your adventure begins\n")
            sleep(1) # Set to 4 once complete
            print("Welcome to...\n")
            sleep(1) # Set to 4 once complete
            print(fontstyle.apply("Malice in Chains", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG')) # Big exciting font
        else:
            print("I guess I'll keep my eyes closed a little bit longer\n")
            sleep(2)

story_intro()

