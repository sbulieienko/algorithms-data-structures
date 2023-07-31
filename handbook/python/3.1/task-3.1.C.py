L = int(input())
N = int(input())

list1 = []

for i in range(N):
    list1.append(input())
 
for i in range(N):
    str1 = list1[i]
    if len(str1) > L:
        print(str1[:(L - 3)] + '...')
    else:
        print(str1)

