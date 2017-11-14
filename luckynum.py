__author__ = 'afrozeshaik'
def islucky(n):
    f=n/1000
    l=n%1000
    fs=0
    ls=0
    for i in str(f):
        fs+=int(i)
    for i in str(l):
        ls+=int(i)
    if fs==ls:
        return True
    else:
        return False
n=input()+1
while True:
    if islucky(n):
        print n
        break
    else:
        n+=1


