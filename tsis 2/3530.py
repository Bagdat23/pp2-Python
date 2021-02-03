n = int(input())
for num in range(10**n, 10**(n - 1) - 1, -1):
    if num % 2 != 0:
        print(num, end = ' ')