a=int(input())
aa=[]
b=[int(i) for i in input().split()]
for x in range(1,1+a,1):
    aa.append(x)
bb=[]
for i in sorted(set(b)):
    bb.append(i)
for i in sorted(b):
    for x in range(len(bb)):
        print(aa[x],bb[x])
    break
    

    
    
            