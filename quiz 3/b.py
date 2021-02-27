import re 
def text_match(text):  
        pattern = '^[a-zA-Z0-9_]*$' 
        if re.search(pattern, text): 
                return('Found a match!') 
        else: 
                return('Not matched!')  
print(text_match(input()))