from colored import Fore, Back, Style
import fontstyle
from time import sleep

def prologue():
    from main import wait_duration
    print(f"{Fore.black}{Back.white}Welcome to Malice in Chains a text based adventure. You control the journey by inputing your choices. \nLook out for any red text as this is an optional {Fore.red}'action'{Fore.black} that can be chosen by typing in that input. \nSometimes you won't be prompted to input that action so keep an eye out for red text. \nRemember that choices can have consequences. Good luck!{Style.reset}\n")
    sleep(10)
    user_input = ""
    options = ["open"]
    while user_input not in options:
        print(f"{Fore.red}open{Style.reset} your eyes")
        user_input = input().lower()
        if user_input == "action":
            print(f"Well done! Here is your Easter Egg {Fore.red}@{Style.reset}\n")
            sleep(wait_duration)
        elif user_input == "@":
            print("Very funny! Please can you start the game already?!\n")
            sleep(wait_duration)
        elif user_input == "open":
            print("You wake feeling dizzy with an aching in your head.\n")
            sleep(wait_duration) 
            print("The last thing you remember is coming for Killjoy.\n")
            sleep(wait_duration) 
            print("Thats right, Killjoy, the one who... wait who is Killjoy, and why were you after him?\n")
            sleep(wait_duration) 
            print("You tracked him down to a warehouse, you think...\n")
            sleep(wait_duration) 
            print("Thats the last thing you remember, something went wrong, why can't you remember?\n")
            sleep(wait_duration) 
            print("Your name. Whats your name? Its all blank.\n")
            sleep(wait_duration) 
            print("Nothing, OK where am you? A dimly lit room...\n")
            sleep(wait_duration) 
            print("The room is unfamiliar, and there are chains around your wrists.\n")
            sleep(wait_duration) 
            print("Your adventure begins...\n")
            sleep(wait_duration) 
            print("Welcome to...\n")
            sleep(wait_duration) 
            print(fontstyle.apply("Malice in Chains", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG'))
            sleep(wait_duration)
            from encounter import random_encounter
            random_encounter()
        else:
            print("I guess I'll keep my eyes closed a little bit longer\n")
            sleep(2)

