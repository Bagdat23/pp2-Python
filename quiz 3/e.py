a=int(input())
aa={}
for i in range(a):
    s=input().split()
    for i in range(2,int(s[1])+2):
        aa[s[i]]=s[0]
b=int(input())
for i in range(b):
    s1=str(input())
    if s1 in aa:
        print(aa[s1])
    else:
        print("Unknown")