aa={}
bb={}
cc={}
a=int(input())
sum_max=0
for x in range(a):
    sname,fname,t,y,u=map(str,input().split())
    sname=sname+" "+fname
    bb[x]=int(t)+int(y)+int(u)
    cc[x]=int(t)+int(y)+int(u)
    aa[sname]=int(t)+int(y)+int(u)
    if bb[x] > sum_max:
        sum_max = bb[x]
    print(sorted(cc[x]))
for x in aa:
    if aa[x] > sum_max-1:
        print(x)