import random
result=[]
while len(result) !=6:
    random.seed()
    r=random.randint(1,60)
    if r not in result:
        result.append(r)
        result.sort()
print(result)
