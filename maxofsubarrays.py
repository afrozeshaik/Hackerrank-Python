__author__ = 'afrozeshaik'
from collections import deque
ar=[12, 1, 78, 90, 57, 89, 56]
k=3

end=k-1
start=0

l=[]
l=deque(l)

for i in xrange(k):
    while(not l and ar[i]>l[start]):
        l.popleft()
    l.append(i)
for j in xrange(3,len(ar)):
    print ar[l[start]],
    while(not l and l[len(l)-1]<=i-k):
        l.remove(l[len(l)-1])
    while(not l and ar[i]>l[start]):
        l.popleft()
    l.append(i)
print ar[l[start]]



