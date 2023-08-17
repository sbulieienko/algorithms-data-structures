list1 = []

while True:
    str1 = input()
    if str1.strip() == '':
        break
    list1.append(str1)

for str1 in list1:
    len1 = len(str1)
    if len1 >= 3:
        if str1[len1 - 3:] == '@@@':
            continue
    if len1 >= 2:
        if str1[:2] == '##':
            print(str1[2:])
        else:
            print(str1)
    else:
        print(str1)
