__author__ = 'afrozeshaik'
curpos=raw_input().strip().split()
curxpos=int(curpos[0])
curypos=int(curpos[1])
gridsize=raw_input().strip().split()
rows=int(gridsize[0])
columns=int(gridsize[1])
grid=[]
dirtyblock=[]
for i in range(rows):
    grid.append(raw_input())
for i in range(rows):
    for j in range(columns):
        if grid[i][j]=='d':
            dirtyblock.append([i,j])

def nearestdirtyblock(dirtyblock,curxpos,curypos):
    mindis=9
    ndb=0
    for i in dirtyblock:
        if abs(curxpos-i[0])+abs(curypos-i[1])<mindis:
            ndb=i
            mindis=abs(curxpos-i[0])+abs(curypos-i[1])
    return ndb
ans= nearestdirtyblock(dirtyblock,curxpos,curypos)
def nextstep(cur_x_pos,cur_y_pos,dirtyblock,grid):
    if(grid[cur_x_pos][cur_y_pos]=='d'):
        print 'CLEAN'
    if(cur_y_pos<dirtyblock[1]):
        print 'RIGHT'
    elif(cur_y_pos>dirtyblock[1]):
        print 'LEFT'
    elif(cur_x_pos<dirtyblock[0]):
        print 'DOWN'
    elif(cur_x_pos>dirtyblock[0]):
        print 'UP'
nextstep(curxpos,curypos,ans,grid)
