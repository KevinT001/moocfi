#f strings are for string interpolation
#prompt 
# The program should print out exactly the following:

# Sample output
# my name is Tim Tester, I am 20 years old

# my skills are
#  - python (beginner)
#  - java (veteran)
#  - programming (semiprofessional)

# I am looking for a job with a salary of 2000-3000 euros per month

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old \n")
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3}) \n")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

#prompt2

# This program already contains two integer variables, x and y:

# x = 27
# y = 15
# Please complete the program so that it also prints out the following:

# Sample output
# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8

#solution
# Write your solution here
x = 27
y = 15
print(f'{x} + {y} = {x+ y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} * {y} = {x*y}')
print(f'{x} / {y} = {x/y}')
# The code above performs basic arithmetic operations on two integers, x and y, and prints the results in a formatted manner using f-strings.


#prompt 3
# Please fix this program so that the entire calculation, complete with result, is printed out on a single line. Do not change the number of print commands used.


# print(5)
# print(" + ")
# print(8)
# print(" - ")
# print(4)
# print(" = ")
# print(5 + 8 - 4)

#solution   
# Fix the code
print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)
# The code above prints a mathematical expression and its result on a single line by using the `end` parameter in the print function to control the output format.