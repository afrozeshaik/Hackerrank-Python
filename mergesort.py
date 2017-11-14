__author__ = 'afrozeshaik'
arr = [1,3,5,2,4,6]

def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    L=[0]*n1
    R=[0]*n2
    for i in xrange(n1):
        L[i]=arr[l+i]
    for i in xrange(n2):
        R[i]=arr[m+1+i]
    print L
    print R
    i=0
    j=0
    k=0
    while(i<n1 and j<n2):
        if(L[i]<R[j]):
            arr[k]=L[i]
            k+=1
            i+=1
        else:
            arr[k]=R[j]
            k+=1
            j+=1
    while(i<n1):
        arr[k]=L[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k]=R[j]
        j+=1
        k+=1
    print arr
merge(arr,0,2,5)


