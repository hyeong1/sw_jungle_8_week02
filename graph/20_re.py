# 프림 896ms
import sys
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append([w, e])
    graph[e].append([w, s])

heap = [[0, 1]]
answer = 0
while heap:
    weight, node = heapq.heappop(heap)
    if not visited[node]:
        visited[node] = True
        answer += weight
        for nxt_weight, nxt_node in graph[node]:
            heapq.heappush(heap, [nxt_weight, nxt_node])

print(answer)
