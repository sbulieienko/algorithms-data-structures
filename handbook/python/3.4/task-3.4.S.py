"""
Теперь выражения могут содержать переменное количество переменных, обозначенных заглавными латинскими буквами.

Напишите программу, которая строит таблицу истинности для заданного логического выражения.

Формат ввода
Вводится логическое выражение от нескольких переменных валидное для языка Python. Все переменные заданы заглавными латинскими буквами.

Формат вывода
Выведите таблицу истинности данного выражения.

Подсказка
Подсчитайте количество переменных и организуйте их перебор с помощью итератора product.

На каждой итерации перебора сформируйте словарь с представлением переменных, 
а затем передайте его в качестве параметра __globals или __locals в функцию eval.

Пример 1

Ввод:
not A or B and C

Вывод:
A B C F
0 0 0 1
0 0 1 1
0 1 0 1
0 1 1 1
1 0 0 0
1 0 1 0
1 1 0 0
1 1 1 1

Пример 2

Ввод:
A and not B and A

Вывод:
A B F
0 0 0
0 1 0
1 0 1
1 1 0
"""

import sys
import re
from itertools import product

data = sys.stdin.read()
if data:
    expr = data.strip()
    if expr:
        vars_list = sorted(set(re.findall(r"[A-Z]", expr)))

        if vars_list:
            print(' '.join(vars_list + ['F']))
            for combo in product((0, 1), repeat=len(vars_list)):
                mapping = {v: bool(val) for v, val in zip(vars_list, combo)}
                try:
                    res = eval(expr, {}, mapping)
                except Exception:
                    res = False
                row_vals = [str(int(v)) for v in combo]
                row_vals.append(str(int(bool(res))))
                print(' '.join(row_vals))
        else:
            print('F')
            try:
                res = eval(expr, {}, {})
            except Exception:
                res = False
            print(str(int(bool(res))))