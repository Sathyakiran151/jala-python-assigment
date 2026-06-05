# Assignment 7: Inheritance & Polymorphism in Python

class A:
    def __init__(self):
        self.value = "A value"
        print("Constructor of A")
    def method_a1(self): print("A specific method 1")
    def method_a2(self): print("A specific method 2")
    def common_method(self): print("Common method from A")

class B(A):
    def __init__(self):
        super().__init__()
        self.value = "B value"
        print("Constructor of B")
    def method_b1(self): print("B specific method 1")
    def method_b2(self): print("B specific method 2")
    def common_method(self):
        super().common_method()
        print("Common method overridden in B")

class C(B):
    def __init__(self):
        super().__init__()
        self.value = "C value"
        print("Constructor of C")
    def method_c1(self): print("C specific method 1")
    def method_c2(self): print("C specific method 2")
    def common_method(self):
        super().common_method()
        print("Common method overridden in C")

print("1-3. Object creation and method calls")
a = A()
b = B()
c = C()
a.method_a1(); a.method_a2(); a.common_method()
b.method_a1(); b.method_a2(); b.method_b1(); b.method_b2(); b.common_method()
c.method_a1(); c.method_b1(); c.method_c1(); c.method_c2(); c.common_method()

print("\n4. Runtime polymorphism")
ref = B()
ref.common_method()
ref = C()
ref.common_method()

print("\n6. Instance variable behavior")
print(a.value)
print(b.value)
print(c.value)
ref = c
print("Superclass reference variable value:", ref.value)

print("\n8. Real-world Example")
class Vehicle:
    def start_engine(self): print("Vehicle engine starts")
class Car(Vehicle):
    def start_engine(self): print("Car engine starts with key")
class ElectricCar(Car):
    def start_engine(self): print("Electric car starts silently")

vehicles = [Vehicle(), Car(), ElectricCar()]
for v in vehicles:
    v.start_engine()
