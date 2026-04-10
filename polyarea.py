class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        print("Area of Rectangle:", area)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of Circle:", area)

# Rectangle input
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

shape = Rectangle(length, breadth)
shape.area()

# Circle input
radius = float(input("\nEnter radius of circle: "))

shape = Circle(radius)
shape.area()
