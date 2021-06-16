from collections import deque

def topology_sort():
    result = []                 # 1. result, queue
    q = deque()                 

    for i in range(1, v+1):     # 2. if indgree == 0: append
        if indegree[i] == 0:    
            q.append(i)

    while q:                    # 3. while
        now = q.popleft()       # 3.1 popleft
        result.append(now)      # 3.2 -> result append
        for i in graph[now]:    # 3.3 indegree - 1, if indegree == 0: append
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
  
    return result

v, e = 7, 8
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)

graph[1].append(2)
indegree[2] += 1
graph[1].append(5)
indegree[5] += 1
graph[2].append(3)
indegree[3] += 1
graph[2].append(6)
indegree[6] += 1
graph[3].append(4)
indegree[4] += 1
graph[4].append(7)
indegree[7] += 1
graph[5].append(6)
indegree[6] += 1
graph[6].append(4)

'''
# Graph Input
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
'''

print(topology_sort())
