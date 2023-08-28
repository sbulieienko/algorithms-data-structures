items = input()

items = items.split()

stack = []

for item in items:
    if item.isdigit():
        stack.append(int(item))
    else:
        b = stack.pop()
        a = stack.pop()
        if item == '*':
            stack.append(a * b)
        elif item == '/':
            stack.append(a / b)
        elif item == '+':
            stack.append(a + b)
        elif item == '-':
            stack.append(a - b)

print(stack[-1])            
