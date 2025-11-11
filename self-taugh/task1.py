"""
Write a program that asks the user to type a number. Convert the number to an integer and print it. 
If you can't convert their input to an integer, print a message that says "Please type an integer."
"""

user_input = input("Please type a number: ")

try:
    number = int(user_input)
    print("You typed the number:", number)
except ValueError:
    print("Please type an integer.")