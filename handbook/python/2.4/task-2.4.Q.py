n = int(input())
count = 0
for i in range(n):
    d = input()
    if d == d[::-1]:
        count += 1
print(count)