import random
def progressbar():
    progressbar = 0
    while progressbar != 100:
        seg = random.randint(0, 1)
        if seg == 0:
            seg_name = "blue"
        else:
            seg_name = "red"
        print("The segment falling is the", seg_name, "segment")
        print("You have", progressbar, "%", "in your progressbar.")
        catch = input("Type in c to catch, anything else to shy away\n")
        if seg == 0 and catch == "c":
            progressbar = progressbar + 5
        elif seg == 1 and catch == "c":
            progressbar = 0
        else:
            continue