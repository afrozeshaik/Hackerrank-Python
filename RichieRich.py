__author__ = 'afrozeshaik'
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
number = raw_input().strip()
num=list(number)
t=0
if(n==1 and k>0):
    print '9'
else:
    for i in xrange(n/2):
        t=i
        if(k>=2):
            if(num[i]!='9'):
                num[i]='9'
                k-=1
            if(num[n-i-1]!='9'):
                num[n-i-1]='9'
                k-=1

            if(num[i]!=num[n-i-1]):
                temp=max(num[i],num[n-i-1])
                num[i]=temp
                num[n-i-1]=temp
                k-=1
        else:
            break
    bol=True
    for i in xrange(n/2):
        if(num[i]!=num[n-i-1]):
            print -1
            bol=False
            break
    if bol:
        print ''.join(num)
