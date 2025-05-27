# prompt 1

# Please write a program which asks the user for a number of days. The program then prints out the number of seconds in the amount of days given.

# The program should function as follows:

# Sample output
# How many days? 1
# Seconds in that many days: 86400

# solution
days =int(input("How many days?"))
second_in_day = int(days * 24 * 60 * 60)
print(f"Seconds in that many days: {second_in_day}")


# prompt 2

# Please write a program which asks the user for two numbers. The program will then print out the sum and the product of the two numbers.

# The program should function as follows:

# Sample output
# Number 1: 3
# Number 2: 7
# The sum of the numbers: 10
# The product of the numbers: 21

num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))

print(f"The sum of the numbers: {num1 + num2}")
print(f"The product of the numbers: {num1 * num2}")

# prompt 3
# Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

# The program should function as follows:

# Sample output
# Number 1: 2
# Number 2: 1
# Number 3: 6
# Number 4: 7
# The sum of the numbers is 16 and the mean is 4.0

num1= int(input("Number 1:"))
num2= int(input("Number 2:"))
num3= int(input("Number 3:"))
num4= int(input("Number 4:"))
sum= int(num1+num2+num3+num4)
average =float(sum/4)
print(f"The sum of the numbers is {sum} and the mean is {average}")

# prompt 4