v_petya = int(input())
v_vanya = int(input())
v_tolya = int(input())

v_max = max(v_petya, v_vanya, v_tolya)

if v_max == v_petya:
    print('Петя')
elif v_max == v_vanya:
    print('Вася')
else:
    print('Толя')
