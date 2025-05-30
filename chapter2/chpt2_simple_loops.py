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

number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number <= 0:
    break

print("Now!")

#prompt 3

# Please write a program which asks the user for a password. The program should then ask the user to type in the password again. If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.

# Have a look at the expected behaviour below:

# Sample output
# Password: sekred
# Repeat password: secret
# They do not match!
# Repeat password: cantremember
# They do not match!
# Repeat password: sekred
# User account created!

#solution

password = input("Password:")
repeat_pass = ""
while password != repeat_pass: 
    repeat_pass =input("Repeat password:")
    if  password == repeat_pass:
        break
    
        
    print("They do not match!")
print("User account created!")


#prompt 
# Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes.

# Sample output
# PIN: 3245
# Wrong
# PIN: 1234
# Wrong
# PIN: 0000
# Wrong
# PIN: 4321
# Correct! It took you 4 attempts
# If the user gets it right on the first try, the program should print out something a bit different:

# Sample output
# PIN: 4321
# Correct! It only took you one single attempt!

#solution

attempts = 0
pin = 4321
user_input = " "
while user_input != pin:
     
    user_input= int(input("PIN:"))

    
    if user_input == 4321:
        attempts +=1
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        elif attempts > 1:
            print(f"Correct! It took you {attempts} attempts") 
        break
    elif user_input != 4321:
        attempts +=1
    print("Wrong")
    

#prompt

# Please write a program which asks the user for a year, and prints out the next leap year.

# Sample output
# Year: 2023
# The next leap year after 2023 is 2024
# If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

# Sample output
# Year: 2024
# The next leap year after 2024 is 2028
    
    
    user_input = int(input("Year:"))
next_leep = False 
the_next = user_input
while next_leep == False:
    
    the_next +=1
    
    if (the_next%4 == 0 and the_next%100 != 0) or (the_next%4 ==0 and (the_next%100 ==0 and the_next%400 == 0)):
        next_leep = True
        print(f"The next leap year after {user_input} is {the_next}" )
    
