import heapq, sys

N = int(input())
max_heap, min_heap = [], []
for _ in range(N):
    num = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    if min_heap and min_heap[0] < -max_heap[0]:
        min_value = heapq.heappop(min_heap)
        max_value = heapq.heappop(max_heap)
        heapq.heappush(min_heap, -max_value)  # 최대 힙에서 꺼낸 값에 (-) 붙여서 원래 값으로
        heapq.heappush(max_heap, -min_value)  # 최소 힙에거 꺼낸 값에 (-) 붙여서 최대 힙으로 push

    print(-max_heap[0])
