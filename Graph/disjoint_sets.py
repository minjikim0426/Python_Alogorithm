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

v, e = 6, 4
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

union_parent(parent, 1, 4)
union_parent(parent, 2, 3)
union_parent(parent, 2, 4)
union_parent(parent, 5, 6)

'''
# Graph Input
v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

cycle = False     
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):    # cycle check
        cycle = True
        break
    else:
        union_parent(parent, a, b)
'''

print("set of each nodes : ", end =  ' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')
print()

print("parents of each nodes : ", end =  ' ')
for i in range(1, v+1):
    print(parent[i], end = ' ')
print()
