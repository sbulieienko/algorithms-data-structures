msg1 = input()
msg2 = input()
msg3 = input()

list1 = [msg1, msg2, msg3]

list1.sort()

for msg in list1:
    if 'зайка' in msg:
        print(msg, len(msg))
        quit()

