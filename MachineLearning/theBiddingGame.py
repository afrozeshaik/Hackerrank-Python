__author__ = 'afrozeshaik'
p=input()
pos=input()
mymon=map(int,raw_input().strip().split())
hismon=map(int,raw_input().strip().split())
draws=0
for i in range(len(mymon)):
    if(mymon[i]-hismon[i]==0):
        draws+=1
def calbid(p,pos,mymon,hismon):
    mymonrem=100-sum(mymon)
    hismonrem=100-sum(hismon)
    myspots=pos
    hisspots=10-pos
    winning = myspots<=hisspots
    if winning:
        return mymonrem/myspots
    else:
        if draws%2!=0:
            return mymonrem/myspots
        else:
            return mymonrem/myspots+2
print calbid(p,pos,mymon,hismon)