from colored import Fore, Back, Style
import fontstyle
from time import sleep
from chapt_2a import chapter_2a

rifle_ammo = False

def chapter_1c():
    from main import wait_duration
    user_input = ""
    options = ["left", "right"]
    print(f"You walk down a long corridor, as you turn a corner you see a guard patrolling near the bottom of some stairs, you can {Fore.red}fire{Style.reset} from your vantage point or try and do this {Fore.red}stealthily{Style.reset}")
    while user_input not in options:
        print("'fire' | 'stealth'")
        user_input = input().lower()
        if user_input == "fire":
            print("You aim the gun down the corridor towards your assailant, it feels natural in your hands, you've done this before")
            sleep(wait_duration)
            print("The guard turns around but isn't quick enough to react, 2 gunshots ring out and the guard drops to the floor")
            sleep(wait_duration)
            print("As you move down towards the fallen guard you hear shouts and multiple heavy footsteps, 'damn, they must have heard the gunshots'")
            sleep(wait_duration)
            print("You aim the gun towards the stairs in preparation, 3 guards appear and quickly take aim at you")
            sleep(wait_duration)
            print("You start firing, there is only 4 rounds left in your pistol and it isn't enough to take down your assailants who start firing back")
            sleep(wait_duration)
            from consequences import you_died
            you_died()
        elif user_input == "stealth":
            print("You make your way down the corridor towards the guard")
            sleep(wait_duration)
            print("The guard suddenly turns around, but you have the drop on him")
            sleep(wait_duration)
            print("You aim your pistol at him, and tell him to drop his weapon. He complies.")
            sleep(wait_duration)
            print("You make him turn around and you incapacitate him. No sounds coming from up the stairs, good, no one heard anything.")
            sleep(wait_duration)
            print("You pick up the guards weapon and start to move up the stairs")
            print(f"{Fore.green}Gained RIFLE + RIFLE AMMO{Style.reset}")
            sleep(wait_duration)
            global rifle_ammo
            rifle_ammo = True
            chapter_2a()
        else:
            print("I need to make a choice quickly!")
