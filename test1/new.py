import re,os,csv
a = ['dias','kana','baga']
b = [1,2,3]
c = [175,200,225]
d = [500,750,1000]
with open('wp.csv','w',newline='') as ans:
    x = ['Title','Count','Unit price','Total price']
    y = csv.DictWriter(ans,fieldnames=x)
    y.writeheader()
    for i in range(len(a)):
        y.writerow({'Title': f'{a[i]}', 'Count': f'{b[i]}', 'Unit price': f'{c[i]}', 'Total price': f'{d[i]}'})

