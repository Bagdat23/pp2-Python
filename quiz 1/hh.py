x,y=map(int,input().split())
aa={}
bb={}
s=0
ss=0
for i in range(x):
    a,b,c=map(int,input().split())
    aa[a,b,c]=a+b+c
    bb[i]=a+b+c
    if bb[i] > s:
        s=bb[i]
for i in aa:
    if aa[i] > s -1:
        ss+=aa[i]
        break
if ss//3>=y:
    print('YES')
else:
    print('NO')