N = int(input())

lines = []

for _ in range(N):
    lines.append(input())

search = input()

for line in lines:
    if line.lower().find(search.lower()) != -1:
        print(line)
