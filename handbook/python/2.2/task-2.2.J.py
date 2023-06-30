msg = input()

if len(msg) != 3:
    quit()

a = int(msg[-1]) + int(msg[-2])
b = int(msg[0]) + int(msg[1])

if a > b:
    print(str(a) + str(b))
else:    
    print(str(b) + str(a))


