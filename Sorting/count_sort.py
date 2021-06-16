n = 5
data = [8, 5, 4, 7, 2]

count = [0] * (max(data)+1)
for i in range(n):
    count[data[i]] += 1

result = []
for i in range(len(count)):
    for j in range(count[i]):
        result.append(i)

print(result)
