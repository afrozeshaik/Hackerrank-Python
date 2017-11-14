__author__ = 'afrozeshaik'
t=input()
for p in xrange(t):
    n=input()
    ar=map(int,raw_input().strip().split())
    myar=[]
    swaps=[]
    for i in xrange(n):
        myar.append(i+1)
        swaps.append(0)
    totalswaps=0
    bol=True

    for i in xrange(n):
        print myar
        if(ar[i]!=myar[i]):
            totalswaps+=1
            for j in xrange(i+1,n):
                if(myar[j]==ar[i]):
                    swaps[myar[i]-1]+=1
                    swaps[ar[i]-1]+=1
                    temp=myar[j]
                    myar[j]=myar[i]
                    myar[i]=temp
                    break
        if(max(swaps)>2):
            bol=False
            break
    print totalswaps
    print swaps
    if bol:
        print totalswaps
    else:
        print 'Too chaotic'













