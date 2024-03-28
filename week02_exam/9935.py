string = input()
bomb = list(input().strip())

stack = []
for s in string:
    stack.append(s)
    if stack[-len(bomb):] == bomb:
        for i in range(len(bomb)):
            stack.pop()

result = ''.join(stack)
if result:
    print(result)
else:
    print("FRULA")
