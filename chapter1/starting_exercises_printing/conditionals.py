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

# prompt 7

# This program calculates the end of year bonus a customer receives on their loyalty card. The bonus is calculated with the following formula:

# If there are less than a hundred points on the card, the bonus is 10 %
# In any other case the bonus is 15 %
# The program should work like this:

# Sample output
# How many points are on your card? 55
# Your bonus is 10 %
# You now have 60.5 points
# But there is a problem with the program, so with some inputs it doesn't work quite right:

# Sample output
# How many points are on your card? 95
# Your bonus is 10 %
# Your bonus is 15 %
# You now have 120.175 points
# Please fix the program so that there is always either a 10 % or a 15 % bonus, but never both.

# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
    

elif points >= 100:      #changed if on this line to elif
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")

# prompt 8

# Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.

# The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

# Some examples of expected behaviour:

# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 21
# Will it rain (yes/no): no
# Wear jeans and a T-shirt
# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 11
# Will it rain (yes/no): no
# Wear jeans and a T-shirt
# I recommend a jumper as well
# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 7
# Will it rain (yes/no): no
# Wear jeans and a T-shirt
# I recommend a jumper as well
# Take a jacket with you
# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 3
# Will it rain (yes/no): yes
# Wear jeans and a T-shirt
# I recommend a jumper as well
# Take a jacket with you
# Make it a warm coat, actually
# I think gloves are in order
# Don't forget your umbrella!

#solution

print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature:"))
rain = input("Will it rain(yes/no)")
shirt = ("Wear jeans and a T-shirt")
jumper = ("I recommend a jumper as well")
jacket = ("Take a jacket with you")
coat = ("Make it a warm coat, actually")
gloves =("I think gloves are in order")
umbrella = ("Don't forget your umbrella!")


if temp > 20: 
    if rain == "no":
        print(f"{shirt}")

    elif rain == "yes": 
     
        print(f"{shirt}")
        print(f"{umbrella}")

if temp <= 20 and temp > 10: 
    if rain == "no":
        print(f"{shirt}")
        print(f"{jumper}")

    elif  rain == "yes":
        print(f"{shirt}")
        print(f"{jumper}")
        print(f"{umbrella}")

if temp <=10 and temp > 5:
    if rain == "yes":
        print(f"{shirt}")
        print(f"{jumper}")
        print(f"{jacket}")
        print(f"{umbrella}")
    elif rain == "no":
        print(f"{shirt}")
        print(f"{jumper}")
        print(f"{jacket}")

if temp <= 5:
    if rain == "yes": 
        print(f"{shirt}")
        print(f"{jumper}")
        print(f"{jacket}")
        print(f"{coat}")
        print(f"{gloves}")
        print(f"{umbrella}")
    elif rain =="no":
        print(f"{shirt}")
        print(f"{jumper}")
        print(f"{jacket}")
        print(f"{coat}")
        print(f"{gloves}")
        
        
# prompt 9
# In the Python math module there is the function sqrt, which calculates the square root of a number. You can use it like so:

# from math import sqrt

# print(sqrt(9))
# This should print out

# Sample output
# 3.0
# We will return to the concept of a module and the import statement later. For now, it is sufficient to understand that the line from math import sqrt allows us to use the sqrt function in our program.

# Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt function is as follows:

# x = (-b ± sqrt(b²-4ac))/(2a).

# You can assume the equation will always have two real roots, so the above formula will always work.

# An example of expected behaviour:

# Sample output
# Value of a: 1
# Value of b: 2
# Value of c: -8

# The roots are 2.0 and -4.0

#solution

from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a = (float(input("Value of a:")))
b = (float(input("Value of b:")))
c = (float(input("Value of c:")))

x1 = (-b + sqrt(b**2 -4*a*c))/(2*a )

x2 = (-b - sqrt(b**2 -4*a*c))/(2*a) 

print(f"The root are {x1} and {x2}")