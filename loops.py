# Assignment 3: Loops & Control Flow in Python

print("1. Bright IT Career 10 times")
for i in range(10):
    print("Bright IT Career")

print("\n2. Numbers 1 to 20")
i = 1
while i <= 20:
    print(i, end=" ")
    i += 1
print()

print("\n3. Equal and Not Equal Check")
a, b = 10, 20
print("Equal:", a == b)
print("Not Equal:", a != b)

print("\n4. Odd and Even Numbers from 1 to 50")
for n in range(1, 51):
    if n % 2 == 0:
        print(n, "Even")
    else:
        print(n, "Odd")

print("\n5. Largest Among Three Numbers")
a, b, c = 25, 90, 70
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
print("Largest:", largest)

print("\n6. Even Numbers between 10 and 20")
n = 10
while n <= 20:
    if n % 2 == 0:
        print(n, end=" ")
    n += 1
print()

print("\n7. Armstrong Number")
num = 153
temp = num
digits = 0
while temp > 0:
    digits += 1
    temp //= 10

temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10
print(num, "is Armstrong" if total == num else "is not Armstrong")

print("\n8. Prime Number Check")
num = 29
is_prime = True
if num <= 1:
    is_prime = False
else:
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
print(num, "is Prime" if is_prime else "is not Prime")

print("\n9. Palindrome Check")
num = 121
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print(original, "is Palindrome" if original == reverse else "is not Palindrome")

print("\n10. Even or Odd")
num = 17
print("Even" if num % 2 == 0 else "Odd")

print("\n11. Gender Identification")
gender = 'M'
if gender == 'M':
    print("Male")
elif gender == 'F':
    print("Female")
else:
    print("Invalid Input")

print("\n12. Multiplication Table")
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("\n13. Count Digits")
num = 98765
count = 0
temp = num
if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10
print("Digits in", num, "=", count)
