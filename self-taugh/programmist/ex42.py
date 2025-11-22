"""
Reverse the string "yesterday" using a stack and print it. You should use a class called Stack.
You need to define a push and pop method in your class.
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")
    
    def len(self):
        return len(self.items)

def reverse_string(input_string):
    stack = Stack()
    
    # Push all characters of the string onto the stack
    for char in input_string:
        stack.push(char)
    
    reversed_string = ""
    
    # Pop all characters from the stack to get them in reverse order
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage
input_str = "yesterday"
print(reverse_string(input_str))    # Output: yadretsey
