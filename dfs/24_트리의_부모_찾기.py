import sys
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(N-1):  # 트리 생성
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(node):
    for nxt in tree[node]:
        if visited[nxt] == 0:
            visited[nxt] = node
            dfs(nxt)


dfs(1)
for i in range(2, N+1):
    print(visited[i])
