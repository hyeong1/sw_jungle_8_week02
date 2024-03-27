import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
heavy = [[] * (N+1) for _ in range(N+1)]
light = [[] * (N+1) for _ in range(N+1)]
adj_count = [0] * (N+1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    heavy[u].append(v)
    light[v].append(u)


def dfs(graph, node):
    count = 0
    for adj in graph[node]:
        if not visited[adj]:
            visited[adj] = True
            count += 1 + dfs(graph, adj)
    return count


mid = (N + 1) / 2
cnt = 0
for i in range(1, N+1):
    visited = [False] * (N + 1)
    if dfs(heavy, i) >= mid:
        cnt += 1
    if dfs(light, i) >= mid:
        cnt += 1

print(cnt)
