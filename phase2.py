"""

# if, elif, else
marks = 78
if marks < 40:
    print("failed")
if marks is 40:
    print("boundary")
if marks > 40:
    print("passed")

# nested conditions
age = 22
haveLicence = True
if age > 18:
    if is_Active:
        print("You can Drive")

# ternary operator
result = "Adult" if age >= 18 else "Minor"

# for loop works ike for-each by default in Python
for i in range(5):    
    print(i)

# loop for collection
nums = [2,3,4,6,5]
for x in nums:
    print(x)

# range function
range(5) # print i range of 5    i.e.  0,1,2,3,4
range(1,5) # print form 1 to 5 i.e.  i.e. 1,2,3,4
range(1,10,2) # print from 1 to 10 stepping 2 numbers   i.e. 1,3,5,7,9

# while loop 
while count < 5:
    count += 1

# nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

for i in range(5):
    if i==3:
        break  #break exits the loop immediately

for i in range(5):
    if i==3:
        continue  # skips current iteration
    print(i)

for i in range(5):
    if i==10:
        break
else:  # this else will executed only if the "if" condition is not satisfied
    print("Loop completed without break")

#STRING

# String are immutable in python like java 

# String Indexing
text = "Indexing"
print(text[0])     # output-I   Characters are accessed like arrays of java
print(text[-2])    # output-n   Negative indexing is also allowed in python
# Slicing
print(text[0:4])   # output-Inde    Character from 0th to 3rd index will print
print(text[:4])    # output-Inde    Character from 0th to 3rd index will print
print(text[2:])    # output-dexing  Character from 3rd to last position will print
print(text[::2])   # output-Idxn    Every 2nd character will print
print(text[0:-1])  #output-gnixednI String will print in reverse

# Some other methods in Python Strings
text = "hello world"

text.strip()
text.upper()
text.lower()
text.len()
text.replace()
text.split()
"world in text"  # True


# COLLECTIONS

#LIST

data = [1, "hello", 3.5, True]  # Python list can store mixed types. In java this is possible only with List<Objects>
# Indexing and Slicing works same as String. While in java to do this loops or stream are required
print(data)
#Some common List methods
data.append("World") # appends world in the end of list
data.insert(1,15)    # insert 15 after 1
data.remove(15)      # remove 15 from the list
data.pop()           # remove the last element
#data.len()          # shows the length
#data.sort()         # sorts the list
data.clear()         # clears the list i.e. empty
print(data)


# List Comprehension 

squares = [x*x for x in range(5)]
print(squares)

evens = [x for x in range(10) if x%2 == 0]   # these are replacement of loops and stream
print(evens)

matrix = [           # declaring a matrix
    [1,2,3],
    [4,5,6]
]
print(matrix[1][2])         # accessing a matrix


# Copy a list
a =[1,2,3]
b=a      # reference copy(shallow copy) only i.e. both point to same list
print(b)

c = a.copy      # proper copy (deep copy) 
#print(c)

import copy
d = copy.deepcopy(a)          # (Deep copy for nested lists)
print(d)

# Modifying lists
a[0]=100
print(a[0])                   # lists are mutable unlike tuples and string

if 10 in nums:
    print("Found")            # same a scontains method of java

# TUPLES
t = (1,2,3,4)
tu = (1,)  # without comma its just int
# accessing, slicing, indexing are same as list
t[0] = 10    # Error- Tuples are immutable

point = (10,20)
(x,y) = point  # Unpacking in tuple

# Multiple assignment
a,b,c = (1,2,3)

#Swapping
a,b = b,a

tup = (1,[2,3])
tup[1].append(4)    # Valid - tuples are immutable but lists inside tuple can be mutated

# Tuples are fast, safe, used as keys in dict

#SET

s = {1,2,3}       # set initialization
s = set()      #empty set initialization, s={} is dict not set
# set characters are same as java unordered, no duplicates, fast lookup (O(1) on avg.)

a = {1,2,3}
b = {2,3,4}
a|b    # this will give set union i.e. 1,2,3,4
a&b    # this will give set intersection i.e. 2,3
a-b    # will give those that are in a but not in b i.e. only 1
a^b    # will give symmetric difference i.e. 1,4

#Frozen Sets
fs = frozenset([1,2,3])    # they are immutable sets i.e. thread safe and can be as dictionary keys

#set methods
s.add(0)
set.remove(0)
set.discard   # to remove safely
set.clear
# set.len()
# set.in()       # same as contains of java
"""

# DICTIONARY
# They are same as java except no generics, values can be type, and keys must be immutable

user = {"name" : "Arun",
        "position" : "Intern",
        "domain" : "Software Development"
        }

details = (user["name"], user["domain"])
print(details)
print(user.get("email", "NA"))     # default value (here NA) will print if email is not found

user["email"] = "arun@gmail.com"   # to add/update

# Some dictionary methods
user.keys()             # to get keys
user.values()           # to get values
user.items()            # to get items
user.pop("position")    # to pop item by key   
# user.len()
user.clear

# Nested Dictionaries
employee = {
    "id" : 1,
    "name" : "Akash",
    "Address" : {
        "city" : "Bhopal",
        "pin" : "462041"
    }
}

print(employee["Address"]["city"])  # to access nested fields

for key in user:
    print(key, user[key])      # to print all key values
            # OR
for key, value in user.items():
    print(key, value)


for value in user.values():    # to print all values only
    print(value)


squares = {x: x*x for x in range(5)}   # to store 1 to 5 squares in dictionary

if "name" in user:                   # to check if key exists
    print("Exists")


