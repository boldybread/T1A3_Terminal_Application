from colored import Fore, Back, Style
import fontstyle
from time import sleep


def chapter_2a():
    user_input = ""
    options = ["left", "right"]
    print("You walk down a long corridor, as you turn a corner you see a guard patrolling near the bottom of some stairs, you can 'fire' from your vantage point or try and do this 'stealthily'")
    while user_input not in options:
        print("'fire' | 'stealth'")
        user_input = input().lower()
        if user_input == "fire":
            print("You aim the gun down the corridor towards your assailant, it feels natural in your hands, you've done this before")
            # sleep(4)
            print("The guard turns around but isn't quick enough to react, 2 gunshots ring out and the guard drops to the floor")
            # sleep(4)
            print("As you move down towards the fallen guard you hear shouts and multiple heavy footsteps, 'damn, they must have heard the gunshots'")
            # sleep(4)
            print("You aim the gun towards the stairs in preparation, 3 guards appear and quickly take aim at you")
            # sleep(4)
            print("You start firing, there is only 4 rounds left in your pistol and it isn't enough to take down your assailants who start firing back")
            # sleep(4)
            print(fontstyle.apply("YOU DIED", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG'))
        elif user_input == "stealth":
            print("You make your way down the corridor towards the guard")
            # sleep(4)
            print("The guard suddenly turns around, but you have the drop on him")
            # sleep(4)
            print("You aim your pistol at him, and tell him to drop his weapon. He complies.")
            # sleep(4)
            print("You make him turn around and you incapacitate him. No sounds coming from up the stairs, good, no one heard anything.")
            # sleep(4)
            print("You pick up the guards weapon and start to move up the stairs")
        else:
            print("I need to make a choice quickly!")