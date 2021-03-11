import re
text = ''
for _ in range(int(input())):
    text = re.sub(r'<!.+-->',r' ',(text+input()))
for er in re.findall(r'<([^/][^>]*)>', text):
    if ' ' in er:       
        for ere in re.findall(r'([a-z]+)? *([a-z-]+)="([^"]+)', er):
            if ere[0]:
                print(ere[0])          
            print('-> '+ere[1]+' > '+ere[2])
    else:
        print(er)