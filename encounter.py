from colored import Fore, Back, Style
import fontstyle
from time import sleep
import names

import random

random_name = names.get_first_name(gender='male')

random_number = random.randint(1, 100)
age = random.randint(60,110) # random number between 60 and 110
age_minus_1 = age - 1
guesses = 10

def guess_correctly():
    from main import wait_duration
    print("'Alright I've played your game, now tell me where are we!?'")
    sleep(wait_duration)
    print(f"Before {random_name} can answer another voice breaks your concentration, a girl's voice.")
    sleep(wait_duration)
    print("You look towards the solitary door of your makeshift cell in anticipation")
    sleep(wait_duration)
    print((f"You turn back to {random_name} but there is no one there! No chains, no cards, nothing. Is your mind playing tricks on you?"))
    sleep(wait_duration)
    from chapt_1a import chapter_1a
    chapter_1a()


def random_encounter():
    from main import wait_duration
    global random_name
    suits = ("Spades","Hearts","Clubs","Diamonds")
    value = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
    print("You look around your cell, there is one other person who seems oblivious to you also chained up to a different wall")
    sleep(wait_duration)
    print("Something seems off about the elderly man. Despite his detainment and advanced years you see him frantically shuffling a deck of cards.")
    sleep(wait_duration)
    print("'Hey Mister, where are we?' You enquire. The man looks up startled, then back to his deck. Then suddenly he draws a card waving it around like a magician.")
    sleep(wait_duration)
    print(f"He shows you the {random.choice(value)} of {random.choice(suits)} and says 'tell me, is this your card?' Then laughs maniacally before muttering something to himself.")
    sleep(wait_duration)
    print(f"'My name is {random_name} and I am a spritely {age} years old although everyone always thinks I'm only {age_minus_1}.' He cackles to himself.")
    sleep(wait_duration)
    print(f"You go to say your name and realise you can't remember it. Who can't even remember their own name?! 'Do you know where we are {random_name}?'")
    sleep(wait_duration)
    print(f"'Hey! Tell ya what, fancy a game?' {random_name} asks, 'If you can guess the number I am thinking of I will answer all your questions, whaddya say?'")
    sleep(wait_duration)
    print("'You can have ten attempts to guess my number, I will pick a number between 1 and 100, I will tell you each time if my number is higher or lower'")
    sleep(wait_duration)
    print("'Whaddya say? I will even tell you what happened to you'")
    sleep(wait_duration)
    print("I suppose I have to play, you think to yourself.")
    number_guess_game()

def number_guess_game():
    from main import wait_duration
    global guesses
    while True:
        if guesses >= 1:
            try:
                number_guess = int(input("Guess a number between 1 and 100: "))
                if number_guess < random_number:
                    guesses -= 1
                    print(f"My number is higher, you have {guesses} guesses left!")
                    sleep(2)
                elif number_guess > random_number:
                    guesses -= 1
                    print(f"My number is lower, you have {guesses} guesses left!")
                    sleep(2)
                elif number_guess == random_number:
                    print(f"Yes thats it! You guessed that my number was {random_number} and you still had {guesses} guesses left!")
                    sleep(2)
                    guess_correctly()
                else:
                    print(f"Enter a number! You have {guesses} guesses left!")
            except ValueError:
                print("ValueError - Input needs to be a number!!")
                continue
        else:
            print(f"Ah you were so close but you've run out of guesses! My number was {random_number}")
            sleep(wait_duration)
            print("Another voice breaks your concentration, a girl's voice.")
            sleep(wait_duration)
            print(f"You turn back to {random_name} but he isn't there. There are no chains, no cards, nothing there at all. Is your mind playing tricks on you?")
            sleep(wait_duration)
            from chapt_1a import chapter_1a
            chapter_1a()

