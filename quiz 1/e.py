a=int(input())
aa={}
for i in range(a):
    x = input().split()
    for i in range(2,int(x[1])+2):
        aa[x[i]]=x[0]
b=int(input())
for i in range(b):
    y=str(input())
    if y in aa:
        print(aa[y])
    else:
        print('Unknown')

    