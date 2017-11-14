__author__ = 'afrozeshaik'
curpos=raw_input().strip().split()
curxpos=int(curpos[0])
curypos=int(curpos[1])

grid=[]
for i in range(5):
    grid.append(raw_input())


def finddirtyblock(grid,curxpos,curypos):
    dirtyblock=[]
    if(curxpos-1>=0 and curypos-1>=0 and grid[curxpos-1][curypos]=='d'):
        dirtyblock.append([curxpos-1,curypos-1])
    if(curxpos-1>=0 and grid[curxpos-1][curypos]=='d'):
        dirtyblock.append([curxpos-1,curypos])
    if(curxpos-1>=0 and curypos+1<=4 and grid[curxpos-1][curypos+1]=='d'):
        dirtyblock.append([curxpos-1,curypos+1])
    if(curypos-1>=0 and grid[curxpos][curypos-1]=='d'):
        dirtyblock.append([curxpos,curypos-1])
    if(curypos+1<=4 and grid[curxpos][curypos+1]=='d'):
        dirtyblock.append([curxpos,curypos+1])
    if(curxpos+1<=4 and curypos-1>=0 and grid[curxpos+1][curypos-1]=='d'):
        dirtyblock.append([curxpos+1,curypos-1])
    if(curxpos+1<=4 and grid[curxpos+1][curypos]=='d'):
        dirtyblock.append([curxpos+1,curypos])
    if(curxpos+1<=4 and curypos+1<=4 and grid[curxpos+1][curypos+1]=='d'):
        dirtyblock.append([curxpos+1,curypos+1])
    if grid[curxpos][curypos]=='d':
        dirtyblock.append([curxpos,curypos])
    return dirtyblock

def nearestdirtyblock(dirtyblock,curxpos,curypos):
    mindis=9
    ndb=0
    if dirtyblock:
        for i in dirtyblock:
            if abs(curxpos-i[0])+abs(curypos-i[1])<mindis:
                ndb=i
                mindis=abs(curxpos-i[0])+abs(curypos-i[1])
    return ndb

def nextstep(cur_x_pos,cur_y_pos,dirtyblock,grid):
    if dirtyblock:
        if(grid[cur_x_pos][cur_y_pos]=='d'):
            print 'CLEAN'
        elif(cur_y_pos<dirtyblock[1]):
            print 'RIGHT'
        elif(cur_y_pos>dirtyblock[1]):
            print 'LEFT'
        elif(cur_x_pos<dirtyblock[0]):
            print 'DOWN'
        elif(cur_x_pos>dirtyblock[0]):
            print 'UP'

dirtlist=finddirtyblock(grid,curxpos,curypos)
db=nearestdirtyblock(dirtlist,curypos,curypos)
nextstep(curxpos,curypos,db,grid)