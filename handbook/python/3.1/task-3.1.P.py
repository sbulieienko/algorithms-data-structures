length = int(input())
N = int(input())

lines = []

for _ in range(N):
    lines.append(input())

for line in lines:
    if length > 3:
        if len(line) >= length - 3:
            print(line[:length - 3] + "...")
        elif length == 4:
            print(line + "...")
        else:
            print(line)
        length -= len(line)
