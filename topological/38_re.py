import sys
from collections import deque

N = int(input())
M = int(input())
in_degree = [0] * (N+1)
graph = {i: [] for i in range(N+1)}
for _ in range(M):
    e, s, v = map(int, sys.stdin.readline().split())
    graph[s].append([e, v])
    in_degree[e] += 1

print(in_degree)
print(graph)

basic = []
q = deque()
needs = [0] * (N+1)
for i in range(1, N+1):
    if in_degree[i] == 0:
        basic.append(i)
        q.append(i)
while q:
    cur = q.popleft()
    # 연결된 중간부품 indegree-1
    # 가중치
    for adj, val in graph[cur]:
        if adj in basic:  # 기본 부품
            needs[cur] = graph[cur][0][1] + val
        else:  # 중간 부품
            needs[cur] = graph[cur][0][1] * val  # 지금까지 필요한 개수에 새로운 가중치 곱하기
        in_degree[adj] -= 1
print(needs)

for i in basic:
    print(i, needs[i])
