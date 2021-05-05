#From Pivin: leave this file unused until I figure out how to invoke this function, it worked with PB95
from math import sqrt
def calc():
    #Do the math based on type of operation
    base = int(input("Type in the first number:\n"))
    additive = int(input("Type in the second number:\n"))
    operation = input("Type in the type of the operation (square, power, add, subtract, multiply, divide)\n")
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