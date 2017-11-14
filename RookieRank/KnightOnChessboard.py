from __builtin__ import xrange
from fileinput import input

__author__ = 'afrozeshaik'
import Queue
n=input()
b=[]
for i in xrange(n):
    b.append([])
    for j in xrange(n):
        b[i].append(0)
print b

def inboard(n,x,y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    else:
        return False


def bfs(n,h,w):
    b=[]
    l=[]
    for i in xrange(n):
        b.append([])
        l.append([])
        for j in xrange(n):
          b[i].append(0)
          l[i].append(0)
    q=Queue.Queue()
    q.put([0,0])
    l[0][0]=0
    while(not q.empty()):
        t=q.get()
        b[t[0]][t[1]]=1
        tx=t[0]
        ty=t[1]
        '''case1'''
        nx=tx+h
        ny=tx+w
        if (inboard(n,nx,ny) and b[nx][ny]==0):
            q.put([nx,ny])
            l[nx][ny]=l[tx][ty]+1
            b[nx][ny]==1
        '''case2'''
        nx=tx+h
        ny=tx-w
        if (inboard(n,nx,ny) and b[nx][ny]==0):
            q.put([nx,ny])
            l[nx][ny]=l[tx][ty]+1
            b[nx][ny]==1
        '''case3'''
        nx=tx-h
        ny=tx+w
        if (inboard(n,nx,ny) and b[nx][ny]==0):
            q.put([nx,ny])
            l[nx][ny]=l[tx][ty]+1
            b[nx][ny]==1
        '''case4'''
        nx=tx-h
        ny=tx-w
        if (inboard(n,nx,ny) and b[nx][ny]==0):
            q.put([nx,ny])
            l[nx][ny]=l[tx][ty]+1
            b[nx][ny]==1
        '''case5'''
        nx=tx+w
        ny=tx+h
        if (inboard(n,nx,ny) and b[nx][ny]==0):
            q.put([nx,ny])
            l[nx][ny]=l[tx][ty]+1
            b[nx][ny]==1
        '''case6'''
        nx=tx+w
        ny=tx-h
        if (inboard(n,nx,ny) and b[nx][ny]==0):
            q.put([nx,ny])
            l[nx][ny]=l[tx][ty]+1
            b[nx][ny]==1
        '''case7'''
        nx=tx-w
        ny=tx+h
        if (inboard(n,nx,ny) and b[nx][ny]==0):
            q.put([nx,ny])
            l[nx][ny]=l[tx][ty]+1
            b[nx][ny]==1
        '''case8'''
        nx=tx-w
        ny=tx-h
        if (inboard(n,nx,ny) and b[nx][ny]==0):
            q.put([nx,ny])
            l[nx][ny]=l[tx][ty]+1
            b[nx][ny]==1
    print b
    if b[n-1][n-1]==0:
        return -1
    else:
        return l[n-1][n-1]
print bfs(5,1,2)








