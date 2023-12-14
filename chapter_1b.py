from colored import Fore, Back, Style
import fontstyle
from time import sleep

pistol_ammo = False
lighter = False
def chapter_1b():
    from chapter_1c import chapter_1c
    user_input = ""
    options = ["left", "right"]
    print(f"You are faced with 2 directions, {Fore.red}left{Style.reset} towards what looks like a store room or {Fore.red}'right'{Style.reset} towards the exit")
    while user_input not in options:
        print("'left' | 'right'")
        user_input = input().lower()
        if user_input == "left":
            print("You enter a small storeroom")
            # sleep(4)
            print("You find a pistol, this will be useful! You pocket the gun")
            print(f"{Fore.green}Gained PISTOL + PISTOL AMMO{Style.reset}")
            global pistol_ammo
            pistol_ammo = True
            # sleep(4)
            print("You find your driver's license, they must have taken it off you, you remember a bit about yourself")
            # sleep(4)
            global fname
            fname = input("Remember your name: ").capitalize()
            # sleep(4)
            print("thats right! my name is " + fname +" and everybody calls me Malice!")
            # sleep(4)
            user_input3 = ""
            options3 = ["take", "leave"]
            print(f"You find a small zippo lighter, could be useful, {Fore.red}take{Style.reset} it or {Fore.red}leave{Style.reset} it?")
            while user_input3 not in options3:
                print("'take' | 'leave'")
                user_input3 = input().lower()
                if user_input3 == "take":
                    print(f"{Fore.green}Gained LIGHTER{Style.reset}")
                    global lighter
                    lighter = True
                    print("Alright time to get out of this place!")
                    chapter_1c()
                elif user_input3 == "leave":
                    print("You decide its best to keep moving")
                    # sleep(4)
                    print("Best to get out of here")
                    chapter_1c()
                else:
                    print("I need to make a choice quickly!")
                    # sleep(4)
        elif user_input == "right":
            print("You travel down a long corridor carefully")
            # sleep(4)
            print("You turn a corner and see a solitary guard patrolling who hasn't seen you yet")
            # sleep(4)
            user_input2 = ""
            options2 = ["go back", "fight guard"]
            print("There is still time to turn around or I could try and take him down...")
            while user_input2 not in options2:
                print("'go back' | 'fight guard'")
                user_input2 = input().lower()
                if user_input2 == "go back":
                    print("You quietly slink back the way you came")
                    # sleep(4)
                    print("You arrive back at the entrance of your would be jail")
                    chapter_1b()
                elif user_input2 == "fight guard":
                    print("You stealthily start moving towards the guard")
                    # sleep(4)
                    print("But he has reached the end of the corridor and begins to turn")
                    # sleep(4)
                    print("You break into a run, but theres not enough time to cover the distance")
                    # sleep(4)
                    print("The guard smirks at your attempted escape and raises a large gun towards you and fires")
                    # sleep(4)
                    from chapter_3b import you_died
                    you_died()
                else:
                    print("I need to make a choice quickly!")
        else:
            print("I need to make a choice quickly!")