#k,n=map(int,input().split())
#a = (n-1) // k + 1 # если нумерация страниц с 1. Если нумерация с 0, то +1 нужно убрать
#b = (n-1) % k + 1
#print(a, b)

h,m,s=map(int,input().split())
h1,m1,s1,=map(int,input().split())
a=h1-h
b=m1-m
c=s1-s
a*=3600
b*=60
sum=a+c+b
print(sum)

