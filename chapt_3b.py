from colored import Fore, Back, Style
import fontstyle
from time import sleep

def chapter_3c(): # 3c is the girl alive final showdown continuation (3a is girl not alive)
    from main import wait_duration
    global pistol_ammo
    from chapt_2a import pistol_ammo
    user_input = ""
    print("You arrive at the club, 'Wonderland'.")
    sleep(wait_duration)
    print("A popular nightspot in the city, yet the outside now is deserted.")
    sleep(wait_duration)
    print("'Malice in Wonderland, got to be a joke in there somewhere.' The girl chuckles.")
    sleep(wait_duration)
    print("You make your way inside, past the foyer you can see at least 5 of Killjoy's goons.")
    if pistol_ammo: 
        print("'Give me the rest of your pistol ammo and I will cover you from upstairs' she says.")
        sleep(wait_duration)
        print(f"I could {Fore.red}handover{Style.reset} my pistol ammo, or I could {Fore.red}keep{Style.reset} it for myself, just in case.")
        handover_input = ""
        handover_options = ["handover", "keep"]
        while user_input not in handover_options:
            print("'handover' | 'keep'")
            handover_input = input().lower()
            if handover_input == "handover":
                print("You hand over your ammo, and the girl heads off up a flight of stairs")
                print(f"{Fore.green}lost PISTOL AMMO{Style.reset}")
                pistol_ammo = False
                sleep(wait_duration)
                print("With the girl in position you bust through the main entrance and start firing.")
                sleep(wait_duration)
                print("The girl provides covering fire and you despatch the goons without incident.")
                sleep(wait_duration)
                print("Suddenly Killjoy bursts through a door in the back dual pistols in hand and starts firing at the both of you")
                sleep(wait_duration)
                print("You throw yourself into cover, you only have a couple of rounds left in your rifle")
                sleep(wait_duration)
                print("The girl lays down covering fire, Killjoy takes cover behind the bar")
                sleep(wait_duration)
                print("If I had something to light I could use the alcohol behind the bar. I might have to charge the bar instead.'")
                sleep(wait_duration)
                global lighter
                from chapt_1b import lighter
                if lighter:
                    user_input = ""
                    options = ["lighter", "charge"]
                    while user_input not in options:
                        print("'lighter' | 'charge'")
                        user_input = input().lower()
                        if user_input == "lighter":
                            print("Thats right I picked up that lighter. 'Shoot out the bottles!' You yell.")
                            sleep(wait_duration)
                            print("The girl fires the last of her rounds into the various bottles behind the bar")
                            sleep(wait_duration)
                            print("You light the lighter and throw it over the bar which immediately erupts in big flames.")
                            sleep(wait_duration)
                            print("With a scream Killjoy stands up in an attempt to avoid the fire")
                            sleep(wait_duration)
                            print("Thats all you needed, you fire the last of your shots and finally take him down.")
                            from outro import outro_2
                            outro_2()
                        elif user_input == "charge":
                            print("You decide to charge the bar in an all or nothing play")
                            from consequences import charge
                            charge()
                else:
                    print("You decide to charge the bar in an all or nothing play")
                    from consequences import charge
                    charge()
            elif handover_input == "keep":
                print("'I think I will just keep all the ammo to myself just in case'")
                sleep(wait_duration)
                print("'You won't give me any ammo? Seriously!? You think thats a good idea?'")
                sleep(wait_duration)
                print("'I just think that I might be able to do more with all this ammo to myself rather than sharing any'")
                sleep(wait_duration)
                print("'Really Mal? You're unbelievable!'")
                sleep(wait_duration)
                print("While you were busy arguing you were spotted by Killjoy's goons who burst through into the foyer firing at you both.")
                sleep(wait_duration)
                from consequences import you_died
                you_died()
            else:
                print("I need to make a choice quickly!")
    else:
        print("'I don't have much ammo left but I can cover you from upstairs'")
        sleep(wait_duration)
        print(f"You can {Fore.red}swap{Style.reset} her pistol for your rifle giving her more ammo to cover you, or trust in your own ability and {Fore.red}keep{Style.reset} the rifle")
        user_input = ""
        options = ["swap", "keep"]
        while user_input not in options:
            print("'swap' | 'keep'")
            user_input = input().lower()
            if user_input == "swap":
                print("'Take this rifle, you can do more with it up there anyway'")
                sleep(wait_duration)
                print("'OK if you're sure, thanks!' The girl hands you the pistol and then runs off up a flight of stairs")
                print(f"{Fore.green}lost RIFLE + RIFLE AMMO{Style.reset}")
                rifle_ammo = False
                print(f"{Fore.green}Gained PISTOL + PISTOL AMMO{Style.reset}")
                pistol_ammo = True
                sleep(wait_duration)
                print("You wait for the girl to start firing, and then use the distraction to move in the main doors and start picking off the goons carefully.")
                sleep(wait_duration)
                print("The girl is skilled with the rifle and you despatch all the goons easily without much fuss.")
                sleep(wait_duration)
                print("Suddenly Killjoy bursts through a door in the back, dual pistols in hand and starts firing at the both of you.")
                sleep(wait_duration)
                print("You groan throwing the empty pistol and dive into cover")
                sleep(wait_duration)
                print("covering fire forces Killjoy to take cover behind the bar")
                sleep(wait_duration)
                print(f"If I had something to {Fore.red}light{Style.reset} I could use the alcohol behind the bar. I might have to {Fore.red}charge{Style.reset} the bar instead.'")
                sleep(wait_duration)
                from chapt_1b import lighter
                from consequences import charge
                if lighter:
                    user_input2 = ""
                    options2 = ["lighter", "charge"]
                    while user_input2 not in options2:
                        print("'lighter' | 'charge'")
                        user_input2 = input().lower()
                        if user_input2 == "lighter":
                            print("Thats right I picked up that lighter. 'Shoot out the bottles!' You yell.")
                            sleep(wait_duration)
                            print("The girl fires into the various bottles behind the bar")
                            sleep(wait_duration)
                            print("You light the lighter and throw it over the bar which immediately erupts in big flames.")
                            sleep(wait_duration)
                            print("With a scream Killjoy stands up in an attempt to avoid the fire")
                            sleep(wait_duration)
                            print("The girl fires at the screaming man who is completely open and he is finally taken down.")
                            from outro import outro_2
                            outro_2()
                        elif user_input2 == "charge":
                            print("You decide to charge the bar in an all or nothing play")
                            charge()
                        else:
                            print("I need to make a choice quickly!")
                else:
                    print("You decide to charge the bar in an all or nothing play")
                    sleep(wait_duration)
                    charge()
            elif user_input == "keep":
                print("'Cover me the best you can, I will do my best down here'")
                sleep(wait_duration)
                print("The girl nods and runs off up a flight of stairs")
                sleep(wait_duration)
                print("With the girl in position you bust through the main door and start firing")
                sleep(wait_duration)
                print("Having the element of surprise helps and the first few goons go down.")
                sleep(wait_duration)
                print("The girl starts firing picking one more off and distracting the rest allowing you to make short work of them.")
                sleep(wait_duration)
                print("Suddenly Killjoy bursts through a door in the back, dual pistols in hand and starts firing at the both of you.")
                sleep(wait_duration)
                print("You groan and jump into cover, half a clip left of rifle ammo, it looks like the girl is out as well")
                sleep(wait_duration)
                from consequences import no_bar
                no_bar()
            else:
                print("I need to make a choice quickly!")