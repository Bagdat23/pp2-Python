import collections
aa={}
bb={}
sum=0
a=int(input())
for x in range(a):
    sname,fname,t,y,u=map(str,input().split())
    sname=sname+" "+fname
    bb[x]=int(t)+int(y)+int(u)
    aa[sname]=int(t)+int(y)+int(u)
for x in aa:
    if aa[x] > 1:
        print(*sorted(x,key=lambda aa: aa[a]))
