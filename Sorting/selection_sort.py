n = 5
data = [8, 5, 4, 7, 2]

for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if data[min_index] > data[j]:
            min_index = j
    data[i], data[min_index] = data[min_index], data[i]

print(data)