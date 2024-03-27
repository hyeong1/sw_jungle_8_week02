import sys
import heapq

K, N = map(int, input().split())
nums = list(map(int, sys.stdin.readline().split()))

heap = []
for n in nums:
    heapq.heappush(heap, n)

num = 0
for _ in range(N):
    num = heapq.heappop(heap)
    for p in nums:
        tmp = p * num
        heapq.heappush(heap, tmp)
        if num % p == 0:
            break

print(num)
