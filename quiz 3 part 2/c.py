a=int(input())
b=[int(x) for x in input().split()]
aa=[]
bb=[]
for x in b:
    if x not in aa:
        aa.append(x)
if aa==b:
    print("YES")
else:
    print("NO")