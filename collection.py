# Basic print command, and input


name = input("Hello and welcome! Please enter your name: ")
print(f"Hello, {name}!")

# Data types are:
# String
# Integer
# Float
# Boolean

# Type conversion:

name = input("Please enter your name: ")
birth_year = int(input("Now your birth year please: "))
age = 2023 - birth_year
print(f"{name}, you are {age} years old")
