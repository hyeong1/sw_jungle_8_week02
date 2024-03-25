import sys
sys.setrecursionlimit(10**9)


# 메모리 초과, 시간 초과
def dfs(r, c):  # 0 이 아닌 칸 dfs 탐색
    visited[r][c] = True
    for d in range(4):
        if not visited[r + dr[d]][c + dc[d]] and (r + dr[d], c + dc[d]) in only_ice:
            dfs(r + dr[d], c + dc[d])


N, M = map(int, input().split())
ice_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
only_ice = set((i, j) for i in range(N) for j in range(M) if ice_map[i][j] != 0)  # 빙산 좌표만 저장
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]  # 북 동 남 서 (위에서 부터 시계 방향)
year = 0

while True:
    visited = [[False] * M for _ in range(N)]
    area = 0
    for x, y in only_ice:
        if not visited[x][y]:
            dfs(x, y)
            area += 1  # 탐색 횟수가 연결 영역
    if area == 0:
        print(0)
        break
    elif area > 1:
        print(year)
        break
    else:
        # 1년 동안 하는 일
        only_ice_copy = set(only_ice)
        for x, y in only_ice:
            down_val = sum(1 for d in range(4) if (x + dr[d], y + dc[d]) not in only_ice)
            ice_map[x][y] = max(ice_map[x][y] - down_val, 0)
            if ice_map[x][y] == 0:
                only_ice_copy.remove((x, y))
        only_ice = only_ice_copy
        year += 1

        # 확인용
        print(year, "년 후")
        for m in ice_map:
            print(m)
