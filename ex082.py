lista = []
listaPar = []
listaImpar = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if n % 2 != 0:
        listaImpar.append(n)
    else:
        listaPar.append(n)

    if continuar == 'N':
        break

print(f'Valores digitados: {lista}')
print(f'Lista de pares: {listaPar}')
print(f'Lista de ímpares: {listaImpar}')
