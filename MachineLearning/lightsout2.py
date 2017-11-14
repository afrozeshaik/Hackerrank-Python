__author__ = 'afrozeshaik'
a=input()
ar=list()
for i in range(8):
    ar.append(raw_input())
mat=[[0 for i in range(8)] for j in range(8)]
maxval=0
'''
1
01001000
00010101
10101000
00101001
10101010
00000001
11000011
00101000
'''
for r in range(8):
    for c in range(8):
        if(ar[r][c]=='1'):
            mat[r][c]+=1
            if mat[r][c]>maxval:
                    maxval=mat[r][c]
            if(r<7 and ar[r+1][c]=='1' ):
                mat[r][c]+=1
                if mat[r][c]>maxval:
                    maxval=mat[r][c]
            if(c<7 and ar[r][c+1]=='1' ):
                mat[r][c]+=1
                if mat[r][c]>maxval:
                    maxval=mat[r][c]

bol=True
for r in range(8):
    for c in range(8):
        if mat[r][c]==maxval:
            bol=False
            print r,c
            break
    if not bol:
        break
