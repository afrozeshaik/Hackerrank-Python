__author__ = 'afrozeshaik'

import math
def isprime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in xrange(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True

n=input()

for i in xrange(2,n):
    if isprime(i) and isprime(n-i):
        print n-i,i
        break

def gcd(a,b):
    m=max(a,b)
    mi=min(a,b)
    if mi==0:
        return m
    else:
        return gcd(mi,m%mi)

print gcd(14,7)