aa={}
s=input().split()
for i in s:
    if i in aa:
        aa[i]+=1
    else:
        aa[i]=1
for i in sorted(aa):
    if aa[i]%2==0:
        print(i)
