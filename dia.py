__author__ = 'afrozeshaik'
m,n = map(int, raw_input().split())
a=[]
for i in xrange(m):
    a.append(map(int,raw_input().strip().split()))



for i in xrange(m):
    k=i
    j=0
    while(k>=0 and j<n):
        print a[k][j],
        k-=1
        j+=1
    print ""

for j in xrange(1,n):
    k=j
    i=m-1
    while(i>=0 and k<n):
        print a[i][k],
        k+=1
        i-=1
    print ""
