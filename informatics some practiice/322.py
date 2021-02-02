#1281. Subtract the Product and Sum of Digits of an Integer1281. Subtract the Product and Sum of Digits of an Integer
print('n = ',end='')
a=int(input())
b=a
sum=0
sum2=1
while a!=0:
    sum+=a%10
    a//=10
while b!=0:
    sum2*=b%10
    b//=10
print(sum2-sum)
