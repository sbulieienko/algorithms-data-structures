N, M = int(input()), int(input())

un_list = list()

for _ in range(N + M):
    secondname = input()
    if secondname in un_list:
        un_list.remove(secondname)
    else:
        un_list.append(secondname)

if len(un_list):
    for secondname in sorted(un_list):
        print(secondname)
else:
    print('Таких нет')

