import fontstyle
from time import sleep

def chapter_3c():
    user_input = ""
    print("You arrive at the club, 'Wonderland'")
    print("A popular nightspot in the city, yet the outside now is deserted")
    print("'Malice in Wonderland, got to be a joke in there somewhere.' The girl chuckles.")
    print("You make your way inside, past the foyer you can see at least 5 of Killjoy's goons.")
    global pistol_ammo
    from chapter_2a import pistol_ammo
    if pistol_ammo == True:
        print("Give me the rest of your pistol ammo and I will cover you from upstairs")
        # sleep(4)
        print("You hand over your ammo, and the girl heads off up a flight of stairs")
        print("lost PISTOL AMMO")
        pistol_ammo = False
        # sleep(4)
        print("With the girl in position you bust through the main entrance and start firing.")
        # sleep(4)
        print("The girl provides covering fire and you despatch the goons without incident.")
        # sleep(4)
        print("Suddenly Killjoy bursts through a door in the back dual pistols in hand and starts firing at the both of you")
        # sleep(4)
        print("You throw yourself into cover, you only have a couple of rounds left in your rifle")
        # sleep(4)
        print("The girl lays down covering fire, Killjoy takes cover behind the bar")
        # sleep(4)
        print("If I had something to light I could use the alcohol behind the bar. I might have to charge the bar instead.'")
        # sleep(4)
        global lighter
        from chapter_1b import lighter
        if lighter == True:
            user_input = ""
            options = ["lighter", "charge"]
            while user_input not in options:
                print("'lighter' | 'charge'")
                user_input = input().lower()
                if user_input == "lighter":
                    print("Thats right I picked up that lighter. 'Shoot out the bottles!' You yell.")
                    # sleep(4)
                    print("The girl fires the last of her rounds into the various bottles behind the bar")
                    # sleep(4)
                    print("You light the lighter and throw it over the bar which immediately erupts in big flames.")
                    # sleep(4)
                    print("With a scream Killjoy stands up in an attempt to avoid the fire")
                    # sleep(4)
                    print("Thats all you needed, you fire the last of your shots and finally take him down.")
                    from outro import outro_2
                    outro_2()
                elif user_input == "charge":
                    print("You decide to charge the bar in an all or nothing play")
                    from chapter_3b import charge
                    charge()
        else:
            print("You decide to charge the bar in an all or nothing play")
            from chapter_3b import charge
            charge()
    else:
        print("'I don't have much ammo left but I can cover you from upstairs'")
        # sleep(4)
        print("You can 'swap' her pistol for your rifle giving her more ammo to cover you, or trust in your own ability and 'keep' the rifle")
        user_input = ""
        options = ["swap", "keep"]
        while user_input not in options:
            print("'swap' | 'keep'")
            user_input = input().lower()
            if user_input == "swap":
                print("'Take this rifle, you can do more with it up there anyway'")
                # sleep(4)
                print("'OK if you're sure, thanks!' The girl hands you the pistol and then runs off up a flight of stairs")
                print("lost RIFLE + RIFLE AMMO")
                rifle_ammo = False
                print("gained PISTOL + PISTOL AMMO")
                pistol_ammo = True
                # sleep(4)
                print("You wait for the girl to start firing, and then use the distraction to move in the main doors and start picking off the goons carefully.")
                # sleep(4)
                print("The girl is skilled with the rifle and you despatch all the goons easily without much fuss.")
                # sleep(4)
                print("Suddenly Killjoy bursts through a door in the back, dual pistols in hand and starts firing at the both of you.")
                # sleep(4)
                print("You groan throwing the empty pistol and dive into cover")
                # sleep(4)
                print("covering fire forces Killjoy to take cover behind the bar")
                # sleep(4)
                print("If I had something to light I could use the alcohol behind the bar. I might have to charge the bar instead.'")
                # sleep(4)
                from chapter_1b import lighter
                from chapter_3b import charge
                if lighter == True:
                    user_input2 = ""
                    options2 = ["lighter", "charge"]
                    while user_input2 not in options2:
                        print("'lighter' | 'charge'")
                        user_input2 = input().lower()
                        if user_input2 == "lighter":
                            print("Thats right I picked up that lighter. 'Shoot out the bottles!' You yell.")
                            # sleep(4)
                            print("The girl fires into the various bottles behind the bar")
                            # sleep(4)
                            print("You light the lighter and throw it over the bar which immediately erupts in big flames.")
                            # sleep(4)
                            print("With a scream Killjoy stands up in an attempt to avoid the fire")
                            # sleep(4)
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
                    charge()
            elif user_input == "keep":
                print("'Cover me the best you can, I will do my best down here'")
                # sleep(4)
                print("The girl nods and runs off up a flight of stairs")
                # sleep(4)
                print("With the girl in position you bust through the main door and start firing")
                # sleep(4)
                print("Having the element of surprise helps and the first few goons go down.")
                # sleep(4)
                print("The girl starts firing picking one more off and distracting the rest allowing you to make short work of them.")
                # sleep(4)
                print("Suddenly Killjoy bursts through a door in the back, dual pistols in hand and starts firing at the both of you.")
                # sleep(4)
                print("You groan and jump into cover, half a clip left of rifle ammo, it looks like the girl is out as well")
                from chapter_3b import no_bar
                no_bar()
            else:
                print("I need to make a choice quickly!")