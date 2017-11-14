__author__ = 'afrozeshaik'
def lszero(A):
    d=dict()
    sum=0
    for i in xrange(len(A)):
        sum+=A[i]
        if sum in d:
            d[sum].append(i)
        else:
            d[sum]=[i]
    print d
    m=-1
    l=-1
    for i in d:
        if(i==0):
            p=d[0][len(d[0])-1]+1
            if(p>m):
                m=p
                l=0
        else:
            p=d[i][len(d[i])-1]-d[i][0]
            if(p>m):
                m=p
                l=i
    ret=[]
    if(l==0):
        for i in xrange(d[0][len(d[0])-1]+1):
            ret.append(A[i])
    else:
        for i in xrange(d[l][0]+1,d[l][len(d[l])-1]+1):
            ret.append(A[i])
    return ret

A=[ 15, -2, 2, -8, 1, 7, 10, 23]
print lszero(A)