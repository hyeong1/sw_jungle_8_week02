# 크러스컬 (유니온파인드) 376ms
import sys


def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]  # node가 속한 집합의 루트 노드 값을 반환


def union(parent, node_a, node_b):  # node_a 집합과 node_b 집합을 합친다
    root_a = find(parent, node_a)
    root_b = find(parent, node_b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


V, E = map(int, input().split())
parent = [0] * (V + 1)
edges = []
result = 0

for i in range(1, V+1):
    parent[i] = i  # 초기 부모는 자기 자신

for _ in range(E):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append([cost, a, b])
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)  # 부모가 같지 않으면 합친다
        result += cost

print(result)
