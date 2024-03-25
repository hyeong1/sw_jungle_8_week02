import sys
sys.setrecursionlimit(10**6)


def dfs(node, color):
    global check_bipartite
    colors[node] = color
    for adj in graph[node]:
        if colors[adj] == color:
            check_bipartite = False
            return
        if colors[adj] == 0:
            dfs(adj, -color)


t = int(input())
for _ in range(t):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    colors = [0] * (V+1)  # visited 확인 + 정점 색깔 확인
    check_bipartite = True
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, V+1):
        if not check_bipartite:  # 중간에 이분 그래프가 안되는 경우 체크
            break
        if colors[i] == 0:
            dfs(i, 1)
    if check_bipartite:
        print("YES")
    else:
        print("NO")

