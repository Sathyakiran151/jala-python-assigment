# Assignment 12: Constructors in Python

ass Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

p1 = Person()
p2 = Person("Sathya")
p3 = Person("Kiran", 21)
print("1. Constructors:", p1.name, p1.age, p2.name, p2.age, p3.name, p3.age)cl

class Parent:
    def __init__(self, parent_name):
        self.parent_name = parent_name
        print("Parent constructor called")

class Child(Parent):
    def __init__(self, parent_name, child_name):
        super().__init__(parent_name)
        self.child_name = child_name
        print("Child constructor called")

child = Child("Parent Name", "Child Name")
print("2.", child.parent_name, child.child_name)

class AccessDemo:
    def __init__(self):
        self.public_value = "Public"
        self._protected_value = "Protected style"
        self.__private_value = "Private style"
    def get_private(self):
        return self.__private_value

obj = AccessDemo()
print("3. Public:", obj.public_value)
print("Protected:", obj._protected_value)
print("Private using method:", obj.get_private())
print("Private using name mangling:", obj._AccessDemo__private_value)

class Student:
    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
    def __str__(self):
        return f"Student(name={self.name}, roll_no={self.roll_no}, branch={self.branch})"

student = Student("Sathya", 101, "CSE")
print("4. Attributes:", student.__dict__)
print("5. str output:", student)

class FlexibleConstructor:
    def __init__(self, *args):
        self.values = args

fc = FlexibleConstructor(10, 20, "Python", True)
print("6. *args values:", fc.values)

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    def __str__(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}"

employees = [Employee("Sathya", 1, 15000), Employee("Kiran", 2, 20000)]
print("7. Employees")
for emp in employees:
    print(emp)
