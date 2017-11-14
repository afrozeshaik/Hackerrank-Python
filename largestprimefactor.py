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



def findprimes(n):
    primes=(n+2)*[0]
    primes[2]=1
    for i in xrange(3,n+2/2,2):
        bol=False
        for j in xrange(2,int(math.sqrt(i))+1):
            if i%j==0:
                bol=True
                break
        if not bol:
            primes[i]=1

    return primes






t=input()
inps=[]
m=-1
for tests in xrange(t):
    p=input()
    if p>m:
        m=p
    inps.append(p)

primes=findprimes(m)

for i in inps:
    for j in xrange(i,0,-1):
        if i%j==0:
            if primes[j]==1:
                print j
                break





