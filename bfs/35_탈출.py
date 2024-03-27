from collections import deque

R, C = map(int, input().split())
forrest = [list(input().rstrip()) for _ in range(R)]
dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]

water = deque()
animal = deque()

for i in range(R):
    for j in range(C):
        if forrest[i][j] == '*':
            water.append([i, j])
        if forrest[i][j] == 'S':
            animal.append([i, j, 0])


def bfs():
    while animal:
        # 물 확장
        for _ in range(len(water)):
            r_w, c_w = water.popleft()
            for k in range(4):
                nr_w = r_w + dr[k]
                nc_w = c_w + dc[k]
                if 0 <= nr_w < R and 0 <= nc_w < C:
                    if forrest[nr_w][nc_w] == '.':
                        forrest[nr_w][nc_w] = '*'
                        water.append([nr_w, nc_w])
        # 고슴도치 이동
        for _ in range(len(animal)):
            r_a, c_a, time = animal.popleft()
            for k in range(4):
                nr_a = r_a + dr[k]
                nc_a = c_a + dc[k]
                if 0 <= nr_a < R and 0 <= nc_a < C:
                    if forrest[nr_a][nc_a] == 'D':
                        return time + 1
                    if forrest[nr_a][nc_a] == '.':
                        forrest[nr_a][nc_a] = 'S'  # 방문 처리
                        animal.append([nr_a, nc_a, time + 1])
    return "KAKTUS"


answer = bfs()
print(answer)
