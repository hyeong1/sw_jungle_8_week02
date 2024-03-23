import sys
sys.setrecursionlimit(10**6)


def dfs(graph, node, visited):
    global result
    if visited[node]:
        return
    visited[node] = True
    for i in range(1, N+1):
        if not visited[i] and graph[node][i]:  # 아직 방문 하지 않았고 연결 되어 있으면 탐색
            dfs(graph, i, visited)
            result += 1


N, M = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]
result = 0
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = True

count = 0
visited = [False] * (N+1)
for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)
