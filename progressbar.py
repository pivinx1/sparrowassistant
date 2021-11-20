# ProgressCLI 95 by Setapdede
# Revision 0.2, created by BurningInfern0.
# This part of Sparrow is intellectual property of Setapdede.

# Imports
import random
from os import system, name
from time import sleep

def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

def progressbar():
    progressbar = 0
    progressbar2 = 0
    lives = 3
    score = 0
    # level = 1
    bar = []
    bardisplay = ""
    segments = ""
    while progressbar != 100:
        # clears the screen for next segment
        clear()

        # checks if lives are 0, breaks if true
        if lives == 0:
            print("You are out of lives. Game over!")
            break

        # randomly chooses a segment and displays its art
        seg = random.randint(0, 3)
        if seg == 0:
            seg_art = "╔══╗\n║  ║\n║  ║\n╚══╝"
        elif seg == 1:
            seg_art = "╔══╗\n║!!║\n║!!║\n╚══╝"
        elif seg == 2:
            seg_art = "╔══╗\n║--║\n║--║\n╚══╝"
        else:
            seg_art = "╔══╗\n║~~║\n║~~║\n╚══╝"
        print(seg_art)

        # checks if you have 1 life left
        if lives == 1:
            print("You have 1 life left. Be careful.")
        else:
            print("You have", lives, "lives left.")

        # checks if you have orange segments in your bar
        bardisplay = ""
        if progressbar2 > 0:
            for segments in bar:
                bardisplay = bardisplay + segments + ", "
            print("\nYour bar:", bardisplay, "\n")
            print("You have", progressbar, "% with", progressbar2, "% orange in your progressbar.")
        else:
            for segments in bar:
                bardisplay = bardisplay + segments + ", "
            print("\nYour bar:", bardisplay, "\n")
            print("You have", progressbar,"%", "in your progressbar.")

        # catches the currently displayed segment
        catch = input("Type 'C' to catch, any other key to move away, and 'Q' to quit.\n")

        # calculates which segment you caught and does stuff
        if seg == 0 and catch == "c":
            progressbar = progressbar + 5
            bar.append("Blue")
            score = score + 5
        elif seg == 1 and catch == "c":
            bar = []
            bardisplay = ""
            lives = lives - 1
            progressbar = 0
            progressbar2 = 0
            score = score - 10
        elif seg == 2 and catch == "c":
            if progressbar == 0:
                continue
            if bar[-1] == "Orange":
                progressbar2 = progressbar2 - 5
                progressbar = progressbar - 5
                bar.pop(-1)
                score = score + 5
            else:
                progressbar = progressbar - 5
                bar.pop(-1)
                score + score - 5
        elif seg == 3 and catch == "c":
            progressbar = progressbar + 5
            progressbar2 = progressbar2 + 5
            bar.append("Orange")

        if catch == "q":
            print('Game Over! Thanks for playing!')
            break

        if catch == "credits":
            clear()
            print('ProgressCLI95 0.2')
            print('Original code (0.1) by Setapdede')
            print('Improved code (0.2) by BurningInfern0')
            print('Made for use with Sparrow Assistant by pivinx1')
            print('\nPress ENTER to get back to the game.')
            input()

        # if you have 100% on your progressbar, the game will end.
        if progressbar == 100:
            if progressbar2 > 0:
                print('Bravo!')
            else:
                print('Perfect!')
            print('Good game! Your final score is:', score)
            break
        else:
            continue
