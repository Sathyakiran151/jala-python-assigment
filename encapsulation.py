# Assignment 8: Encapsulation & Data Control in Python

class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
    def set_values(self, name, age):
        self.name = name
        if age > 0:
            self.age = age
        else:
            print("Invalid age")
    def get_values(self):
        return self.name, self.age

s = Student()
s.set_values("Sathya", 21)
print("1-2. Student:", s.get_values())

class StudentProperty:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Invalid age")
            self._age = 0

sp = StudentProperty("Kiran", 22)
print("3. Property age:", sp.age)

class Employee:
    def __init__(self, emp_id):
        self._id = emp_id
    @property
    def id(self):
        return self._id

emp = Employee(101)
print("4. Read-only id:", emp.id)

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

acc = BankAccount("Sathya", 1000)
acc.deposit(500)
acc.withdraw(300)
print("5. Balance:", acc.balance)

class InternalDemo:
    def __init__(self):
        self._internal_value = "Internal use only"

demo = InternalDemo()
print("6. Internal variable can be accessed but should not:", demo._internal_value)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def area(self):
        return self.length * self.width

rect = Rectangle(10, 5)
print("7. Area:", rect.area)

class PasswordSystem:
    def __init__(self):
        self._password = ""
    def set_password(self, password):
        has_number = False
        for ch in password:
            if ch >= '0' and ch <= '9':
                has_number = True
        if len(password) >= 8 and has_number:
            self._password = password
            print("Password accepted")
        else:
            print("Password must be at least 8 characters and contain a number")

p = PasswordSystem()
p.set_password("Python123")
