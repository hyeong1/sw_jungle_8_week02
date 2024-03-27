from collections import deque

X, Y, Z = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(Y)] for _ in range(Z)]

q = deque()
for i in range(Z):
    for j in range(Y):
        for k in range(X):
            if graph[i][j][k] == 1:
                q.append([i, j, k])

direction = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1]]
while q:
    z, y, x = q.popleft()
    for d in direction:
        nz, ny, nx = z + d[0], y + d[1], x + d[2]
        if (0 <= nz < Z) and (0 <= nx < X) and (0 <= ny < Y):
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                q.append([nz, ny, nx])

result = 0
cannot_complete = False
for i in range(Z):
    for j in range(Y):
        for k in range(X):
            if graph[i][j][k] == 0:
                cannot_complete = True
            result = max(result, graph[i][j][k])

if cannot_complete:
    print(-1)
else:
    print(result - 1)
