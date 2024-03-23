import sys
from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s][e] = graph[e][s] = 1

visited_dfs = [0] * (N+1)
visited_bfs = visited_dfs.copy()


def dfs(node):
    visited_dfs[node] = 1
    print(node, end=" ")
    for i in range(1, N+1):
        if visited_dfs[i] == 0 and graph[node][i] == 1:
            dfs(i)

    # stack = [node]
    # while stack:
    #     cur = stack.pop()
    #     print(cur, end=" ")
    #     for i in range(1, N+1):
    #         if visited_dfs[i] == 0 and graph[cur][i] == 1:
    #             visited_dfs[i] = 1
    #             stack.append(i)
    #             break


def bfs(node):
    queue = deque([node])
    visited_bfs[node] = 1

    while queue:
        cur = queue.popleft()
        print(cur, end=" ")
        for i in range(1, N+1):
            if visited_bfs[i] == 0 and graph[cur][i] == 1: # 방문 하지 않았고, 현재 노드에서 갈 수 있으면 방문
                visited_bfs[i] = 1
                queue.append(i)


dfs(V)
print()
bfs(V)
