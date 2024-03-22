n, k = map(int, input().split())
num_str = input()
stack = []
check = k

for i in range(n):
    while (check > 0) and stack and (num_str[i] > stack[-1]):
        stack.pop()
        check -= 1
    stack.append(num_str[i])

print("".join(stack[:n-k]))
