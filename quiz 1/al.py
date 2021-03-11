a=int(input())
b=input()
ans=""
for i in b:
    ans+=chr(ord("A")+(ord(i)-ord("A")+a)%26)
print(ans)