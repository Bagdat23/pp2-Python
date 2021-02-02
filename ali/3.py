cnt=0
nums=input()
n=len(nums)
for i in range(n):
    for i2 in range(i+1,n):
        if nums[i]==nums[i2]:
            cnt+=1
print(cnt)