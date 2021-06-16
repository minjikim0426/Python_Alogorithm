# bubble sort
def bubble_sort(data):
  for i in range(len(data)):
    for j in range(i+1, len(data)):
      if data[i] > data [j]:
        data[i], data[j] = data[j], data[i] 
  return data

# selection sort
def selection_sort(data):
  for i in range(len(data)):
    min_index = i
    for j in range(i+1, len(data)):
      if data[i] > data[j]:
        min_index = j
    data[i], data[min_index] = data[min_index], data[i]
  return data

# insertion sort
def insertion_sort(data):
  for i in range(1, len(data)):
    for j in range(i, 0, -1):
      if data[j-1] > data[j]:
        data[j-1], data[j] = data[j], data[j-1]
      else:
        break
  return data

# count sort
def count_sort(data):
  count = [0] * (max(data)+1)
  for i in range(len(data)):
    count[data[i]] += 1
  result = []
  for i in range(len(count)):
    for j in range(count[i]):
      result.append(i)
  return result

# quick sort
def quick_sort(data):
  if len(data) < 2:
    return data
  pivot = data[0]
  tail = data[1:]
  left = [x for x in tail if x <= pivot]
  right = [x for x in tail if x > pivot]
  return quick_sort(left) + [pivot] + quick_sort(right)

# heap sort
import heapq
def heap_sort(data):
  h = []
  result = []
  for x in data:
    heapq.heappush(h, x)
  for _ in range(len(h)):
    result.append(heapq.heappop(h))
  return result
