a=int(input())
b=[int(x) for x in input().split()]
aa=[]
bb=[]
for x in b:
    aa.append(x)
    bb.append(x)
if a == 1:
    print('Clean:',end='')
    print(a)
    print('Dirty:0')
else:
    print("Clean:0")
    print("Dirty:",end='')
    print(a)