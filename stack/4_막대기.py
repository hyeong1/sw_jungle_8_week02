t = int(input())
stack = []

for i in range(t):
    current = int(input())
    while stack and stack[-1] <= current:
        stack.pop()
    stack.append(current)

print(len(stack))

# 2
# sp = -1
# for i in range(t):
#     current = int(input())
#     if len(stack) == 0:
#         stack.append(current)
#         sp += 1
#     else:
#         if current < stack[-1]:
#             stack.append(current)
#             sp += 1
#         else:
#             while sp != -1 and current >= stack[sp]:
#                 stack.pop()
#                 sp -= 1
#             if len(stack) == 0:
#                 stack.append(current)
#                 sp += 1
#             elif current != stack[-1]:
#                 stack.append(current)
#                 sp += 1
#
# print(len(stack))

# 3
# import sys
# sticks = []
# for i in range(t):
#     sticks.append(int(sys.stdin.readline()))
# 
# count = 0
# max_h = 0
# for s in reversed(sticks):
#     if s > max_h:
#         count += 1
#         max_h = s
# 
# print(count)
