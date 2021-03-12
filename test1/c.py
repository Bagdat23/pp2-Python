a=input()
b=int(input())
ans=''
for i in a:
    ans += chr((ord(i)+13+b)%26+65)
print(ans)