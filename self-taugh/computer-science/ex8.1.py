"""
Измените свою программу сбалансированных строк ex8.py, чтобы проверить, 
сбалансированы ли в строке круглые скобки () и фигурные скобки {}.
"""
def check_balanced_parentheses(s):
    stack = []
    opening = {'(': ')', '{': '}'}
    closing = {')', '}'}
    
    for char in s:
        if char in opening:
            # Добавляем открывающую скобку в стек
            stack.append(char)
        elif char in closing:
            # Проверяем наличие соответствующей открывающей скобки
            if not stack:
                return False
            last_opening = stack.pop()
            # Проверяем, что закрывающая скобка соответствует открывающей
            if opening[last_opening] != char:
                return False
    
    # В конце стек должен быть пуст
    return len(stack) == 0


# Примеры использования
print(check_balanced_parentheses("(a + b) * (c + d)"))  # True
print(check_balanced_parentheses("(a + b) * (c + d))"))  # False
print(check_balanced_parentheses("((a + b) * (c + d))"))  # True
print(check_balanced_parentheses("{a + (b * c)}"))  # True
print(check_balanced_parentheses("{a + (b * c}"))  # False
print(check_balanced_parentheses("({a + b) * (c + d]}"))  # False