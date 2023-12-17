from colored import Fore, Back, Style
import fontstyle
from time import sleep
from computational_stopwatch import Stopwatch



def outro_1():
    global sw
    from main import sw
    from chapter_1b import fname
    print(f"{Fore.black}{Back.white}Well well well, Killjoy is dead! We have revenge at last, but at what cost? The girl who helped you escape died for her troubles, no thanks to us, thats on our conscience now, and the wounds we sustained may claim us yet. Time will tell if we will heal. Thanks for playing Malice in Chains!")
    print(f"Well done {fname} you completed the game in {sw}. Why don't you see if you can improve on that time next time!{Style.reset}")
    print("'exit' | 'start over'")
    if input().lower() == "start over":
        from main import story_intro
        story_intro()
    else:
        exit()

def outro_2():
    global sw
    from main import sw
    from chapter_1b import fname
    print(f"{Fore.black}{Back.white}Well well well, Killjoy is dead! We have revenge at last and we managed to save the girl whoever she is! Hopefully she can fill in a few blanks for us on the story. You managed to achieve the best ending, good on you! Thanks for playing Malice in Chains!")
    print(f"Well done {fname} you completed the game in {sw}. Why don't you see if you can improve on that time next time!{Style.reset}")
    print("'exit' | 'start over'")
    if input().lower() == "start over":
        from main import story_intro
        story_intro()
    else:
        exit()