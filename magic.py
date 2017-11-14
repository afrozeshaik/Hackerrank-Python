__author__ = 'afrozeshaik'
t=input()
for i in xrange(t):
    n=input()
    s=bin(n)[2:]
    res=0
    p=len(s)
    for i in xrange(p):
        res+=int(s[p-1-i])*(5**(i+1))
    print res
