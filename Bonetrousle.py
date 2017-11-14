__author__ = 'afrozeshaik'
t=input()
for i in xrange(t):
    a=raw_input().strip().split()
    n=int(a[0])
    k=int(a[1])
    b=int(a[2])
    if ((b*(b+1))/2>n):
        print -1

