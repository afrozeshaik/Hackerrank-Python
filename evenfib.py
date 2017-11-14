__author__ = 'afrozeshaik'

def fib(n):
    ar=[]
    ar.append(1)
    ar.append(2)
    res=0
    i=0
    while(res<=n):
        res=ar[i]+ar[i+1]
        i+=1
        ar.append(res)
    return ar



t=input()
inp=[]
m=-1
for tests in xrange(t):
    p=input()
    if p>m:
        m=p
    inp.append(p)
ar=fib(m)
for i in inp:
    tem=0
    res=0
    while(ar[tem]<i):
        if ar[tem]%2==0:
            res+=ar[tem]
        tem+=1
    print res



