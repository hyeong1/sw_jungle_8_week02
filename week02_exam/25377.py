import heapq

N = int(input())
case = [list(map(int, input().split())) for _ in range(N)]

heap = []
for c in case:
    if c[0] <= c[1]:
        heapq.heappush(heap, c[1])

if heap:
    print(heapq.heappop(heap))
else:
    print(-1)
