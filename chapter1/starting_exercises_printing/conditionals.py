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
name = input("Please tell me your name:")


if name == "Jerry":
    print("Next please!")

if name != "Jerry":
    portions = int(input("How many portions of soup?"))

    costtotal= (portions * 5.9)

    print(f"The total cost is {costtotal}")
    print("Next please!")

# prompt 3
# Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number according to the following examples.

# Sample output
# Please type in a number: 950
# This number is smaller than 1000
# Thank you!
# Sample output
# Please type in a number: 59
# This number is smaller than 1000
# This number is smaller than 100
# Thank you!
# Sample output
# Please type in a number: 2
# This number is smaller than 1000
# This number is smaller than 100
# This number is smaller than 10
# Thank you!
# Sample output
# Please type in a number: 1123
# Thank you!


#solution

number =int(input("Please type in a number: "))

if number > 1000:
    print("Thank you!")
if number < 1000 and number > 100:
    print("This number is smaller than 1000")
    print("Thank you!")

if number < 100 and number > 10:    
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("Thank you!")

if number < 10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print("Thank you!")
    
    # prompt 4
    
#     Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

# Some examples of expected behaviour:

# Sample output
# Number 1: 10
# Number 2: 17
# Operation: add

# 10 + 17 = 27
# Sample output
# Number 1: 4
# Number 2: 6
# Operation: multiply

# 4 * 6 = 24
# Sample output
# Number 1: 4
# Number 2: 6
# Operation: subtract

# 4 - 6 = -2

#solution

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operation = input("Operation: ")

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2

if operation != ("add", "subtract", "multiply"):
    print("")
if operation == "add":
    print(f"{num1} + {num2} = {add}")

if operation == "subtract":
    print(f"{num1} - {num2} = {subtract}")

if operation =="multiply":
    print(f"{num1} * {num2} = {multiply}")   

# prompt 5

# Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

# The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

# Two examples of expected behaviour:

# Sample output
# Please type in a temperature (F): 101
# 101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius

# Please type in a temperature (F): 21
# 21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
# Brr! It's cold in here!

faren = float(input("Please type in a temperature(F): "))
celsius = ((faren -32) * (5/9))

if celsius >= 0 :
    print(f"{faren} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print(f"{faren} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")
    
# prompt 6

# Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

# Sample output
# Hourly wage: 8.5
# Hours worked: 3
# Day of the week: Monday
# Daily wages: 25.5 euros
# Sample output
# Hourly wage: 12.5
# Hours worked: 10
# Day of the week: Sunday
# Daily wages: 250.0 euros

#solution
hourly = float(input("Hourly wage:" ))
hours_worked = int(input("Hours worked:"))
day_of_week = input("Day of the week:")

normal_pay = (hourly*hours_worked)
double_pay = ((hourly*2) * hours_worked)

sunday = (hourly * 2)

if day_of_week in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"): 
    print(f"Daily wages: {normal_pay} euros")

if day_of_week == "Sunday":
    print(f"Daily wages: {double_pay} euros")
