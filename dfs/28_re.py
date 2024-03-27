import sys
sys.setrecursionlimit(10**9)


def dfs(r, c):
    visited[r][c] = True
    for d in range(4):
        if not visited[r + dr[d]][c + dc[d]] and (r + dr[d], c + dc[d]) in ice:
            dfs(r + dr[d], c + dc[d])


R, C = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
year = 0
ice = set((i, j) for i in range(R) for j in range(C) if graph[i][j] > 0)
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

# 1년 동안 하는 일 (BFS로 빙산 녹이기)
while True:
    # 연결 유무를 칸이 0이 아닌 걸로 체크
    visited = [[False] * C for _ in range(R)]
    count = 0
    for a, b in ice:
        if not visited[a][b] and graph[a][b] != 0:
            dfs(a, b)
            count += 1
    if count > 1:
        print(year)
        break
    elif count == 0:
        print(0)
        break
    else:
        copy_ice = set(ice)
        for cur_r, cur_c in ice:
            cnt = sum(1 for d in range(4) if (cur_r + dr[d], cur_c + dc[d]) not in ice)
            graph[cur_r][cur_c] = max(graph[cur_r][cur_c] - cnt, 0)
            if graph[cur_r][cur_c] == 0:
                copy_ice.remove((cur_r, cur_c))
        ice = copy_ice
        year += 1
