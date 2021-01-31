a = int(input())
b = [int(x) for x in input().split(' ')]

max = 0
for x in b:
    if x > max:
        max = x
print(max)