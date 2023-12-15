from colored import Fore, Back, Style
import fontstyle
from time import sleep
import random

while True:
    rps_choice = input(f"Enter {Fore.red}Rock{Style.reset}, {Fore.red}Paper{Style.reset} or {Fore.red}Scissors{Style.reset}: ").lower()
    game_choices = ["rock", "paper", "scissors"]
    nikki_choice = random.choice(game_choices)

    print(f"You chose {rps_choice} and the girl chose {nikki_choice}")
    if rps_choice == nikki_choice:
        print(f"Both of you chose {rps_choice}, its a tie! Lets go again on 3!")
    elif rps_choice == "rock":
        if nikki_choice == "paper":
            print("The girl beat you with paper!")
        else:
            print("You beat her with trusty old rock!")
    elif rps_choice == "scissors":
        if nikki_choice == "rock":
            print("The girl beat you with rock!")
        else:
            print("You beat her with scissors!")
    elif rps_choice == "paper":
        if nikki_choice == "scissors":
            print("The girl beat you with scissors!")
        else:
            print("You beat her with paper!")

    play_again = ""
    play_options = ["yes", "no"]
    print("Do you want to play one more game?")
    while play_again not in options:
        print("'yes' | 'no'")
        play_again = input().lower()
        if play_again == "yes":
            print("There is always time for one more game") # Could look at adding a value to track if last game was won or not and then comment in code about it
        elif play_again == "no":
            print("No there isn't much time, we should get a move on!")
        else:
            print("This is harder to choose than choosing between rock, paper, scissors! But seriously, make a choice!")