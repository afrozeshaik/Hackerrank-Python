#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int, raw_input().strip().split(' '))
c=sorted(c)
count=1
for i in xrange(1,n):
    if c[i]==c[0]:
        count+=1
    else:
        break

print c
if n==1:
    print 2*c[0],1

elif (count==1):
    if(2*c[0]<c[1]):
        print 2*c[0],1
    else:
        print c[1],n
else:
    print c[0],count
