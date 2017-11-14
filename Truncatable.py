__author__ = 'afrozeshaik'
import math


def isprime(n):
    if(n<2):
        return False
    elif(n==2 or n==3):
        return True
    elif(n%2==0 or n%3==0):
        return False
    else:
        for i in xrange(2,int(math.sqrt(n))+1):
            if(n%i==0):
                return False
    return True

def TruncatablePrime(n): # 3797
    ''' '''
    a=n
    b=n
    c=n
    p=10
    while(a>0):         # 3797, 379, 37, 3
        if(not isprime(a)):
            return False
        a=a/10
    while(p<n):         #3797, 7,97,797,
        c=b%p
        if(not isprime(c)):
            return False
        p=p*10

    return True
k=input()
sum=0
for i in xrange(11,k):
    if(TruncatablePrime(i)):
        sum+=i
print sum




