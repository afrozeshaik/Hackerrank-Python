__author__ = 'afrozeshaik'
n=int(raw_input())
l=list()
ch=list()

for i in range(n):
    l.append(int(raw_input()))
    ch.append(1)
for i in range(n-1):
    if l[i+1]>l[i]:
        ch[i+1]=ch[i]+1
    else:
        ch[i+1]=1
for i in range(n-1,0,-1):
    if l[i-1]>l[i] and ch[i-1]<=ch[i]:
        ch[i-1]=ch[i]+1
print sum(ch)