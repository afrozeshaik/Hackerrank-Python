__author__ = 'afrozeshaik'
n=input()
r=input()
d=[]
for i in xrange(n+1):
    d.append([])
    for j in xrange(r+1):
        d[i].append(0)
for i in xrange(1,n+1):
    for j in xrange(r+1):
        if(j<=i):
            if(j==0 or i==j):
                d[i][j]=1
            else:
                d[i][j]=d[i-1][j-1]+d[i-1][j]

print d[n][r]