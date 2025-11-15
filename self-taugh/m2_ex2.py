"""
Define a method in your Square class called change_size that allows you to pass in a number 
that increases or decreases (if the number is negative) each side of a Square object by that number. 
Make sure your Square class's instance variable is self.s1.
"""

class Square:
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return 4 * self.s1  

    def change_size(self, amount):
        self.s1 += amount