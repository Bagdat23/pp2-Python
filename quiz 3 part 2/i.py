a=int(input())
f=""
s=""
b = [str(x) for x in input().split()]
k = int(input())
if k == 0:
    print(0)
    exit()
for x in b[:k]:
    f+=x
for x in b[k:]:
    s+=x
print(int(f)*int(s))