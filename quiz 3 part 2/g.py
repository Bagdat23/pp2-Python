import re
a=input()
b=input()
c=input()
d=input()
a=re.sub(b,c,a)
ans=re.findall(d,a)
print(len(ans))