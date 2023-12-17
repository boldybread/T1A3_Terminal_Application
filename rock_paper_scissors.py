from colored import Fore, Back, Style
import fontstyle
from time import sleep
import random

def rock_paper_scissors():
    print("'sure we've got time for a quick game I guess!'")
    rps_choice = input(f"Enter {Fore.red}Rock{Style.reset}, {Fore.red}Paper{Style.reset} or {Fore.red}Scissors{Style.reset}: ").lower()
    game_choices = ["rock", "paper", "scissors"]
    nikki_choice = random.choice(game_choices)
    player_wins = 0
    nikki_wins = 0

    if rps_choice == nikki_choice:
        print(f"Both of you chose {rps_choice}, its a tie! Lets go again on 3!")
    elif rps_choice == "rock":
        print(f"You chose {rps_choice} and the girl chose {nikki_choice}")
        if nikki_choice == "paper":
            print("she beat you! 'Men always seem to go for rock!' she chuckles")
            nikki_wins += 1
        else:
            print("You won! Trusty old rock!")
            player_wins += 1
    elif rps_choice == "scissors":
        print(f"You chose {rps_choice} and the girl chose {nikki_choice}")
        if nikki_choice == "rock":
            print("She beat you!")
            nikki_wins += 1
        else:
            print("You won! 'Shoot, I thought you'd be predictable and go rock!' She says.")
            player_wins += 1
    elif rps_choice == "paper":
        print(f"You chose {rps_choice} and the girl chose {nikki_choice}")
        if nikki_choice == "scissors":
            print("The girl beat you with scissors!")
            nikki_wins += 1
        else:
            print("You beat her with paper!")
            player_wins += 1
    else:
        print("Its a tough choice I know! Maybe trusty old rock?")

    play_again = ""
    play_options = ["yes", "no"]
    print("Do you want to play one more game?")
    while play_again not in play_options:
        print("'yes' | 'no'")
        play_again = input().lower()
        if play_again == "yes":
            print("There is always time for one more game")
            sleep(2)
            rock_paper_scissors()
        elif play_again == "no":
            print("No there isn't much time, we should get a move on!")
            sleep(2)
            print("She looks disapointed. 'Come on lets go she says'")
            from main import wait_duration
            if player_wins > nikki_wins:
                print("'I won more games, so I guess you go check on Killjoy?'")
                sleep(wait_duration)
            elif player_wins < nikki_wins:
                print("'You won more games, so I guess I'll go check if Killjoy is here?'")
                sleep(wait_duration)
            else:
                print("'We tied overall, so who is going to see if Killjoy is here?'")
                sleep(wait_duration)
            print("The girl laughs, 'Thats his car right there' she points to a done up Mustang, 'come on lets go, we've wasted enough time already' she jests")
            from chapter_3a import chapter_3a
            chapter_3a()
        else:
            print("This is harder to choose than choosing between rock, paper, scissors! But seriously, make a choice!")

