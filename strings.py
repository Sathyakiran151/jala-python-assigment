# Assignment 6: Strings in Python
import re

single = 'Single quoted string'
double = "Double quoted string"
triple = '''Triple quoted string'''
print("1.", single, double, triple)

first = "Bright"
second = "Career"
print("2. Concatenation:", first + " IT " + second)

text = "Python Programming"
print("3. Length:", len(text))
print("4. Substring:", text[0:6])

main_text = "Welcome to Python Programming"
sub = "Python"
print("5. find():", main_text.find(sub))
try:
    print("index():", main_text.index(sub))
    print("index missing:", main_text.index("Java"))
except ValueError:
    print("Substring not found using index()")

s1 = "apple"
s2 = "banana"
print("6. Equality:", s1 == s2)
print("Not Equal:", s1 != s2)

file_name = "assignment.py"
print("7. Starts with assign:", file_name.startswith("assign"))
print("Ends with .py:", file_name.endswith(".py"))

if s1 > s2:
    print("8.", s1, "is greater")
elif s1 < s2:
    print("8.", s2, "is greater")
else:
    print("8. Both are equal")

space_text = "   Python   "
print("9. Strip:", space_text.strip())

sentence = "I like Java"
print("10. Replace:", sentence.replace("Java", "Python"))

csv = "Python,SQL,ML"
print("11. Split:", csv.split(","))

num = 100
num_str = str(num)
print("12. Integer to String:", num_str, type(num_str))

word = "Python"
print("13. Upper:", word.upper())
print("Lower:", word.lower())

email = "test@gmail.com"
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
print("14. Valid email:", bool(re.match(pattern, email)))
print("Only digits:", bool(re.match(r'^\d+$', "12345")))

line = "Python Programming"
vowels = 0
consonants = 0
for ch in line.lower():
    if ch >= 'a' and ch <= 'z':
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("15. Vowels:", vowels, "Consonants:", consonants)

print("16. Reverse:", line[::-1])
