__author__ = 'afrozeshaik'
import Queue
def inboard(n,a,b):
    if a>=0 and a<n and b>=0 and b<n:
        return True
    else:
        return False
def bfs(n,a,b):
    board=[]
    level=[]
    for i in xrange(n):
        board.append([])
        level.append(([]))
        for j in xrange(n):
            board[i].append(0)
            level[i].append(0)
    q=Queue.Queue()
    q.put([0,0])
    level[0][0]=0
    board[0][0]=1
    while(not q.empty()):
        t=q.get()
        x=t[0]
        y=t[1]

        if(x==n-1 and y==n-1):
            break

        '''case1'''
        nx=x+a
        ny=y+b
        if (inboard(n,nx,ny) and board[nx][ny]==0):
            q.put([nx,ny])
            board[nx][ny]=1
            level[nx][ny]=level[x][y]+1

        '''case2'''
        nx=x+a
        ny=y-b
        if (inboard(n,nx,ny) and board[nx][ny]==0):
            q.put([nx,ny])
            board[nx][ny]=1
            level[nx][ny]=level[x][y]+1

        '''case3'''
        nx=x-a
        ny=y+b
        if (inboard(n,nx,ny) and board[nx][ny]==0):
            q.put([nx,ny])
            board[nx][ny]=1
            level[nx][ny]=level[x][y]+1

        '''case4'''
        nx=x-a
        ny=y-b
        if (inboard(n,nx,ny) and board[nx][ny]==0):
            q.put([nx,ny])
            board[nx][ny]=1
            level[nx][ny]=level[x][y]+1

        '''case5'''
        nx=x+b
        ny=y+a
        if (inboard(n,nx,ny) and board[nx][ny]==0):
            q.put([nx,ny])
            board[nx][ny]=1
            level[nx][ny]=level[x][y]+1

        '''case6'''
        nx=x+b
        ny=y-a
        if (inboard(n,nx,ny) and board[nx][ny]==0):
            q.put([nx,ny])
            board[nx][ny]=1
            level[nx][ny]=level[x][y]+1

        '''case7'''
        nx=x-b
        ny=y+a
        if (inboard(n,nx,ny) and board[nx][ny]==0):
            q.put([nx,ny])
            board[nx][ny]=1
            level[nx][ny]=level[x][y]+1

        '''case8'''
        nx=x-b
        ny=y-a
        if (inboard(n,nx,ny) and board[nx][ny]==0):
            q.put([nx,ny])
            board[nx][ny]=1
            level[nx][ny]=level[x][y]+1


    if board[n-1][n-1]:
        return level[n-1][n-1]
    else:
        return -1

n=input()
for i in xrange(1,n):
    for j in xrange(1,n):
        print bfs(n,i,j),
    print ""


