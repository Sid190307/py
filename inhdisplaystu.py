class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Students(Person):
    def __init__(self, name, age, roll_no):
        Person.__init__(self, name, age)
        self.roll_no = roll_no

    def display_Students(self):
        print("Roll no:",self.roll_no)

name = input("Enter Name:")
age = int(input("Enter Age:"))
roll_no = int(input("Enter Roll no:"))

s = Students(name, age, roll_no)

s.display_Students()
s.display_person()
