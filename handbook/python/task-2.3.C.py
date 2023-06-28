a = int(input())
b = int(input())

answer = ''

for i in range(a, b + 1):
    if len(answer) == 0:
        answer = str(i)
    else:
        answer = answer + ' ' + str(i)

print(answer)