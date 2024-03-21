t = int(input())
answer = ["NO", "YES"]

for i in range(t):
    stack = []
    ps = input()
    for p in ps:
        if p == "(":
            stack.append(p)
        else:
            if len(stack) == 0 or stack[-1] != "(":
                stack.append(p)
            elif stack[-1] == "(":
                stack.pop()
    if len(stack) == 0:
        print(answer[1])
    else:
        print(answer[0])
