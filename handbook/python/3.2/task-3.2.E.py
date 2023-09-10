N = int(input())
M = int(input())

list1 = list()
only_one = 0

for _ in range(N + M):
    name = input()
    if name not in list1:
        list1.append(name)
        only_one += 1
    else:
        only_one -= 1

if only_one == 0:
    print('Таких нет')
else:
    print(only_one)
