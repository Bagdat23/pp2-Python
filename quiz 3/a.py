import re 
def text_match(text):  
        pattern = '[A-Z]+[a-z]+' 
        if re.search(pattern, text): 
                return('Found a match!') 
        else: 
                return('Not matched!')  
print(text_match(input()))