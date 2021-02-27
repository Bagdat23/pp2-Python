aa={}
bb={}
a,f=map(int,input().split())
sum_max=0
sum1=0
for x in range(a):
    t,y,u=map(int,input().split())
    bb[x]=y+u+t
    aa[x]=t+y+u
    if bb[x] > sum_max:
        sum_max = bb[x]
for x in aa:
    if aa[x] > sum_max-1:
        sum1+=aa[x]
        break
if sum1//3 >= f:
    print("YES")
else:
    print("NO")