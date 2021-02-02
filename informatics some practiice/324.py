import math
a=int(input())
sum=0
sum1=0
cn=[]
nc=[]
aa={}
bb={}
cc={}
sum_max=0
sum_min=math.inf
for i in range(a):
    x,y=map(int,input().split())
    aa[x,y]=x+y
    cc[x,y]=x+y
    bb[i]=x+y
    if bb[i] > sum_max:
        sum_max=bb[i]
    elif bb[i]<sum_min:
        sum_min=bb[i]
for i in aa:
    for p in cc:
        if aa[i] > sum_max-1:
            if cc[p] < sum_min+1:
                nc=[*i]
                cn=[*p]
                g=max(nc)
                h=min(nc)
                gg=max(cn)
                hh=min(cn)
                lol = g-gg
                l = h-hh
                break
print(math.sqrt(lol**2+l**2))
                
                





