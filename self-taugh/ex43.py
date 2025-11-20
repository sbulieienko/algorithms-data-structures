"""
Use a stack to create a new list with the items in the following list reversed: [1, 2, 3, 4, 5]
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

def reverse_list(input_list):
    stack = Stack()
    
    # Push all items of the list onto the stack
    for item in input_list:
        stack.push(item)
    
    reversed_list = []
    
    # Pop all items from the stack to get them in reverse order
    while not stack.is_empty():
        reversed_list.append(stack.pop())
    
    return reversed_list

# Example usage
input_list = [1, 2, 3, 4, 5]
print(reverse_list(input_list))    # Output: [5, 4, 3, 2, 1]