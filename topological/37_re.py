import sys
from collections import deque

N, M = map(int, input().split())
in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    in_degree[e] += 1
    graph[s].append(e)

q = deque()
for i in range(1, N+1):
    if not visited[i] and in_degree[i] == 0:
        q.append(i)
    while q:
        node = q.popleft()  # 노드를 방문 하는 순간
        visited[node] = True
        print(node, end=" ")
        for adj in graph[node]:
            in_degree[adj] -= 1
            if in_degree[adj] == 0:
                q.append(adj)
