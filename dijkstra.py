__author__ = 'afrozeshaik'
import sys
def mindistance(dist,sptset):
    minid=sys.maxint
    minindex=-1
    for i in xrange(len(dist)):
        if(not sptset[i]):
            if(dist[i]<minid):
                minid=dist[i]
                minindex=i
    return minindex

t=input()
for i in xrange(t):
    a=raw_input().strip().split()
    n=int(a[0])
    e=int(a[1])
    g=[]
    dist=[]
    sptset=[]
    for j in xrange(n):
        g.append([])
        dist.append(sys.maxint)
        sptset.append(False)
        for k in xrange(n):
            g[j].append(0)
    for j in xrange(e):
        a=raw_input().strip().split()
        n1=int(a[0])
        n2=int(a[1])
        w=int(a[2])
        if(g[n1-1][n2-1]==0 or g[n1-1][n2-1]>w):
            g[n1-1][n2-1]=w
            g[n2-1][n1-1]=w
    start=input()
    dist[start-1]=0



    for j in xrange(n):
        p=mindistance(dist,sptset)
        sptset[p]=True
        for k in xrange(n):
            if(g[p][k]!=0 and dist[p]!=sys.maxint and (not sptset[k]) and dist[k]>dist[p]+g[p][k]):
                dist[k]=dist[p]+g[p][k]
    for j in xrange(n):
        if(j!=start-1):
            if(dist[j]==sys.maxint):
                print -1,
            else:
                print dist[j],
    print ''



