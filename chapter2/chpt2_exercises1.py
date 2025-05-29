# The following program contains several syntactic errors. Please fix the program so that the syntax is in order and the program works as specified by the examples below.

#   number = input("Please type in a number: ")
#   if number>100
#     print("The number was greater than one hundred")
#     number - 100
#     print("Now its value has decreased by one hundred)
#      print("Its value is now"+ number)
#  print(number + " must be my lucky number!")
#  print("Have a nice day!)
# Sample output
# Please type in a number: 13
# 13 must be my lucky number!
# Have a nice day!
# Sample output
# Please type in a number: 101
# The number was greater than one hundred
# Now its value has decreased by one hundred
# Its value is now 1
# 1 must be my lucky number!
# Have a nice day!

#solution

number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    
    number = number - 100
    print("Now its value has decreased by one hundred")
    print(f"Its value is now + {number}")
print(f"{number} must be my lucky number!")
print("Have a nice day!")

#prompt 2 

# The function len can be used to find out the length of a string, among other things. The function returns the number of characters in a string.

# Some examples of how this works:

# word = "abcd"
# print(len(word))

# print(len("hi there"))

# word2 = "howdydoody"
# length = len(word2)
# print(length)

# empty_string = ""
# length = len(empty_string)
# print(length)
# Sample output
# 4
# 8
# 10
# 0
# Please write a program which asks the user for a word and then prints out the number of characters, if there was more than one typed in.

# Examples of expected behaviour:

# Sample output
# Please type in a word: hey
# There are 3 letters in the word hey
# Thank you!
# Sample output
# Please type in a word: banana
# There are 6 letters in the word banana
# Thank you!
# Sample output
# Please type in a word: b
# Thank you!

#Solution 

word = input("Please type in a word:")

length = len(word)

if length > 1:

    print(f"There are {length} letters in the word {word}")
print("Thank you!")

#prompt 3

# Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function.

# You can assume the number given by the user is always greater than zero.

# An example of expected behaviour:

# Sample output
# Please type in a number: 1.34
# Integer part: 1
# Decimal part: 0.34