__author__ = 'afrozeshaik'
import Queue as Q

t=input()
for i in xrange(t):
    a=raw_input().strip().split()
    n=int(a[0])
    e=int(a[1])
    g=[]
    visited=[]
    level=[]
    for j in xrange(n):
        g.append([])
        visited.append(0)
        level.append(-1)
        for k in xrange(n):
            g[j].append(0)
    for j in xrange(e):
        a=raw_input().strip().split()
        p1=int(a[0])-1
        p2=int(a[1])-1
        g[p1][p2]=1
        g[p2][p1]=1
    start=input()-1
    q=Q.Queue()
    q.put(start)
    visited[start]=1
    level[start]=0
    while(not q.empty()):
        p=q.get()
        for i in xrange(n):
            if(g[p][i]==1 and visited[i]==0):
                q.put(i)
                visited[i]=1
                level[i]=level[p]+1
    for i in xrange(n):
        if(i!=start):
            if(level[i]>0):
                print 6*level[i],
            else:
                print level[i],
    print ""




