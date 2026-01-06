""" 
# Functions

def add(a, b):
    return a+b
result=add(10,70)
print(result)

def greet (name):
    return f"hello {name}"
print(greet("abhi"))


def get_point():           # multiple return values
    return 10, 20
x, y = get_point()
print(y,x)

def greet(name, msg="Hello"):            # default argument like method overloading of java (Python does not support method overloading)
    return f"{msg} {name}"
print(greet("Abhi"))

greet(msg = "hi", name = "Abhi")         # keyword arguments
print(greet(msg="welcome", name="Abhimanyu"))

def add_all(*args):                      # variable length args (Varargs)
    return sum(args)
print(add_all(3,4,5,6))

def func(**pwargs):
    print (pwargs)
func(name="Vaibhav", sirname="Malviya", age=25, role="devops")
                            # OR
def print_user(**kwargs):                # keyword Varargs
    for key, value in kwargs.items():
        print(key, value)
print_user(name="AbhimanyuSingh", age=25, active=True)

def add(a:int, b:int) -> int:            # type hints are not enforced at run time they are used by IDEs, FastAPI
    return a + b

def add_item(item, lst=[]):              # mutable default argument trap 
    lst.append(item)
    return lst

def square (x):                          # calling function stored in a variable (First class function)
    return x*x
f=square
print(f(5))
"""

def multiply(a, b):
    """
    Multiplies two numbers.         # this is document string
    """
    return a * b
print(multiply(3, 4))
print(multiply.__doc__)             # This will also print document string of multiply on console



# LAMBDA FUNCTION -- anonymous function written in a single line
square = lambda x: x*x            # returns implicitly unlike java
print(square(5)) 

# MAP -- transforms data 
nums=[1,2,3,4,5]
squares = list(map(lambda x: x*x, nums))
print(squares)

# FILTERS -- selecting data
nums = [4,5,6,7,8,9]

evens = list(filter(lambda x:x%2 == 0, nums))
