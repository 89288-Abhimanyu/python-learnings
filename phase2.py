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


# Collections
data = [1, "hello", 3.5, True]  # Python list can store mixed types. In java this is possible only with List<Objects>
# Slicing works same as String. While in java to do this loops or stream are required

#Some common List methods
data.append
data.insert(1,15)
data.remove(15)
data.pop()
data.len()
data.sort()
data.clear()