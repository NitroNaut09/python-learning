# Basic print command, and input

# Prompt the user to enter their name
name = input("Hello and welcome! Please enter your name: ")
# Print a greeting message with the entered name
print(f"Hello, {name}!")

# Data types are:
# String
# Integer
# Float
# Boolean

# Type conversion:

# Prompt the user to enter their name
name = input("Please enter your name: ")
# Prompt the user to enter their birth year
birth_year = (input("Now your birth year please: "))
# Calculate the age by subtracting the birth year from the current year
age = 2023 - int(birth_year)
# Print a message with the entered name and calculated age
print(f"{name}, you are {age} years old")

# Define a string variable
course = "Python for beginners"
# Print the character at index 1 of the string
print(course[1])
# Print a substring of the string from index 0 to 2 (exclusive)
print(course[0:3])

# Define a string variable
course = "Python for beginners"
# Create a copy of the string
another = course[:]


first = 'John'
second = 'Abrams'

message = first + '[' + last + '] is a coder'
print(message)
message = (f"{first}{second} is a coder")

