__author__ = 'afrozeshaik'
n=input()
l=[]
for i in xrange(n):
    l.append(map(int,raw_input().split()))
start=0
fuel=l[0][0]
count=0
i=0
while(count<n and start<n):
    if fuel<l[i][1]:
        start=(start+1)
        count=0
        i=start
    else:
        fuel=fuel-l[i][1]
        count+=1
        i=(i+1)%n
print start

