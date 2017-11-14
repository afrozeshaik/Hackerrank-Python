__author__ = 'afrozeshaik'
t=input()
for i in range(t):
    a=raw_input().strip().split()
    rows=int(a[0])
    columns=int(a[1])
    rws=[]
    for j in range(rows):
        rws.append(raw_input())
    sa=raw_input().strip().split()
    srows=int(sa[0])
    scolumns=int(sa[1])
    srws=[]
    for j in range(srows):
        srws.append(raw_input())
    bol=False
    ans='NO'
    for p in range(rows-srows):
        for q in range(0,columns-scolumns+1):
            rowcount=0
            for r in range(p,p+scolumns):
                if rws[p][q:q+scolumns]==srws[rowcount]:
                    rowcount+=1
                else:break
                if rowcount==srows:
                    ans='YES'
            if ans=='YES':
                break
        if ans=='YES':
                break
    print ans










