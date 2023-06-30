n = int(input())

first = None

for i in range(n):
    name = input()
    if first is None:
        first = name
    if first > name:
        first = name

print(first)