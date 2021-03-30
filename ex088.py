from random import randint
from time import sleep

user = int(input('Quantos jogos sortear?: '))
lista = []
sorteio = []

for x in range(user):
    while len(lista) < 6:
        pc = randint(1, 60)
        if pc not in lista:
            lista.append(pc)
    lista.sort()
    sorteio.append(lista[:])
    lista.clear()

print('JOGOS SORTEADOS')
print('=-'*15)
for lista in sorteio:
    print(lista)
    print('=-' * 15)
    sleep(0.3)
