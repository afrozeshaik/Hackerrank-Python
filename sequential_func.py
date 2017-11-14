__author__ = 'afrozeshaik'

def seqfun(l):
    p=len(l)
    bol=True
    if(p==0 or p==1):
        return 0
    else:
        for i in xrange(p/2,p):
            if (l[i:p]==l[0:p-i]):
                return p-i
    return 0

n=input()
l=[]
for i in xrange(n):
    a=raw_input().strip().split()
    if (a[0]=='+'):
        l.append(int(a[1]))
    else:
        l.pop()
    print seqfun(l)


