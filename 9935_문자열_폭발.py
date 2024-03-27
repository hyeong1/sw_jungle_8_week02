string = input()
bomb = input()

stack = []
for s in string:
    stack.append(s)
    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

result = ''.join(stack)
if result:
    print(result)
else:
    print("FRULA")
