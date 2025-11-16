"""
Create Rectangle and Square classes. Rectangle should have two instance variables: self.width and self.length. 
Square should have one instance variable self.s1. Define a method for both classes called calculate_perimeter 
that calculates the perimeter of the shapes they represent ad returns it. 
Then, create Rectangle and Square objects and call the method on both of them.
"""

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

class Square:
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return 4 * self.s1  

# Create Rectangle and Square objects
rectangle = Rectangle(4, 6)        
square = Square(5)

# Call the calculate_perimeter method on both objects
print("Rectangle perimeter:", rectangle.calculate_perimeter())
print("Square perimeter:", square.calculate_perimeter())
