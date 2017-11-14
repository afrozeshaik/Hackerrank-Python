__author__ = 'afrozeshaik'
n=input()
a=map(int,raw_input().strip().split())
d=dict()
for i in xrange(100):
    d[i]=0
maxn=-1
for i in a:
    d[i]+=1
res=-1

for i in xrange(1,99):
    res=max(res,d[i]+d[i+1])
print res

