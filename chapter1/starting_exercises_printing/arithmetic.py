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

