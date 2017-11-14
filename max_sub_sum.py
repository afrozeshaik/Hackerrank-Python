__author__ = 'afrozeshaik'
t=input()
for i in xrange(t):
    a=raw_input().strip().split()
    n=int(a[0])
    m=int(a[1])
    ar=map(int,raw_input().strip().split())
    maxi=-1
    for j in xrange(n-1):
        sum=ar[j]
        for k in xrange(j+1,n):
            sum=(sum+ar[k])%m
            if(sum>maxi):
                maxi=sum
print maxi

