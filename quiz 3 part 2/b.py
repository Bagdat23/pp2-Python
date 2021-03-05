import re
a=input()
b=input()
try:
    print('First time',b,'occured in position: ',a.index(b))
except:
    print('Not found')