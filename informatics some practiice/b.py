aa={}
bb={}
a=int(input())
sum_max=0
for x in range(a):
    sname = str(input())
    t,y,u=map(int,input().split())
    bb[x]=t+y+u
    aa[sname]=t+y+u
    if bb[x] > sum_max:
        sum_max = bb[x]
for x in aa:
    if aa[x] > sum_max-1:
        print(x)

