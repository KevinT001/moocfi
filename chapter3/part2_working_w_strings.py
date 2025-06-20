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
    
#prompt 5

# Please write a program which prints out a line of hash characters, the width of which is chosen by the user.

# Sample output
# Width: 3
# ###
# Sample output
# Width: 8
########

#solution
width = int(input("Width:"))

print(width * "#")

#prompt 6

# Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

# Sample output
# Width: 10
# Height: 3
# ##########
# ##########
# ##########

#solution

width = int(input("Width:"))
height = int(input("Height:"))
length = width * "#"
# print(width * "#")

while height > 0 : 
    print(length)
    height -=1
    
    #prompt 7
    # Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.
    
#     Sample output
# Please type in a string: Hi there!

# Hi there!
# ---------
# Please type in a string: This is a test

# This is a test
# --------------
# Please type in a string: a

# a
# -
# Please type in a string:

#solution
string = input("Please type in a string:")


while string != "":
    
    print(string)
    print (len(string) * "-")
    string = input("Please type in a string:")
    if string == "":
        break
    
    #prompt
#     Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

# You may assume the input string is at most 20 characters long.
# Please type in a string: python
# **************python
# Sample output
# Please type in a string: alongerstring
# *******alongerstring
# Sample output
# Please type in a string: averyverylongstring
# *averyverylongstring

#solution

string = input("Please type in a string:")
additional= ((20 - len(string)) * "*")
length = len(string)
if length < 20:
    print(additional + string)
else:
    print(string)
    
    #prompt
#     Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

# If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.
# Word: testing
# ******************************
# *          testing           *
# ******************************
# Sample output
# Word: python
# ******************************
# *           python           *
# ******************************

#solution
string = input("Word")

top_bot = 30 * "*"
space_minus = int((28- len(string))/2)
space = (space_minus * " ")

middle = ("*" + space + string + space + "*" )
middle_plus = ("*" + space + string + space + " " + "*" )

if string != "":
    print(top_bot)
    if len(string)%2 != 0:
        print(middle_plus)
    else:
        
        print (middle)
    print(top_bot)
    
    #prompt 
    # Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest. Have a look at the example below.
    


# Please type in a string: test
# t
# te
# tes
# test

string = input("Please type in a string:")


for char in range(len(string)):

   print(string[:char+1])

#prompt
# Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below.

#Please type in a string: test
# t
# st
# est
# test

#solution
string = input("Please type in a string:")

for char in range(len(string)-1,-1,-1):

    print(string[char:])
    #"-1,-1,-1" first -1 is the start position of string. second -1 is the stopping postion. and the third -1 is the condtion/ the increment. so working backwards from end to index 0. 
    
#prompt

# Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e or o.

# You may assume the input will be in lowercase entirely. Have a look at the examples below.

# Please type in a string: hello there
# a not found
# e found
# o found
# Sample output
# Please type in a string: hiya
# a found
# e not found
# o not found

#solution
#need to fix/ correctly solve later
# string = input("Please type in a string:")
# vowels = ["a","e","i", "o", "u"]
# for char in string:
#     if char == vowels[0]:
#         print("a found")
#     elif char == vowels[1]:
#         print("e found")
#     elif char == vowels[2]:
#         print("i found")
#     elif char == vowels[3]:
#         print("o found")
#     elif char == vowels[4]:
#         print("u found")
#     else: 
#         print(f"{char} not found")

#prompt

# Please write a program which asks the user to type in a string and a single character. The program then prints the first three character slice which begins with the character specified by the user. You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.

# Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for. In that case nothing should be printed out, and there should not be any indexing errors when executing the program.
# Please type in a word: mammoth
# Please type in a character: m
# mam
# Sample output
# Please type in a word: banana
# Please type in a character: n
# nan
# Sample output
# Please type in a word: tomato
# Please type in a character: x
# Sample output
# Please type in a word: python
# Please type in a character: n

#solution (come back)

word = input("Please type in a word:")
char = input("Please type in a character:")
#start with if conditional? use .find method? 

#save? connection test # ignore this line. 