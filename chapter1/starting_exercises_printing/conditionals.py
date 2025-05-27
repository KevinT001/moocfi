# prompt 1 

# Please write a program which asks the user for an integer number. If the number is less than zero, the program should print out the number multiplied by -1. Otherwise the program prints out the number as is. Please have a look at the examples of expected behaviour below.

# Sample output
# Please type in a number: -7
# The absolute value of this number is 7
# Sample output
# Please type in a number: 1
# The absolute value of this number is 1

num =int(input("Please type in a number:"))
statement = "The absolute value of this number is"
if (num < 0):
    print(f"{statement}", end=" ") 
    print(int((num * -1)))

if (num >= 0):
     print(f"{statement}", end=" ")
     print (num)    
     

# prompt 2
# Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.

# Two examples of the program's execution:

# Sample output
# Please tell me your name: Kramer
# How many portions of soup? 2
# The total cost is 11.8
# Next please!
# Sample output
# Please tell me your name: Jerry
# Next please!

#solution
