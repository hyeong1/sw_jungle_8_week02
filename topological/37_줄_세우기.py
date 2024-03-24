import sys
from collections import deque

N, M = map(int, input().split())
in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]  # 인접 그래프
visited = [False] * (N+1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    in_degree[b] += 1  # in_degree 설정
    graph[a].append(b)


# BFS
def topological_sort():
    queue = deque()
    result = []
    for i in range(1, N+1):
        if not visited[i] and in_degree[i] == 0:
            queue.append(i)
            visited[i] = True
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for v in graph[vertex]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    for r in result:
        print(r, end=" ")


topological_sort()
