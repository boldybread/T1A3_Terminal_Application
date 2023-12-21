import fontstyle
from time import sleep
from main import wait_duration

# This file contains the various game over functions either as a player died or Killjoy has died and game is complete 

def you_died():
    print(fontstyle.apply("YOU DIED", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG'))
    sleep(wait_duration)
    print("Would you like to try again?")
    start_over = ""
    opt = ["yes", "no"]
    while start_over not in opt:
        print("'yes' | 'no'")
        # global start_over
        start_over = input().lower()
        if start_over == "yes":
            print("good luck")
            sleep(wait_duration)
            from main import prologue
            prologue()
        elif start_over == "no":
            exit()
        else:
            print("Don't give up!")

def charge():
    print("You summon all your remaining strength, get up and start charging the bar")
    sleep(wait_duration)
    global wounded
    global injured
    from chapt_2a import wounded
    from chapt_3a import injured
    if wounded or injured:
        print("Killjoy is taken by surprise with your brash move but quickly overpowers you in your weakened condition. He throws you down and aims his gun at you.")
        sleep(wait_duration)
        from chapt_1b import fname
        print(f"'Nice try {fname}, see ya around!'")
        you_died()
    else:
        print("Killjoy is taken by surprise with your brash move, you both wrestle on the ground of the bar.")
        sleep(wait_duration)
        print("You manage to knock his guns out of his hands, but he throws you off of him")
        sleep(wait_duration)
        global girl_alive
        from chapt_2a import girl_alive
        if girl_alive:
            print("Killjoy stands, but the girl has taken his weapons, you hear a gunshot, and Killjoy drops to the floor, finally defeated.")
            sleep(wait_duration)
            from outro import outro_2
            outro_2()
        else:
            print("Killjoy stands picking up his weapons, he aims at you and fires.")
            sleep(wait_duration)
            you_died()

def girl_saves():
    print("Suddenly the girl appears behind Killjoy and smashes a bottle on his head")
    sleep(wait_duration)
    print("You seize the opportunity and raise the rifle and fire. Killjoy is down for good.")
    sleep(wait_duration)
    from outro import outro_2
    outro_2()

def leave():
    print("You decide to get out of there, you've been shot, you just want to go lie down somewhere")
    sleep(wait_duration)
    print("You limp out of there and back to your apartment")
    sleep(wait_duration)
    print("You lay down in your bed and feel better already, nothing a bit of sleep won't fix!")
    sleep(wait_duration)
    print("You wake up to a bang as Killjoy's goons bust through your door")
    sleep(wait_duration)
    you_died()

def no_bar():
    print("You exchange shots with each other")
    sleep(wait_duration)
    from chapt_1b import fname
    print(f"Then a silence as both of you stop shooting. 'You still alive there {fname}?'")
    sleep(wait_duration)
    user_input2 = ""
    options2 = ["say nothing", "answer"]
    while user_input2 not in options2:
        print("'say nothing' | 'answer'")
        user_input2 = input().lower()
        global girl_alive
        if user_input2 == "say nothing":
            print("You decide its best not to answer and try to relocate instead to get an advantage.")
            sleep(wait_duration)
            print("Unfortunately Killjoy had the same idea and beat you to it, he has the drop on you")
            sleep(wait_duration)
            print("'Any last words?'")
            sleep(wait_duration)
            from chapt_2a import girl_alive
            if girl_alive:
                girl_saves()
            else:
                user_input3 = ""
                options3 = ["say nothing", "screw you!"]
                while user_input3 not in options3:
                    print("'say nothing' | 'screw you!'")
                    user_input3 = input().lower()
                    if user_input3 == "say nothing":
                        print("'Figures, no one is ever cocky facing the inevitable.'")
                        sleep(wait_duration)
                        you_died()
                    elif user_input3 == "screw you!":
                        print("'Yeah I'd probably say the same if the shoe was on the foot. See ya Malice.'")
                        sleep(wait_duration)
                        you_died()
                    else:
                        print("I need to make a choice quickly!")
        elif user_input2 == "answer":
            print("'Yeah I'm still here. How are you doing?'")
            sleep(wait_duration)
            from chapt_2a import girl_alive
            if girl_alive:
                print("'So Nikki couldn't bear the thought of you locked away' I'm going to kill her after I kill you just so you know")
                sleep (wait_duration)
                girl_saves()
            else:
                print("'How did you manage to get out by the way? Was it Nikki?'")
                sleep(wait_duration)
                last_chance = ""
                lc_options = ["wait", "charge"]
                while last_chance not in lc_options:
                    print("'wait' | 'charge'")
                    last_chance = input().lower()
                    if last_chance == "wait":
                        print("Nikki, that was her name!")
                        sleep(wait_duration)
                        print("'and where is nik...'")
                        sleep(wait_duration)
                        print("You seize your chance and spring up from cover and fire one round. It hits Killjoy cleanly.")
                        sleep(wait_duration)
                        print("'She is dead, just like you are.'")
                        from outro import outro_1
                        outro_1()
                    elif last_chance == "charge":
                        charge()
                    else:
                        print("Choose quickly!!")
        else:
            print("I need to make a choice quickly!")
