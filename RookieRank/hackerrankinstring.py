__author__ = 'afrozeshaik'
#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    g='hackerrank'
    c=0
    for i in s:
        if g[c]==i:
            c+=1
        if c==10:
            break
    if c==10:
        print 'YES'
    else:
        print 'NO'
'''hereiamstackerrank
hackerworld'''