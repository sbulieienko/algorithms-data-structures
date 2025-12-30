"""
На этот раз придётся справиться с выражением, в котором встречаются нестандартные логические операции: импликация, строгая дизъюнкция и эквивалентность.
Они не поддерживаются в Python напрямую, но вы сможете реализовать их самостоятельно.

Напишите программу, которая для заданного логического выражения строит таблицу истинности, включая поддержку следующих операций:

-> — импликация
^ — строгая дизъюнкция
~ — эквивалентность
Формат ввода
Вводится логическое выражение от нескольких переменных.

Возможное содержание выражения:

Заглавная латинская буква — переменная;
not — отрицание;
and — конъюнкция;
or — дизъюнкция;
^ — строгая дизъюнкция;
-> — импликация;
~ — эквивалентность;
() — логические скобки.
Формат вывода
Выведите таблицу истинности данного выражения.


Подсказка
Вспомните задачу "Польский калькулятор".

Пример 1
Ввод

A -> B ~ C
Вывод

A B C F
0 0 0 0
0 0 1 1
0 1 0 0
0 1 1 1
1 0 0 1
1 0 1 0
1 1 0 0
1 1 1 1
Пример 2
Ввод

A or C ~ not (A -> B) or C
Вывод

A B C F
0 0 0 1
0 0 1 1
0 1 0 1
0 1 1 1
1 0 0 1
1 0 1 1
1 1 0 0
1 1 1 1
"""
import sys
import re
from itertools import product


# Tokenize expression into variables, operators and parentheses
def tokenize(s):
	token_pattern = r"->|not|and|or|\(|\)|\^|~|[A-Z]"
	return re.findall(token_pattern, s)


# Convert infix tokens to postfix (RPN) using shunting-yard algorithm
def infix_to_postfix(tokens):
	prec = {'not': 5, 'and': 4, 'or': 3, '->': 2, '^': 2, '~': 1}
	# associativity: left = 'L', right = 'R'
	assoc = {'not': 'R', 'and': 'L', 'or': 'L', '->': 'R', '^': 'L', '~': 'L'}

	out = []
	stack = []
	for tok in tokens:
		if re.fullmatch(r"[A-Z]", tok):
			out.append(tok)
		elif tok in prec:
			while stack and stack[-1] != '(' and (
				(assoc[tok] == 'L' and prec[stack[-1]] >= prec[tok]) or
				(assoc[tok] == 'R' and prec[stack[-1]] > prec[tok])
			):
				out.append(stack.pop())
			stack.append(tok)
		elif tok == '(':
			stack.append(tok)
		elif tok == ')':
			while stack and stack[-1] != '(':
				out.append(stack.pop())
			if stack and stack[-1] == '(':
				stack.pop()
		else:
			# ignore unknown tokens/spaces
			pass

	while stack:
		out.append(stack.pop())
	return out


# Evaluate postfix expression given variable mapping
def eval_postfix(postfix, mapping):
	st = []
	for tok in postfix:
		if re.fullmatch(r"[A-Z]", tok):
			st.append(bool(mapping[tok]))
		elif tok == 'not':
			a = st.pop()
			st.append(not a)
		else:
			b = st.pop()
			a = st.pop()
			if tok == 'and':
				st.append(a and b)
			elif tok == 'or':
				st.append(a or b)
			elif tok == '->':
				st.append((not a) or b)
			elif tok == '^':
				st.append(a != b)
			elif tok == '~':
				st.append(a == b)
			else:
				st.append(False)
	return st[-1] if st else False


data = sys.stdin.read()
if data:
	expr = data.strip()
	if expr:
		tokens = tokenize(expr)
		postfix = infix_to_postfix(tokens)

		vars_list = sorted(set(re.findall(r"[A-Z]", expr)))
		if vars_list:
			print(' '.join(vars_list + ['F']))
			for combo in product((0, 1), repeat=len(vars_list)):
				mapping = {v: val for v, val in zip(vars_list, combo)}
				res = eval_postfix(postfix, mapping)
				row = [str(int(v)) for v in combo] + [str(int(bool(res)))]
				print(' '.join(row))
		else:
			print('F')
			try:
				# no variables: evaluate constant expression
				val = eval(expr, {}, {})
			except Exception:
				val = False
			print(str(int(bool(val))))
