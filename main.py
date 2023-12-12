# from playsound import playsound
from colored import Fore, Back, Style
import fontstyle
from time import sleep



print(f"{Fore.black}{Back.white}Welcome to Malice in Chains a text based adventure. You control the journey by your choices. Look out for text in quotations as this is an optional 'action' that can be chosen by typing in that input. Remember that choices can have consequences. Good luck!{Style.reset}\n")
sleep(1) # Set to 10 once complete

def chapter_1b():
    user_input = ""
    options = ["left", "right"]
    print("You are faced with 2 directions, left towards what looks like a store room or right towards the exit")
    while user_input not in options:
        print("'left' | 'right'")
        user_input = input().lower()
        if user_input == "left":
            print("You enter a small storeroom")
            sleep(1)
            print("You find a pistol, this will be useful! You pocket the gun")
            sleep(1)
            print("You find your driver's license, they must have taken it off you, you remember a bit about yourself")
            sleep(1)
            name = input("remember your name: ")
            sleep(1)
            print("thats right! my name is" + name +" and everybody calls me Malice!")
            sleep(1)
            print("Alright time to get out of this place!")
            pass #chapter_1c
        elif user_input == "right":
            print("You travel down a long corridor carefully")
            sleep(1)
            print("You turn a corner and see a solitary guard patrolling who hasn't seen you yet")
            sleep(1)
            user_input2 = ""
            options2 = ["go back", "fight guard"]
            print("There is still time to turn around or I could try and take him down...")
            while user_input2 not in options2:
                print("'go back' | 'fight guard'")
                user_input2 = input().lower()
                if user_input2 == "go back":
                    print("You quietly slink back the way you came")
                    sleep(1)
                    print("You arrive back at the entrance of your would be jail")
                    chapter_1b()
                elif user_input == "fight guard":
                    print("You stealthily start moving towards the guard")
                    sleep(1)
                    print("But he has reached the end of the corridor and begins to turn")
                    sleep(1)
                    print("You break into a run, but theres not enough time to cover the distance")
                    sleep(1)
                    print("The guard smirks at your attempted escape and raises a large gun towards you and fires")
                    sleep(1)
                    print(fontstyle.apply("YOU DIED", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG'))
                else:
                    print("I need to make a choice quickly!")
        else:
            print("I need to make a choice quickly!")

def chapter_1a():
    user_input = ""
    options = ["call out", "stay quiet"]
    print("Suddenly a voice calls out, 'Malice, are you in here?'")
    while user_input not in options:
        print("'call out' | 'stay quiet'")
        user_input = input().lower()
        if user_input == "call out":
            print("Hey I recognise that voice, 'Hey in here! you yell'")
            sleep(1)
            print("The door swings open, a confident and familiar looking woman stands in the doorway")
            sleep(1)
            print("'Mal, keep your voice down or Killjoy's goons will hear!'")
            sleep(1)
            print("'I managed to get the key to your chains, but you'll have to get out of here by yourself, I can't risk Killjoy finding me helping you, you understand'")
            sleep(1)
            print("The mysterious girl tosses you a key and you hastily start unshackling your cuffs. When you look up, she is already gone.")
            sleep(1)
            print("Alright, time to make for the exit")
            chapter_1b()
        elif user_input == "stay quiet":
            print("The voice is coming closer, I think they're going to find me!")
            sleep(1)
            print("The door swings open quietly revealing a beautiful woman who you feel you have seen before")
            sleep(1)
            print("'Hey Mal, don't feel like talking to your saviour? Guess what? I got the keys!'")
            sleep(1)
            print("'You'll have to find your own way out though, if Killjoy's men figure out what I've done they'll kill us both!'")
            sleep(1)
            print("The mysterious girl tosses you a key and you hastily start unshackling your cuffs. When you look up, she is already gone.")
            sleep(1)
            print("Alright, time to make for the exit I guess")
            chapter_1b()
        else:
            print("I need to make a choice quickly!")

def story_intro():
    user_input = ""
    options = ["open"]
    while user_input not in options:
        print("open your eyes")
        user_input = input().lower()
        if user_input == "action":
            print("Well done! Here is your Easter Egg '@'\n")
            sleep(2)
        elif user_input == "@":
            print("Very funny! Please can you start the game already?!\n")
            sleep(2)
        elif user_input == "open":
            print("You wake feeling dizzy with an aching in your head\n")
            sleep(1) # Set to 4 once complete
            print("The last thing you remember is coming for Killjoy\n")
            sleep(1) # Set to 4 once complete
            print("Thats right, Killjoy, the one who... wait who is Killjoy, and why was I after him?\n")
            sleep(1) # Set to 4 once complete
            print("You tracked him down to a warehouse, you think...\n")
            sleep(1) # Set to 4 once complete
            print("Thats the last thing you remember, something went wrong, why can't I remember?\n")
            sleep(1) # Set to 4 once complete
            print("My name. Whats my name?\n")
            sleep(1) # Set to 4 once complete
            print("Nothing, OK where am I? A dimly lit room...\n")
            sleep(1) # Set to 4 once complete
            print("The room is unfamiliar, and there are chains around your wrists\n")
            sleep(1) # Set to 4 once complete
            print("Your adventure begins\n")
            sleep(1) # Set to 4 once complete
            print("Welcome to...\n")
            sleep(1) # Set to 4 once complete
            print(fontstyle.apply("Malice in Chains", 'bold/Italic/red/INVERSE/UNDERLINE/WHITE_BG')) # Big exciting font
            sleep(4)
            chapter_1a()
        else:
            print("I guess I'll keep my eyes closed a little bit longer\n")
            sleep(2)



story_intro()

