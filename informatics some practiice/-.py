import math
a=int(input())
sum=0
sum1=0
cn=[]
nc=[]
aa={}
bb={}
for i in range(a):
    x,y=map(int,input().split())
    cn.append(x)
    nc.append(y)
    aa[x,y]=x+y
    bb[i]=x+y
    mx=max(cn)
    mn=max(nc)
    g=min(cn)
    h=min(nc)
    lol=mx-g
    l=mn-h
print(math.sqrt(lol**2+l**2))