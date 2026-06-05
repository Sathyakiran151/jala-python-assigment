# Assignment 9: Abstract Classes in Python
from abc import ABC, abstractmethod
import math

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

print("1-4. Abstract and child class")
dog = Dog()
dog.sleep()
dog.sound()

print("5. Attempt to instantiate abstract class")
try:
    animal = Animal()
except TypeError as e:
    print("Error:", e)
    print("Reason: Abstract class cannot be instantiated directly.")

class Machine(ABC):
    @abstractmethod
    def start(self): pass
    @abstractmethod
    def stop(self): pass

class Laptop(Machine):
    def start(self): print("Laptop started")
    def stop(self): print("Laptop stopped")

print("6. Multiple abstract methods")
lap = Laptop()
lap.start(); lap.stop()

class Shape(ABC):
    @abstractmethod
    def area(self): pass
    def display(self): print("This is a shape")

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width): self.length = length; self.width = width
    def area(self): return self.length * self.width

print("7. Real-world shape example")
c = Circle(5)
r = Rectangle(10, 4)
c.display(); print("Circle area:", c.area())
r.display(); print("Rectangle area:", r.area())

class PartialShape(Shape):
    pass

print("8. Partial implementation")
try:
    ps = PartialShape()
except TypeError as e:
    print("Error because all abstract methods are not implemented:", e)
