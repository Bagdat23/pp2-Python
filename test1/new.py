import csv
import re
import math,os
title = ['adam', 'erzhan', 'zhandos']
count = [13, 14, 54]
unit = [1, 2, 3]
total = [123, 145, 121]
with open('gg.csv','w',newline='') as ans:
    a = ['Title', 'Count', 'Unit price', 'Total price']
    writer = csv.DictWriter(ans,fieldnames=a)
    writer.writeheader()
    for i in range(len(title)):
        writer.writerow({'Title': f'{title[i]}', 'Count': f'{count[i]}', 'Unit price': f'{unit[i]}', 'Total price': f'{total[i]}'})



