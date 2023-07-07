
n = int(input())
w = int(input())

for x in range(1, n + 1):
    row = ''
    for y in range(1, n + 1):
        if w % 2 == 0:
            cell = str(x * y)
        else:
            cell = str(x * y) + ' '
        
        if row == '':
            row = cell.center(w)
        else:
            row += '|' + cell.center(w)
    
    print(row)
    if x < n:
        print('-' * len(row))
