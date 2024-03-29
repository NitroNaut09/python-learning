import math
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
print(course[1])                                           # Print a substring of the string from index 0 to 2 (exclusive)
print(course[0:3])                                         # Define a string variable
course = "Python for beginners"                            # Create a copy of the string
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

# Math Functions
abs(x): Returns the absolute value of x.
pow(x, y): Returns x raised to the power y.
sqrt(x): Returns the square root of x.
exp(x): Returns the exponential of x (e^x).
log(x): Returns the natural logarithm of x.
log10(x): Returns the base-10 logarithm of x.
sin(x): Returns the sine of x (x is in radians).
cos(x): Returns the cosine of x (x is in radians).
tan(x): Returns the tangent of x (x is in radians).
degrees(x): Converts angle x from radians to degrees.
radians(x): Converts angle x from degrees to radians.

#Math Module functions
math.ceil(x): Returns the smallest integer greater than or equal to x.
math.floor(x): Returns the largest integer less than or equal to x.
math.fabs(x): Returns the absolute value of x.
math.factorial(x): Returns the factorial of x.
math.exp(x): Returns the exponential of x (e^x).
math.log(x, base): Returns the natural logarithm of x to the given base.
math.sqrt(x): Returns the square root of x.
math.sin(x): Returns the sine of x (x is in radians).
math.cos(x): Returns the cosine of x (x is in radians).
math.tan(x): Returns the tangent of x (x is in radians).
math.degrees(x): Converts angle x from radians to degrees.
math.radians(x): Converts angle x from degrees to radians.
math.pi: A constant representing the mathematical constant π (pi).
math.e: A constant representing the mathematical constant e.

# For Loops
for item in range(5,10, 2) 
# The 2 at the end indicates how much to skip

# Nested Loops

for x in range(5):
    print(x)

for x in range(5):
    for y in range(5):
        print(x, y)

#Lists
names = ['John', 'Bob', 'Mosh', 'Deeraj' ]

#Functions with the list:

names.append('Sarah')
names.insert(0, 'Jack')
names.remove('Mosh')
names.sort()
names.reverse()
names.pop()
print(names)
print(names[3])
print(names[2:])
print(names[:3])

# Program which prints the highest number

numbers = [3, 1, 5, 6, 9, 11,92229893864000264520 ]
numbers.sort
print(numbers[-1])



# 2D Lists

matrix = [

        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]

]

for row in matrix:   # How nested loops can be used in 2D lists
    for item in row:
        print(item)


# List methods

numbers = [5, 2, 1, 7, 4]
numbers.append(20)
numbers.inset(2, 65)
numbers.remove(5)
numbers.clear()
numbers.pop()
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
print(numbers.count(5))


# Duplication remover program

ig = [2,2,2,2, 3,3,3,54,6, 3,6 4,645 6,46 45,665 4]
unique = []
for num in ig:
    if num not in unique:
        unique.append(number)
print(uniques)


# Tuples

numbers = (1, 2, 3)

# Tuple Methods
numbers[0]
numbers.count()
numbers.index()

coordinates = (23.54.,45,56,)

#Below code is:
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

#Same as this code:
x, y, z = coordinates
#This is called unpacking

#Dictionaries:

customer = {} #This is called an empty dict
customer = {
    "name": "John Smith", #Note that you CANNOT have duplicate value
    "age": 30,
    "is_verified": True
}                       
#Access dict items:
customer["name"]
#Use .get method instead so the program doesn't yell at us.
customer.get("name")
#To assign a value, use this:
customer["birthdate"] = "Jan 1 1980"`
#To make a new value-key pair:

#Programs that uses dict to translate numbers into their
#respective words
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
    }
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

#Emoji Converter Program:
emoji = {
    ":)": "😀",
    ":(": "😔"
}
message = input(">")
words = message.split(" ")
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)

#Defining functions:

#Why do we use functions?

#We use functions in Python for several reasons. Firstly, functions allow you to write a block of code and use it multiple, which saves time and makes your code easier to maintain. Functions also make your code easier read and understand by providing descriptive names for blocks of code. Additionally, functions can accept arguments, which are values that can be passed to the function to customize its behavior. Functions can also return values, which can be assigned to variables or used in expressions.
#By using functions, you can make your code more modular, reusable, and easier to debug. Functions can also help you avoid duplicating code, which can make your code more efficient and easier to maintain.

def greet_user():
    print("Hi There")
    print("Welcome abroad")

#Also keep in mind that order matters whenh defining fdunctions. So if you define a function only after calling it, it will return an error.

#Passing info through functions

def greet_user_2(namez):
    print(f"Hi there, {namez}")
    print("welcome abroad")

greet_user_2(input("What's your name? "))

#Arguments in functions are referred to as positional areguments

#Note that parameters and arguments AREN'T the same. Parameters are like "holes" in the code, that act as the placeholder for values. While arguments are itself the thing that supply the information.

#Now, we'll look at keyword arguments. These are arguments which explicitly mention which parameter they refer to, instead of relying on the order of parameters.

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')

greet_user(last_name = "Smith", first_name = "John")


#Return statements:   

def square(number):
    return number * number
print(square(3))

#Things learnt: By default, all funtions in python return none.

#Converting emoji program into a functions:

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))


#Exceptions:

age = int(input('Age: '))
print(age)

#Now, since in this code errors could occur, we will use the try: command.

try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value")

#Classes:
#What we have learnt so far:
#Numbers, strings, booleans, lists, dicts

#Points:
#Classes are used to define objects. Objects are instances of a class. Objects have attributes and methods
#Notice that the first word is capitalized. This is called the pascal naming convention.

class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
print(point2)

#Contrusctors: A constructor is a special method in a class that is automatically called when an instance of the class is created. It is used to initialize the object's state. In Python, the constructor method is denoted by __init__.

class Point:
    def __init__(self, x, y):


    def move(self):
        print("move")

    def draw(self):
        print("draw")
        
class Mammal:
    # Define a method named walk for the Mammal class
    def walk(self):
        print("walk")

# Define a class named Dog which inherits from the Mammal class
class Dog(Mammal):
    # The pass keyword is used as a placeholder for future code. 
    # As the Dog class is inheriting from Mammal, it doesn't need any additional code at this time.
    pass

# Define a class named Cat which also inherits from the Mammal class
class Cat(Mammal):
    # Define a method named be_annoying for the Cat class
    def be_annoying(self):
        # This method is currently empty and needs to be implemented
        pass

# Create an instance of the Dog class
dog1 = Dog()
# Call the walk method on the dog1 instance. This method is inherited from the Mammal class.
dog1.walk()

   
#Modules
#Module is a file with some python code. Used t organize code into multiple files. Like sections in a super market. Each broekn file is called a module. As we write more functions and classes, we put them in their respective modules. Modules should contain all the related functions and classes.

#To import modules, just write import "file" without the extension. Insetad of importing entire modules, we can just import specific functions from the module. Example:

import converter
print(converter.kg_to_lb(70))

#Now, moving on to importing specific functions:

import converter
from converter import kg_to_lb
kg_to_lb(70)

#Take-aways; We use modules to better organize our code. Instead of writing all code in one file, we break it up into more files. Each file is called a module and it should contain all the reated functions and classes. Then we can import a module into another module, as written above.


#Packages:

# A package is a container for multiple modules

#Generating random values

import random

mumbers = ['John', 'Jack', 'Grover']
random.choice(mumbers)

#Some libs

from pathlib import Path 

path = Path('emails')
path.mkdir
path.rmdir 

#Thank you completing Mosh Hamedani's amazing 6 hour python tutorial. 







