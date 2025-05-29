#prompt 1 

# Please write a program which asks the user for their age. The program should then print out a message based on whether the user is of age or not, using 18 as the age of maturity.

# Some examples of expected behaviour:

# Sample output
# How old are you? 12
# You are not of age!
# Sample output
# How old are you? 32
# You are of age!

age = int(input("How old are you? "))
if age < 18:
    print("You are not of age!")
else:
    print("You are of age!")
    
#prompt 2

# Please write a program which asks for two integer numbers. The program should then print out whichever is greater. If the numbers are equal, the program should print a different message.

# Some examples of expected behaviour:

# Sample output
# Please type in the first number: 5
# Please type in another number: 3
# The greater number was: 5
# Sample output
# Please type in the first number: 5
# Please type in another number: 8
# The greater number was: 8
# Sample output
# Please type in the first number: 5
# Please type in another number: 5
# The numbers are equal!

#solution

num1 = int(input("Please type in the first number:"))
num2 = int(input("Please type in another number:"))
if num1 > num2:
    print(f"The greater number was: {num1}")
elif num2 > num1:
    print(f"The greater number was: {num2}")
else:
    print("The numbers are equal!")
#prompt 3

# Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

# Some examples of expected behaviour:

# Sample output
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada
# Sample output
# Person 1:
# Name: Bill
# Age: 1
# Person 2:
# Name: Jean
# Age: 1
# Bill and Jean are the same age

#solution

print("Person 1:")
name= input("Name:")
age = int(input("Age:"))
print("Person 2:")
name2= (input("Name:"))
age2 = int(input("Age:"))

if age > age2:
    print(f"The elder is {name}")
elif age < age2:
    print(f"The elder is {name2}")

else:
    print(f"{name} and {name2} are the same age")

#prompt 3

# Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

# You can assume all words will be typed in lowercase entirely.

# Some examples of expected behaviour:

# Sample output
# Please type in the 1st word: car
# Please type in the 2nd word: scooter
# scooter comes alphabetically last.
# Sample output
# Please type in the 1st word: zorro
# Please type in the 2nd word: batman
# zorro comes alphabetically last.
# Sample output
# Please type in the 1st word: python
# Please type in the 2nd word: python
# You gave the same word twice.

word1= input("Please type in the 1st word:")
word2 = input("Please type in the 2nd word:")



if word1 == word2:
    print("You gave the same word twice.")

elif word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word1 < word2:
    print(f"{word2} comes alphabetically last.")


#prompt 

# Please write a program which asks for the user's age. If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, the program should print out a comment.

# Have a look at the examples of expected behaviour below to figure out which comment is applicable in each case.

# Sample output
# What is your age? 13
# Ok, you're 13 years old
# Sample output
# What is your age? 2
# I suspect you can't write quite yet...
# Sample output
# What is your age? -4
# That must be a mistake

#solution

age = int(input("What is your age?"))

if age >= 5:
    print(f"Ok, you're {age} years old")
elif age < 5 and age >= 0:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")
    
#prompt

# Please write a program which asks for the user's name. If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.

# In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

# Some examples:

# Sample output
# Please type in your name: Morty
# I think you might be one of Mickey Mouse's nephews.
# Sample output
# Please type in your name: Huey
# I think you might be one of Donald Duck's nephews.
# Sample output
# Please type in your name: Ken
# You're not a nephew of any character I know of.

#solution 
name = input("Please type in your name:")

if name == "Huey" or name =="Dewey" or name =="Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Ferdie" or name == "Morty":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")
    
#Other solution 
# name = input("Please type in your name:")

# if name in("Huey", "Dewey", "Louie"):
#     print("I think you might be one of Donald Duck's nephews.")
# elif name in ("Morty", "Ferdie"):
#     print("I think you might be one of Mickey Mouse's nephews.")
# else:
#     print("You're not a nephew of any character I know of.")
    
    
#prompt

# The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

# points	grade
# < 0	impossible!
# 0-49	fail
# 50-59	1
# 60-69	2
# 70-79	3
# 80-89	4
# 90-100	5
# > 100	impossible!
# Some examples:

# Sample output
# How many points [0-100]: 37
# Grade: fail
# Sample output
# How many points [0-100]: 76
# Grade: 3
# Sample output
# How many points [0-100]: -3
# Grade: impossible!

#solution 

points = int(input("How many points[0-100]:"))

if 0> points or points > 100:
    print("impossible!")

elif 0<= points <= 49:
    print("fail")
elif 50 <= points <= 59:
    print(f"Grade: 1")
elif 60 <= points <= 69:
    print("Grade: 2")
elif 70 <= points <= 79:
    print("Grade: 3")
elif 80 <= points <= 89:
    print("Grade: 4")
else:
    print("Grade: 5")

#prompt 

# Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz. If the number is divisible by five, the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.

# Some examples of expected behaviour:

# Sample output
# Number: 9
# Fizz
# Sample output
# Number: 7
# Sample output
# Number: 20
# Buzz
# Sample output
# Number: 45
# FizzBuzz

#Solution 
number = int(input("Number:"))

if number%3 == 0 and number%5 == 0:
    print("FizzBuzz")

elif number%3 == 0:
    print("Fizz")

elif number%5 ==0:
    print("Buzz")
    
#prompt

# Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

# Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

# Some examples:

# Sample output
# Please type in a year: 2011
# That year is not a leap year.
# Sample output
# Please type in a year: 2020
# That year is a leap year.
# Sample output
# Please type in a year: 1800
# That year is not a leap year.

#solution

