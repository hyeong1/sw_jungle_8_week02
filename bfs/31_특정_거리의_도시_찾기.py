import sys
from collections import deque


def bfs(node):
    answer = []
    queue = deque([node])
    visited[node] = True
    dist[node] = 0

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                dist[i] = dist[now] + 1
                if dist[i] == K:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for v in answer:
            print(v)


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

dist = [0] * (N+1)
visited = [False] * (N+1)
bfs(X)
