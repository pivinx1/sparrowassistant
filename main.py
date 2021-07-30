# supposedly start here
import random
import datetime
from math import sqrt
from progressbar import progressbar
import calc
import os
from Choices import choices
greetingID = random.randint(0, 4)
ordinal = lambda n: "%d%s"%(n,{1:"st",2:"nd",3:"rd"}.get(n if n<20 else n%10,"th"))
usercmd = input("\nPlease input how do you want to be called\n")
user = usercmd
devmode = False
exit = 0
# Greet the user
if greetingID == 0:
    print("\n*nom nom nom* Hi!")
elif greetingID == 1:
    print("\nHello there,", user + "!")
elif greetingID == 2:
    print("\nHey there,", user + "!")
elif greetingID == 3:
    print("\nWelcome", user + "!")
else:
    print("\nHi,", user + "!")
# Command loop
while True: 
    if devmode != True:
        usercmd = input('\nWhat do you want me to do?\n') 
    else:
        usercmd = input('\nWhat do you want me to do?\nDevmode enabled, use command List developer actions to see what you can do\n')
        #if usercmd == "What time it is?":
        #time = datetime.datetime.now()
        #print("It\'s ", time.strftime("%A %B "), ordinal(int(time.strftime("%-d"))), time.strftime(", %Y"), sep=" ")
    #this piece of code is written by leap of azzam since pivin sucks at this
    #yeah pretty much, thanks
    #code in lines 27 and 28 seems to be broken boi
    #commented out so sparrow works perfectly
    if usercmd == "Who am I?":
        print("\nYou're", user, "if I'm not mistaken. \n")
    elif usercmd == "Exit":
        print("\nBye", user,"!")
        quit()
    #Useful
    elif usercmd == "Take notes":
      note = input("\nSure! What do you want me to note?\n")
      open("note.txt", "w").write(note)
      print("Noted.")
    elif usercmd == "Read my notes":
      with open("note.txt", "r") as notes:
        for line in notes:
          print("\nThese are your notes.\n")
          print(line.strip())
    elif usercmd == "Do I have any notes?":
      if os.path.exists("note.txt"):
        print("You have a note written down.")
        read = input("\nWould you like me to read it, delete, or continue?(r/d/c)")
        if read == "r":
          with open("note.txt", "r") as note:
            print("\nThese are your notes.\n")
            for line in note: 
              print(line.strip())
        elif read == "d":
          os.remove("note.txt")
          print("I have fed your Bin with your notes.")
        else:
          continue
      else:
        print("\nYou don't have any notes.\n")
        writedown = input("\nWould you like me to write something down for you or no?(y/n)\n")
        if writedown == "y":
          note = input("\nOkay. What do you want me to note?\n")
          open("note.txt", "w").write(note)
          print("Noted.")
    #Quick Menu
    elif usercmd == "Show the Quick Menu":
        print("\nQuick Menu\n")
        print("DOS")
        print("Progressbar95")
        print("Calculator")
        print("Choices")
        usercmd = input("Return to Sparrow\n")
        if usercmd == "Return to Sparrow":
          print("Returned")
        if usercmd == "DOS":
          exit = 0
          print("\nDOS for Sparrow Assistant\n")
          while exit == 0:
           DOS = input(">")
           if DOS == "exit":
            exit = 1;
        if usercmd == "Progressbar95":
         progressbar()
        elif usercmd == "Calculator":
          #Do the math based on type of operation
          base = int(input("\nType in the first number:\n"))
          additive = int(input("\nType in the second number:\n"))
          operation = input("\nType in the type of the operation (square, power, add, subtract, multiply, divide)\n")
          if operation == "add":
            equality = base + additive
            print(equality)
          elif operation == "substract":
            equality = base - additive
            print(equality)
          elif operation == "multiply":
            equality = base * additive
            print(equality)
          elif operation == "divide":
            equality = base / additive
            print(equality)
          elif operation == "power":
            equality = base ^ additive
            print(equality)
          elif operation == "square":
            #Square root to-do: first ask for operation, omit additive if is square root
            equality = sqrt(base)
            print(equality)
          else:
            print("Invalid operation")
        elif usercmd == "Choices":
            choices()
    #Quick Menu
    elif usercmd == "Show the Quick Menu":
        print("\nQuick Menu\n")
        usercmd = input("Return to Sparrow\n")
        if usercmd == "Return to Sparrow":
          print("Returned")
    #About
    elif usercmd == "Who created you?":
        print("\nI was originaly built by pivinx1, with contributions from setapdede and Leap of Azzam.")
    elif usercmd == "What is your version?":
        print("\nYou're running Sparrow version 0.1.1.")
    elif usercmd == "Who are you?":
      print("I am an narrow reactive AI codenamed Sparrow, developed by pivinx1, with contributions from setapdede and Leap of Azzam.")
      print("You can call me Sofia though.")
    #Settings
    elif usercmd == "Change my name":
        while usercmd == "Change my name":
         usercmd = input("\nPlease input how do you want to be called\n")
         user = usercmd
    #Jokes
    elif usercmd == "Hey Cortana!":
      print("\nHaha! It surely was funny but I'm not Cortana.")
    elif usercmd == "Ok Google":
      print("\nSorry ", user, ", but I'm sure I'm not Google's assistant.",sep="")
    elif usercmd == "Hey Siri!":
      print("\nI'm sure you're not Siri-ous.")
    #Dev tools
    elif usercmd == "Enter developer mode":
        passwd = "fuckingpassword"
        passwd_input = input("Fine. What's the password? If you get it correct, I will let you in.\n")
        if passwd_input != passwd:
            print("Wrong password.")
        else:
            print("You got in. Great. Type in \"List developer actions\" to see what you can do in the developer mode.\n")
            devmode = True
    elif usercmd == "List developer actions":
        print("List variables - Lists all available variables.")
        print("Change dev mode password - Changes your dev mode password (VOLATILE)")
        print("Disable developer mode - Disables dev mode")
    elif usercmd == "List variables" and devmode == True:

        print("greetingID = " + str(greetingID))
        print("user = " + user)
        print("devmode = " + str(devmode))
    elif usercmd == "Change dev mode password" and devmode == True:
        passwd = input("Okay. What is the dev mode password that you want to have?\nRemember that it is volatile, meaning that it will not save when leaving this program.")
        print("Done.")
    elif usercmd == "List variables" or usercmd == "Change dev mode password" and devmode == False:
        print("You can't do this while the dev mode is disabled.")
    elif usercmd == "Disable developer mode" and devmode == False:
        print("The developer mode is already disabled.")
    #Invalid
    else:
        tryID = random.randint(0, 4)
        print("\nI didn't understand what you meant. Could you try rephrasing it?\n")
        if tryID == 0:
          print("(Try 'Who am I?'')")
        if tryID == 1:
          print("(Try 'Who created you?'')")
        if tryID == 2:
          print("(Try 'Hey Cortana!')")
        if tryID == 3:
          print("(Try 'Ok Google')")
        if tryID == 4:
          print("(Try 'What is your version?')")
