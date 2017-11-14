__author__ = 'afrozeshaik'
import Queue
n=input()

def bfs(n,a,b):
    g=[]
    level=[]
    for i in xrange(n):
        g.append([])
        level.appned([])
        for j in xrange(n):
            g[i].append(0)
            level[i].append(-1)

    level[0][0]=0
    q=Queue.Queue()
    q.put([0,0])

    while(q):
        tem=q.get()
        g[tem[0]][tem[1]]=1





