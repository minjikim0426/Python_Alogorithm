n = 5
data = [8, 5, 4, 7, 2]

for i in range(n):
    for j in range(i+1,n):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i] 

print(data)
