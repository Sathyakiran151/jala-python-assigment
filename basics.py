# Assignment 1: Python Basics & Variables

# 1. Print Your Name
print("1. Print Your Name")
print("Sathya Kiran")

# 2. Comments in Python
print("\n2. Comments in Python")
# This is a single-line comment.
"""
This is a multi-line comment.
It is written using triple quotes.
"""
print("Comments are used to explain code and make it easy to understand.")

# 3. Working with Basic Data Types
print("\n3. Basic Data Types")
integer_value = 25
float_value = 25.75
boolean_value = True
string_value = "A"

print(integer_value, type(integer_value))
print(float_value, type(float_value))
print(boolean_value, type(boolean_value))
print(string_value, type(string_value))

# 4. Local vs Global Variables
print("\n4. Local vs Global Variables")
message = "Global Message"

def scope_demo():
    global message
    local_message = "Local Message"
    print("Local variable:", local_message)
    print("Global variable before change:", message)
    message = "Global Message Modified"
    print("Global variable inside function after change:", message)

scope_demo()
print("Global variable outside function:", message)

# 5. Type Checking & Dynamic Typing
print("\n5. Dynamic Typing")
data = 100
print(data, type(data))
data = 45.6
print(data, type(data))
data = "Python"
print(data, type(data))
data = False
print(data, type(data))

# 6. User Input Practice
print("\n6. User Input Practice")
# Uncomment below lines to take actual input.
# name = input("Enter your name: ")
# age = input("Enter your age: ")
name = "Sathya"
age = 21
print("Name:", name)
print("Age:", age)
