import sys
stack = []
sp = -1

n = int(input())
for i in range(n):
    input_str = sys.stdin.readline().split()
    if input_str[0] == "push":
        stack.append(input_str[1])
        sp += 1
    if input_str[0] == "pop":
        if sp > -1:
            print(stack.pop())
            sp -= 1
        else:
            print(sp)
    if input_str[0] == "size":
        print(sp + 1)
    if input_str[0] == "empty":
        print(1 if sp == -1 else 0)
    if input_str[0] == "top":
        if sp > -1:
            print(stack[sp])
        else:
            print(sp)
