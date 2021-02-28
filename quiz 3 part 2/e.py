s = input().split()
aa = []
for i in s:
    aa.append(len(i))
print(s[aa.index(max(aa))])
print(len(s[aa.index(max(aa))]))