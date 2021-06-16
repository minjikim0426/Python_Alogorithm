import heapq
import sys

def dijkstra(start):
    h = []                                          # 1. queue 
    heapq.heappush(h, (0, start))                   # 2. heap queue (dist = 0, start)
    distance[start] = 0                             # 3. distance[start] = 0
    while h:                                        # 4. while
        dist, now = heapq.heappop(h)                # 4.1 minimum dist node heappop
        if distance[now] < dist:                    # 4.2 if now == visited node: continue
            continue                                
        for i in graph[now]:                        # 4.3 now -> next node cost comparison
            cost = dist + i[1]                      # dist: dist(start~now), i[1]: dist(now~next)
            if cost < distance[i[0]]:               # 4.4 if (cost = dist(start~now~next)) < dist(start~next): update distance, heappush 
                distance[i[0]] = cost               # distance[i[0]] : dist(start~next)
                heapq.heappush(h, (cost, i[0]))     

INF = int(1e9)
n, m = 6, 11
start = 1
graph = [[] for _ in range(n+1)]
graph[1].append((2, 2))
graph[1].append((3, 5))
graph[1].append((4, 1))
graph[2].append((3, 3))
graph[2].append((4, 2))
graph[3].append((2, 3))
graph[3].append((6, 5))
graph[4].append((3, 3))
graph[4].append((5, 1))
graph[5].append((3, 1))
graph[5].append((6, 2))

'''
# Graph Input
input = sys.stdin.readline
n, m = map(int, input().split()) # 6 11
start = int(input()) # 1
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
'''

# Distance Initialization
distance = [INF] * (n+1)

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

