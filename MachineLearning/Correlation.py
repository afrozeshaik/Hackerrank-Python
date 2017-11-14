
__author__ = 'afrozeshaik'

# (nsigma(xiyi)-sigma(xi)sigma(yi))/sqrt(nsigma(xi^2)-(sigma(xi))^2)
t=input()
math=[]
phy=[]
chem=[]

for i in range(t):
    s=raw_input().strip().split()
    math.append(int(s[0]))
    phy.append(int(s[1]))
    chem.append(int(s[2]))
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
    return round(numer/denom,2)

print correlation(math,phy,t)
print correlation(chem,phy,t)
print correlation(math,chem,t)


