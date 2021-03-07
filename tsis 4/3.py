import re as regex
n = int(input())
arr = list()
for _ in range(n):
    p = input()
    x = regex.search("^([7]|[8]|[9]){1}[1-9]{9}$", p)
    if x:
        arr.append("YES")
    else:
        arr.append("NO")
for a in arr:
    print(a)