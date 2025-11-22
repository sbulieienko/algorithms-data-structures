"""
Add a square_list class variable to a class called Square and set your class up so that every time you create a new Square object, 
the new object gets added to the square_list.
"""

class Square:

    square_list = []


    def __init__(self):
        Square.square_list.append(self)
