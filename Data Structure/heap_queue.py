import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)

heapq.heappop(heap)
heapq.heappop(heap)

heapq.heappush(heap, 1)
heapq.heappush(heap, 4)

heapq.heappop(heap)

print(heap)
print(heap[::-1])
