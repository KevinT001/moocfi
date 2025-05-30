#prompt 1
# Let's create a program along the lines of the example above. This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". Then the program should print out "okay then" and finish. Please have a look at the example below.

# Sample output
# hi
# Shall we continue? yes
# hi
# Shall we continue? oui
# hi
# Shall we continue? jawohl
# hi
# Shall we continue? no
# okay then

#solution
print("hi")
while True:

    hello = input("Shall we continue?")
    if hello == "no":
        break 
    print("hi")
    
print("okay then")

#prompt 2 

# Please write a program which asks the user for integer numbers.

# If the number is below zero, the program should print out the message "Invalid number".

# If the number is above zero, the program should print out the square root of the number using the Python sqrt function.

# In either case, the program should then ask for another number.

# If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

# Below you'll find a reminder of how the sqrt function is used. Remember to import it in the beginning of the program.

# # sqrt function will not work without this line in the beginning of the program
# from math import sqrt

# print(sqrt(9))
# Sample output
# 3.0
# An example of expected behaviour of your program:

# Sample output
# Please type in a number: 16
# 4.0
# Please type in a number: 4
# 2.0
# Please type in a number: -3
# Invalid number
# Please type in a number: 1
# 1.0
# Please type in a number: 0
# Exiting...

#solution
from math import sqrt
# Write your solution here
number = ("")

while number != 0:
    number = int(input("Please type in a number:")) 
    if number > 0: 
        print(sqrt(number))
    elif number < 0:
        print("Invalid number")
print("Exiting...")

#prompt

# This program should print out a countdown. The code is as follows:

# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number > 0:
#     break

# print("Now!")
# This should print out

# Sample output
# Countdown!
# 5
# 4
# 3
# 2
# 1
# Now!

