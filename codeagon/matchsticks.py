__author__ = 'afrozeshaik'
n,c = raw_input().strip().split(' ')
n,c = [int(n),int(c)]
d=dict()
mat=[]
for crate_i in xrange(c):
    crate_temp = map(int,raw_input().strip().split(' '))
    d[crate_temp[1]]=crate_temp[0]
    mat.append(crate_temp[1])
mat.sort(reverse=True)
print mat
result=0
for i in xrange(c):
    if(n<=0):
        break
    else:
        if(d[mat[i]]<n):
            result+=mat[i]*d[mat[i]]
            n-=d[mat[i]]
        else:
            result+=mat[i]*n
            n-=d[mat[i]]
print result




