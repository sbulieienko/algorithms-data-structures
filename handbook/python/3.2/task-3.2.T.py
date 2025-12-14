"""
Напомним, что взаимно простыми называются числа, которые не имеют общих делителей, кроме 1.

Напишите программу, которая:

получает список чисел, разделённых точкой с запятой и пробелом;
для каждого числа определяет, с какими другими числами оно взаимно просто;
выводит результат в порядке возрастания чисел без повторений;
если для числа не найдено ни одного взаимно простого числа — его не нужно выводить вовсе.
Формат ввода
Задана последовательность чисел записанных через точку с запятой (;) и пробел.

Формат вывода
Список чисел с указанием взаимно простых ему среди переданных.
Все числа должны быть выведены в порядке возрастания без повторений.
Строки следует отформатировать по правилу:
число - взаимно простое 1, взаимно простое 2, ...
Если для числа не было найдено ни одного взаимно простого, то и выводить его не требуется.

Подсказка
Рассмотрите все возможные пары чисел.
Если два числа a и b являются взаимно простыми, то по ключу a в список добавьте b и наоборот.

Пример
Ввод:
7; 2; 2; 12; 14; 7; 2; 49

Вывод:
2 - 7, 49
7 - 2, 12
12 - 7, 49
49 - 2, 12
"""

numbers = list(map(int, input().split("; ")))

divisors = dict()
for number in numbers:
    divisors[number] = set()
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors[number].add(i)
            divisors[number].add(number // i)

relatively_prime_numbers = dict()
for number in divisors.keys():
    for i in divisors.keys():
        if i != number and divisors[number].intersection(divisors[i]) == {1}:
            if number not in relatively_prime_numbers:
                relatively_prime_numbers[number] = set()
            relatively_prime_numbers[number].add(i)
            if i not in relatively_prime_numbers:
                relatively_prime_numbers[i] = set()
            relatively_prime_numbers[i].add(number)

for number in sorted(relatively_prime_numbers.keys()):
    print(number, "-", ", ".join(map(str, sorted(relatively_prime_numbers[number]))))
