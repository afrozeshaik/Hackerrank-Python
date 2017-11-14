__author__ = 'afrozeshaik'
import Queue

def bfs(g,n,start,visited):
    Q=Queue.Queue()
    Q.put(start)
    count=0
    visited[start]=1
    while(not Q.empty()):
        tem=Q.get()
        count+=1
        for i in g[tem]:
            if visited[i]==0:
                Q.put(i)
                visited[i]=1
    return count,visited




t=input()
for i in xrange(t):
    n,m,cl,cr=map(int,raw_input().split())
    g=[]
    visited=n*[0]
    for j in xrange(n):
        g.append([])
        visited.append(0)
    for j in xrange(m):
        a,b=map(int,raw_input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    res=0

    if cl<=cr:
        print n*cl
    else:
        while(True):
            bol=False
            for j in xrange(n):
                if visited[j]==0:
                    start=j
                    bol=True
                    break
            if bol==False:
                break
            nodes,visited=bfs(g,n,start,visited)
            res+=(nodes-1)*cr+cl

        print res



