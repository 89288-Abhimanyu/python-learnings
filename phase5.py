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