N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()


def dfs(node):
    global visited

    visited[node] = True
    print(node, end=" ")
    for adj in graph[node]:
        if not visited[adj]:
            dfs(adj)


dfs(V)
