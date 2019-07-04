# while print exit is not true, do below 
# else exit


print "Welcome to Calculator 101"
name = raw_input("What is you're name?")
print "Thank you" , name ,", let's get cracking!"



###########################################
x = float(input ("Type the first Integar"))
y = float(input ("Type the Second Integar"))
print "What would you like to do with these two number?"
print "Type [A] to add, [S] to subtract, [D] to divide, [M] to multiply"

operator = raw_input()


if operator.upper() == "A":
    print x + y 
elif operator.upper() == "S":
    print x - y 
elif operator.upper() == "D":
    print "%.2f" %(x / y) 
elif operator.upper() == "M":
    print x * y 
else:
    print "Incorrect Operator"
###########################################        