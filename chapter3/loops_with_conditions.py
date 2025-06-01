# prompt 

# Please write a program which prints out all the even numbers between two and thirty, using a loop. Print each number on a separate line.

# The beginning of your output should look like this:

# Sample output

# 2
# 4
# 6
# 8
# etc...

#solution

num = 0

while num < 30 : 
    num += 2
    print(num)
    if num == 30:
        break  
    
    #prompt 2
    
#     The program below has some syntactic issues:

# print("Are you ready?")
# number = int(input("Please type in a number: "))
# while number = 0:
# print(number)
# print("Now!")
# Please fix it so that it prints out the following:

# Sample output
# Are you ready?
# Please type in a number: 5
# 5
# 4
# 3
# 2
# 1
# Now!
# This exercise is similar to the countdown exercise in the last section, but please don't use a while True loop this time round!

#solution


print("Are you ready?")
number = int(input("Please type in a number: "))
while number != 0:
    print(number)
    number -= 1
    
        

print("Now!")

#prompt

# Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.

# Sample output
# Upper limit: 5
# 1
# 2
# 3
# 4
# Please don't use the value True as the condition of your while loop in this exercise!

#solution

number = int(input("Upper limit:"))
counter =0

while counter != (number -1):
    counter += 1
    print(counter)
    

#prompt

# Please write a program which asks the user to type in an upper limit. The program then prints out numbers so that each subsequent number is the previous one doubled, starting from the number 1. That is, the program prints out powers of two in order.

# The execution of the program finishes when the next number to be printed would be greater than the limit set by the user. No numbers greater than the limit should be printed.

# Sample output
# Upper limit: 8
# 1
# 2
# 4
# 8
# Sample output
# Upper limit: 20
# 1
# 2
# 4
# 8
# 16
# Please don't use the value True as the condition of your while loop in this exercise!

# What are powers of two? The first power of two is the number 1. The next one is 1 times 2, which is 2. The next is 2 times 2, which is 4. The next is 4 times 2, which is 8, and so forth. Each power in the sequence is multiplied by two to produce the next one.

#solution

upper_limit = int(input("Upper limit:"))
numbers = 1 

while numbers <= upper_limit:
    print(numbers)
    numbers*=2
