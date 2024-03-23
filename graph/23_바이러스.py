import sys

c = int(input())
pair = int(input())
graph = [[False] * (c+1) for _ in range(c+1)]
for _ in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = True

visited = [False] * (c+1)
count = 0


def dfs(graph, node, visited):
    global count
    if visited[node]:
        return
    visited[node] = True
    for i in range(c+1):
        if not visited[i] and graph[node][i]:
            dfs(graph, i, visited)
            count += 1


dfs(graph, 1, visited)
print(count)
