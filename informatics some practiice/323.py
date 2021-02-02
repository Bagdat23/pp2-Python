a=int(input())
sum=0
sum1=0
sum2=0
for x in range(a):
    t,y=map(str,input().split())
    sum+=int(t)/a
    sum1+=int(y)/a
print(sum,end=' ')
print(sum1)