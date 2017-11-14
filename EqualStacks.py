__author__ = 'afrozeshaik'
#!/bin/python

import sys


n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))
s1=sum(h1)
s2=sum(h2)
s3=sum(h3)
ht1=len(h1)
ht2=len(h2)
ht3=len(h3)
while(True):
    if (s1==s2 and s1==s3):
        print s1
        break
    else:
        if(ht1>ht2 and ht1>ht3):
            s1=s1-h1.pop()
            ht1-=1
            print "popped form 1"
        elif(ht2>ht1 and ht2>ht3):
            s2=s2-h2.pop()
            ht2-=1
            print "popped from 2"
        else:
            s3=s3-h3.pop()
            ht3-=1
            print "popped from 3"



