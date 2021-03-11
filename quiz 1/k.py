a=int(input())
b=set()
c=set()
for i in range(a):
    x=input()
    if i == 0:
        for j in x:
            b.add(j)
    for j in x:
        c.add(j)
    b=b.intersection(c)
    c.clear()
if b:
    print(*b)
else:
    print("idi nahui")