s=str(input())
x,y=0,0
checker = False
a,b=map(int,input().split())
if x == a and y == b:
    checker = True 
for i in s:
    if i =='R':
        x+=1
    if i =='L':
        x-=1
    if i =='U':
        y+=1
    if i =='D':
        y-=1
    if x == a and y == b:
        checker = True
if checker==True:
    print('Passed')
else:
    print('Missed')

