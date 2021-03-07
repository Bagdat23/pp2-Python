 l = [20, 15, 14, 435, 314, 31]
def take_adult(age):
    return age>=18
print(list(filter(lambda x:x>=18, l)))