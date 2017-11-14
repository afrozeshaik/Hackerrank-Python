__author__ = 'afrozeshaik'
import Queue

def bfs(adm,start,n,visited):
    Q=Queue.Queue()
    Q.put(start)
    visited[start]=1
    count=0
    while(not Q.empty()):
        tem=Q.get()
        count+=1
        for i in xrange(n):
            if adm[tem][i]==1 and visited[i]==0:
                Q.put(i)
                visited[i]=1
    return count,visited




t=input()
for k in xrange(t):
    n,m,cl,cr=map(int,raw_input().split())
    visited=n*[0]
    adm=[]
    for i in xrange(n):
        adm.append([])
        for j in xrange(n):
            adm[i].append(0)
    for i in xrange(m):
        a,b=map(int,raw_input().split())
        adm[a-1][b-1]=1
        adm[b-1][a-1]=1
        start=0

    if cr>=cl:
        print n*cl
    else:
        res=0
        while(True):
            bol=True
            for i in xrange(n):
                if visited[i]==0:
                    bol=False
                    start=i
                    break
            if bol:
                break
            nodes,visited=bfs(adm,start,n,visited)
            res+=(nodes-1)*cr+cl

        print res





