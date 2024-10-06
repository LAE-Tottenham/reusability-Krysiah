import math 

def hypotenuse():
    checktrue = True
    while checktrue == True:
        try:   
            opposite = float(input("Enter the triangle's opposite side length:"))
            adjacent = float(input("Enter the triangle's adjacent side length:"))
            hyp = math.sqrt(opposite**2 + adjacent**2)
            checktrue == False
            return hyp
        except ValueError:
            print("Enter a valid number")

def SOH():
    checktrue = True
    while checktrue == True:
        try:
            opposite = float(input("Enter the triangle's opposite side length:"))
            hypotenuse = float(input("Enter the triangle's hypotenuse side length:"))
            sin = opposite // hypotenuse
            checktrue == False
            return sin
        except ValueError:
            print("Enter a valid number")

def CAH():
    checktrue = True
    while checktrue == True:
        try:
            adjacent = float(input("Enter the triangle's adjacent side length:"))
            hypotenuse = float(input("Enter the triangle's hypotenuse side length:"))
            cos = adjacent // hypotenuse
            checktrue == False
            return cos
        except ValueError:
            print("Enter a valid number")

def TOA():
    checktrue = True
    while checktrue == True:
        try:
            opposite = float(input("Enter the triangle's opposite side length:"))
            adjacent = float(input("Enter the triangle's adjacent side length:"))
            toa = opposite // adjacent
            checktrue == False
            return toa
        except ValueError:
            print("Enter a valid number")
    