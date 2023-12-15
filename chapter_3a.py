from colored import Fore, Back, Style
import fontstyle
from time import sleep

injured = False

def chapter_3a():
    global injured
    user_input = ""
    print("You arrive at the club, 'Wonderland'")
    print("A popular nightspot in the city, yet the outside now is deserted")
    options = ["guns", "leave"]
    print("You make your way inside, past the foyer you can see at least 5 of Killjoy's goons.")
    print("Odds are against you, but you don't mind that, could go in guns blazing take as many of them down with you as you can. Or its not too late to leave either.")
    while user_input not in options:
            print("'guns' | 'leave'")
            user_input = input().lower()
            if user_input == "guns":
                print("You check your rifle one last time and settle into the best vantage point you can")
                sleep(4)
                print("You start firing in controlled bursts")
                sleep(4)
                print("The element of surprise helps you take out a few goons before they start firing back")
                sleep(4)
                print("You move to a new piece of cover and keep firing")
                sleep(4)
                print("You take a few more rounds yourself before the last goon falls")
                print(f"{Fore.green}INJURED{Style.reset}")
                injured = True
                sleep(4)
                print("Killjoy bursts through a door in the back dual pistols in hand and starts firing")
                sleep(4)
                print("You groan throwing the empty rifle and pull out your pistol")
                sleep(4)
                from chapter_3b import no_bar
                no_bar()
            elif user_input == "leave":
                from chapter_3b import leave
                leave()
            else:
                print("I need to make a choice quickly!")
    

