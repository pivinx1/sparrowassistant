import random
def progressbar():
    progressbar = 0
    while progressbar < 96:
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
            if progressbar == 100:
                break