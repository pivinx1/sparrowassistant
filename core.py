# Project Sparrow
# CopyLEFT pivinx1 2021-2022
# How modular it can get? Let's find out!
# Go on, break my muppet.
# This bad boy, or girl, is supposed to be extremely modular. Expect this to be FILLED with module calls.
import userwrapper as user
from modules import notes
from progresscli.boot import remoteBoot

username = user.userwrapper()
user.greet(username)

while True:
    # Off to making a huge disaster of an if-elif chain. Now split into menus.
    command = input(">")
    if command == "Menu":
        print("Menu\nRetype the menu entry name to the prompt to run the command.\n1. Notepad\n2. ProgressCLI 95")
    elif command == "Notepad":
        print("Notepad\nRetype menu entry name to run the command.\n1. Add new line to note\n2. Delete note\n3. Read note\n4. Exit")
        noteCommand = input(">")
        if noteCommand == "Add new line to note":
            noteText = input("Type in what do you want to note.\n")
            notes.takeNote(noteText)
        elif noteCommand == "Delete note":
            notes.rmNote()
        elif noteCommand == "Read note":
            notes.readNote()
        elif noteCommand == "Exit":
            continue
        else:
            print("No such command")
    elif command == "ProgressCLI 95":
        remoteBoot()