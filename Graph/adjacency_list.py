graph = []

# Graph Creation
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
print(graph)

# Graph Initialization
n, m = map(int,input("n m : ").split()) # 8 3
graph = [[0]*m for _ in range(n+1)]
print(graph)

# Graph Input
graph = []
for _ in range(n):
    graph.append(list(map(int, input("adjacency list input >> ").split())))   # list(map(int,input()))
print(graph)
