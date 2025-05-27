# Please write a program which asks for the user's name and then prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, another between the two names and a third one at the end of the line.

# The program should function as follows:

# Sample output
# What is your name? Paul
# !Paul!Paul!

#solution
name = input("What is your name?")

print("!"+name+"!"+name+"!")
# The code above prompts the user for their name and then prints it out twice on a single line, with exclamation marks at the beginning, between the names, and at the end.

# Prompt 2

# Please write a program which asks for the user's name and address. The program should also print out the given information, as follows:

# Sample output
# Given name: Steve
# Family name: Sanders
# Street address: 91 Station Road
# City and postal code: London EC05 6AW
# Steve Sanders
# 91 Station Road
# London EC05 6AW

name =input("Given name:")
family_name= input("Family name:")
address = input("Street address:")
city_and_postal= input("City and postal code:")

print(name +" "+ family_name)
print(address)
print(city_and_postal)