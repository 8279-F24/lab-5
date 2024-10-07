def displayInstructions():
    print("Hello there")
    print("This amazing piece of python code")
    print("Converts Fahrenheit to Celsius")
    return

def FahrToCel(Temperature):
    Celsius = 5/9*(Temperature-32)
    return Celsius

def validateFloat():
    while True:
        try:
            f = float(input("Value in Fahrenheit as a float? >"))
            break
        except ValueError:
            print("This is not a float")
    return f


displayInstructions()
F = validateFloat()
C = FahrToCel(F)
print("{} F = {} C".format(F,C))




