graph = []
INF = 999999999

# Graph Creation
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph)

# Graph Initialization
n = int(input("n : ")) # 3
graph = [[0]*n for _ in range(n)]
print(graph)

# Graph Input
graph = []
for _ in range(n):
    graph.append(list(map(int, input("adjacency matrix input >> ").split())))   # list(map(int,input().split()))
print(graph)
