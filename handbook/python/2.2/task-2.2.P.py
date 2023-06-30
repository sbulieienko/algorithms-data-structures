v_petya = int(input())
v_vasya = int(input())
v_tolya = int(input())

v_max = max(v_petya, v_vasya, v_tolya)
v_min = min(v_petya, v_vasya, v_tolya)

if v_max == v_petya:
    first = ' ' * 10 + 'Петя' + ' ' * 10
elif v_max == v_vasya:
    first = ' ' * 10 + 'Вася' + ' ' * 10
else:
    first = ' ' * 10 + 'Толя' + ' ' * 10

if v_min == v_petya:
    third = ' ' * 18 + 'Петя' + ' ' * 2
elif v_min == v_vasya:
    third = ' ' * 18 + 'Вася' + ' ' * 2
else:
    third = ' ' * 18 + 'Толя' + ' ' * 2

if v_max != v_petya and v_min != v_petya:
    second = ' ' * 2 + 'Петя' + ' ' * 18
elif v_max != v_vasya and v_min != v_vasya:
    second = ' ' * 2 + 'Вася' + ' ' * 18
else:
    second = ' ' * 2 + 'Толя' + ' ' * 18

print(first)
print(second)
print(third)
print('   II      I      III   ')
