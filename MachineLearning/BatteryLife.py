__author__ = 'afrozeshaik'
import pylab as pl

data = open('trainingdata.txt').read().split('\n')
x = []
y = []
for line in data:
    if not ',' in line:
        continue
    (lx, ly) = map(float, line.split(','))
    x.append(lx)
    y.append(ly)
data = float(raw_input())

if data >= 4.00:
    print 8.00
else:
    print round(2*data, 2)
