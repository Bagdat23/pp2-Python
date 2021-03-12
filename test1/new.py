import csv,os,re
a = ['kana','baga','dias']
b = [1,2,3]
c = [11,12,13]
d = [123,124,125]
with open('gg.csv','w',newline='') as ans:
    aaa = ['Title','Count','Unit price','Total price']
    aa = csv.DictWriter(ans,fieldnames=aaa)
    aa.writeheader()
    for i in range(len(a)):
        aa.writerow({'Title': f'{a[i]}', 'Count': f'{b[i]}', 'Unit price': f'{c[i]}', 'Total price': f'{d[i]}'})



