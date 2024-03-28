import sys
import heapq

N, M = map(int, input().split())
in_degree = [0] * (N+1)
graph = [[] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    in_degree[e] += 1
    graph[s].append(e)

prev = []
for i in range(1, N+1):
    if in_degree[i] == 0:
        heapq.heappush(prev, i)

result = []
while prev:
    cur = heapq.heappop(prev)
    for adj in graph[cur]:
        in_degree[adj] -= 1
        if in_degree[adj] == 0:
            heapq.heappush(prev, adj)
    result.append(cur)

for r in result:
    print(r, end=" ")
