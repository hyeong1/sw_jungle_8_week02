# 메모리 초과
import sys

n = int(sys.stdin.readline())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))

max_end = 0
for i in info:
    max_end = max(max_end, i[2])
height = [[] for _ in range(max_end)]

for building in info:
    left, building_height, right = building
    for i in range(left, right):
        height[i].append(building_height)

skyline = []
cur_height = 0
prev_height = 0

for x in range(0, max_end):
    if height[x]:
        cur_height = max(height[x])
    else:
        cur_height = 0
    if cur_height != prev_height:
        skyline.append([x, cur_height])
        prev_height = cur_height

for point in skyline:
    print(point[0], point[1], end=" ")

