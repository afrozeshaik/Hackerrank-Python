__author__ = 'afrozeshaik'

import math

def isprime(n):
    if n==0 or n==1:
        return False
    if n==2:
        return True
    bol=False
    for i in xrange(2,int(math.sqrt(n))+1):
        if n%i==0:
            bol=True
            break
    if not bol:
        return True
    return False

t=input()
inps=[]
m=-1
for testcases in xrange(t):
    p=input()
    if p>m:
        m=p
    inps.append(p)

primes=[0]
tem=0
i=2
while(tem<m):
    if isprime(i):
        primes.append(i)
        tem+=1
    i+=1

for i in inps:
    print primes[i]




