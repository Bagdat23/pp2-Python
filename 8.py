a = int(input())
b = [int(x) for x in input().split(' ')]

ev=0
odd=0
for x in b:
    if x %2==0:
        ev=ev+1
    else:
        odd=odd+1
print(ev,odd)