str1 = input()

set1 = set()

for char in str1:
    set1.add(char)

str2 = ''

for char in set1:
    str2 += str(char)

print(str2)    
