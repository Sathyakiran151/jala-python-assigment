# Assignment 11: File Handling in Python
import os
from datetime import datetime   

sample_file = "sample.txt" 
copy_file = "copy_sample.txt" 


# Prepare sample file
with open(sample_file, "w") as f:
    f.write("Python file handling example.\nSecond line of file.\nThird line here.")

print("1. Read a Text File")
with open(sample_file, "r") as f:
    content = f.read()
    print(content)

print("2. Write to a Text File")     
user_text = "This text is written into the file."
with open("user_input.txt", "w") as f:
    f.write(user_text)
with open("user_input.txt", "a") as f:
    f.write("\nThis line is appended.")
print("Data written successfully")

print("3. Read using read(), readline(), readlines()")
with open(sample_file, "r") as f:
    print("read():", f.read())
with open(sample_file, "r") as f:
    print("readline():", f.readline())
with open(sample_file, "r") as f:
    print("readlines():", f.readlines())

print("4. Random Access File Reading")
with open(sample_file, "r") as f:
    f.seek(7)
    print("From position 7:", f.read())

print("5. Read from Specific Index")
with open(sample_file, "r") as f:
    f.seek(10)
    print("5 characters from index 10:", f.read(5))

print("6. Check File Permissions")
print("Read permission:", os.access(sample_file, os.R_OK))
print("Write permission:", os.access(sample_file, os.W_OK))

print("7. Count Words, Lines, Characters")
with open(sample_file, "r") as f:
    data = f.read()
lines = data.splitlines()
words = data.split()
characters = len(data)
print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

print("8. Copy File Content")
with open(sample_file, "r") as src:
    data = src.read()
with open(copy_file, "w") as dest:
    dest.write(data)
print("File copied")

print("9. Append Data with Timestamp")
with open(sample_file, "a") as f:
    f.write("\nAppended at: " + str(datetime.now()))
print("Timestamp appended")
