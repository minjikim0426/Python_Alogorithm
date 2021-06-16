import heapq

n = 5
data = [8, 5, 4, 7, 2]

def heap_sort(data):
    h = []
    result = []

    for x in data:
        heapq.heappush(h, x) # Max heap : -x

    for _ in range(len(h)):
        result.append(heapq.heappop(h)) # Max heap : -heapq.heappop(h)
    
    return result

print(heap_sort(data))