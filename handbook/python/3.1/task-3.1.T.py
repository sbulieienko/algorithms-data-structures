def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


items = input()

items = items.split()

stack = []

for item in items:
    if item.isdigit():
        stack.append(int(item))
    else:
        if item == '*':
            a2 = stack.pop()
            a1 = stack.pop()
            stack.append(a1 * a2)
        elif item == '/':
            a2 = stack.pop()
            a1 = stack.pop()
            stack.append(a1 // a2)
        elif item == '+':
            a2 = stack.pop()
            a1 = stack.pop()
            stack.append(a1 + a2)
        elif item == '-':
            a2 = stack.pop()
            a1 = stack.pop()
            stack.append(a1 - a2)
        elif item == '~':
            a = stack.pop()
            stack.append(-a)
        elif item == '#':
            a = stack.pop()
            stack.append(a)
            stack.append(a)
        elif item == '!':
            a = stack.pop()
            stack.append(factorial(a))
        elif item == '@':
            a3 = stack.pop()
            a2 = stack.pop()
            a1 = stack.pop()
            stack.append(a2)
            stack.append(a3)
            stack.append(a1)
        

print(stack[-1])            
