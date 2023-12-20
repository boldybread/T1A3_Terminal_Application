from colored import Fore, Back, Style
import fontstyle
from time import sleep


wounded = False
girl_alive = True

def chapter_2a():
    from main import wait_duration
    from chapt_3a import chapter_3a
    from chapt_3c import chapter_3c
    from rps_minigame import rps_minigame
    from chapt_3b import leave
    global pistol_ammo
    from chapt_1b import pistol_ammo
    user_input = ""
    options = ["save her", "wait"]
    print("At the top of the stairs is a big open room, there you see 2 guards one on either side of the room, and straight ahead of you is the woman who helped you escape")
    sleep(wait_duration)
    print(f"You realise a third guard is facing her holding a gun up to her, you can intervene and {Fore.red}save her{Style.reset} or {Fore.red}wait{Style.reset} and see how this plays out")
    while user_input not in options:
        print("'save her' | 'wait'")
        user_input = input().lower()
        if user_input == "save her":
            print("You decide you owe this girl and you're going to do what you can to ensure she doesn't pay for helping you escape")
            sleep(wait_duration)
            print(f"You can use the {Fore.red}pistol{Style.reset} or {Fore.red}rifle{Style.reset} or you could always try and {Fore.red}talk{Style.reset} your way out of this")
            user_input2 = ""
            options2 = ["pistol", "rifle", "talk"]
            while user_input2 not in options2:
                print("'pistol' | 'rifle' | 'talk'")
                user_input2 = input().lower()
                if user_input2 == "pistol":
                    print("You pull out your pistol, take aim at the guard threatening the girl, and fire.")
                    sleep(wait_duration)
                    print("There is confusion and panic by the two other guards as the third guard drops to the floor.")
                    sleep(wait_duration)
                    print("The girl is the first to react, she pulls out a pistol and shoots the guard on the left")
                    sleep(wait_duration)
                    print("The third guard stands and draws on you, but he isn't quick enough, you fire the rest of your pistol rounds and take him down")
                    sleep(wait_duration)
                    print(f"{Fore.green}lost PISTOL AMMO{Style.reset}")
                    pistol_ammo = False
                    sleep(wait_duration)
                    print("The girl gives you a relieved smile before returning to her normal confident demeanor, 'took you long enough Mal!'")
                    sleep(wait_duration)
                    print("'Come on, I know where Killjoy is, he owns a club downtown, I'll drive us there'")
                    rps_minigame()
                elif user_input2 == "rifle":
                    print("You lift up the rifle, and take aim at the guard threatening the girl, and fire.")
                    sleep(wait_duration)
                    print("There is confusion and panic by the two other guards as the third guard drops to the floor.")
                    sleep(wait_duration)
                    print("The girl is the first to react, she pulls out a pistol and shoots the guard on the left")
                    sleep(wait_duration)
                    print("The third guard stands and draws on you, but he isn't quick enough, you fire a few more rounds from the rifle and take him down")
                    sleep(wait_duration)
                    print("The girl gives you a relieved smile before returning to her normal confident demeanor, 'took you long enough Mal!'")
                    sleep(wait_duration)
                    print("'Come on, I know where Killjoy is, he owns a club downtown, I'll drive us there'")
                    sleep(wait_duration)
                    rps_minigame()
                elif user_input2 == "talk":
                    sleep(wait_duration)
                    print("Alright here goes nothing, maybe I am a really smooth talker")
                    sleep(wait_duration)
                    print("'Hey! I am the one you want, not her'")
                    sleep(wait_duration)
                    print("The room looks at you. The girl looks at you dejectedly, but then offers a slight smile in thanks for trying")
                    sleep(wait_duration)
                    print("'The boss will love this!' The third guard turns the gun on you, the girl shrieks as the gun fires.")
                    sleep(wait_duration)
                    from chapt_3b import you_died
                    you_died()
                else:
                    print("I need to make a choice quickly!")
        elif user_input == "wait":
            print("You decide to let this play out, whats the worst that could happen?")
            sleep(wait_duration)
            print("The girl pleads with the guard that she is innocent.")
            sleep(wait_duration)
            print("The guard laughs and says he has been waiting for an excuse to do this. Panic in the girls voice before a gunshot, then silence")
            global girl_alive 
            girl_alive = False
            sleep(wait_duration)
            print("'Go check on Malice! If he has escaped Killjoy will have our heads!'")
            sleep(wait_duration)
            print("The two guards stand up and turn to walk in your direction. Now is your chance to catch them unaware")
            sleep(wait_duration)
            print("Time to open fire with the 'pistol' or 'rifle'")
            user_input3 = ""
            options3 = ["pistol", "rifle"]
            while user_input3 not in options3:
                print("'pistol' | 'rifle'")
                user_input3 = input().lower()
                if user_input3 == "pistol":
                    print("You raise the pistol up and start firing")
                    sleep(wait_duration)
                    print("You manage to drop both advancing guards before your pistol empties")
                    sleep(wait_duration)
                    print("The third guard quickly raises his rifle at you and fires")
                    sleep(wait_duration)
                    from chapt_3b import you_died
                    you_died()
                elif user_input3 == "rifle":
                    print("'You raise the rifle up and start firing")
                    sleep(wait_duration)
                    print("You easily drop both advancing guards and start aiming for the third, who is raising his rifle towards you")
                    sleep(wait_duration)
                    print("You both start firing, you take him down, but also receive a flesh wound")
                    sleep(wait_duration)
                    print(f"{Fore.green}WOUNDED{Style.reset}")
                    global wounded
                    wounded = True
                    sleep(wait_duration)
                    print(f"I can either {Fore.red}search{Style.reset} around or I can just {Fore.red}leave{Style.reset} and forget all this")
                    user_inputwait_duration = ""
                    optionswait_duration = ["search", "leave"]
                    while user_inputwait_duration not in optionswait_duration:
                        print("'search' | 'leave'")
                        user_inputwait_duration = input().lower()
                        if user_inputwait_duration == "search":
                            print("You start looking around for some clue to Killjoy's whereabouts")
                            sleep(wait_duration)
                            print("At first it seems hopeless, then you see the VIP cards for a club on the table")
                            sleep(wait_duration)
                            print("'Thats right! Killjoy owns that stupid club, Wonderland, he might be there'")
                            sleep(wait_duration)
                            print("'Malice in Wonderland, there is a joke in there somewhere' You chuckle to yourself as you head out to find the place")
                            sleep(wait_duration)
                            chapter_3a()
                        elif user_inputwait_duration == "leave":
                            leave()
                        else:
                            print("I need to make a choice quickly!")
                else:
                    print("I need to make a choice quickly!")
        else:
            print("I need to make a choice quickly!")
