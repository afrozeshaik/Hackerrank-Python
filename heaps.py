__author__ = 'afrozeshaik'
import heapq
l=[1,2,5,6,7,5,4,4]
heap=[]
for i in l:
    heapq.heappush(heap,i)
print heapq.heappop(heap)
print heapq.heappop(heap)
print heapq.heappop(heap)
print heapq.heappop(heap)