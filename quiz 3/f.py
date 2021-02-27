n = int(input())
s = input()
res = ""
for i in s:
    num = ord(i) + n
    if num > 90: num -= 26
    res += chr(num)
print(res)