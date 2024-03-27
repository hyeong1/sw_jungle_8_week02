# 다익스트라
import sys
import heapq


def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])  # 비용 순서 최소힙
    weights = [float("inf")] * (N+1)
    weights[start] = 0  # 자기 자신으로 가는 건 0

    while heap:
        weight, cur = heapq.heappop(heap)
        if weight > weights[cur]:
            continue
        for nxt_w, nxt in graph[cur]:
            new_weight = weight + nxt_w
            if weights[nxt] > new_weight:
                weights[nxt] = new_weight
                heapq.heappush(heap, [new_weight, nxt])
    return weights


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append([w, e])

start, end = map(int, input().split())
result = dijkstra(start)
print(result[end])
