class rectangle:
    number = 1

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area (self):
        a = (self.length * self.breadth)
        print("Area of the rectangle is: ", a)

    def perimeter (self):
        p = 2 * (self.length + self.breadth)
        print("Area of the rectangle is: ", p)

length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

rect1 = rectangle(length,breadth)

print("----------------------------------------")
 
print("This is class variable:")
print("number: ",rectangle.number)

print("----------------------------------------")

print("These are instance variable:")
print("Length: ",rect1.length)
print("Breadth: ",rect1.breadth)

print("---------------------------------------")

print("Area: ",rect1.area()," Perimeter: ",rect1.perimeter())

print("---------------------------------------")

print("Changing the class variable")
rectangle.number = 2

print("After changing the class variable: ",rectangle.number) 
