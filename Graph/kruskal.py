def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(edges, parent):
    edges.sort()                                                # 1. edges sort
    cost = 0                                                    # 2. cost initilization
    for edge in edges:                                          # 3. union noncyclic edges
        dist, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            cost += dist   
    return cost

v, e = 7, 9
parent = [0] * (v+1)

edges = []

for i in range(1, v+1):
    parent[i] = i

edges.append((29, 1, 2))
edges.append((75, 1, 5))
edges.append((35, 2, 3))
edges.append((34, 2, 6))
edges.append((7, 3, 4))
edges.append((23, 4, 6))
edges.append((13, 4, 7))
edges.append((53, 5, 6))
edges.append((25, 6, 7))

'''
# Edges Input
for _ in range(e):
    a, b, dist = map(int, input().split())
    edges.append((dist, a, b))
'''
print("Minimum cost :", kruskal(edges, parent))
