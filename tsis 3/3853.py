a=list(map(int,input().split()))
b=int(input())
if b < 0 :
    b=abs(b)
    print(*a[n:],end=' ')
    print(*a[0:b])
else:
    b=abs(b)
    print(*a[-b:],end=' ')
    print(*a[0:-b])
