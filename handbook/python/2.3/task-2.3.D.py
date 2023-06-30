a = int(input())
b = int(input())

answer = ''

if a <= b:
    for i in range(a, b + 1):
        if len(answer) == 0:
            answer = str(i)
        else:
            answer = answer + ' ' + str(i)
else:
    for i in range(a, b - 1, -1):
        if len(answer) == 0:
            answer = str(i)
        else:
            answer = answer + ' ' + str(i)

print(answer)
