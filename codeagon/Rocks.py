__author__ = 'afrozeshaik'
a=raw_input().strip().split()
n=int(a[0])
s=int(a[1])
ar=map(int,raw_input().strip().split())
cnt=0
bol=False
for i in ar:
    if i<=s:
        cnt=cnt+1
    elif i>s and bol==False:
        bol=True
    elif i>s and bol:
        break
print cnt

