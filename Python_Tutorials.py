# definition
print('# defitnition')
n = 5
m = 3
INF = 1e9
print(INF)
print()

# list Comprehension
print('# list Comprehension')
list1 = [i for i in range(n) if i%2==0]
print(list1)
print()

# 2D list
print('# 2D list')
array2D = [[0]*m for _ in range(n)]
print(array2D)
print()

# list remove_all()
print('# list remove_all()')
remove_set = {0,1}
list1 = [i for i in range(n) if i not in remove_set]
print(list1)
print()

# list sort(), reverse(), insert(), count(), remove(), sorted()
print('# list sort(), reverse(), insert(), count(), remove(), sorted()')
list1 = [2, 1, 0, 3]
print(list1)

list1.insert(2,4)
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list1.reverse()
print(list1)

print(list1.count(1))

list1.remove(0)
print(list1)

list1 = [('a', 1), ('b', 2), ('c', 3)]
print(sorted(list1,key=lambda n: n[1], reverse=True))
print()

# tuple
print('# tuple')
tuple1 = (0, 1, 2) 
print(tuple1*n)
print()

# tuple in list
print('# tuple in list')
tuple_in_list = [(m,m) for _ in range(n)]
print(tuple_in_list)
print()

# dictionary
print('# dictionary')
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1)
print(dict1['a'])
print('a' in dict1)
print(dict1.keys())
print(dict1.values())
print()

# set
print('# set')
set1 = set([i for i in range(5)]+[4,5])
print(set)
set1 = {0,1,2,3,4,4,5}
print(set)

# set operator
print('# set operator')
set1 = set([1,2,3])
print(set1)
set2 = set([2,3,4])
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print()

# set add(), update(), remove()
print('# set add(), update(), remove()')
set1.add(4)
print(set1)
set1.update([5,6])
print(set1)
set1.remove(1)
print(set1)
print()

# inequality
print('# inequality')
print(1<2<5)
print(1<10<5)
print()

# lambda
print('# lambda')
print((lambda a, b: a+b)(1,2))
print()

# input & output
print('# input & output')

'''
list1 = list(map(int,input())) # 123
print(list1)

import sys
input = sys.stdin.readline # input = int(sys.stdin.readline)
print(input()) # hello
print(input().rstrip()) # hello

n, m, k = map(int,input().split()) # 1 2 3
print(n,m,k)
list1 = list(map(int,input().split())) # 1 2 3
print(list1)

array2D = []
for _ in range(n):
  array2D.append(list(map(int,input().split())))
print(array2D)
'''

print(f'n의 값은 {n}입니다.')
print()

# sum, min, max, eval
print('# sum, min, max, eval')
print(sum([1,2,3]))
print(min(1,2))
print(max(1,2))
print(eval('1+2'))
print()

# itertools - permutations, combinations, product
from itertools import permutations, combinations, product

print('# itertools - permutations, combinations, product')
list1 = ['a', 'b', 'c']
print(list(permutations(list1,2)))
print(list(combinations(list1,2)))
print(list(product(list1,repeat=2)))
print()

# heapq
import heapq

print('# heapq')
def heapsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h,-value) # max heap : -value
  for _ in range(len(h)):
    result.append(-heapq.heappop(h)) # max heap : -heapq.heappop(h)
  return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
print()

# bisect
from bisect import bisect_left, bisect_right

print('# bisect')
list1 = [1,2,4,4,8]
x = 4
print(bisect_left(list1,x))
print(bisect_right(list1,x))
print(bisect_right(list1,x)-bisect_left(list1,x)) # list1.count(x)
print(bisect_right(list1,4)-bisect_left(list1,2)) # list1.count(2~4)
print()

# collections - deque, Counter
from collections import deque, Counter

print('# collections - deque, Counter')
d = deque()
for i in range(n):
  d.append(i) # stack : list - append()
# d.appendleft(n)
print(d)
for i in range(n):
  d.popleft() # stack : deque - pop()
  print(d)

counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])
print(counter['blue'])
print(dict(counter))
print()

# math 
import math

print('# math')
print(math.factorial(5))
print(math.sqrt(7))
print(math.gcd(21,14))
print(21*14//math.gcd(21,14))
print(math.pi)
print(math.e)

# is_prime_number
print('# is_prime_number')

def is_prime_number(n):
  for i in range(2,int(math.sqrt(n)+1)):
    if n%i==0:
      return False
  return True
print(is_prime_number(7))