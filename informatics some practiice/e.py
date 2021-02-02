import itertools
aa={}
bb={}
a=int(input())
sum_max=0
pairs=''
for x in range(a):
    sname,fname,t,y,u=map(str,input().split())
    sname=sname+" "+fname
    bb[x]=int(t)+int(y)+int(u)
    aa[sname]=int(t)+int(y)+int(u)
    pairs=[aa[sname],bb[x]]
    for p in reversed(pairs):
        print(p)
#for x in aa:
    #if aa[x] > sum_max-1:
        #print(x)