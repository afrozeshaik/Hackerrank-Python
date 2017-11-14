def permute(a,l,r):
    if l==r:
        print ''.join(a)
    else:
        for i in xrange(l,r):
            a[i],a[l]=a[l],a[i]
            permute(a,l+1,r)
            a[i],a[l]=a[l],a[i]

a=list(raw_input())
permute(a,0,len(a))
