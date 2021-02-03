a=int(input())
b=int(input())
cn=[]
if a < b:
    for x in range(a,b+1):
        print(x,end=' ')
else:
    for x in range(a,b-1,-1):
        print(x,end=' ')
        