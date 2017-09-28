from igraph import *
from math import *
from time import *
#g  =  Graph()
start=clock()
g = Graph.GRG(200,0.1)
summary(g)


n=g.vcount()
m=4
x=[[0]*m for i in range(n)]
temp=g.evcent()
#决策矩阵p
for i in range(n):
    x[i][0]=g.degree(i)
    x[i][1]=temp[i]
    x[i][2]=g.closeness(i)
    x[i][3]=g.betweenness(i)
#print(x)
#规范化
maxarr= []
for j in range(m):
    max = 0
    for i in range(n):
        if (x[i][j] > max):
            max = x[i][j]
    maxarr.append(max)
#print(maxarr)
#规范化决策矩阵
for i in range(n):
    for j in range(m):
        if(maxarr[j]==0):
            x[i][j]=0
        else:
            x[i][j]=x[i][j]/maxarr[j]
print("R:")
print(x)

w=[0.0861,0.2073,0.2073,0.4993]
#加权规范化决策矩阵
y=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        y[i][j]=w[j]*x[i][j]
print("Y:")
print(y)
a1=[]
a2=[]
#正负理想决策方案
for j in range(m):
    max = 0
    min= 100
    for i in range(n):
        if (y[i][j] > max):
            max = y[i][j]
        if(y[i][j]<min):
            min = y[i][j]
    a1.append(max)
    a2.append(min)
#print(a1)
#print(a2)
#距离
d1=[]
d2=[]
for i in range(n):
    sum1=0
    sum2=0
    for j in range(m):
        sum1 += (y[i][j]-a1[j])*(y[i][j]-a1[j])
        sum2 += (y[i][j] - a2[j]) * (y[i][j] - a2[j])
    d1.append(sqrt(sum1))
    d2.append(sqrt(sum2))
#print("d1 d2:")
#print(d1)
#print(d2)
z=[]
for i in range(n):
    #print(d2[i])
    z.append(d2[i]/(d1[i]+d2[i]))
print("z:")
print(z)
end=clock()
print('Running time: %s Seconds'%(end-start))
