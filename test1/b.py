import json
import sys
import math
data = json.loads(sys.stdin.read())
name = ''
mn = 1000000000
for i in range(len(data['Subscriptions'])):
    price = int(data['Subscriptions'][i]['price'])
    discount = int(data['Subscriptions'][i]['discount'])
    ans = int((price/100)*(1*100-discount))
    if mn > ans:
        mn = ans
        name = data['Subscriptions'][i]['name']
print("Name: ", name)
print('Price:', int(mn))
