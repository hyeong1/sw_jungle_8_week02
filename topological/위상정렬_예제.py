from collections import deque

in_degree = {'A': 0, 'B': 3, 'C': 0, 'D': 1, 'E': 2, 'F': 1, 'G': 0}
graph = {'A': ['B'],
         'B': [],
         'C': ['B', 'D'],
         'D': ['B', 'E'],
         'E': ['F'],
         'F': [],
         'G': ['E']}
visited = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False}

queue = deque()
result = []
for v in in_degree:
    if not visited[v] and in_degree[v] == 0:
        queue.append(v)
        visited[v] = True
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for adj in graph[vertex]:
            in_degree[adj] -= 1
            if not visited[adj] and in_degree[adj] == 0:
                queue.append(adj)
                visited[adj] = True

print(result)
