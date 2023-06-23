x = input()
y = input()

len_x = len(x)
len_y = len(y)

if len_x >= len_y:
    max = len_x
else:
    max = len_y

x = x[::-1]
y = y[::-1]

z = ''

for i in range(0, max):
    if i < len_x:
        a = int(x[i])
    else:
        a = 0
    if i < len_y:
        b = int(y[i])
    else:
        b = 0
    z = z + str(a + b)[-1]

z = z[::-1]

print(int(z))    
