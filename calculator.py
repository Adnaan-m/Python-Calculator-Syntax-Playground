import math  

def standard_calc():
    operator = raw_input()
    if operator.upper() == "A":
        print x + y 
    elif operator.upper() == "S":
        print x - y 
    elif operator.upper() == "D":
        try:
            print "%.2f" %(x / y)
        except ZeroDivisionError:
            print "Error 00: Cannot Divide by Zero"
        else:
            print "%.2f" %(x / y)
    elif operator.upper() == "M":
        print x * y 
    else:
        print "Incorrect Operator"

print "Welcome to Calculator 101"
name = raw_input("What is your name? ")
print "Thank you" , name ,", let's get cracking!"
        
Restart = True
while Restart == True:
    option = raw_input("Standard / Advanced / Circle? [S] or [A] or [C]")

    # Standard - Add, Sub, Mul, Div
    if option.upper() == "S":
        x = float(input ("First Integar: "))
        y = float(input ("Second Integar: "))
        print "What would you like to do with these two numbers", name,"?"
        print "[A] to Add"
        print "[S] to Subtract"
        print "[D] to Divide"
        print "[M] to Multiply"

        standard_calc()

    # Advanced - Power + Square Root
    elif option.upper() == "A":
        print "[R] to Square Root"
        print "[P] for Power of a Value"
        operator = raw_input()
        # Square Root
        if operator.upper() == "R":
            x = float(input ("Square Root of: "))
            print math.sqrt(x)
        # Power
        elif operator.upper() == "P":
            x = float(input ("First Integar: "))
            y = float(input ("To the Power of: "))
            powr = pow(x, y)

            print powr 


    # Circle
    elif option.upper() == "C":
        print "[C] for Circumference"
        print "[A] for Area"
        circle_option = raw_input("")
        # Circumference
        if circle_option.upper() == "C":
            print "Do you have the Radius or Diameter of the circle?"
            length_option = raw_input("R / D : ")
            if length_option.upper() == "R":
                radius = float(input("Radius Length : "))
                print math.pi*(radius * 2)
            elif ength_option.upper() == "D":
                diameter = float(input("Diameter Length : "))
                print math.pi*(diameter)
        # AREA
        elif circle_option.upper() == "A":
            print "Do you have the Radius or Diameter of the circle?"
            length_option = raw_input("R / D : ")
            if length_option.upper() == "R":
                radius = float(input("Radius Length : "))
                print math.pi*(radius * radius)
            elif length_option.upper() == "D":
                diameter = float(input("Diameter Length : "))
                diam_area = diameter/2
                print math.pi*(math.pow(diam_area,2))

    Replay = raw_input("Would you like to start again? Y / N: ")
    if Replay.upper() == "N":
        Restart = False
    elif Replay.upper() == "Y":
        Restart = True
else:
    print "Goodbye"