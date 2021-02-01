aa={}
a=int(input())
max_sum=0
for x in range(a):
    sname= str(input())
    y,u,i=map(int,input().split())
    aa[x]=y+u+i
    aa[sname]=x
    if aa[x]>max_sum:
        max_sum=aa[x]
        aa[sname]=aa[x]
for x in aa:
    if aa[x]==aa[sname]:
        print(x)