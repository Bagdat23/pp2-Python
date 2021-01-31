a = int(input())
b = [int(x) for x in input().split(' ')]

cnt=0
for x in b:
    if x %10==7:
        cnt=cnt+1
print(cnt)