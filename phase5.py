"""
class Student:
    __name: str            # not necessary to initialize variable like that, you can directly initialize with __init__
    __roll_no: int
    __age: int
    __gender = "male"      # static variable -- can be called directly like Person.gender

    def __init__(self, name, roll_no, age):
        self.name = name
        self.roll_no = roll_no
        self.age = age
 
    def show(self):
        print(self.name)

    def greet(self):
        return f"Hi, I'm {self.name}"

s = Student("Abhimanyu", 77, 26)

print(s.name)
print(s.roll_no)
print(s.age)

s.show()


# INHERITANCE
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):                  
    def bark(self):
        print("Woof")

d = Dog()
d.speak()
d.bark() 

# Method overriding  (same as java, before python 3.12 python doesn't require @Override)
class Reptiles:
    def eat(self):
        print("reptiles eat")

class Crocodiles(Reptiles):
    def eat(self):
        print("crocodiles Swallow")
Reptiles().eat()
Crocodiles().eat()

# POLYMORPHISM
def make_sound(animal):         # like void makeSound(Animal animal) { } in java, it will decide object type at runtime
    animal.speak()              # that's why it's called duck typing, if it walks like a duck, it's a duck

make_sound(Dog())
make_sound(Animal())
# make_sound(Reptiles())        # will give error because Reptile class is not inhereting Animals class

# ENCAPSULATION
class User:
    def __init__(self):
        self._email = "test@mail.com"     # SINGLE_ means protected
        self.__password = "secret"        # Double__ means private
User._email        # allowed (discouraged)
User.__password    # ❌ AttributeError

# ABSTRACTION
# python does not have abstract keyword or interface, but it has Abstract Base Class (ABC)

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        return 10
Shape()   # TypeError it cannot be instantiated

# Multiple Inheritance
class A:
    def show(self):
        print("A")
class B:
    def show(self):
        print("B")
class C(A, B):
    pass
C().show()   # using MRO (method resolution order)

# super keyword
class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")
Dog().speak()
"""