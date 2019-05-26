"""

"""

import random
from time import sleep
from os import system, name


# Dictionary of moves
moves = {"rock": "Rock",
         "paper": "Paper",
         "scissors": "Scissors",
         "dynamite": "Dynamite"}


# Computer chooses move
def computer_choice():
    pick = random.choice(list(moves.keys()))
    while pick == "dynamite":
        pick = random.choice(list(moves.keys()))
    c_move = moves[pick]
    return c_move


# Player chooses move
def player_choice():
    while True:
        print()
        print("Make your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        choice = input(">> ")
        clear()

        if choice == "1":
            p_move = moves["rock"]
        elif choice == "2":
            p_move = moves["paper"]
        elif choice == "3":
            p_move = moves["scissors"]
        elif choice == "4":
            finish()
        elif choice.lower() == "boom" or choice == "5":
            p_move = moves["dynamite"]
        else:
            print("\nNot a valid move.\n")
            continue

        return p_move


def throwdown():
    # Reads as "x beats y"
    options = {"Rock": ("Scissors", "bashes"),
               "Paper": ("Rock", "covers"),
               "Scissors": ("Paper", "cuts"),
               "Dynamite": (["Rock", "Paper", "Scissors"], "blows up")}

    c_score = 0
    p_score = 0

    while True:
        clear()
        c = computer_choice()
        p = player_choice()

        print("\n\n\n")
        print("**READY!**".center(40))
        sleep(1.5)
        clear()
        print()
        print("*thwop!*".center(20))
        sleep(.3)
        print("*thwop!*".center(20))
        sleep(.3)
        print("\nPlayer throws {}!".format(p))
        print("Computer throws {}!".format(c))
        sleep(1.5)

        if c == p:
            if c and p == "Scissors":
                print("\n;)")
            print("\nTie game! Restarting...\n")
            sleep(2)
            continue
        elif p in options[c]:
            # Computer wins
            print("\n{} {} {}!!  CPU scores a point.".format(c, options[c][1], p))
            c_score += 1
        else:
            # Player wins
            if p == "Dynamite":
                print("\n**BOOM!**")
                print("\n{} {} {}!".format(p, options[p][1], c))
                p_score += 100
            else:
                print("\n{} {} {}!! Player scores a point.".format(p, options[p][1], c))
                p_score += 1

        print("\nPlayer: {} | CPU: {}\n".format(p_score, c_score))
        sleep(2)

        print("\nPlay again? Y/N")
        choice = input(">> ")
        if choice.lower() == "n":
            finish()
        elif choice.lower() == "y":
            continue
        else:
            print("I'll take that as a yes...")
            sleep(2)
            continue


def insult():
    # Dict of insults
    insults = {"1": "Quitter...",
               "2": "Had enough, eh?",
               "3": "Run home to mama!",
               "4": "Too scared to play?",
               "5": "*bwaAAAAK!*",
               "6": "Fine. Run away.",
               "7": "Your mother was a hamster, and your father smells of elderberries!",
               "8": "I fart in your general direction!"}

    haha = random.choice(list(insults.keys()))
    sleep(1)
    print("\n" + insults[haha])


def finish():
    clear()
    insult()
    quit()


def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


def welcome():
    clear()
    print("Welcome to Rock, Paper, Scissors!\n".center(45))
    sleep(3)
    print("\n	The rules are simple:")
    sleep(2.5)
    print("\n	Rock beats Scissors...")
    sleep(1.5)
    print("	 Paper beats Rock...")
    sleep(1.5)
    print("	  Scissors beats Paper...")
    sleep(2)
    input("\n\n\n\nPress Enter to play.")
    throwdown()


if __name__ == "__main__":
    system("mode con cols=45 lines=15")
    welcome()
    quit()
