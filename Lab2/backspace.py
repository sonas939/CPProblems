str = input()
stack = []
for i in str:
    if i == '<':
        stack.pop()
    else:
        stack.append(i)
print(''.join(stack))