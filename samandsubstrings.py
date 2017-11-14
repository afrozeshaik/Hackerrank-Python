__author__ = 'afrozeshaik'
a=raw_input()
n=len(a)
sum=0

dp=[[0 for i in xrange(n)] for j in xrange(n)]
for i in xrange(n):
    dp[i][i]=int(a[i])
    #sum+=int(a[i])

for i in xrange(n-1):
    for j in xrange(i,n):
        dp[i][j]=dp[i][j-1]*10+int(a[j])
        sum+=dp[i][j]
        print a[i:j+1], sum


print sum%1000000009