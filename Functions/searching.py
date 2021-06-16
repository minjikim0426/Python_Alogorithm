# dfs
def dfs(graph, v, visited):
  visited[v] = True
  print(v,end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# bfs
from collections import deque

def bfs(graph, v, visited):
  queue = deque([v])
  visited[v] = True
  print(v, end = ' ')
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        print(i, end = ' ')

# binary search
def binary_search(target, data, start, end):
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid + 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

# sequential search
def sequential_search(target, data):
    for i in range(len(data)):
        if data[i] == target:
            return i+1
