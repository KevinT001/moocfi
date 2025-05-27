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

# Please write a program which estimates a user's typical food expenditure.

# The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

# Based on this information the program calculates the user's typical food expenditure both weekly and daily.

# The program should function as follows:

# Sample output
# How many times a week do you eat at the student cafeteria? 4
# The price of a typical student lunch? 2.5
# How much money do you spend on groceries in a week? 28.5

# Average food expenditure:
# Daily: 5.5 euros
# Weekly: 38.5 euros

#solution 

caf_week=int(input("How many times a week do you eat at the student cafeteria?"))
lunch_cost=float(input ("The price of a typical student lunch?"))
grocery_cost=float(input("How much money do you spend on groceries in a week?"))

daily_avg= float(((caf_week*lunch_cost)/7)+(grocery_cost/7))

weekly_avg=float((grocery_cost)+ (lunch_cost*caf_week))

print("Average food expenditure:")
print(f"Daily: {daily_avg} euros")
print(f"Weekly: {weekly_avg} euros")

# prompt 5
