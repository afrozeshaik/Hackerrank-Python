__author__ = 'afrozeshaik'
s1=raw_input()
s2=raw_input()
m=len(s1)
n=len(s2)
dp=[]
for i in xrange(m+1):
    dp.append([])
    for j in xrange(n+1):
        dp[i].append(0)

for i in xrange(m+1):
    for j in xrange(n+1):
        if(i==0):
            dp[i][j]=j
        elif(j==0):
            dp[i][j]=i
        elif(s1[i-1]==s2[j-1]):
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
print dp[m][n]