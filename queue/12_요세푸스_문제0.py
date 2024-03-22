from collections import deque

N, K = map(int, input().split())
people = deque(str(i+1) for i in range(N))
answer = []

while people:
    people.rotate(-(K-1))
    answer.append(people.popleft())

print("<", end="")
print(", ".join(answer), end="")
print(">")
