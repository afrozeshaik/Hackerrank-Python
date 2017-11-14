__author__ = 'afrozeshaik'
me=raw_input()
him=""
if(p=="r"):
    him="g"
else:him="p"
pos=raw_input().strip().split()
myxpos=int(pos[0])
myypos=int(pos[1])
hisxpos=int(pos[2])
hisypos=int(pos[3])
themap=list()
for i in range(15):
    themap.append(raw_input())
def nextmove(me,him,myxpos,myypos,hisxpos,hisypos,themap):
    if(themap[myxpos-1][myypos]!=me and themap[myxpos-1][myypos]!='#' and themap[myxpos-1][myypos]!=him ):
        print "UP"
    elif (themap[myxpos][myypos+1]!='#' and themap[myxpos][myypos+1]!=him and themap[myxpos+1][myypos+1]!=me):
        print "RIGHT"
    elif(themap[myxpos+1][myypos]!=me and themap[myxpos+1][myypos]!='#' and themap[myxpos+1][myypos]!=him):
        print "DOWN"
    else:
        print "LEFT"
nextmove(me,him,myxpos,myypos)
