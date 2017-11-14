__author__ = 'afrozeshaik'
import Queue
q=input()
for x in xrange(q):
    a=raw_input().strip().split()
    n=int(a[0])
    m=int(a[1])
    dep=[]
    for i in xrange(n):
        a=map(int,raw_input().strip().split())
        a=a[1:]
        a.sort(reverse=True)
        dep.append(a)
    tobe=map(int,raw_input().strip().split())
    qu=Queue.Queue()
    res=[]
    for i in tobe:
        qu.put(i)
    while(not qu):
        p=qu.get()



