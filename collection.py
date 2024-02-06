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
print(10/3)   #Division
print(10**3)  #Exponentiation
print(10%3)   #Shows the remainder after performing dvision.
print(10//3)  #Floor division, returns integer value.

#  Assignment Operator

a = 10
a += 3 #Adds the value of "3" to the variable "a"
a -= 3 #Subtracts the value of "3" from the variable "a"

#  Comparison Operator

a == b #Equal to
a != b #Not equal to
a > b  #Greater than
a < b  #Less than
a >= b #Greater than or equal to
a <= b #Less than or equal to

#  Membership operator:
x in y        #Is x a member of y?
x not in y    #Is x not a member of y?

#  Operator Precendence

** (Exponentiation)
+x, -x (Positive, Negative)
*, /, //, % (Multiplication, Division, Floor Division, Modulus)
+, - (Addition, Subtraction)
<<, >> (Bitwise Shifts)
& (Bitwise AND)
^ (Bitwise XOR)
| (Bitwise OR)
in, not in, is, is not, <, <=, >, >=, !=, == (Comparisons, including membership tests and identity tests)
not x (Boolean NOT)
and (Boolean AND)
or (Boolean OR)


