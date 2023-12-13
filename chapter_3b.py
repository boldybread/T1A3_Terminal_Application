from colored import Fore, Back, Style
import fontstyle
from time import sleep
from chapter_1b import name

def charge():
    print("You summon all your remaining strength, get up and start charging the bar")
    # sleep(4)
    if wounded == True:
        print("Killjoy is taken by surprise with your brash move but quickly overpowers you in your weakened condition. He throws you down and aims his gun at you.")
        # sleep(4)
        print(fontstyle.apply("YOU DIED", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG'))
    else:
        print("Killjoy is taken by surprise with your brash move, you both wrestle on the ground of the bar.")
        # sleep(4)
        print("You manage to knock his guns out of his hands, but he throws you off of him")
        if girl_alive == True:
            print("Killjoy stands, but the girl has taken his weapons, you hear a gunshot, and Killjoy drops to the floor, finally defeated.")
            pass # outro_2()
        else:
            print("Killjoy stands picking up his weapons, he aims at you and fires.")
            # sleep(4)
            print(fontstyle.apply("YOU DIED", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG'))

def girl_saves():
    print("Suddenly the girl appears behind Killjoy and smashes a bottle on his head")
    # sleep(4)
    print("You seize the opportunity and raise the rifle and fire. Killjoy is down for good.")
    pass # outro_2

def leave():
    print("You decide to get out of there, you've been shot, you just want to go lie down somewhere")
    # sleep(4)
    print("You limp out of there and back to your apartment")
    # sleep(4)
    print("You lay down in your bed and feel better already, nothing a bit of sleep won't fix!")
    # sleep(4)
    print("You wake up to a bang as Killjoy's goons bust through your door")
    # sleep(4)
    print(fontstyle.apply("YOU DIED", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG'))

def no_bar():
    print("You exchange shots with each other")
    # sleep(4)
    print(f"Then a silence as both of you stop shooting. 'You still alive there {name}?'")
    # sleep(4)
    user_input2 = ""
    options2 = ["say nothing", "answer"]
    while user_input2 not in options2:
        print("'say nothing' | 'answer'")
        user_input2 = input().lower()
        if user_input2 == "say nothing":
            print("You decide its best not to answer and try to relocate instead to get an advantage.")
            # sleep(4)
            print("Unfortunately Killjoy had the same idea and beat you to it, he has the drop on you")
            # sleep(4)
            print("'Any last words?'")
            # sleep(4)
            if girl_alive == True:
                 girl_saves()
            else:
                user_input3 = ""
                options3 = ["say nothing", "screw you!"]
                while user_input not in options3:
                print("'say nothing' | 'screw you!'")
                user_input3 = input().lower()
                if user_input3 == "say nothing":
                        print("'Figures, no one is ever cocky facing the inevitable.'")
                    print(fontstyle.apply("YOU DIED", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG'))
                elif user_input3 == "screw you!":
                    print("'Yeah I'd probably say the same if the shoe was on the foot. See ya Malice.'")
                    print(fontstyle.apply("YOU DIED", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG'))
        elif user_input2 == "answer":
            print("'Yeah I'm still here. How are you doing?'")
            # sleep(4)
            if girl_alive == True:
                print("'So Nikki couldn't bare the thought of you locked away' I'm going to kill her after I kill you just so you know")
                # sleep (4)
                girl_saves()
            else:
                print("'How did you manage to get out by the way? Was it Nikki?'")
                # sleep(4)
                print("Nikki, that was her name!")
                # sleep(4)
                print("'and where is nik...'")
                # sleep(4)
                print("You seize your chance and spring up from cover and fire one round. It hits Killjoy cleanly.")
                # sleep(4)
                print("'She is dead, just like you are.'")
                pass # outro_1
        else:
            print("I need to make a choice quickly!")