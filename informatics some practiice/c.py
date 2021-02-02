a=int(input())
sum=-1000000000
aa={}
bb={}
for i in range(a):
    x,y=map(int,input().split())
    bb[i]=x+y
    aa[x,y]=x+y
    if bb[i]>sum:
        sum=bb[i]
for i in aa:
    if aa[i]>sum-1:
        print(*i)        