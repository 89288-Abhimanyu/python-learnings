name = "Abhimanyu Singh"
age: int=26
bornYear = int(input("Which Year did you born")) #input with print statement and casting is mandatory in python
role, department = "Intern", "Development"

print(name, age, role, department)

print(f"Name: {name}, Age: {age}, BornYear: {bornYear}, Role: {role}, Department: {department}")


c = 3 + 4j
print(c.real, c.imag)

is_Active= True #case sensitive

x=10
type(x)  #will print class

y = int(10.5)
z = bool(1)  # only explicit type casting is allowed

d = 5/2 # 2.5
dd = 5//2 #2 i.e. ceiling division

p = 2**3 # 8 i.e. power operator

x = 10
5 < x < 20   # True

# and or not in java && || !

nums = [2,4,5]
print(2 in nums) # True
print (5 in nums) # True

g = [1, 2]
h = [1, 2]

g == h   # True (value) i.e. "==" in python means ".equals" of java
g is h   # False (different objects) i.e. "is" in python means "==" of java

print("A", "B", "C", sep="-", end="!") #A-B-C!


#Escape Characters

# Escape      |      Meaning      |

 # `\n`               New line
 #`\t`               Tab          
 #`\\`               Backslash    
 #`\"`               Double quote 
 #`\'`               Single quote

print("Hello\nWorld")
print("Name:\tAbhi")

# Multiline Strings
message = """
Hello Abhi,
Welcome to Python.
"""
print(message)
