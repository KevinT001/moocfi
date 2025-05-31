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
