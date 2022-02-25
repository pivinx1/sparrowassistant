import os
# The syntax highlighting got a little bit weird. Send help.
def takeNote(text):
    # Open the note file (or make a new one); then append data passed through the text variable to the note.
    note = open("note.snf", "a")
    if(os.path.getsize("note.snf") > 0):
        note.write("\n" + text)
    else:
        note.write(text)
    note.close()
def rmNote():
    if os.path.exists("note.snf"):
        os.remove("note.snf")
        print("Done.")
    else:
        print("I couldn't delete your note, because there isn't one.")
def readNote():
    note = open("note.snf", "r")
    print(note.read())
    note.close()