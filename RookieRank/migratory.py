__author__ = 'afrozeshaik'
#!/bin/python

import sys
n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
l=[]
for i in xrange(5):
    l.append(0)
for i in types:
    l[i-1]+=1
res=0
maxnum=0
for i in xrange(5):
    if l[i]>maxnum:
        maxnum=l[i]
        res=i+1
print res


