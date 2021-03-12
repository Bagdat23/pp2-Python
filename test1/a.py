import csv
import re
title = ['adam', 'erzhan', 'zhandos']
count = [13, 14, 54]
unit = [1, 2, 3]
total = [123, 145, 121]
with open('names.csv', 'w', newline='') as csvfile:
    field = ['Title', 'Count', 'Unit price', 'Total price']
    writer = csv.DictWriter(csvfile, fieldnames=field)
    writer.writeheader()
    # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans', 'Bagdat': '18'})
    for i in range(len(title)):
      writer.writerow({'Title': f'{title[i]}', 'Count': f'{count[i]}', 'Unit price': f'{unit[i]}', 'Total price': f'{total[i]}'})