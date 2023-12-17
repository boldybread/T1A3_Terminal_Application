from colored import Fore, Back, Style
import fontstyle
from time import sleep
from names_generator import generate_name
from main import wait_duration
import random

random_name = ""
random_number = random.randint(1, 100)
guesses = 10
age = random.randint(60,110) # random number between 60 and 110
age_minus_1 = age - 1

def guess_correctly():
    sleep(wait_duration)
    print("'Alright I've played your game, now tell me where are we!?'")
    sleep(wait_duration)
    print(f"Before {random_name} can answer another voice breaks your concentration, a girls voice.")
    sleep(wait_duration)
    print("You look towards the solitary door of your makeshift cell in anticipation")
    sleep(wait_duration)
    print((f"You turn back to {random_name} but there is no one there! No chains, no cards, nothing. Is your mind playing tricks on you?"))
    sleep(wait_duration)
    from chapter_1a import chapter_1a
    chapter_1a()


def random_encounter():
    global random_name
    generate_name = random_name
    suits = {"Spades","Hearts","Clubs","Diamonds"}
    value = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"}
    print("You look around your cell, there is one other person who seems oblivious to you also chained up to a different wall")
    sleep(wait_duration)
    print("The elderly man is energetic despite his detainment and advanced years you see him frantically shuffling a deck of cards")
    sleep(wait_duration)
    print("'Hey you! Where are we?' You enquire. The man looks up startled, then draws a card from his deck.")
    sleep(wait_duration)
    print(f"He shows you the {value} of {suits} and says 'is this your card?' Then laughs maniacally before muttering something to himself")
    sleep(wait_duration)
    print(f"'My name is {random_name} and I am a spritely {age} although you probably thought that I wasn't a day older than {age_minus_1}.' He cackles to himself.")
    sleep(wait_duration)
    print("You go to say your name and realise you can't remember it. Who can't even remember there own name?!")
    sleep(wait_duration)
    print(f"'Fancy a game?' {random_name} asks, 'I tell you what if you can guess the number I am thinking of I will answer all your questions, whaddya say?'")
    sleep(wait_duration)
    print("'I will give you ten guesses to guess my number that is between 1 and 100, every time you guess wrong I will tell you if my number is higher or lower'")
    sleep(wait_duration)
    number_guess = int(input("Guess a number between 1 and 100: "))
    if guesses >= 1:
        if number_guess < random_number:
            guesses -= 1
            print(f"My number is higher, you have {guesses} guesses left!")
        elif number_guess > random_number:
            guesses -= 1
            print(f"My number is lower, you have {guesses} guesses left!")
        elif number_guess == random_number:
            print(f"Yes thats it! You guessed that my number was {random_number} in {guesses} guesses!")
            guess_correctly()
        else:
            print(f"Enter a number! You have {guesses} guesses left!")
    else:
        print(f"Ah you were so close but you've run out of guesses! My number was {random_number}")
        sleep(wait_duration)
        print("Another voice breaks your concentration, a girls voice.")
        sleep(wait_duration)
        print(f"You turn back to {random_name} but he isn't there. There is no chains, no cards, nothing there at all. Is your mind playing tricks on you?")
        sleep(wait_duration)
        from chapter_1a import chapter_1a
        chapter_1a()

random_encounter()