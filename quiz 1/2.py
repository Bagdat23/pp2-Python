with open("gg.txt", "r") as ans:
    x = list(map(lambda a : len(a.strip()),ans.readlines()))
for i in range(1,len(x)):
    if x[i] <= x[i-1]:
        print('NO')
        exit()
print('YEs')