"""
Create a class called Shape. Define a method in it called what_am_i that prints "I am a shape" when called. 
Change your Square and Rectangle classes from the previous challenges to inherit from Shape, 
create Square and Rectangle objects, and call the new method on both of them.
"""

class Shape:
    def what_am_i(self):
        print("I am a Shape")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

    def what_am_i(self):
        print("I am a Rectangle")


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return 4 * self.s1  

    def what_am_i(self):
        print("I am a Square")

# Create objects
shape = Shape()
rectangle = Rectangle(4, 6)        
square = Square(5)

# Call the what_am_i method on objects
shape.what_am_i()
rectangle.what_am_i()
square.what_am_i()