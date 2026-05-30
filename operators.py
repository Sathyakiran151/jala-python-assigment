# Assignment 2: Operators in Python

def arithmetic(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division not possible by zero")

def increment_decrement(num):
    print("Original:", num)
    num += 1
    print("After increment:", num)
    num -= 1
    print("After decrement:", num)

def equality_check(a, b):
    if a == b:
        print("Both numbers are equal")
    else:
        print("Both numbers are not equal")

def relational_demo(a, b):
    print(a, "<", b, "=", a < b)
    print(a, "<=", b, "=", a <= b)
    print(a, ">", b, "=", a > b)
    print(a, ">=", b, "=", a >= b)

def smaller_larger(a, b):
    if a < b:
        print("Smaller:", a, "Larger:", b)
    elif b < a:
        print("Smaller:", b, "Larger:", a)
    else:
        print("Both are equal")

def largest_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    print("Largest:", largest)

def calculator(a, b, op):
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        print("Result:", a / b if b != 0 else "Cannot divide by zero")
    else:
        print("Invalid operator")

if __name__ == "__main__":
    arithmetic(20, 5)
    increment_decrement(10)
    equality_check(7, 7)
    relational_demo(10, 15)
    smaller_larger(50, 30)
    largest_of_three(12, 99, 45)
    calculator(8, 4, '*')
