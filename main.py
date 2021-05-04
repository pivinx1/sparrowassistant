# supposedly start here
import random
import datetime
greetingID = random.randint(0, 4)
usercmd = input("\nPlease input how do you want to be called\n")
user = usercmd
# Greet the user
print("\nDEBUG_GREET: ", greetingID)
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
    #if usercmd == "What time it is?":
        #time = datetime.datetime.now()
        #print('It\'s', time)
    #this piece of code is unused because pivin sucks at this
    if usercmd == "Who am I?":
        print("\nYou're", user, "if I'm not mistaken. \n")
    elif usercmd == "Exit":
        print("\nBye", user,"!")
        break
    #Quick Menu
    elif usercmd == "Show the Quick Menu":
        print("\nQuick Menu\n")
        usercmd = input("Return to Sparrow\n")
        if usercmd == "Return to Sparrow":
          print("Returned")
    #About
    elif usercmd == "Who created you?":
        print("\nI was originaly built by pivinx1, but this fork is made by my master setapdede.")
    elif usercmd == "What is your version?":
        print("\nI see i've got a tech expert here :). I do not have a specific release version but you could say this is 'my first release'.")
    #Settings
    elif usercmd == "Change my name":
        while usercmd == "Change my name":
         usercmd = input("\nPlease input how do you want to be called\n")
         user = usercmd
    #Jokes
    elif usercmd == "Hey Cortana!":
        print("\nHaha! It surely was funny but I'm not Cortana.")
    elif usercmd == "Ok Google":
        print("\nSorry", user, "but I'm sure I'm not Google's assistant.")
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
