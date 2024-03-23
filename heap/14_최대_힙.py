import heapq, sys

n = int(input())
arr = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if arr:
            print(arr[0][1])
            heapq.heappop(arr)
        else:
            print(0)
    else:
        heapq.heappush(arr, (-x, x))
