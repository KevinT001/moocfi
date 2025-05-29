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
    