b = [int(x) for x in input().split()]
a = [int(y) for y in input().split()]
print(*sorted(set(b).intersection(set(a))))