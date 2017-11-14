__author__ = 'afrozeshaik'
a=input()
if a==1:

    ar=list()
    for i in range(8):
        ar.append(raw_input())
    bol1=True
    bol2=True
    bol3=True
    bol4=True
    '''
    1
    01000100
    10100001
    00001000
    00100101
    00100000
    01000001
    00100000
    00001001'''
    for i in range(7):
        for j in range(7):
            if(ar[i][j]=='1' and ar[i][j+1]=='1' and ar[i+1][j]=='1'):
                bol1=False
                bol2=False
                bol3=False
                print i,j
                break
        if not(bol1):
            break
    if bol1:
        #print "not in first"
        for i in range(8):
            for j in range(7):
                if(ar[i][j]=='1' and ar[i][j+1]=='1'):
                    bol2=False
                    bol3=False
                    print i,j
                    break
            if not(bol2):
                break
    if bol2:
        #print "not in second"
        for i in range(7):
            for j in range(8):
                if(ar[i][j]=='1' and ar[i+1][j]=='1'):
                    bol3=False
                    print i,j
                    break
            if not(bol3):
                break
    if bol3:
        #print "not in third"
        for i in range(8):
            for j in range(8):
                if(ar[i][j]=='1'):
                    bol4=False
                    print i,j
                    break
            if not(bol4):
                break