from collections import deque

N = int(input())
K = int(input())
pos_apples = [list(map(int, input().split())) for _ in range(K)]
for apple in pos_apples:
    apple[0] -= 1
    apple[1] -= 1
L = int(input())
change_d = {}
for _ in range(L):
    key, value = input().split()
    change_d[key] = value

sec, apple_check = 0, 0
head = [0, 0]
tail = [0, 0]
path = deque([])
direct_queue = deque([0, 1, 2, 3])
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
while (head[0] <= N-1 and head[1] <= N-1) and (head[0] >= 0 and head[1] >= 0):
    path.append(head.copy())
    if str(sec) in change_d.keys():
        # "L", "D"에 따라 링큐 rotate
        if change_d[str(sec)] == "L":  # "L" 이면 direct_queue.rotate(1) 오른쪽 회전
            direct_queue.rotate(1)
        elif change_d[str(sec)] == "D":  # "D" 면 direct_queue.rotate(-1) 왼쪽 회전
            direct_queue.rotate(-1)
    # 현재 방향에 따라
    head[0] += dy[direct_queue[0]]  # 행
    head[1] += dx[direct_queue[0]]  # 열
    if head in path:  # 자기 몸을 물었을 때
        sec += 1
        break
    # 사과 체크
    if apple_check < K and head in pos_apples:  # 사과는 한 번 먹으면 없어짐
        apple_check += 1
        pos_apples.remove(head)
    else:
        tail[0] += dy[direct_queue[0]]
        tail[1] += dx[direct_queue[0]]  # 꼬리 자르기
        path.popleft()
    sec += 1

print(sec)
