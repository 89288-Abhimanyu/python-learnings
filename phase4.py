"""
# FILE HANDLING
# uses -- to maintain logs, config, ETL, reports, data migration

#   Python uses modes to tell how you want to open a file.
#   modes
#   'r'         read
#   'w'         write
#   'a'         append
#   'x'         create file (fail if exists)
#   'b'         binary mode
#   't'         text mode (default)


#open("data.txt", "x")

file = open("data.txt", "a")
file.write("Hello World\n")
file.close()


with open("data.txt", "a") as file:
    file.write("How are you\n")                 # this will automatically close the file

lines = ["Lets learn:\n","Python\n", "Flask\n", "FastAPI\n"]    # to append multiple lines
with open("data.txt", "a") as file:
    file.writelines(lines)

tempfile = open("data.txt", "r")
content = tempfile.read()
tempfile.close()
print(content)                      # to print contents of a file
# Encoding
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
"""

# CSV FILES (comma seperated value) -- a plain text file used to store tabular data

import csv
#  writing csv
with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "age"])
    writer.writerow([1, "Abhi", 25])

# reading csv 
with open("users.csv", newline="") as file:
    reader =csv.reader(file)
    for row in reader:
        print(row)

# EXCEPTION HANDLING -- errors that come on runtime

try:
    x = int("abc")
except ValueError:
    print("Invalid number")

# multiple errors can also be caught in tuple style
try:
    x =10/0
except ZeroDivisionError:
    print("divide by zero")
except(ValueError):
    print("Invalid value")

# else block
try:
    x = int("10")
except ValueError:
    print("Error")
else:
    print("Success:", x)            # this runs if code ran successfully

# finally block
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File missing")
finally:                            # this block will executed in any condition
    file.close()

# raising exceptions
raise ValueError("Invalid age")     # its like throw of java

# custom exceptions
#   class AgeError(Exception):
#       pass
#   def validate_age(age):
#       if age < 18:
#           raise AgeError("Age must be 18+")


