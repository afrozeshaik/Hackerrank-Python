__author__ = 'afrozeshaik'
a=raw_input().strip().split()
rows=int(a[0])
columns=int(a[1])
rws=[]
for j in range(rows):
    rws.append(raw_input())
sa=raw_input().strip().split()
srows=int(sa[0])
scolumns=int(sa[1])
srws=[]
for j in range(srows):
    srws.append(raw_input())
print rws[4][3:7]