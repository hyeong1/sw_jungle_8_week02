import sys
t = int(input())
tops = list(map(int, sys.stdin.readline().split()))
stack = []

# 시간초과
# for i in range(t-1, -1, -1):
#     for j in range(i-1, -1, -1):
#         if tops[i] < tops[j]:
#             check.append(j+1)
#             break
#         while tops[i] >= tops[j]:
#             if j == 0:
#                 check.append(0)
#                 break
#             j -= 1
# check.append(0)  # 마지막은 무조건 못 받음
# for c in reversed(check):
#     print(c, end=" ")

answer = [0] * t
for i in range(t-1, -1, -1):
    if not stack:
        stack.append([i, tops[i]])
        continue
    if tops[i] > stack[-1][1]:
        while stack and tops[i] > stack[-1][1]:
            answer[stack[-1][0]] = i + 1
            stack.pop()
        stack.append([i, tops[i]])
    if tops[i] < stack[-1][1]:
        stack.append([i, tops[i]])

for c in answer:
    print(c, end=" ")
