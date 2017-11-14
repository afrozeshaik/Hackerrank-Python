__author__ = 'afrozeshaik'
def gcd(a,b):
    g=0
    l=0
    if a>b:
       g,l=a,b
    else:
        g,l=b,a
    while(l):
        g,l=l,g%l
    return g
n=input()
a1=map(int,raw_input().strip().split())
a2=map(int,raw_input().strip().split())

a1=sorted(a1)[::-1]
a2=sorted(a2)[::-1]



maxs,curs=0,0
maxg=0
curg=0
for i in a1:
    for j in a2:
        curg=gcd(i,j)
        curs=i+j
        if curg==maxg:
            if curs>maxs:
                maxs=curs
        if curg>maxg:
            maxg=curg
            maxs=curs
        if curg==i or curg ==j:
            break
print maxs


