a=int(input())
sum=0
sum1=0
sum2=0
for x in range(a):
    sname,fname,t,y,u=map(str,input().split())
    sname=sname+" "+fname
    sum+=int(t)
    sum1+=int(y)
    sum2+=int(u)
if sum%2==0:
    print(sum//a,end=' ')
else:
    print(sum/a,end=' ')
if sum1%2==0:
    print(sum1//a,end=' ')
else:
    print(sum1/a,end=' ')
if sum2%2==0:
    print(sum2//a,end=' ')
else:
    print(sum2/a,end=' ')