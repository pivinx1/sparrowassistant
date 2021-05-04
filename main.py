# supposedly start here
import random
import getpass
import datetime
greetingID = random.randint(0, 4)
usercmd = input("\nPlease input how do you want to be called\n")
user = usercmd
exit = 0
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
    if usercmd == "Who am I?":
        print("\nYou're", user, "if I'm not mistaken. \n")
    elif usercmd == "Exit":
        print("\nBye", user,"!")
        break
    #Quick Menu
    elif usercmd == "Show the Quick Menu":
        print("\nQuick Menu\n")
        print("DOS")
        print("Progressbar95")
        usercmd = input("Return to Sparrow\n")
        if usercmd == "Return to Sparrow":
          print("Returned")
        if usercmd == "DOS":
          exit = 0
          print("\nDOS for Sparrow Assistant SD\n")
          while exit == 0:
           DOS = input(">")
           if DOS == "exit":
            exit = 1;
        if usercmd == "Progressbar95":
          progressbar = 0
          while progressbar < 101:
           segment = random.randint(0, 1)
           progressbar2 = progressbar
           if (progressbar == 100):
             print("Congrats you won!")
             progressbar == 102
           if (segment == 0):
             print("\nBlue")
           if (segment == 1):
             print("\nRed")
           print("Progressbar is", progressbar,"% filled")
           pb95 = input("\ntype c to catch the segment or type anything to avoid it\n")
           if (pb95 == "c"):
             if (segment == 0):
               if (progressbar == 0):
                 progressbar = 5
               elif (progressbar == 5):
                 progressbar = 10
               elif (progressbar == 10):
                 progressbar = 15
               elif (progressbar == 15):
                 progressbar = 20
               elif (progressbar == 20):
                 progressbar = 25
               elif (progressbar == 25):
                 progressbar = 30
               elif (progressbar == 30):
                 progressbar = 35
               elif (progressbar == 35):
                 progressbar = 40
               elif (progressbar == 40):
                 progressbar = 45
               elif (progressbar == 45):
                 progressbar = 50
               elif (progressbar == 50):
                 progressbar = 55
               elif (progressbar == 55):
                 progressbar = 60
               elif (progressbar == 60):
                 progressbar = 65
               elif (progressbar == 65):
                 progressbar = 70
               elif (progressbar == 70):
                 progressbar = 75
               elif (progressbar == 75):
                 progressbar = 80
               elif (progressbar == 80):
                 progressbar = 85
               elif (progressbar == 85):
                 progressbar = 90
               elif (progressbar == 90):
                 progressbar = 95
               elif (progressbar == 95):
                 progressbar = 100
             if (segment == 1):
              progressbar = 0
             
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