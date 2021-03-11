import re
a=int(input())
aa={}
ans = r"<[a-z0-9]+@[a-z]+[\.](com|ru|net)>"
for i in range(a):
    x,y=input().split()
    aa[x,y]=y
    if re.search(ans,y):
        print(x,y)
    else:
        break