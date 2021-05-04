# supposedly start here
import random
import getpass
import datetime
user = getpass.getuser()
greetingID = random.randint(0, 3)
print("DEBUG: ", greetingID)
# Greet the user
if greetingID == 0:
    print("*nom nom nom* Hi!")
elif greetingID == 1:
    print("Hello there,", user + "!")
elif greetingID == 2:
    print("Hey there,", user + "!")
else:
    print("Hi,", user + "!")
# Command loop
while True:
    usercmd = input('What do you want me to do?')
    #if usercmd == "What time it is?":
        #time = datetime.datetime.now()
        #print('It\'s', time)
    if usercmd == "Who am I?":
        print("You're", user, "if I'm not mistaken.")
    if usercmd == "Exit":
        print("Bye", user,"!")
        break