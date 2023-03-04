import random
maridos=['João', 'José','Mario','Cleiton',]
esposas=['Julia','Maria','Lethicia','Camili']
x=random.randint(0,3)
n=int(input('escolha seu sexo 1-homem 2-mulher [enter]:'))
if n==1:
        print('Você vai casar com a',esposas[x])
elif n==2:
        print('Você vai casar com', maridos[x])
else:
        print('solteiro')