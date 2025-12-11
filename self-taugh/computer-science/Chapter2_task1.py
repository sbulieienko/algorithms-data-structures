"""
Выведите числа от 1 до 10 рекурсивно.
"""

def print_numbers(n):
    if n == 1:
        print(1)
    else:
        print_numbers(n - 1)
        print(n)

print_numbers(10)
