# Assignment 10: Packages & Modules in Python

import mypackage.class_one
from mypackage.class_two import ClassTwo
import mypackage.class_one as c1
from mypackage import ClassOne

print("Using import mypackage.class_one")
obj1 = mypackage.class_one.ClassOne("Sathya")
print(obj1.show_name())

print("\nUsing from mypackage.class_two import ClassTwo")
obj2 = ClassTwo("Python package demo")
print(obj2.show_message())

print("\nUsing alias import")
obj3 = c1.ClassOne("Alias Object")
print(obj3.show_name())

print("\nUsing import from __init__.py")
obj4 = ClassOne("Direct Package Import")
print(obj4.show_name())

print("\nRelative import demonstration")
print(obj4.call_class_two())
