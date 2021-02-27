a=int(input())
b=[int(x) for x in input().split()]
aa=[]
bb=[]
cc=[]
for x in b:
    aa.append(x)
    bb.append(x)
cc=(sorted(aa,key=int))
if(bb == cc):
    print('Interesting')
else:
    print("Not interesting")