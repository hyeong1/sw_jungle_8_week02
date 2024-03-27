from collections import deque

N = int(input())
maze = [list(input().rstrip()) for _ in range(N)]
visited = [[float("inf")] * N for _ in range(N)]  # 방문 체크와 동시에 뚫은 방의 개수 저장

q = deque()
q.append([0, 0])
visited[0][0] = 0

while q:
    cur_r, cur_c = q.popleft()
    for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:  # 북 동 남 서
        nr, nc = cur_r + dr, cur_c + dc
        if (nr >= 0) and (nr < N) and (nc >= 0) and (nc < N):
            if maze[nr][nc] == '1':
                if visited[nr][nc] > visited[cur_r][cur_c]:  # 새로 뚫을 방 개수 보다 지금 까지 뚫은 방 개수가 적으면 갱신
                    visited[nr][nc] = visited[cur_r][cur_c]
                    q.append([nr, nc])
            else:  # 검은 방이면
                if visited[nr][nc] > visited[cur_r][cur_c] + 1:
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
                    q.append([nr, nc])

print(visited[N-1][N-1])
