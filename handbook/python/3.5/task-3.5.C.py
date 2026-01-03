"""
Как вы помните, когда вы комментируете свой код, перед его выполнением интерпретатор удаляет комментарии.
Напишите программу, которая выполняет эту функцию — удаляет комментарии из кода.

Формат ввода
Вводятся строки программы.

Формат вывода
Каждую строку нужно очистить от комментариев.
А если комментарий — вся строка, то выводить её не нужно.


Подсказка
Задача аналогична задаче I из параграфа 3.1 за исключением метода ввода данных.

Пример 1
Ввод

# Моя первая супер-пупер программа
print("What is your name?") #  Как тебя зовут?
name = input() #  Сохраняем имя
print(f"Hello, {name}!") #  Здороваемся# Конец моей супер-пупер программы
Вывод

print("What is your name?")
name = input()
print(f"Hello, {name}!")
Пример 2
Ввод

# Мой первый цикл
for i in range(10): # Считаем до 10
    print(i) # выводим число
Вывод

for i in range(10):
    print(i)
"""

from sys import stdin
lines = []
for line in stdin:
    lines.append(line.rstrip('\n'))
for line in lines:
    if line.startswith('#'):
        continue
    try:
        indx = line.index('#')
        print(line[:indx].rstrip())
    except Exception:
        print(line)