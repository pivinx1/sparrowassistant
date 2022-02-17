
def takeNote(text):
    note = open("note.snf", "a")
    note.write(text)
    note.close()