n = int(input())
count1 = 0

for i in range(n):
    m = int(input())
    
    if m == 1:
        flag = False
    else:
        flag = True
    
    for j in range(2, m // 2 + 1):
        if m % j == 0:
            flag = False
            break
    if flag:
        count1 += 1 

print(count1)