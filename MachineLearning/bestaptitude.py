__author__ = 'afrozeshaik'
def correlation(l1,l2,n):
    sigma_l1=sum(l1)
    sigma_l2=sum(l2)
    numer=0
    denom=0
    sigmal1l2=0
    sigma_l1sq=0
    sigma_l2sq=0
    for i in range(n):
        sigmal1l2+=l1[i]*l2[i]
        sigma_l1sq+=l1[i]**2
        sigma_l2sq+=l2[i]**2
        numer=n*sigmal1l2-(sigma_l1*sigma_l2)
        denom=abs((n*sigma_l1sq-(sigma_l1)**2)*(n*sigma_l2sq-(sigma_l2)**2))**0.5
    return (numer/denom)

def ranking(l,n):
    dic={}
    for i in l:
        dic[i]=0
    sl=sorted(l)
    cnt=0
    for i in sl:
        dic[i]=cnt
        cnt+=1
    newl=[]
    for i in l:
        newl.append(dic[i])
    return newl
t=input()
numofstudents=input()
gpa=ranking(map(float,raw_input().strip().split()),numofstudents)
testmarks=[]
for i in range(5):
    testmarks.append(ranking(map(float,raw_input().strip().split()),numofstudents))
cor=[]
for i in range(5):
    cor.append(abs(correlation(testmarks[i],gpa,numofstudents)))
minimum=1
ans=0
for i in range(5):
    if cor[i]<minimum:
        minimum=cor[i]
        ans=i

