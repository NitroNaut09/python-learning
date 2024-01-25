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

name = input("Please enter your name: ")
birth_year = (input("Now your birth year please: "))
age = 2023 - int(birth_year)
print(f"{name}, you are {age} years old")

           
course = "Python for beginners"
print(course[1])                                                # Print a substring of the string from index 0 to 2 (exclusive)
print(course[0:3])                                              # Define a string variable
course = "Python for beginners"                                 # Create a copy of the string
another = course[:]

first = 'John'
second = 'Abrams'
message = first + '[' + last + '] is a coder'
print(message)
message = (f"{first}{second} is a coder")

print(course.find('Beginners'))
#This will return the index from where the string "Beginners" starts from. Note that it is case sensitive.

print(len(course)) 
#Prints the character length of the variable

course.replace('Python', 'DJ')
#This will replace the string "Python" with "DJ".

print("Python" in course)
#This will return a boolean whether there is string called "Python" in "course" var.


#   Types of var functions
 
 var.upper()
 var.lower()
 var.title()
 var.find()
 var.replace()
 "..." in var 

 #  Arithmetic Operations 

print(10+3)   #Addition
print(10-3)   #Subtraction
print(10*3)   #Multiplication
print(10/3)   #Division, returns quotient in integer from
print(10**3)  #Exponentiation
print(10%3)   #
print(10//3)    
