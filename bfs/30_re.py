import sys
from collections import deque

R, C = map(int, input().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(R)]

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
q = deque()
q.append([0, 0])

visited = [[False] * C for _ in range(R)]
while q:
    r, c = q.popleft()
    visited[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] == 1 and not visited[nr][nc]:
            q.append([nr, nc])
            maze[nr][nc] = maze[r][c] + 1  # 막힌 길 되돌아 오는 처리 대신 maze 배열에 바로 경로 더함

print(maze[R-1][C-1])
