import sys
sys.setrecursionlimit(10**6)


def dfs(node):
    for nxt in graph[node]:
        if visited[nxt] == 0:  # 이미 방문한 노드는 방문 하지 않음. for 문 밖에서 visited 체크를 하면 현재 노드만 확인함
            visited[nxt] = node
            dfs(nxt)


N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
for i in range(2, N + 1):
    print(visited[i])
