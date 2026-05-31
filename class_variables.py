# Assignment 5: Class Variables in Python

class Course:
    course_name = "Python Basics"

print("1. Access via Class:", Course.course_name)

obj = Course()
print("2. Access via Object:", obj.course_name)

obj.course_name = "Python Advanced"
print("3. Modified via Instance:", obj.course_name)
print("Class value remains:", Course.course_name)

Course.course_name = "Python Full Course"
obj1 = Course()
obj2 = Course()
print("4. Modified via Class:", Course.course_name, obj1.course_name, obj2.course_name)

class Employee:
    company = "JALA Academy"  # class variable
    def __init__(self, name):
        self.name = name       # instance variable

e1 = Employee("Sathya")
e2 = Employee("Kiran")
print("5. Class Variable:", e1.company, e2.company)
print("Instance Variables:", e1.name, e2.name)
e1.name = "Sathya Kiran"
Employee.company = "Bright IT Career"
print("After change:", e1.name, e2.name, e1.company, e2.company)

class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

s1 = Student("A")
s2 = Student("B")
s3 = Student("C")
print("6. Total students:", Student.count)

class AppConfig:
    course_name = "Python Basics"

c1 = AppConfig()
c2 = AppConfig()
print("7. Before:", c1.course_name, c2.course_name)
AppConfig.course_name = "Python + Django"
print("After:", c1.course_name, c2.course_name)
