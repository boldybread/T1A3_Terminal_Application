from colored import Fore, Back, Style
import fontstyle
from time import sleep
import random

def rps_minigame():
    from main import wait_duration
    global wounded
    from chapter_2a import wounded
    print("Soon you're driving through the neon lit streets towards your confrontation with Killjoy")
    # sleep(wait_duration)
    print("The girl's blue Honda races through the streets")
    # sleep(wait_duration)
    # from chapt blah import blah
    if wounded:
        print("You look down at your injury and grimace as your body braces against the girl's hasty driving")
    print("Before long you arrive in front of a giant night club")
    sleep(wait_duration)
    print("The outside of the place is deserted, 'You sure Killjoy is here?' you ask.")
    sleep(wait_duration)
    print("'No idea' she responds, 'I figure one of us goes and takes a look'")
    sleep(wait_duration)
    print("'I can go' you say. 'Why don't we Rock, Paper, Scissors to see who goes?' She jests")
    sleep(wait_duration)
    print("You look at her quizzically and you realise she is seriously waiting for an answer")
    choice = ""
    choice_options = ["yes", "no"]
    print(f"{Fore.red}play{Style.reset} rock, paper, scissors or {Fore.red}no{Style.reset}")
    while choice not in choice_options:
        print("'play' | 'no'")
        choice = input().lower()
        if choice == "play":
            from rock_paper_scissors import rock_paper_scissors
            rock_paper_scissors()
        elif choice == "no":
            print("Is she crazy? There is no time for games!")
            sleep(wait_duration)
            from chapter_3a import chapter_3a
            chapter_3a()
        else:
            ("I need to make a decision!")