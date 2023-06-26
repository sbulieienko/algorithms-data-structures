a = int(input())
b = int(input())
c = int(input())
 
if a + b > c or a + c > b or c + b > a:
    if a >= b and a >= c:
        if a ** 2 == b ** 2 + c ** 2:
            print('100%')
        if a ** 2 > b ** 2 + c ** 2:
            print('велика') 
        if a ** 2 < b ** 2 + c ** 2:
            print('крайне мала') 
    if b > a and b >= c:
        if b ** 2 == a ** 2 + c ** 2:
            print('100%') 
        if b ** 2 > a ** 2 + c ** 2:
            print('велика') 
        if b ** 2 < a ** 2 + c ** 2:
            print('крайне мала') 
    if c > a and c > b:
        if c ** 2 == a ** 2 + b ** 2:
            print('100%') 
        if c ** 2 > a ** 2 + b ** 2:
            print('велика')
        if c ** 2 < b ** 2 + a ** 2:
            print('крайне мала')