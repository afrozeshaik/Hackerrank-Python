__author__ = 'haanu'
import Queue
n,m=map(int,raw_input().split())
adl=[]
visited=[]
for i in xrange(n):
    adl.append([])
    visited.append(0)
for j in xrange(m):
    a,b=map(int,raw_input().split())
    adl[a-1].append(b-1)
    adl[b-1].append(a-1)

Q=Queue.Queue()
Q.put(0)
while(Q):
    print Q.empty()
    t=Q.get()
    print t
    visited[t]=1
    for i in adl[t]:
        if visited[i]==0:
            Q.put(i)
            visited[i]==1
print 'out'
