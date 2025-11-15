"""
Create a module named cubed with a function that takes a number as a parameter, and returns the number cubed. 
Import and call the function from another module.
"""
from cubed import cube_number

number = 3
result = cube_number(number)
print(f"The cube of {number} is {result}")  # Output: The cube of 3 is 27