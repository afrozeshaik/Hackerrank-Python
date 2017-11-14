__author__ = 'afrozeshaik'
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=raw_input().strip().split()
m=int(a[0])
n=int(a[1])
X=map(int,raw_input().strip().split())
Y=map(int,raw_input().strip().split())
c=[]
d=[]
for i in xrange(m+1):
    c.append([])
    d.append([])
    for j in xrange(n+1):
        c[i].append(0)
        d[i].append('x')

for i in xrange(1,m+1):
    for j in xrange(1,n+1):
        if(X[i-1]==Y[j-1]):
            c[i][j]=c[i-1][j-1]+1
            d[i][j]='c'
        elif(c[i][j-1]>c[i-1][j]):
            c[i][j]=c[i][j-1]
            d[i][j]='l'
        else:
            c[i][j]=c[i-1][j]
            d[i][j]='u'
finlist=[]
i=m
j=n
while(i and j):
    if(d[i][j]=='c'):
        finlist.append(str(X[i-1]))
        i-=1
        j-=1
    elif(d[i][j]=='u'):
        i-=1
    else:
        j-=1
finlist=finlist[::-1]
for i in finlist:
    print i,

