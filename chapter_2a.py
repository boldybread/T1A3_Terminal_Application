from colored import Fore, Back, Style
import fontstyle
from time import sleep
from chapter_3a import chapter_3a

def chapter_2a():
    user_input = ""
    options = ["save girl", "wait"]
    print("At the top of the stairs is a big open room, there you see 2 guards one on either side of the room, and straight ahead of you is the woman who helped you escape")
    #sleep(4)
    print("You realise a third guard is facing her holding a gun up to her, you can intervene and save her or wait and see how this plays out")
    while user_input not in options:
        print("'save girl' | 'wait'")
        user_input = input().lower()
        if user_input == "save girl":
            print("You decide you owe this girl and you're going to do what you can to ensure she doesn't pay for helping you escape")
            # sleep(4)
            print("You can use the 'pistol' or 'rifle' or you could always try and 'talk' your way out of this")
            user_input2 = ""
            options2 = ["pistol", "rifle", "talk"]
            while user_input2 not in options2:
                print("'pistol' | 'rifle' | 'talk'")
                user_input2 = input().lower()
                if user_input2 == "pistol":
                    print("You pull out your pistol, take aim at the guard threatening the girl, and fire.")
                    # sleep(4)
                    print("There is confusion and panic by the two other guards as the third guard drops to the floor.")
                    # sleep(4)
                    print("The girl is the first to react, she pulls out a pistol and shoots the guard on the left")
                    # sleep(4)
                    print("The third guard stands and draws on you, but he isn't quick enough, you fire the rest of your pistol rounds and take him down")
                    pistol_ammo = False
                    # sleep(4)
                    print("The girl gives you a relieved smile before returning to her normal confident demeanor, 'took you long enough Mal!'")
                    # sleep(4)
                    print("'Come on, I know where Killjoy is, he owns a club downtown, I'll drive us there'")
                    chapter_3a()
                elif user_input2 == "rifle":
                    print("You lift up the rifle, and take aim at the guard threatening the girl, and fire.")
                    # sleep(4)
                    print("There is confusion and panic by the two other guards as the third guard drops to the floor.")
                    # sleep(4)
                    print("The girl is the first to react, she pulls out a pistol and shoots the guard on the left")
                    # sleep(4)
                    print("The third guard stands and draws on you, but he isn't quick enough, you fire a few more rounds from the rifle and take him down")
                    # sleep(4)
                    print("The girl gives you a relieved smile before returning to her normal confident demeanor, 'took you long enough Mal!'")
                    # sleep(4)
                    print("'Come on, I know where Killjoy is, he owns a club downtown, I'll drive us there'")
                    chapter_3a()
                elif user_input2 == "talk":
                    # sleep(4)
                    print("Alright here goes nothing, maybe I am a really smooth talker")
                    # sleep(4)
                    print("'Hey! I am the one you want, not her'")
                    # sleep(4)
                    print("The room looks at you. The girl looks at you dejectedly, but then offers a slight smile in thanks for trying")
                    # sleep(4)
                    print("'The boss will love this!' The third guard turns the gun on you, the girl shrieks as the gun fires.")
                    # sleep(4)
                    print(fontstyle.apply("YOU DIED", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG'))
                else:
                    print("I need to make a choice quickly!")
        elif user_input == "wait":
            print("You decide to let this play out, whats the worst that could happen?")
            # sleep(4)
            print("The girl pleads with the guard that she is innocent.")
            # sleep(4)
            print("The guard laughs and says he has been waiting for an excuse to do this. Panic in the girls voice before a gunshot, then silence")
            girl_alive = False
            # sleep(4)
            print("'Go check on Malice! If he has escaped Killjoy will have our heads!'")
            # sleep(4)
            print("The two guards stand up and turn to walk in your direction. Now is your chance to catch them unaware")
            # sleep(4)
            print("Time to open fire with the 'pistol' or 'rifle'")
            user_input3 = ""
            options3 = ["pistol", "rifle"]
            while user_input3 not in options3:
                print("'pistol' | 'rifle'")
                user_input3 = input().lower()
                    if user_input3 == "pistol":
                        print("You raise the pistol up and start firing")
                        # sleep(4)
                        print("You manage to drop both advancing guards before your pistol empties")
                        # sleep(4)
                        print("The third guard quickly raises his rifle at you and fires")
                        # sleep(4)
                        print(fontstyle.apply("YOU DIED", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG'))
                    elif user_input3 == "rifle":
                        print("'You raise the rifle up and start firing")
                        # sleep(4)
                        print("You easily drop both advancing guards and start aiming for the third, who is raising his rifle towards you")
                        # sleep(4)
                        print("You both start firing, you take him down, but also receive a flesh wound")
                        print("INJURED")
                        injured = True
                        # sleep(4)
                        print("I can either 'search' around or I can just 'leave' and forget all this")
                        user_input4 = ""
                        options4 = ["search", "leave"]
                        while user_input4 not in options4:
                        print("'search' | 'leave'")
                        user_input4 = input().lower()
                            if user_input4 == "search":
                                print("You start looking around for some clue to Killjoy's whereabouts")
                                # sleep(4)
                                print("At first it seems hopeless, then you see the VIP cards for a club on the table")
                                # sleep(4)
                                print("'Thats right! Killjoy owns that stupid club, Wonderland, he might be there'")
                                # sleep(4)
                                print("'Malice in Wonderland, there is a joke in there somewhere' You chuckle to yourself as you head out to find the place")
                                # sleep(4)
                                chapter_3a()
                            elif user_input4 == "leave":
                                leave()
                            else:
                            print("I need to make a choice quickly!")
                    else:
                    print("I need to make a choice quickly!")
        else:
            print("I need to make a choice quickly!")
