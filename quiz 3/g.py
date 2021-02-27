a=int(input())
d=set()
f=set()
sum=0
for i in range(a):
    s=str(input())
    if i==0:
        for j in s:
            d.add(j)
    for j in s:
        f.add(j)
    d=d.intersection(f)
    f.clear()
d=sorted(d,key=str)
if d:
    print(*d)
else:
    print("NO COMMON CHARACTERS")
