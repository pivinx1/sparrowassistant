# Userwrapper
# Effectively does things like pull username.
import time


def userwrapper():
    print("Sparrow Assistant version 0.2.0 - Under Construction")
    username = input("Username:")
    # You shouldn't expect more from this.
    return username
def greet(username):
    datetime = time.time()
    current_time = time.ctime(datetime)
    print("Welcome,", username + ". The time is", current_time + ".")
    print("Warning: Sparrow is in it's early stages of development. Except things to change a lot.")
    print("To see a list of currently available features, type \"Menu\" into the prompt.")