#1732. Find the Highest Altitude
b = [int(x) for x in input().split(' ')]
max = -1000000000
for x in b:
    if x > max:
        max = x
print(max)