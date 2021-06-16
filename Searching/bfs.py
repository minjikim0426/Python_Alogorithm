from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])              # 1. queue 
    visited[v] = True               # 2. visit
    print(v, end=' ')   
    while queue:                    # 3. while
        v = queue.popleft()         # 3.1 popleft 
        for i in graph[v]:          # 3.2 append and visit (not visited nodes)
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end=' ')

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False]*9

bfs(graph, 1, visited)
print()
