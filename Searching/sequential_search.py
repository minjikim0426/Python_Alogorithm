def sequential_search(target, data):
    for i in range(len(data)):
        if data[i] == target:
            return i+1

data = input("data : ").split() # target
print(sequential_search("target", data)) 
