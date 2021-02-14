import math
a=list(map(int,input().split()))
ans=10**9
for x in a:
    if 0 < x < ans:
        ans =x
print(ans)