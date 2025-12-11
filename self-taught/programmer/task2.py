"""
Write a program with an infinite loop and a list of numbers.
Each time through the loop the program should ask the user to guess a number
(or type q to quit). If they type q, the program should end.
Otherwise, it should tell them whether or not they successfully guessed a number
in the list or not.
"""

numbers = [3, 7, 12, 19, 25, 30]
while True:
    user_input = input("Guess a number (or type 'q' to quit): ")
    if user_input.lower() == 'q':
        print("Goodbye!")
        break
    try:
        guess = int(user_input)
        if guess in numbers:
            print("Congratulations! You guessed a number in the list.")
        else:
            print("Sorry, that number is not in the list.")
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")