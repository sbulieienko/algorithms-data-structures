lines = []

while True:
    line = input()
    if len(line) == 0:
        break
    lines.append(line)

for line in lines:
    if line.startswith('#'):
        continue
    try:
        indx = line.index('#')
        print(line[:indx])
    except Exception:
        print(line)