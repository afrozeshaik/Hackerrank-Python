__author__ = 'afrozeshaik'
import numpy
import numpy as np
import scipy as sp
import scipy.stats
import math


n=input()
ar=raw_input().strip().split()
ar=map(int,ar)

def mode(lst):
    count={}
    modelist=[]
    for i in lst:
        count[i]=0
    for i in lst:
        count[i]+=1
    max=0
    for i in lst:
        if(count[i]>max):
            max=count[i]
    for i in lst:
        if(count[i]==max):
            modelist.append(i)
    return min(modelist)

def myConfidenceInterval(x, N):
	m = float(sum(x)) / N
	sd_i = list()
	for i in x:
		sd_i.append(math.pow((i - m), 2))
	sd = math.sqrt((sum(sd_i) / N))
	sigma_m = sd / math.sqrt(N)
	upper = m + 1.96 * sigma_m
	lower = m - 1.96 * sigma_m
	upper_rounded = round(upper, 1)
	lower_rounded = round(lower, 1)
	printstr = str(lower_rounded) + " " + str(upper_rounded)
	return printstr

print (numpy.mean(ar))
print (numpy.median(ar))
print mode(ar)
print round(numpy.std(ar),1)
print (myConfidenceInterval(ar,n))

