import csv,os,re
a = ['kana','baga','dias']
b = [1,2,3]
c = [11,12,13]
d = [123,124,125]
with open('gg.csv','w',newline='') as ans:
    a = ['Title','Count','Unit price','Total price']
    aa = csv.DictWriter(ans,fieldnames=a)
    aa.writeheader()
    for i in range(len(a)):
        writer.writerow({'Title': f'{title[i]}', 'Count': f'{count[i]}', 'Unit price': f'{unit[i]}', 'Total price': f'{total[i]}'})



