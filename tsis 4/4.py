import re as regex
n = int(input())
hexs = list()
stat = 0
for _ in range(n):
    c = input()
    if regex.search("^[{]", c):
        stat = 1
    elif regex.search("^[}]", c):
        stat = 0
    if stat == 1:
        six = regex.findall("^[#][0-9a-fA-F]{6}", c)
        for s in six:
            hexs.append(s)
        thi = regex.findall("^[#][0-9a-fA-F]{3}", c)
        for t in thi:
            hexs.append(t)
for h in hexs:
    print(h)