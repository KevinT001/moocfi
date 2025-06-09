#prompt 1

# Please write a program which asks the user for a string and an amount. The program then prints out the string as many times as specified by the amount. The printout should all be on one line, with no extra spaces or symbols added.

# An example of expected behaviour:

# Sample output
# Please type in a string: hiya
# Please type in an amount: 4
# hiyahiyahiyahiya

#solution

string = input("Please type in a string:")
amount = int(input("Please type in an amount:"))

print(string * amount)

#prompt
# Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

# Some examples of expected behaviour:

# Sample output
# Please type in string 1: hey
# Please type in string 2: hiya
# hiya is longer
# Sample output
# Please type in string 1: howdy doody
# Please type in string 2: hola
# howdy doody is longer
# Sample output
# Please type in string 1: hey
# Please type in string 2: bye
# The strings are equally long

# solution

string1 = input("Please type in a string 1:")
string2 = input("Please type in a string 2:")

if len(string1) > len(string2):
    print(f"{string1} is longer")
elif len(string1) < len(string2):
    print(f"{string2} is longer")
else:
    print("The strings are equally long")
    
    #prompt 3
    
#     Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a string: hiya
# a
# y
# i
# h

#solution
string = input("Please type in a string:")
index = 0

while index <= len(string):
    
    index -= 1
    print(string[index])
    
    #prompt 4
    
#     Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.

# Sample output
# Please type in a string: python
# The second and the second to last characters are different
# Sample output
# Please type in a string: pascal
# The second and the second to last characters are a
 
 #solution
 
 string = input("Please type in a string:")

if string[1] == string[-2]:
    print(f"The second and the second to last characters are {string[1]} ")
else:
    print("The second and the second to last characters are different")