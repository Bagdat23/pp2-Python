a=int(input())
aa=[str(x) for x in input().split()]
b=int(input())
bb=[str(y) for y in input().split()]
print('Missed students:')
for x in aa:
    if x not in bb:
        print('-',end=' ')
        print(x)
print('Not in the group:')
for y in bb:
    if y not in aa:
        print('-',end=' ')
        print(y)