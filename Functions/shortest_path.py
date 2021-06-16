INF = int(1e9)
n = 10    '''n = # of nodes'''

# dijkstra
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

'''graph append'''

import heapq

def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))

# floyd warshall
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

'''graph modification'''
            
def floyd_warshall(graph):
    for k in range(len(graph)):
        for a in range(1, len(graph)):
            for b in range(1, len(graph)):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
