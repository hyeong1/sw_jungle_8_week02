ps = input()
stack = []

answer = 0
tmp = 1
for i in range(len(ps)):
    if ps[i] == "(":
        if i == len(ps) - 1:
            answer = 0
        stack.append(ps[i])
        tmp *= 2
        continue
    if ps[i] == "[":
        if i == len(ps) - 1:
            answer = 0
        stack.append(ps[i])
        tmp *= 3
        continue
    if ps[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        elif ps[i-1] == "(":
            answer += tmp
        tmp //= 2
        stack.pop()
    if ps[i] == "]":
        if not stack or stack[-1] == "(":
            answer = 0
            break
        elif ps[i-1] == "[":
            answer += tmp
        tmp //= 3
        stack.pop()
    if i == len(ps)-1 and stack:
        answer = 0


print(answer)
