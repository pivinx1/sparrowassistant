# To-do: make a delete note and read note function, unless you wanna do these two things by yourself, then there is nothing stopping ya :v
def takeNote(text):
    note = open("note.snf", "a")
    note.write(text)
    note.close()