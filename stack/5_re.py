# 괄호
ps = input()
stack = []

answer = 0
tmp = 1
for i in range(len(ps)):
    if ps[i] == '(':
        if i == len(ps) - 1:
            answer = 0
        else:
            stack.append(ps[i])
            tmp *= 2
    elif ps[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        elif ps[i-1] == '(':  # 문자열 바로 이전이 닫는 괄호일 때만 답에 더하기
            answer += tmp
        tmp //= 2
        stack.pop()
    elif ps[i] == '[':
        if i == len(ps) - 1:
            answer = 0
        else:
            stack.append(ps[i])
            tmp *= 3
    elif ps[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
        elif ps[i-1] == '[':  # 문자열 바로 이전이 닫는 괄호일 때만 답에 더하기
            answer += tmp
        tmp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(answer)
