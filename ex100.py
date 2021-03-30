from random import randint

numeros = list()

def sortear():
    for c in range(5):
        pc = randint(1,50)
        numeros.append(pc)
    print(f'Números sorteados {numeros}')

def soma_par():
    soma = 0
    print(f'Números pares da lista:', end = ' ')
    for dados in numeros:
        if dados % 2 == 0:
            soma += dados
            print(dados, end = '...')
    print()
    print(f'A soma dos números pares sorteados é de {soma}')

sortear()
soma_par()