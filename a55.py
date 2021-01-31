a,b=map(int,input().split())
s=''
while a<=b:
    if a%2==0:
        s=s+str(a)+" "
        a+=1
print(s)