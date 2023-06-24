v_petya = int(input())
v_vasya = int(input())
v_tolya = int(input())

v_max = max(v_petya, v_vasya, v_tolya)
v_min = min(v_petya, v_vasya, v_tolya)

if v_max == v_petya:
    first = 'Петя'
elif v_max == v_vasya:
    first = 'Вася'
else:
    first = 'Толя'

if v_min == v_petya:
    third = 'Петя'
elif v_min == v_vasya:
    third = 'Вася'
else:
    third = 'Толя'

if v_max != v_petya and v_min != v_petya:
    second = 'Петя'
elif v_max != v_vasya and v_min != v_vasya:
    second = 'Вася'
else:
    second = 'Толя'

print(f"1. {first}")
print(f"2. {second}")
print(f"3. {third}")
