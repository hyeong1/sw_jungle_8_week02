from collections import deque

N = int(input())
M = int(input())
graph = {i: [] for i in range(1, N+1)}
in_degree = [0] * (N+1)

for _ in range(M):
    e, s, val = map(int, input().split())
    graph[s].append((e, val))
    in_degree[e] += 1

queue = deque()
needs = [[0] * (N+1) for _ in range(N+1)]
basic = []
for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)
        basic.append(i)
while queue:
    cur = queue.popleft()
    for adj, val in graph[cur]:
        if cur in basic:  # 현재 노드가 기본 부품이면
            needs[adj][cur] += val  # 가중치만 더하기
        else:  # 현재 노드가 중간 부품이면
            for i in range(1, N+1):
                needs[adj][i] += needs[cur][i] * val  # (필요한 기본 부품 * 가중치) 더하기
        in_degree[adj] -= 1
        if in_degree[adj] == 0:
            queue.append(adj)

for idx in basic:
    print(idx, needs[N][idx])
