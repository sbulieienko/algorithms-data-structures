"""
Вам дана строка. Используйте стек для проверки наличия в ней сбалансированных круглых скобок. 
То есть нужно проверить, что за каждой открывающей круглой скобкой следует закрывающая круглая скобка.
"""
def check_balanced_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

# Примеры использования
print(check_balanced_parentheses("(a + b) * (c + d)"))
print(check_balanced_parentheses("(a + b) * (c + d))"))  # False
print(check_balanced_parentheses("((a + b) * (c + d))"))
