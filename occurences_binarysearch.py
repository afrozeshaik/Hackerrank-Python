__author__ = 'afrozeshaik'
a=map(int,raw_input().strip().split())
length=len(a)

def binsearch(a,e,left,right):
    l=len(a)
    mid=left+(right-1)/2
    if(left<right):
        if(a[mid]==e):
            return mid
        else:
            if a[mid]>e:
                binsearch(a,e,left,mid-1)
            else:
                binsearch(a,e,mid+1,right)
print(binsearch(a,2,0,len(a)-1))

