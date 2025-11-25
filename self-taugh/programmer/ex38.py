"""
Create a Square class that has one method that calculates its perimeter. When you print a Square object, 
a message should print telling you the length of each of the four sides of the shape. 
For example, the code print(Square(29))  should print "29 by 29 by 29 by 29".
"""

class Square:

    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        Square.square_list.append(self)

    def calculate_perimeter(self):
        return 4 * self.s1

    def __str__(self):
        return f"{self.s1} by {self.s1} by {self.s1} by {self.s1}"

# Example usage:
square = Square(29)      
print(square)  # This will print "29 by 29 by 29 by 29"
print("Perimeter:", square.calculate_perimeter())  # This will print the perimeter of the square
