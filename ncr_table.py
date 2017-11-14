__author__ = 'afrozeshaik'
gl=list()
for i in range(6):
    gl.append([])
    for j in range(i+1):
        gl[i].append(0)
print gl

for i in range(6):
    for j in range(i+1):
        if i==1 or i==j or j==0:
            gl[i][j]=1
        else:
            gl[i][j]=(gl[i-1][j-1]+gl[i-1][j])%(10^9)
print gl[2],gl[3]