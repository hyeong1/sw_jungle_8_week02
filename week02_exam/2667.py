import sys
from collections import deque


def dfs(r, c):
    global count
    visited[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and MAP[nr][nc] == 1 and not visited[nr][nc]:
            house.remove([nr, nc])
            count += 1
            dfs(nr, nc)


N = int(input())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
house = deque()

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            house.append([i, j])

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = [[False] * N for _ in range(N)]
result = []
while house:
    cur_r, cur_c = house.popleft()
    count = 1
    dfs(cur_r, cur_c)
    result.append(count)

print(len(result))
result.sort()
for r in result:
    print(r)

