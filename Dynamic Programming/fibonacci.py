'''Top-Down'''
d = [0] * 100

def fibonacci(x):
    print('f(' + str(x) + ')', end = ' ')
    if x in [1,2]:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibonacci(x-1) + fibonacci(x-2) 
    return d[x]

fibonacci(6)
print()

'''Bottom-Up'''
d = [0] * 100

d[1] = 1
d[2] = 2
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])