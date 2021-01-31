a=int(input())
b=[int(x) for x in input().split(' ')]
max=-1000000000
for x in b:
    if x>max:
        max=x

f=b.index(max)     
print(f+1)


