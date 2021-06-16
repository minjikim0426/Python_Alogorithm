n = 5
data = [8, 5, 4, 7, 2]

def quick_sort(data):
    if len(data) < 2:
        return data
    
    pivot = data[0]
    tail = data[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(data))



