aa={}
bb={}
a=int(input())
sum_max=0
for x in range(a):
    sname,fname,t,y,u=map(str,input().split())
    sname=sname+" "+fname
    if int(t)!=3 or int(y)!=3 or int(u)!=3:   
        bb[x]=int(t)+int(y)+int(u)
        aa[sname]=int(t)+int(y)+int(u)
for x in aa:
    if aa[x] > 12:
        print(x)