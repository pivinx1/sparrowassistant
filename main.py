# supposedly start here
import random
import datetime
from math import sqrt
from progressbar import progressbar
import calc
greetingID = random.randint(0, 4)
ordinal = lambda n: "%d%s"%(n,{1:"st",2:"nd",3:"rd"}.get(n if n<20 else n%10,"th"))
usercmd = input("\nPlease input how do you want to be called\n")
user = usercmd
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
    usercmd = input('\nWhat do you want me to do?\n')
    if usercmd == "What time it is?":
        time = datetime.datetime.now()
        print('It\'s ', time.strftime("%A %B "), ordinal(int(time.strftime("%-d"))), time.strftime(", %Y"),sep="")
    #this piece of code is written by leap of azzam since pivin sucks at this
    #yeah pretty much, thanks
    if usercmd == "Who am I?":
        print("\nYou're", user, "if I'm not mistaken. \n")
    elif usercmd == "Exit":
        print("\nBye", user,"!")
        quit()
    #Quick Menu
    elif usercmd == "Show the Quick Menu":
        print("\nQuick Menu\n")
        print("DOS")
        print("Progressbar95")
        print("Calculator")
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
        print("\nI see i've got a tech expert here :). I do not have a specific release version but you could say this is 'my first release'.")
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
      print("\nSorry", user, "but I'm sure I'm not Google's assistant.")
    elif usercmd == "Hey Siri!":
      print("\nI'm sure you're not Siri-ous.")
    #Invalid
    else:
        tryID = random.randint(0, 4)
        print("\nI didn't understand what you ment. Could you try rephrasing it?\n")
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
