import random

lista=[]
for _ in range(20):
    szam=random.randint(1,12)
    if szam %3 ==0:
        print(szam)
        lista.append(szam)


print(lista)
print(len(lista))