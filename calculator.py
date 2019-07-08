import math  
def standard_calc():
    operator = raw_input()
    if operator.upper() == "A":
        print x + y 
    elif operator.upper() == "S":
        print x - y 
    elif operator.upper() == "D":
        # if x == 0 or y == 0:
        #     print "ERROR 00: Rhys likes eggs and bugs but not computers"
        # else:
            print "%.2f" %(x / y) 
    elif operator.upper() == "M":
        print x * y 
    else:
        print "Incorrect Operator"

print "Welcome to Calculator 101"
name = raw_input("What is you're name? ")
print "Thank you" , name ,", let's get cracking!"
        
Restart = True
while Restart == True:
    option = raw_input("Would you like a Standard Calculator or Advanced? [S] or [A] ")

    if option.upper() == "S":
        x = float(input ("First Integar: "))
        y = float(input ("Second Integar: "))
        print "What would you like to do with these two numbers", name,"?"
        print "Type [A] to add, [S] to subtract, [D] to divide, [M] to multiply"
        
        try:
            standard_calc()
        except:
            print "Error 00: Cannot Calculate Total"

        Replay = raw_input("Would you like to start again? Y / N: ")
        if Replay.upper() == "N":
            Restart = False
        elif Replay.upper() == "Y":
            Restart = True

    elif option.upper() == "A":
        print "Type [R] to Square Root Or [P] to measure the Power of a Value"
        operator = raw_input()

        if operator.upper() == "R":
            x = float(input ("Square Root of: "))
            print math.sqrt(x)
            
        elif operator.upper() == "P":
            x = float(input ("First Integar: "))
            y = float(input ("To the Power of: "))
            powr = pow(x, y)

            print powr 

        Replay = raw_input("Would you like to start again? Y / N: ")
        if Replay.upper() == "N":
            Restart = False
        elif Replay.upper() == "Y":
            Restart = True
else:
    print "Goodbye"

