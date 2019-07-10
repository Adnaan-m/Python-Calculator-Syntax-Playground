# Python-Calculator-Syntax-Playground

## Introduction
The creation of a simplistic Calculator with interaction through the terminal. The following ReadME displays the use of a variety of Python commands to help create this. 



## Simple Commands
>**Run script** -  ```python <App Name>```
>
>**Display in Terminal Command** - ```print "Welcome ", <variable>```
>
>**User Interaction:** 
>>Literal Raw Data - ```raw_input()```
>>
>>Mostly Integar inputs - ```input()```
>>>Define the type of character input (float,int etc.) - ```float(input ("Question: "))```

##Import Modules
At the top of the script (best practice), Insert:
>**```import <module name>```**

Note: No colon is required!!

## Functions

**Syntax:** 

>def function_name():

**To Call a Function:**
>function_name()

##Try / Exceptions
Python applications throw an error and exit immediately if an error occurs. To avoid this, a try/exception can be implemented to prevent applications from exiting. The following code is implemented within the calculator function to prevent error in dividing from 0. 

The Application first tries to print x/y to two decimal points. . . If x or y is 0, an error is thrown. Rather than the application crashing, an Exception catches the error, relays an error and carries on with the rest of the code.

```python
try:
	print "%.2f" %(x / y)
except ZeroDivisionError:
	print "Error 00: Cannot Divide by Zero"
else:
	print "%.2f" %(x / y)
```
## IF Statements

Syntax: 

```pythonß
if <statement> :
	<Do something>
elif <statement> :
	<Do something>
else:
	<Do something>
``` 

Example: 

```python
if x <= 5:
	print "x is", x
elif x >= 7:
	print "x is", x
else:
	print "x is 6"
``` 
## Loops
### While Loops
Syntax: 

```python
while Restart == True:
	<do stuff>
	<bare in mind indentation>
else:
	<do something else>
```

## General Notes
- **Indentation is KEY 🔑.** No parenthesis are used for functions, if statements + loops etc. So the program won't function without correct indentation.
- AND / OR is used as operators, '&& / ||' do not work.
- Variables are specified as literally just the variable name with potential comma for seperation. No requirement for dollar signs or parenthesis. 

> i.e. ```print "Name:",name```      **Not**         ~~print "Name:" ${name}~~



