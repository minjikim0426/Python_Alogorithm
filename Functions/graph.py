# v = # of nodes, e = # of edges
# parent = [0] * (v+1)
# edges = [(dist, a, b)] * e

# find parent
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# kruskal
def kruskal(edges, parent):
    edges.sort()
    cost = 0
    for edge in edges:
        dist, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            cost += dist
    return cost

